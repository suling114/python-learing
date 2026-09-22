#根据输入的数字，打印数字金字塔
s1 = int(input("请输入您想要的数字："))
for i in range(1,s1+1):
    for j in range(1,i+1):
        print(f"{int(j)}",end =" ")
    print()