fruit = 'banana'

index = len(fruit) - 1

while index >= 0:
    letter = fruit[index]
    print (letter)
    index = index -1

#going forwards code is
# fruit = 'banana'
#index = 0
# while index < len(fruit)
#     letter = fruit[index]
#     print(letter)
#     index = index + 1

for char in fruit: #alternative code for printing all letters forward
    print (char)