import random
from list_words import *

lst = set()

# Можно подставить свой список со словами вместо wrds в файле list_words
wrds = wrds

# Обработка списка слов
x = " ".join(line.strip().upper() for line in wrds.split('\n') if line.strip()).split(' ')

# Основная логика игры
while True:
    try:
        print("Добро пожаловать в игру Виселица, для начала игры напишите 'старт'")
        choose = input()
    
        if choose == "старт":
            lst = set()
            random_letter = list(random.choice(x))  # рандомное слово
            stars_word = list(len(random_letter) * "*")
            counter = 0
            print(stars_word)
            while True:
                indices = []
                print("\nВведите одну русскую букву: ", end='')
                char = input().upper()
                if len(char) > 1:
                    print("Введите только ОДНУ букву")
                    continue
    
                if char.upper() in lst:
                    print("Вы уже вводили эту букву, попробуйте другую")
                    print("Вы использовали эти буквы:", *sorted(lst))
                    continue
                lst.update(char.upper())
    
                if char in random_letter:
                    print("\nВы угадали букву")
                    for index, letter in enumerate(random_letter):
                        if letter == char:
                            indices.append(index)
                            stars_word[index] = char.upper()
                    print("Текущее слово: ", *stars_word)
                    print("Вы использовали эти буквы: ", *sorted(lst))
    
                else:
                    print("\nВы не угадали букву")
                    print("Вы использовали эти буквы: ", *sorted(lst))
                    counter += round(8/len(random_letter))
                    print(f"У вас {counter} ошибок из 8")
    
                if str(stars_word) == str(random_letter).upper():
                    print("\nВы победили, загаданное слово было", ''.join(random_letter))
                    break
                if counter == 8:
                    print(f"\nВы проиграли, загаданное слово было", ''.join(random_letter))
                    break
        
        elif choose == "выйти":
            print("Вы вышли")
            break
    
    except KeyboardInterrupt:
        print("\nВы вышли")
        break
        