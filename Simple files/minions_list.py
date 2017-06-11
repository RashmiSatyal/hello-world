data = [1, 1, 2, 3, 4, 4, 4, 5]
n = 2
output_list = []
for i in data:
    if data.count(i) < n:
        output_list.append(i)

print(output_list)
