name_prompt = "\n你叫什么？"
place_prompt = "如果你能去世界上的一个地方，你会去哪里？"
continue_prompt = "\n你想让别人回答吗？(yes/no)"

#调查结果将存储在形如{name: place}的字典中。
responses = {}

while True:
    #询问用户想去哪里度假
    name = input(name_prompt)
    place = input(place_prompt)

    #存储调查结果
    responses[name] = place

    #询问是否还有其他人要参与调查。
    repeat = input(continue_prompt)
    if repeat !='yes':
        break

#显示调查结果
print("\n-- Results --")
for name, place in responses.items():
    print(f"{name.title()}想参观{place.title()}")