from collections import deque


def palindrome(str_rts):
    double_queue = deque()

    for i in str_rts:
        double_queue.append(i)