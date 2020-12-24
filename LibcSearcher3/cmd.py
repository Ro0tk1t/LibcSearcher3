#!/usr/bin/env python
# coding=utf-8

import argparse


def Command():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--init', dest='init', action='store_true', help='初始化libc库')
    parser.add_argument('-l', '--local', dest='local_libc', help='添加本地libc信息')
    parser.add_argument('-f', '--func', dest='func', help='已泄露的函数名')
    parser.add_argument('-d', '--addr', dest='addr', help='已泄露函数的实际地址')
    parser.add_argument('-t', '--to_leak', dest='to_leak', help='需要泄露的函数偏移')

    cmd = parser.parse_args()
    if not cmd.init and not cmd.local_libc and not (cmd.func and cmd.addr and cmd.to_leak):
        parser.print_usage()
    return cmd

