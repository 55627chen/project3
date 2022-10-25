import random

List = []
odd = 0
even = 0

for i in range(1, 11):
    degree = random.randint(1, 5)
    List.append(degree)

    if (degree % 2) == 0:
        odd += 1
    else:
        even += 1

print("====== 10個整數 如下 ======")
print(List)
print(f"====== 偶數有:{odd}  個======")
print(f"====== 奇數有:{even} 個======")
print(f"====== 最大值:{max(List)}  ======")
print(f"====== 最小值:{min(List)}  ======")
print(f"====== 加總 :{sum(List)}  ======")
print(f"====== 平均值:{float(sum(List))/5}  ======")
print(f"====== 1出現:{List.count(1)} 次  ======")
print(f"====== 2出現:{List.count(2)} 次  ======")
print(f"====== 3出現:{List.count(3)} 次  ======")
print(f"====== 4出現:{List.count(4)} 次  ======")
print(f"====== 5出現:{List.count(5)} 次  ======")
# print(vars())
