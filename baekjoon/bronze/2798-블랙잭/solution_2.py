from itertools import combinations

n, T = map(int, input().split())
nums = list(map(int, input().split()))

max_sum = 0

for comb in combinations(nums, 3):
    total = sum(comb)
    if total <= T:
        max_sum = max(max_sum, total)

print(max_sum)
