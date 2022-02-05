def close_point(p):
    global x, y
    return (x - p[0]) ** 2 + (y - p[1]) ** 2

x, y = map(int, input().split())
coords = []
for _ in range(int(input())):
    coords.append(tuple(map(int, input().split())))
coords.sort(key=close_point)
for i in coords:
    print(*i)
