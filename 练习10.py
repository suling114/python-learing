#输入三个数字，并求最大值，最小值，平均值
num_list = [] #定义一个空列表

for i in range(3):
    num = int(input("请输入一个有效数字： "))
    num_list.append(num)#将输入的数字加入列表
print("数字列表为：",num_list)
num_list.sort()
print("排序成功后的数字列表为：",num_list)
print("最小值为：",num_list[0])
print("最大值为：",num_list[-1])
print("平均值为：",sum(num_list)/len(num_list))