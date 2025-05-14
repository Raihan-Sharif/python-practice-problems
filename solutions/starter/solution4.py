numbers=[3, 5, 1, 9, 7, 2, 8 ]

index_of_7 = -1

for index in range(len(numbers)):
    if numbers[index] == 7:
        index_of_7 = index
        break

print(f"The index of 7 is: {index_of_7}")