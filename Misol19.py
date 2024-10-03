royxat = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

toq = list(filter(lambda son: son % 2 != 0, royxat))
juft = list(filter(lambda son: son % 2 == 0, royxat))

print(f"Juft sonlar: {juft}")
print(f"Toq sonlar: {toq}")