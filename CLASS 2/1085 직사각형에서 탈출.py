x, y, w, h = map(int, input().split())

min_x = w - x if w - x < x else x
min_y = h - y if h - y < y else y

print(min_x if min_x <= min_y else min_y)
