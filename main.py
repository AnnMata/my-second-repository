import random

my_list = ['камень', 'ножницы', 'бумага']
my_score = 0
comp_score = 0

while my_score < 3 and comp_score < 3:
  my_choice = input("Выберите камень, ножницы или бумага: ")
  random_element = random.choice(my_list)

  if my_choice == random_element:
    print(f"Ничья! Оба игрока выбрали {my_choice}.")

  elif my_choice == "камень":
    if random_element == "ножницы":
      print("Камень бьет ножницы! Вы победили!")
      my_score += 1

    else:
      print("Бумага оборачивает камень! Вы проиграли.")
      comp_score += 1

  elif my_choice == "ножницы":

    if random_element == "камень":
      print("Камень бьет ножницы! Вы проиграли.")
      comp_score += 1
    else:
      print("Ножницы режут бумагу! Вы победили!")
      my_score += 1

  elif my_choice == "бумага":
    if random_element == "камень":
       print("Бумага оборачивает камень! Вы победили!")
       my_score+=1
    else:
      print("Ножницы режут бумагу! Вы проиграли.")
      comp_score+=1
  print(f"Счет: {my_score}:{comp_score}")

if my_score == 3:
  print(f"Вы победили со счетом {my_score}:{comp_score}")
else:
  print(f"Вы проиграли со счетом {my_score}:{comp_score}")

