#!/usr/bin/env python
# coding=utf-8

import subprocess

from os import path


def extract_libc():
    fn = 'libc.tar.bz2'
    fb = path.join(path.dirname(path.abspath(__file__)), 'db/')
    fp = path.join(fb, fn)
    cmd = ['tar', '-jxf', fp, '-C', fb]
    proc = subprocess.Popen(cmd)
    print('[*] init libc database')
    try:
        proc.communicate()
    except Exception as e:
        print(e)


def parse_libc(path_):
    if not path.exists(path_):
        print('[-] libc file not exists: ', path_)
        return
    base_path = path.dirname(path.abspath(__file__))
    script = path.join(base_path, 'scripts')
    script = path.join(script, 'add')
    cmd = [script, path_]
    proc = subprocess.Popen(cmd)
    try:
        proc.communicate()
    except Exception as e:
        print(e)
