#用循环来数字符串中特定字符个数
s = "hello world"
target = "l"
count = 0
for ch in s:
    if ch == target:
        count += 1
print(f"这个单词里面l的个数是{count}")
