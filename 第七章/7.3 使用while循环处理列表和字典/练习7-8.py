sandwich_orders = [
    '五香烟熏牛肉', '蔬菜', '烤奶酪', '五香烟熏牛肉',
    '火鸡', '烤牛肉', '五香烟熏牛肉']
finished_sandwiches = []

print("很抱歉，我们今天的五香烟熏牛肉卖完了.")
while '五香烟熏牛肉' in  sandwich_orders:
    sandwich_orders.remove('五香烟熏牛肉')

print("\n")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"我正在做你的{current_sandwich}三明治.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print(f"我制作好了{sandwich}三明治.")