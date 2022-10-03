n, q = map(int, input().split())
nums = list(map(int, input().split()))
prefixsum = [0]
for num in nums:
    prefixsum.append(prefixsum[-1] + num)
for _ in range(q):
    l, r = map(int, input().split())
    print(prefixsum[r] - prefixsum[l-1])
