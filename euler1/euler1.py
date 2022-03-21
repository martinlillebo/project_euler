# Fetching input
print("type in a number: ")
number = int(input())

# initialising variables
multiples_of_3_or_5 = []

# Skal finne alle tall som er multipler av enten 3 eller 5
for i in range(1, number):
	if i % 3 == 0 or i % 5 == 0:
		multiples_of_3_or_5.append(i)
		# print(i)

print(multiples_of_3_or_5)
sum_multiples = sum(multiples_of_3_or_5)
print("Sum: ", sum_multiples)
pause = input()
