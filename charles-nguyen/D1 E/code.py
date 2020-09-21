f = open("WoA Coding Challenge Day 1 E.txt", "r")
sum = 0
temp = 0
for line in f:
    temp = int(line)
    sum = sum + temp

f.close()

i = 0
ans = str(sum)
print(ans)

while(i < 10):
    print(ans[i], end="")
    i = i + 1






