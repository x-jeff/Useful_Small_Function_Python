string_1 = "15"

# 原字符串左侧对齐， 右侧补零
string_2 = string_1.ljust(4, '0')
print(string_2)  # 输出：1500

# 原字符串右侧对齐， 左侧补零
string_3 = string_1.rjust(4, '0')
print(string_3)  # 输出：0015
