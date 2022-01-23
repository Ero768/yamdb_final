![example workflow](https://github.com/<OWNER>/<REPOSITORY>/actions/workflows/<WORKFLOW_FILE>/badge.svg

# Проект YaMDb
Проект YaMDb собирает отзывы (Review) пользователей на произведения (Titles). Произведения делятся на категории: «Книги», «Фильмы», «Музыка». Список категорий (Category) может быть расширен администратором (например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»).
Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.
В каждой категории есть произведения: книги, фильмы или музыка. Например, в категории «Книги» могут быть произведения «Винни-Пух и все-все-все» и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» группы «Насекомые» и вторая сюита Баха.
Произведению может быть присвоен жанр (Genre) из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»). Новые жанры может создавать только администратор.
Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы (Review) и ставят произведению оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — рейтинг (целое число). На одно произведение пользователь может оставить только один отзыв.

## Запуск проекта в контейнере docker:
 Для запуска необходим фаил .env содержащий следующие переменные:
 ```
 DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql
 DB_NAME=postgres # имя базы данных
 POSTGRES_USER=postgres # логин для подключения к базе данных
 POSTGRES_PASSWORD=postgres # пароль для подключения к БД (установите свой)
 DB_HOST=db # название сервиса (контейнера)
 DB_PORT=5432 # порт для подключения к БД
```
1.  собрать контейнера 
    ```shell
    docker-compose up -d --build
    ```
2. выполнить миграции внутри контейнера:
    ```shell
    docker-compose exec web python manage.py migrate --noinput
    ```
3. собрать статику внутри контейнера:
    ```shell
    docker-compose exec web python manage.py collectstatic --no-input
    ```
4. импортировать тестовые данные: 
    ```shell
    docker-compose exec web python manage.py loaddata fixtures.json
    ```
После запуска документацию можно посмотреть по адресу http://localhost/redoc/