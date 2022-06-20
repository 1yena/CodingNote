

import time

# 시간초 세기 게임

input("엔터를 누르고 10초를 세보세요.")

start = time.time()

input("10초를 센 다음에 엔터를 누르세요.")

end = time.time()

t_interval = end - start

print("실제 시간 : ", t_interval, "초")
print("시간차 : ", abs(10-t_interval), "초")

