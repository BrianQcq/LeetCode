# import sys 
# if __name__ == "__main__":
#     m, n = sys.stdin.readline().strip().split()
#     temp = sys.stdin.readline().strip()
#     salaries = list(map(int, temp.split()))
#     print(salaries)

#     ref = {}
#     for salary in salaries:
#         if salary not in ref:
#             ref[salary] = 1
#         else:
#             ref[salary] += 1
#     print(ref)


# import sys 
# if __name__ == "__main__":
#     num_set = int(sys.stdin.readline().strip())
#     for i in range(num_set):
# 	    n, k = sys.stdin.readline().strip().split()
# 	    temp = sys.stdin.readline().strip()
# 	    zhuzi = list(map(int, temp.split()))
	    
# 	    n, k = int(n), int(k)
# 	    dp = [0] * n
# 	    for i in range(k+1):
# 	        if zhuzi[i] > zhuzi[0]:
# 	            dp[i] = 1
# 	    for i in range(k, n):
# 	        temp = []
# 	        for j in range(i-k,i):
# 	            if zhuzi[i] > zhuzi[j]:
# 	                temp.append(dp[j]+1)
# 	            else:
# 	                temp.append(dp[j])
# 	        dp[i] = min(temp)

# 	    if dp[-1] <= 1:
# 	        print('YES')
# 	    else:
# 	        print('NO')

import sys 
if __name__ == "__main__":
    n, B = sys.stdin.readline().strip().split()
    temp = sys.stdin.readline().strip()
    nums = list(map(int, temp.split()))
    
    n, B = int(n), int(B)
    min_diff = float('inf')
    
    for i in range(1, B//2 + 1):
        temp_nums = [1] * (n - 2)
        if B % i == 0:
            temp_nums += [B//i, i]
            temp_diff = sum([abs(nums[i]-temp_nums[i]) for i in range(n)])
            if temp_diff < min_diff:
                min_diff = temp_diff
    print(min_diff)