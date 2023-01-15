secret_word = input("\nВведите слово:")
print("\033[2J")
win = False
all_letters = []
true_letters = []
points = [0, 0, 0]
counter = 0
final_points = ''
for item in secret_word:
    if item not in final_points:
        final_points += item
final_points = len(final_points)
while win==False:
    if counter== 0:
        letter = input("\nИгрок 1 введите букву:")
        counter+= 1
    elif counter== 1:
        letter = input("\nИгрок 2 введите букву:")
        counter += 1
    elif counter== 2:
        letter = input("\nИгрок 3 введите букву:")
        counter -= 2
    if letter in all_letters:
        print("Была такая буква!")
    elif letter in secret_word:
        all_letters.append(letter)
        true_letters.append(letter)
        print("Вы угадали букву", letter)
        if counter == 0:
            points[0] += 1
            print("Ваши очки:", points[0])
        elif counter == 1:
            points[1] += 1
            print("Ваши очки:", points[1])
        elif counter == 2:
            points[2] += 1
            print("Ваши очки:", points[2])
        for item in secret_word:
            if item in true_letters:
                print(item, end="")
            else:
                print('*', end="")
    else:
        print("Нет такой буквы!")
        print("Ваши очки не изменились")
    if points[2] + points[1] + points[0] == final_points:
        win = True
print("Очки игроков:")
print("Игрок 1:", points[0])
print("Игрок 2:", points[1])
print("Игрок 3:", points[2])
