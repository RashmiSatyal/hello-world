# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

result = 0
max_index1 = -1
max_index2 = -1

for i in range(0, n):
    if (max_index1 == -1 or a[i]>a[max_index1] ):
    	max_index1 = i



for j in range(0, n):
 	if (j != max_index1 and (max_index2 == -1 or a[j]>a[max_index2] )):
 		max_index2 = j

         

#        if a[i]*a[j] > result:
#            result = a[i]*a[j]

result = a[max_index2]*a[max_index1]

print(result)

