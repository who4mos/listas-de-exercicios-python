nums = []

for i in range(3):
    nums.append(int(input(f"Digite o {i+1}o numero: ")))

for i in sorted(nums, reverse=True):
    print(i, end=" ")

print()
