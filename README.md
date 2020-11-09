# App_films
Application with films of the viewer's choice. The DB "Kinopoisk Top 250 films" is used here.
БД  - на локальном сервере.


## First step. Start apache2 service & mysql

systemctl start apache2
systemctl start mysql

## Функции приложения


![Снимок экрана 2020-11-09 в 13 39 22](https://user-images.githubusercontent.com/61711711/98531697-c4a9d980-2291-11eb-8805-845b7e0ae7b6.png)


### Поиск фильма
Здесь есть расширенный поиск по разным критериям: 
по году , рейтингу , стране , режиссеру , актеру и сценаристу.
Искать можно как по одному критерию ,так и по нескольким перечисленным выше

![Снимок экрана 2020-11-09 в 13 41 18](https://user-images.githubusercontent.com/61711711/98531587-9a581c00-2291-11eb-8204-0575ce143599.png)

## Все топ 250

Тут все очевидно просто. Выводится весь список фильмов из БД

![Снимок экрана 2020-11-09 в 13 39 40](https://user-images.githubusercontent.com/61711711/98531757-dbe8c700-2291-11eb-943c-7e58693bb0ba.png)


## Рандомный фильм

![Снимок экрана 2020-11-09 в 13 39 54](https://user-images.githubusercontent.com/61711711/98531730-d2f7f580-2291-11eb-90d0-c53b1f26210a.png)


## Самый популярный актер

Тот красавчик, который чаще всего встречается в этом топе фильмов

(в процессе разработки)
