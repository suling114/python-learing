#简易计算器，输入两个数和一个运算符，输出运算结果，不合法的运算符报错
s1 = float(input("请输入第一个数 : "))
s2 = float(input("请输入第二个数 : "))
op = input("请输入运算符 : ")
if (op == "-" ):
    print(f"{s1} - {s2} = {s1 - s2}")
elif (op == "*" ):
    print(f"{s1} * {s2} = {s1 * s2}")
elif (op == "+" ):
    print(f"{s1} + {s2} = {s1 + s2}")
elif (op == "/" ):
    if(s2 == 0):
        print("除数不能为 0 ")
    else:
        print(f"{s1} / {s2} = {s1 / s2}")
else:
    print("错误")