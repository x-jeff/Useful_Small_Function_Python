import os

path = "E:\\result_review\\JointsInfo"  # 修改为自己的路径
file_list = os.listdir(path)  # 列出该路径下所有的文件
suffix = ".txt"  # 修改为自己需要的文件后缀
suffix_list = []
for file in file_list:
    if os.path.splitext(file)[1] == suffix:
        suffix_list.append(file)
