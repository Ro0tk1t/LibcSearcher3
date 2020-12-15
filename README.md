# LibcSearcher3

(Search libc function offset)


## 简介

这是针对CTF比赛所做的小工具，在泄露了Libc中的某一个函数地址后，常常为不知道对方所使用的操作系统及libc的版本而苦恼，常规方法就是挨个把常见的Libc.so从系统里拿出来，与泄露的地址对比一下最后12位。

为了不在这一块浪费太多生命，写了几行代码，方便以后重用。

这里用了[libc-database](https://github.com/niklasb/libc-database)的数据库。

## 安装

```shell
$ git clone https://github.com/Ro0tk1t/LibcSearcher3.git
$ pip3 install -e LibcSearcher3
```

## 初始化

```bash
$ libcsearch --init
```

## 使用

### 实例化

```python
from LibcSearcher import *

#第二个参数，为已泄露的实际地址,或最后12位(比如：d90)，int类型
obj = LibcSearcher("fgets", 0X7ff39014bd90)

obj.dump("system")        #system 偏移
obj.dump("str_bin_sh")    #/bin/sh 偏移
obj.dump("__libc_start_main_ret")    
```

### 命令行

```bash
$ libcsearch --help
$ libcsearch -f fgets -d 0X7ff39014bd90 -t system
Multi Results:
 0: kali-glibc (id libc6-x32_2.31-3_amd64)
 1: ubuntu-old-eglibc (id libc6-amd64_2.13-0ubuntu13.2_i386)
 2: kali-glibc (id libc6-x32_2.31-3_i386)
 3: ubuntu-old-glibc (id libc6_2.19-10ubuntu2_amd64)
 4: archive-glibc (id libc6-amd64_2.23-0ubuntu10_i386)
Please supply more info using 
        add_condition(leaked_func, leaked_address).
You can choose it by hand
Or type 'exit' to quit: 0
[+] kali-glibc (id libc6-x32_2.31-3_amd64) be choosed.
[+] system offset:  0x40130
```

如果遇到返回多个libc版本库的情况，可以通过`add_condition(leaked_func, leaked_address)`来添加限制条件，也可以手工选择其中一个libc版本（如果你确定的话）。

## 其它

水平一般，代码很烂，如有bug，欢迎吐槽。

欢迎贡献不同linux发行版的libc信息。
