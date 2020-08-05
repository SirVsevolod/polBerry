phrase = "don't panic"
plist = list(phrase)
print(phrase)
print(plist)

for i in range(3):
    plist.pop()
plist.remove("'")
plist.remove("d")
plist.append(plist.pop(2))
plist.insert(3,plist.pop(5))
plist.append(plist.pop(4))

new_phrase = "".join(plist)
print(plist)
print(new_phrase)

#on tap