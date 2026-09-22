#用户名密码登录，正确的用户名和密码为admin/666888,zhangsan/123456,taoge/888666,有5次登录机会，若输入错误五次即不允许再操作
for i in range(1,6):
    username = input("请输入用户名：")
    password = input("请输入密码：")
    if username == "admin" and password == "666888":
        print("登录成功！")
        break
    elif username == "zhangsan" and password == "123456":
        print("登录成功！")
        break
    elif username == "taoge" and password == "888666":
        print("登录成功！")
        break
    else:
        print("登录失败")
else:
    print("尝试次数过多，账号已锁定")

