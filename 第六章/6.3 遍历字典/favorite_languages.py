favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
#遍历所有键值对
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
#遍历字典中的所有键
for name in favorite_languages.keys():
    print(name.title())

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}")
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}")
if 'erin' not in favorite_languages.keys():
    print("Erin please take our poll")
#按特定顺序遍历字典中的所有键
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you taking the poll.")
#遍历字典中的所有值
print("The following languages have been mentioned:")
# for language in favorite_languages.values():
#     print(language.title())
for language in set(favorite_languages.values()):
    print(language.title())