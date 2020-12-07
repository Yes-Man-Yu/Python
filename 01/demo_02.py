#
# Created by Yes.Man on 2020/12/7 14:42.
#

# 转义字符
print('hello\nworld')
print('hello\tworld')
print('hello\rworld')
print('hello\bworld')
print('https:\\\\www.baidu.com')
print('Miss Chen said: \'you are very beautiful\'' )

# 原字符，就是在字符串之前加上 r 或者 R
# 不希望字符串中的转义字符起作用，就用原字符
print(r'hello \n world')
# 注意：最后一个字符不可以单独的反斜杠 如：print(r'\n\')
print(r'\n\\')
