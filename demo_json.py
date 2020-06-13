import json

class PracticeJson:
    def __init__(self):
        self.data = {"z":1, "a":2, "b":3}
    #json.dumps 将dict转化为string类型；参数sort_keys为true,则去排序，为false,则不排序；参数indent表示换行
    def practice_dumps(self):
        # print("dumps之前")
        # print(type(self.data))
        # print("dumps之后")
        # print(type(json.dumps(self.data)))
        print(json.dumps(self.data, sort_keys=True , indent=4))
        # json.dump(self.data, sort_keys=True)
    #将dict类型转换为json格式字符串，存入文件
    def practice_dump(self):
        with open("./demo1.json", "w") as fs:
            json.dump(self.data, fp=fs)
    #将string类型转换为dict类型
    def practice_loads(self):

        json_data = json.dumps(self.data)
        print("loads之前")
        print(type(json_data))
        print("loads之后")
        print(type(json.loads(json_data)))
    #将json格式字符串转换为dict类型，读取文件
    def practice_load(self):
        print(json.load(open("demo.json")))