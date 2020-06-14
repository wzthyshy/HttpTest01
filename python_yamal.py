
import yaml

data = [1, 2, 3]

# with open("demo.yml","w") as f:
#     yaml.dump(data,f)

'''
函数yaml.load将yaml文档转换为python对象
'''
print(yaml.safe_load(open("./demo.yml")))

