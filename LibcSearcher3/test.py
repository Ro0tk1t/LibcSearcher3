from LibcSearcher3 import *

#第二个参数，为已泄露的实际地址,或最后12位(比如：d90)，int类型
obj = LibcSearcher("fgets", 0x7ff39014bd90)

obj = LibcSearcher("fgets", 0x7ff39014bd90) # 使用一个已知符号地址作为初始约束，初始化 LibcSearcher
obj.add_condition("atoi", 218528) # 添加一个约束条件

print("[+]/bin/sh offset: ", hex(obj.dump("str_bin_sh"))) # 根据已有约束条件，查询某个符号在 Libc 中的地址
print("[+]system  offset: ", hex(obj.dump("system")))
