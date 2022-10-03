N = int(input())
cargo_inspection = []
for _ in range(N):
    T, L = map(int, input().split())
    cargo_inspection.append((T, 'start'))
    cargo_inspection.append((T + L, 'end'))
cargo_inspection.sort()
num_of_cargo = 0
max_num_of_cargo = 0
for i in range(len(cargo_inspection)):
    if cargo_inspection[i][1] == 'start':
        num_of_cargo += 1
    elif cargo_inspection[i][1] == 'end':
        num_of_cargo -= 1
    max_num_of_cargo = max(num_of_cargo, max_num_of_cargo)
print(max_num_of_cargo)
