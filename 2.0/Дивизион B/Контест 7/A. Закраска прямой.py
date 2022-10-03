N = int(input())
segment_ends = []
for _ in range(N):
    L, R = map(int, input().split())
    segment_ends.append((L, 'L'))
    segment_ends.append((R, 'R'))
segment_ends.sort()
num_of_segments = 0
length = 0
for i in range(len(segment_ends)):
    if num_of_segments > 0:
        length += segment_ends[i][0] - segment_ends[i - 1][0]
    if segment_ends[i][1] == 'L':
        num_of_segments += 1
    elif segment_ends[i][1] == 'R':
        num_of_segments -= 1
print(length)
