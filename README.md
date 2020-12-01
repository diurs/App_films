# App_films V.1
Application with films of the viewer's choice. The DB "Kinopoisk Top 250 films" is used here.


## First step. Start apache2 service & mysql

systemctl start apache2

systemctl start mysql

python3 windows.py

## Функции приложения


![Снимок экрана 2020-12-01 в 16 42 57](https://user-images.githubusercontent.com/61711711/100748364-4bb32300-33f4-11eb-901a-084f68441812.png)


### Поиск фильма
Здесь есть расширенный поиск по разным критериям: 
по году , рейтингу , стране , режиссеру , актеру и сценаристу.
Искать можно как по одному критерию ,так и по нескольким перечисленным выше

![Снимок экрана 2020-12-01 в 14 52 36](https://user-images.githubusercontent.com/61711711/100748438-5ec5f300-33f4-11eb-8122-06f5bd4269f5.png)


![Снимок экрана 2020-12-01 в 14 52 56](https://user-images.githubusercontent.com/61711711/100748520-78ffd100-33f4-11eb-8172-0e662cef3203.png)


![Снимок экрана 2020-12-01 в 14 53 20](https://user-images.githubusercontent.com/61711711/100748535-7dc48500-33f4-11eb-9702-b236bc5a5ec2.png)

### Поиск по нескольким критериям


![Снимок экрана 2020-12-01 в 16 15 27](https://user-images.githubusercontent.com/61711711/100748620-9a60bd00-33f4-11eb-855e-4e034bd76d15.png)


![Снимок экрана 2020-12-01 в 14 59 08](https://user-images.githubusercontent.com/61711711/100748631-9d5bad80-33f4-11eb-8275-2af8484fde3f.png)


![Снимок экрана 2020-12-01 в 14 54 39](https://user-images.githubusercontent.com/61711711/100748648-a0569e00-33f4-11eb-9d74-9b8fa49e6e97.png)


## Все топ 250

Тут все очевидно просто. Выводится весь список фильмов из БД

![Снимок экрана 2020-12-01 в 16 17 34](https://user-images.githubusercontent.com/61711711/100748687-aea4ba00-33f4-11eb-87a8-c9249a5d4d71.png)



## Рандомный фильм

![Снимок экрана 2020-12-01 в 16 17 43](https://user-images.githubusercontent.com/61711711/100748727-bd8b6c80-33f4-11eb-837b-155618718568.png)



## Самый популярный актер

Тот красавчик, который чаще всего встречается в этом топе фильмов

![Снимок экрана 2020-12-01 в 16 17 53](https://user-images.githubusercontent.com/61711711/100748770-d09e3c80-33f4-11eb-89e3-8b4fbab75391.png)

