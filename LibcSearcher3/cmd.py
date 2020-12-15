#!/usr/bin/env python
# coding=utf-8

import argparse


def Command():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--init', dest='init', action='store_true', help='初始化libc库')
    parser.add_argument('-f', '--func', dest='func', help='已泄露的函数名')
    parser.add_argument('-d', '--addr', dest='addr', help='已泄露函数的实际地址')
    parser.add_argument('-t', '--to_leak', dest='to_leak', help='需要泄露的函数偏移')

    commands = parser.parse_args()
    return commands
