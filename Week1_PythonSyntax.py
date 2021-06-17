# 1. odd_enen 함수 작성

## 문제에서 요구한 기본 답
def odd_even(n1: int, n2: int) -> str:
    m1, m2 = n1**2, n2**2
    return '짝수' if (m1 + m2) % 2 == 0 else '홀수'
    

## 함수 입력값을 좀 더 유연하게
from functool import reduce
def odd_even_v1(*args) -> str:
    tp = tuple([x**2 for x in args])
    return '짝수' if reduce(lambda x, y: x + y, tp) % 2 == 0 else '홀수'
 
 
# 2. Person 클래스 작성
## 문제에서 요구한 기본 답
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        
# 3. Child 클래스 작성
## 문제에서 요구하는 기본 답
class Child(Person):
    def play(self):
        print('{} is playing.'.format(self.name))
