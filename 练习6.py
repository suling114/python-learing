#编写一个简易的游戏角色移动控制系统，根据玩家输入的不同指令，控制游戏角色执行相应的动作（输出控制台）
oper = input("请输入操作：")
match oper:
    case "w"| "W":
        print("往前移动")
    case "a" |"A":
        print("往左移动")
    case "s" |"S":
        print("往后移动")
    case "d" |"D":
        print("往右移动")
    case " " :
        print("角色跳跃")
    case "j" |"J":
        print("角色攻击")
    case "esc"| "ESC":
        print("角色退出游戏")