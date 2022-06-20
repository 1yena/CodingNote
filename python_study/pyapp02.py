

import time

# 시간 초 세기 게임 (+오차율)

print("초세기 감각 게임 !")
print("")

a = int(input("숫자 입력하기 : "))
b = ('엔터를 누르는 순간부터', a, '초를 세기 시작하세요!')

input(b)

start = time.time()

c = (a, '초를 센 다음에 엔터를 누르세요.')

input(c)

end = time.time()

t_interval = end - start

tte = a - t_interval

print("실제 시간 : ", t_interval, "초")
print("시간차 : ", tte, "초")

# 오차율 구하기
if t_interval > a:
    d = a / t_interval * 100
    print("실제 시간보다 늦군요 !", d, "%만큼 초과했습니다~")

if t_interval < a:
    d = t_interval / a * 100
    print("실제 시간보다 빠르군요 !", d, "%만큼 못 미칩니다.")


