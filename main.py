# lesson 2
# task 1
# li = [35, 10005, True, 'strings', 2.6, 3.777]
# for el in li:
#     print(f"element {el} belongs to type {type(el)}")

# task 2
li = list(input('Type 10 integers:'))
n = 0
length = len(li)
if length % 2 == 0:
    length = length
else:
    length = length - 1
while n <= length - 1:
    li[n], li[n + 1] = li[n+1], li[n]
    n = n + 2
print(f"Your list, with pairs of elements flipped, {li}")


# task 3-1
# mo = input('What month were you born in? Type its number in the year (1 to 12, counting from January):')
# di_year = {'winter': [12, 1, 2], 'spring': [3, 4, 5], 'summer': [6, 7, 8], 'autumn': [9, 10, 11]}
# for el in di_year:
#     if mo in el:
#         print(f"You are a(n) {el} baby")
#         break

# task 3-2
# mo = input('What month were you born in? Type its number in the year (1 to 12, counting from January):')
# di_year = ['12, 1, 2', '3, 4, 5', '6, 7, 8', '9, 10, 11']
# if mo in di_year[0]:
#     print("You are a winter baby")
# elif mo in di_year[1]:
#     print("You are a spring baby")
# elif mo in di_year[2]:
#     print("You are a summer baby")
# elif mo in di_year[3]:
#     print("You are an autumn baby")
# else:
#     print('Invalid value')

# task4




