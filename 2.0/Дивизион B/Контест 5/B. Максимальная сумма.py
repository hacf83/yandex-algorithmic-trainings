n = int(input())
nums = list(map(int, input().split()))
prefixsum = [0]
for num in nums:
    prefixsum.append(prefixsum[-1] + num)
l = 0
max_sum = prefixsum[1]
for r in range(1, len(prefixsum)):
    if prefixsum[r] < 0:
        l = r
        continue
    max_sum = max(prefixsum[r] - prefixsum[l], max_sum)
print(max_sum)