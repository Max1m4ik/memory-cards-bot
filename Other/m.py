answ = ""
# Получаем список со строками из файла
file_path = "cards.txt"

with open(file_path) as file_object:
  lines = file_object.readlines()


#Нечётные строки - вопрос, чётные - ответ
#Узнаём что хочет пользователь
cu ="Да"
while cu == "Да":
  chouse = int(input("Что вы хотите сделать?\n1 - Проверить знания\n2 - Редоктировать карточки\n3 - Список карточек ")) 
  print("")
  if chouse == 1:
    #Проверка что в файле чётное количество строк (есть отвт на каждый вопрос)
    
  elif chouse == 2: #Если пользователь выбрал редоктирование
    #Узнаём что хочет пользователь
    q = "Да"
    while q == "Да":
      chouse1 = int(input("Что вы хотите сделать?\n1 - Добавить карточку\n2 - Удалить карточку\n3 - Изменить карточку ")) 
      print("")
      if chouse1 == 1: #Если добавить карточку
        with open(file_path, 'a') as file_object:
          file_object.write(input("Введите вопрос: ") + "\n")
          file_object.write(input("Введите ответ: ") + "\n")
          print("")
          q = input("Хотите ещё редактировать? (Да/Нет)? ").title()
      elif chouse1 == 2: #Если удалить карточку
        #Присвоиваем карточкам номер и спрашиваем под каким 
        #номером карточку удалить
        #Удаляем выбранную карточку из списка полученного в 
        #начале
        #Стираем файл и записываем в него всё что осталось в 
        #списке
        c = -2
        with open(file_path) as file_object:
          lines = file_object.readlines()
        for i in range(0, len(lines), 2):
          c += 2
          print(f"{c} - {lines[i]}")
        del_card = int(input("Введите номер карточки которую хотите удалить: "))
        print("")
        del lines[del_card]
        del lines[del_card]
        with open(file_path, 'w') as file_object:
          for i in range(0, len(lines)):
            file_object.write(lines[i])
            #file_object.write(lines[i + 1] + "\n")
        q = input("Хотите ещё редактировать? (Да/Нет)? ").title()
      elif chouse1 == 3: #Если изменить карточку
        c = -2
        with open(file_path) as file_object:
          lines = file_object.readlines()
        for i in range(0, len(lines), 2):
          c += 2
          print(f"{c} - {lines[i]}")
        r_card = int(input("Введите номер карточки которую хотите изменить: "))
        print("")
        lines[r_card] = input("Введите вопрос: ") + "\n"
        lines[r_card + 1] = input("Введите ответ: ") + "\n"
        with open(file_path, 'w') as file_object:
          for i in range(0, len(lines)):
            file_object.write(lines[i])
        q = input("Хотите ещё редактировать? (Да/Нет)? ").title()
    cu = input("Вы хотите выйти в меню? (Да/Нет)? ").title()
    print("")
  elif chouse == 3:
    cc = 0
    with open(file_path) as file_object:
      lines = file_object.readlines()
    for i in range(0, len(lines), 2):
      cc += 1
      print(f"{cc} - {lines[i]}")
    cu = input("Вы хотите выйти в меню? (Да/Нет)? ")