# 文件读取
f = open("./io.py" , mode="w" , encoding="utf-8")
try:
    f.write("#\n")
finally:
    f.close()

# with推荐使用，可以确保每次资源得到释放
with open("./io.py" , mode="r" , encoding="utf-8") as f:
    f.write("#\n")
