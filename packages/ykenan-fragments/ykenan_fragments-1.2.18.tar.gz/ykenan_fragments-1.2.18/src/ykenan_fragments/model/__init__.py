#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
from typing import TextIO
from multiprocessing.dummy import Pool
from multiprocessing.pool import ThreadPool

import pandas as pd
from pandas import DataFrame
from ykenan_log import Logger
from ykenan_file import StaticMethod, Read

from ykenan_fragments.util import chrtype


class GetFragments:

    def __init__(self, base_path: str, output_path: str, record_count: int = 100000, thread_count: int = 8):
        """
        Form an unordered fragments
        :param base_path: Path to store three files
        :param output_path: Path to store three files
        :param record_count: record count
        :param thread_count: thread count
        """
        self.log = Logger("YKenan_fragments", "log/fragments.log")
        self.file = StaticMethod(log_file="log")
        self.read = Read(header=None, log_file="log")
        self.read_header = Read(log_file="log")
        # Folder path containing three files
        self.record_count: int = record_count
        self.thread_count: int = thread_count
        # path
        self.base_path: str = base_path
        self.output_path: str = output_path
        self.barcodes_file: str = os.path.join(base_path, "barcodes.tsv")
        self.mtx_file: str = os.path.join(base_path, "matrix.mtx")
        self.peaks_file: str = os.path.join(base_path, "peaks.bed")
        self.fragments_file = os.path.join(output_path, "fragments.tsv")
        # Create a folder to store chromatin
        self.chromosome_path: str = os.path.join(output_path, f"chromosome")
        self.sort_chromosome_path: str = os.path.join(output_path, f"sort_chromosome")
        self.file.makedirs(self.chromosome_path)
        self.file.makedirs(self.sort_chromosome_path)
        self.chr_file_dict: dict = {}

    def judge_mtx_is_true(self, one_len: str, two_len: str, peaks_len: int, barcodes_len: int) -> int:
        # 此处现象认为没有表头情况
        if int(one_len) == peaks_len and int(two_len) == barcodes_len:
            self.log.info(f"The `features` and `barcodes` files have no headers.  The first column in the `mtx` file represents the row index information in the `features` file, and the second column represents the row index information in the `barcodes` file.")
            return 1
        elif int(one_len) == barcodes_len and int(two_len) == peaks_len:
            self.log.info(f"The `features` and `barcodes` files have no headers.  The first column in the `mtx` file represents the row index information in the `barcodes` file, and the second column represents the row index information in the `features` file.")
            return 2
        # 此处现象认为有表头情况
        elif int(one_len) + 1 == peaks_len and int(two_len) + 1 == barcodes_len:
            self.log.info(f"The `features` and `barcodes` files have headers.  The first column in the `mtx` file represents the row index information in the `features` file, and the second column represents the row index information in the `barcodes` file.")
            return 3
        elif int(one_len) + 1 == barcodes_len and int(two_len) + 1 == peaks_len:
            self.log.info(f"The `features` and `barcodes` files have headers.  The first column in the `mtx` file represents the row index information in the `barcodes` file, and the second column represents the row index information in the `features` file.")
            return 4
        else:
            return -1

    @staticmethod
    def get_peaks(line: str) -> str:
        return line.rstrip()

    @staticmethod
    def get_barcodes(line: str) -> str:
        return line.rstrip()

    def set_chr_filename(self, peaks) -> None:

        chr_list: list = []

        for peak in peaks:
            peak_info: str = self.get_peaks(peak)
            chr_list.append(peak_info.split("\t")[0])

        for _chr_ in set(chr_list):
            chromosome_path_file: str = f"{self.chromosome_path}/{_chr_}.tsv"
            self.chr_file_dict.update({_chr_: chromosome_path_file})

    def read_file_line(self, path: str, mode: str = 'r', encoding: str = "utf-8") -> list:
        """
        Read file by line
        :param path:
        :param mode:
        :param encoding:
        :return:
        """
        content = []
        self.log.info(f"Start reading file {path}")
        with open(path, mode, encoding=encoding) as f:
            while True:
                line = f.readline().strip()
                if not line:
                    break
                if line == "":
                    continue
                content.append(line)
        return content

    def write_chr_file(self) -> None:
        """
        Form fragments file
        :return:
        """
        # Get Barcodes
        self.log.info(f"Getting barcodes file information")
        barcodes: list = self.read_file_line(self.barcodes_file)

        if len(barcodes) != len(set(barcodes)):
            self.log.error("")
            raise ValueError("")

        self.log.info(f"Getting feature file information")
        peaks: list = self.read_file_line(self.peaks_file)
        self.set_chr_filename(peaks)

        # length
        barcodes_len: int = len(barcodes)
        peaks_len: int = len(peaks)

        if barcodes_len < 2 or peaks_len < 2:
            self.log.error(f"Insufficient file read length barcodes: {barcodes_len}, features: {peaks_len}")
            raise ValueError("Insufficient file read length")

        # Convert to dictionary
        barcodes_dict: dict = dict(zip(list(range(barcodes_len)), barcodes))
        peaks_dict: dict = dict(zip(list(range(peaks_len)), peaks))

        self.log.info(f"Quantity or Path barcodes: {barcodes_len}, mtx: {self.mtx_file}, features: {peaks_len}")
        # Read quantity
        mtx_count: int = 0
        error_count: int = 0
        mtx_all_number: int = 0
        is_peaks_barcodes: int = -1

        chr_f_list: list = list(self.chr_file_dict.keys())
        chr_f_dict: dict = {}
        for chromosome in chr_f_list:
            chr_f = open(self.chr_file_dict[chromosome], "w", encoding="utf-8", newline="\n", buffering=1)
            chr_f_dict.update({chromosome: chr_f})

        # create a file
        self.log.info(f"Starting to form {self.fragments_file} fragments file")
        with open(self.mtx_file, "r", encoding="utf-8") as r:
            line: str = r.readline().strip()

            while True:
                if line.startswith("%"):
                    self.log.info(f"Annotation Information: {line}")
                    line: str = r.readline().strip()
                else:
                    break

            split: list = line.split(" ")

            if len(split) == 3 and line:
                self.log.info(f"Remove Statistical Rows: {line}")
                mtx_all_number = int(split[2])
                is_peaks_barcodes = self.judge_mtx_is_true(split[0], split[1], peaks_len, barcodes_len)

                if is_peaks_barcodes == -1:
                    raise ValueError(f"File mismatch features: {int(split[0])} {peaks_len}, barcodes: {int(split[1])} {barcodes_len}")

            while True:
                line: str = r.readline().strip()

                if not line:
                    break

                if mtx_count >= self.record_count and mtx_count % self.record_count == 0:
                    self.log.info(f"Processed {mtx_count} lines, completed {round(mtx_count / mtx_all_number, 4) * 100} %")

                split: list = line.split(" ")
                split_peak_index: int = 0
                split_barcode_index: int = 0

                # judge
                if is_peaks_barcodes == 1:
                    split_peak_index: int = int(split[0]) - 1
                    split_barcode_index: int = int(split[1]) - 1
                elif is_peaks_barcodes == 2:
                    split_peak_index: int = int(split[1]) - 1
                    split_barcode_index: int = int(split[0]) - 1
                elif is_peaks_barcodes == 3:
                    split_peak_index: int = int(split[0])
                    split_barcode_index: int = int(split[1])
                elif is_peaks_barcodes == 4:
                    split_peak_index: int = int(split[1])
                    split_barcode_index: int = int(split[0])

                # To determine the removal of a length of not 3
                if len(split) != 3:
                    mtx_count += 1
                    error_count += 1
                    self.log.error(f"mtx information ===> content: {split}, line number: {mtx_count}")
                    continue

                if split_peak_index > peaks_len or split_barcode_index > barcodes_len:
                    self.log.error(f"`{split_peak_index} > {peaks_len} or {split_barcode_index} > {barcodes_len}` appears in the mtx file")
                    mtx_count += 1
                    continue

                # peak, barcode, There is a header+1, but the index starts from 0 and the record starts from 1
                peak_info: str = self.get_peaks(peaks_dict[split_peak_index])
                barcode_info: str = self.get_barcodes(barcodes_dict[split_barcode_index])
                chromosome = peak_info.split("\t")[0]
                # Obtaining files with added content
                chromosome_file: TextIO = chr_f_dict[chromosome]

                # Adding information, it was found that some files in mtx contain two columns, less than three columns. This line was ignored and recorded in the log
                try:
                    chromosome_file.write(f"{peak_info}\t{barcode_info}\t{split[2]}\n")
                except Exception as e:
                    error_count += 1
                    self.log.error(f"peak information: {peaks_dict[split_peak_index]}")
                    self.log.error(f"barcodes information: {barcodes_dict[split_barcode_index]}")
                    self.log.error(f"mtx information ===> content: {split}, line number: {mtx_count}")
                    self.log.error(f"Write error: {e}")
                mtx_count += 1

        # close file
        for chromosome in chr_f_list:
            chromosome_file: TextIO = chr_f_dict[chromosome]
            chromosome_file.close()

        self.log.info(f"The number of rows ignored is {error_count}, {round(error_count / mtx_all_number, 4) * 100} % of total")
        self.log.info(f"Complete the formation of {self.fragments_file} fragments file")

    def sort_position_files_core(self, _chr_: str):
        self.log.info(f"Start sorting file {self.chr_file_dict[_chr_]} Sort")
        chr_file_content: DataFrame = pd.read_table(self.chr_file_dict[_chr_], encoding="utf-8", header=None)
        # 进行排序
        chr_file_content.sort_values(1, inplace=True)
        position_file: str = os.path.join(self.sort_chromosome_path, f"{_chr_}.tsv")
        chr_file_content.to_csv(position_file, sep="\t", encoding="utf-8", header=False, index=False)
        self.log.info(f"To file {_chr_} Sort completed")

    def sort_fragments(self):
        self.write_chr_file()
        # sort position
        pool: ThreadPool = Pool(self.thread_count)
        # Form fragments file
        pool.map(self.sort_position_files_core, self.chr_file_dict.keys())
        pool.close()

        chr_info: DataFrame = pd.DataFrame(
            columns=["chr", "_chr_", "file"], data={
                "chr": self.chr_file_dict.keys(),
                "_chr_": self.chr_file_dict.keys(),
                "file": self.chr_file_dict.values()
            }
        )
        chr_info["chr"] = chr_info["chr"].astype(chrtype)
        chr_info["_chr_"] = chr_info["_chr_"].astype(str)
        chr_info["file"] = chr_info["file"].astype(str)

        chr_info.sort_values(["chr", "_chr_"], inplace=True)

        with open(self.fragments_file, "w", encoding="utf-8", buffering=1, newline="\n") as w:
            for _chr_, _file_ in zip(chr_info["_chr_"], chr_info["file"]):
                self.log.info(f"Start adding {_file_} file")
                with open(_file_, "r", encoding="utf-8") as r:
                    while True:
                        line: str = r.readline().strip()
                        if not line:
                            break
                        w.write(f"{line}\n")
                self.log.info(f"Completed adding {_chr_} file")
