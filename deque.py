from collections import deque
def palindrome(word):
    dq = deque(word)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True

print(palindrome('racecar'))
print(palindrome('radar'))

def another_palindrome(word):
    return word == word[::-1]

print(another_palindrome('radar'))
print(another_palindrome('halibut'))