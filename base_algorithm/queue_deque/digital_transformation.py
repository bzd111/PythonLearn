from collections import deque


def auto_change(start_value, result):
    p = deque([(start_value, 0)])
    check = {start_value}
    while True:
        current_value, times = p.popleft()
        if current_value == result:
            break
        if current_value < result:
            if current_value+1 not in check:
                p.append((current_value+1, times+1))
                check.add(current_value+1)
            if current_value*2 not in check:
                p.append((current_value*2, times+1))
                check.add(current_value*2)
        if current_value > 0 and current_value-1 not in check:
            p.append((current_value-1, times+1))
            check.add(current_value-1)
    return p.popleft()[-1]

result = auto_change(3, 11)
print(result)