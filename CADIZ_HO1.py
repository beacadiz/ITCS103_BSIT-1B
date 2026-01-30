# Hands-On 1. Word vs Number Average 

cutesie= input("\nEnter a word: ")
length = len (cutesie)

number = []

for i in range(length):
    cutesie = int(input(f"Enter the number {i + 1 }: "))
    number.append(cutesie)

print(number)
print(f"The length of the word is {i + 1}.")

ave = sum(number) / len(number)

print(f"The average of the numbers is {ave}.")

if length < ave:
    print(f"The length of the word '{cutesie}' is less than the average.\n")
elif length < ave:
    print(f"The length of the word '{cutesie}' is greater than the average.\n")
else:
    print(f"The length of the word '{cutesie}' is equal to the average.\n")