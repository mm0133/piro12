a = int(input())

for i in range(1, a):
    j = str(i)
    sum = 0;
    for k in range(len(j)):
        sum += int(j[k])
    sum += i

    if sum == a:
        print(i)
        break;
if sum!=a:
    print(0)


