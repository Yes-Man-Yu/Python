#
# Created by Yes.Man on 2020/12/7 10:51.
#

# 输出函数 print()

# 可以输出数字
print(666)
print(520)

# 可以输出字符串
print('hello world')
print("hello world")

# 含有运算符的表达式
print(3 + 1)

# 将数据输出到文件中
fp = open('./py.txt', 'a+')
print('hello world', file=fp)
fp.close()

# 输出不换行
print('hello', 'world', 'Python')
