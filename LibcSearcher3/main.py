#!/usr/bin/env python3
# coding=utf-8

from LibcSearcher3.cmd import Command
from LibcSearcher3.utils import extract_libc, parse_libc

import os
import re


class LibcSearcher(object):
    def __init__(self, func=None, address=None):
        self.condition = {}
        if func is not None and address is not None:
            self.add_condition(func, address)
        self.libc_database_path = os.path.join(
            os.path.realpath(os.path.dirname(__file__)), "db/")
        self.db = ""

    def add_condition(self, func, address):
        assert isinstance(func, str), isinstance(address, int)
        self.condition[func] = address

    #Wrapper for libc-database's find shell script.
    def decided(self):
        if len(self.condition) == 0:
            print("No leaked info provided.")
            print("Please supply more info using add_condition(leaked_func, leaked_address).")
            return

        res = []
        for name, address in self.condition.items():
            addr_last12 = address & 0xfff
            res.append(re.compile("^%s .*%x" % (name, addr_last12)))

        db = self.libc_database_path
        # only read "*.symbols" file to find
        files = [x for x in os.listdir(db) if x.endswith('.symbols')]
        
        result = []
        for ff in files:
            with open(db+ff, 'rb') as f:
                data = f.read().decode(errors='ignore').split("\n")
                for x in res:
                    if any(map(lambda line: x.match(line), data)):
                        result.append(ff)
                        break

        if len(result) == 0:
            print("No matched libc, please add more libc or try others")
            return

        if len(result) > 1:
            print("Multi Results:")
            for x, y in enumerate(result):
                print("%2d: %s" % (x, self.pmore(y)))
            print("Please supply more info using \n\tadd_condition(leaked_func, leaked_address).")
            while True:
                in_id = input(
                    "You can choose it by hand\nOr type 'exit' to quit: ")
                if in_id == "exit" or in_id == "quit":
                    return
                try:
                    in_id = int(in_id)
                    self.db = result[in_id]
                    break
                except:
                    continue
        else:
            self.db = result[0]
        print("[+] %s be choosed." % self.pmore(self.db))

    def pmore(self, result):
        result = result[:-8]  # .strip(".symbols")
        with open(self.libc_database_path + result + ".info") as f:
            info = f.read().strip()
            return("%s (id %s)" % (info, result))

    #Wrapper for libc-database's dump shell script.
    def dump(self, func=None):

        if not self.db:
            self.decided()
        if not self.db:
            return 0
        db = self.libc_database_path + self.db
        with open(db, 'rb') as fd:
            data = fd.read().decode(errors='ignore').strip("\n").split("\n")
        if not func:
            result = {}
            func = [
                "__libc_start_main_ret", "system", "dup2", "read", "write",
                "str_bin_sh"
            ]
            for ff in func:
                for d in data:
                    f = d.split(" ")[0]
                    addr = d.split(" ")[1]
                    if ff == f:
                        result[ff] = int(addr, 16)
                        print(ff, hex(result.get(ff)))
            return result

        for d in data:
            f, addr, *_ = d.split(' ', 2)
            if func == f:
                return int(addr, 16)

        print("No matched, Make sure you supply a valid function name or just add more libc.")
        return 0


def main():
    parser = Command()
    if parser.init:
        extract_libc()
    if parser.local_libc:
        parse_libc(parser.local_libc)
    if all([parser.func, parser.addr, parser.to_leak]):
        obj = LibcSearcher(parser.func, int(parser.addr, 16))
        print(f"[+] {parser.to_leak} offset: ", hex(obj.dump(parser.to_leak)))


if __name__ == "__main__":
    obj = LibcSearcher("fgets", 0x7ff39014bd90)
    print("[+]system  offset: ", hex(obj.dump("system")))
    print("[+]/bin/sh offset: ", hex(obj.dump("str_bin_sh")))
