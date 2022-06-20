# while 반복문

import random


x= random.randint(0, 100)
# print(x)


while True:
    a= input('컴퓨터가 생각하는 숫자를 입력해보세요 : ')
    a= int(a)
    print(a)
    print(type(a))

    if x == a:
        print('정답입니다.')
        print('잘하시는군요.\n')
        break
    elif x > a:
        print('오답입니다.')
        print('%d보다 큰수를 입력하세요.\n'%a)
    else:
        print('오답입니다.')
        print('%d보다 작은수를 입력하세요.\n'%a)










