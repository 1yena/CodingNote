

# while문과 for문을 활용한 구구단


print("구구단을 시작합니다.")
print()
c = input("엔터를 누르면 구구단을 시작합니다.")
a = 2
b = 1

# 0 ~ 8 : 9개
for i in range(8):
    print("이번에 할 구구단은 ", a, "단입니다.")
    b = 1
    for j in range(9):
        print(a, "*", b, "=", a*b)
        b += 1
    a += 1
    print("===================")
print("구구단을 마칩니다.")

