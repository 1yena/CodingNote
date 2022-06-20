

import random


# 랜덤숫자 업다운게임

print("숫자 업다운 게임입니다.")
print("1부터 100사이의 숫자가 랜덤으로 표시됩니다.")
print()

a = random.randint(1, 100)
# print(a)
c = 1


while 1:

    b = int(input("숫자를 입력하세요 : "))

    if b == a:
        print("정답입니다. 총", c, "번만에 맞추셨습니다.")
        break
    elif b > a:
        print("다운")
        c += 1
    elif b < a:
        print("업")
        c += 1


