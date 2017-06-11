thatfile = open("THAT_FILE.txt", "r")
count = 0
text = thatfile.read()
print(text)
for char in text:
    if char.isupper():
        count += 1

print(count)
