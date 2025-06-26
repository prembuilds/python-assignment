import random

parent_list = [random.randint(1, 100) for _ in range(15)]
print("Original List of 15 Numbers:")
print(parent_list)

random.shuffle(parent_list)
list1 = parent_list[0:5]
list2 = parent_list[5:10]
list3 = parent_list[10:15]

sum1 = sum(list1)
sum2 = sum(list2)
sum3 = sum(list3)

print("\nSublist 1:", list1, "→ Sum:", sum(list1))
print("Sublist 2:", list2, "→ Sum:", sum(list2))
print("Sublist 3:", list3, "→ Sum:", sum(list3))

sums = [sum(list1), sum(list2), sum(list3)]
largest_sum = max(sums)

if ((sum1 > sum2) and (sum1 > sum3)):
    print(f"{sum1} is the winner")
elif (sum2 > sum3):
    print(f"{sum2} is the largest sum")
else:
    print(f"{sum3} is the largest sum")