
a = int(input())
b = int(input())

count = 0

for min in range((b+1),a):
    if min%2!=0:
        count+=min

print(count)