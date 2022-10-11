number = input("请输入一个数字：")
number = int(number)

if number % 10 == 0:
    print(f"{number}是十的整数倍")
else:
    print(f"{number}不是十的整数倍")