import json
# 写入json文件
usre = {
    "name" : "宇崎崎",
    "age" : "22"
}
with open("./resources/test.json" , mode="w" , encoding="utf-8") as f:
    # 写入
    json.dump(usre, f , ensure_ascii=False, indent=4)

with open("./resources/test.json" , mode="r" , encoding="utf-8") as f:
    # 读取
    user = json.load(f)
    print(type(usre))