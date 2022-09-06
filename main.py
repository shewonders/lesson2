# lesson 2
# task 1
# li = [35, 10005, True, 'strings', 2.6, 3.777]
# for el in li:
#     print(f"element {el} belongs to type {type(el)}")

# task 2
# li = list(input('Type a sentence:'))
# length = len(li)
# if length % 2 == 0:
#     length = length
# else:
#     length = length - 1
# n = 0
# while n <= length - 2:
#     li[n], li[n + 1] = li[n+1], li[n]
#     n = n + 2
# print(f"Your sentence, with pairs of elements flipped - {li}")


# task 3-1
# mo = int(input('What month were you born in? Type its number in the year (1 to 12, counting from January):'))
# di_year = {'winter': [12, 1, 2], 'spring': [3, 4, 5], 'summer': [6, 7, 8], 'autumn': [9, 10, 11]}
# for el in di_year:
#     if mo in di_year[el]:
#         print(f"You are a(n) {el} baby")



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
# st = str(input("Type a few words separated by spaces:"))
# st1 = st.split(' ')
# n = 1
# for el in st1:
#     length = len(el)
#     if length <= 10:
#         print(f"{n} {el}")
#     else:
#         print(f"{n} {el[0:9]}")
#     n = n + 1

#task5
# ranking1 = [7, 5, 3, 3, 2]
# length = len(ranking1)
# n = 0
# x = int(input("Type an integer to be added to our ranking of [7, 5, 3, 3, 2]:"))
# while n <= (length - 1):
#     if x >= ranking1[n]:
#         ranking1.insert(n,x)
#         break
#     else:
#         n = n + 1
# print(f"Your updated ranking is {ranking1}")

# task6 (не доковыряла и принципиаьно не поняла, как не по буквам выводить на печать)
x = 3
# could be as many as needed
i = 1
g3 = []
datab = []
while i <= x:
    g1 = input("Type the product's name, price, q-ty, and measurement unit (separated by spaces):")
    g2 = tuple(g1)
    g3.extend(g1.split(" "))
    g31 = tuple(g3)
    print(g31)
    i = i + 1
j = 0
g4 = ()
while j <= (len(g31) - 1):
    g5 = tuple(g31[j])
    g4 = g4 + g5
    j = j + 4
print(f"names: {g4}")
k = 1
g6 = ()
while k <=(len(g31) - 1):
     g7 = tuple(g31[k])
     g6 = g6 + g7
     k = k + 4
print(f"prices: {g6}")
l = 2
g8 = ()
while l <=(len(g31) - 1):
     g9 = tuple(g31[l])
     g8 = g8 + g9
     l = l + 4
print(f"quantities: {g8}")
m = 3
g10 = ()
while m <= (len(g31) - 1):
    g11 = tuple(g31[m])
    g10 = g10 + g11
    m = m + 4
print(f"measurement units: {g10}")
#warehouse = dict(t[0], t[])







# dict1 = {"sku": n, "name": g2[0], "price": g2[1], "qty": g2[2], "unit": g2[3]}
# tuple1 = (n, dict1)
#     print(dict1)
#     seq = {'names', 'prices', 'qties', 'units'}
#     dict_gen = dict.fromkeys(seq,g2[1])
#     print(dict_gen)









