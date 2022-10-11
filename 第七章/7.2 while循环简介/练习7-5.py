prompt = "请输入年龄："
prompt += "\n完成后输入'quit'。"

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print("您可以免费观看")
    elif age < 13:
        print("您的票价为10美元。")
    else:
        print("您的票价为15美元。")