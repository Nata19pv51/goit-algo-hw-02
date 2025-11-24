from collections import deque


def palindrome(str_rts):
    double_queue = deque()
    for i in str_rts:
        double_queue.append(i)

    while len(double_queue) > 1:
        if double_queue.pop() != double_queue.popleft():
            return False
    return True


print(palindrome("akzka"))
print(palindrome("kazka"))