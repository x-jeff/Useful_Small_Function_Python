import os

#利用command拷贝文件
filename1="E:\\before\\1.png"#原始文件的路径，文件后缀自行修改
filename2="E:\\after\\2.png"#拷贝到目标路径，文件名字自行修改
os.system("copy %s %s" % (filename1,filename2))