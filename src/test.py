
# [6,5,3,4]
# 3 2 0 1

num_robot = 4
robot = [6, 5, 3, 4]

res = [0 for i in range(num_robot)]
last = robot[-1]
for i in range(num_robot - 1, -1, -1):
    for j in range(i-1, -1, -1):
        if robot[j] >= robot[i]:
            res[j] += 1
            break

print(res)

print(robot[res.index(max(res))])