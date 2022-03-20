# api_yatube
API к социальной сети Yatube
### Как запустить проект (Windows)
Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/plngu/api_yatube.git
cd api_yatube
```
Cоздать и активировать виртуальное окружение:
```
python -m venv venv
source venv/Scripts/activate
```
Установить зависимости из файла requirements.txt:
```
python -m pip install --upgrade pip
python pip install -r requirments.txt
```
Сделать миграции и запустить проект:
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
### Набор доступных эндпоинтов:
- ```posts/``` - отображение постов и публикаций (GET, POST);
- ```posts/{id}/``` - получение, изменение, удаление поста с соответствующим id (GET, PUT, PATCH, DELETE);
- ```posts/{post_id}/comments/``` - получение комментариев к посту с соответствующим post_id и публикация новых комментариев(GET, POST);
- ```posts/{post_id}/comments/{id}/``` - получение, изменение, удаление комментария с соответствующим id к посту с соответствующим post_id (GET, PUT, PATCH, DELETE);
- ```posts/groups/``` - получение описания зарегестрированных сообществ (GET);
- ```posts/groups/{id}/``` - получение описания сообщества с соответствующим id (GET);
- ```posts/follow/``` - получение информации о подписках текущего пользователя, создание новой подписки на пользователя (GET, POST).
