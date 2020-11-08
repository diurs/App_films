# App_films
Application with films of the viewer's choice. The DB "Kinopoisk Top 250 films" is used here.
БД  - на локальном сервере.


## First step. Start apache2 service & mysql

systemctl start apache2
systemctl start mysql

## Функции приложения

### Поиск фильма
Здесь есть расширенный поиск по разным критериям: 
по году , рейтингу , стране , режиссеру , актеру и сценаристу.
Искать можно как по одному критерию ,так и по нескольким перечисленным выше

## Все топ 250

Тут все очевидно просто. Выводится весь список фильмов из БД

## Рандомный фильм

## Самый популярный актер

Тот красавчик, который чаще всего встречается в этом топе фильмов
