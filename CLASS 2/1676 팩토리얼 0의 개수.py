N = int(input())
f = 1
cnt = 0

for i in range(1, N+1):
    f = f * i

f = list(str(f))
f.reverse()

for i in f:
    if i == '0':
        cnt += 1
    else:
        break

print(cnt)
