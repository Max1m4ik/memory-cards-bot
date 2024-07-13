# INSERT INTO (имя таблицы) (столбцы) VALUES (значения)  - вставка данных
# SELECT (столбцы) FROM (имя таблицы) WHERE (условие)  - выборка данных
# UPDATE (имя таблицы) SET (столбцы) WHERE (условие) - обновление данных
# DELETE FROM (имя таблицы) WHERE (условие) - удаление данных


cur.execute("SELECT question FROM cards") 
question = cur.fetchall() #Список вопросов
cur.execute("SELECT answer FROM cards")
answer = cur.fetchall() #Список ответов

with sq.connect('cards.db') as con:
    cur = con.cursor()

reset()
for i in range (0, num_columns-1):
    cur.execute(f"INSERT INTO cards (quastion, answer) VALUES ({question[i]}, {answer[i]})")