# Yatube_project

Добро пожаловать в проект Yatube, социальную сеть для писателей, желающих поделиться своим оригинальным контентом. Этот файл README доступен на нескольких языках:

- [English](README.md)
- [Русский](README.ru.md)

Пожалуйста, выберите предпочитаемый язык для продолжения.

## Описание
Yatube - это социальная сеть для писателей, которые хотят поделиться своим оригинальным контентом с единомышленниками. Это приветливое пространство для творческого самовыражения и связи между авторами.

### Возможности
- **Последние посты:** Пользователи могут просматривать самые свежие публикации, чтобы быть в курсе последних новостей.
- **Посты из групп:** Возможность просмотра публикаций по группам позволяет сосредоточиться на интересующих тематиках.
- **Размещение постов:** Авторы могут публиковать свои посты через административную панель, делая процесс удобным и быстрым.
- **Группы:** Создание и управление группами обеспечивает сбор единомышленников вокруг общих интересов.

### Технологии
- Python 3.9
- Django 2.2.19

### Запуск проекта в режиме разработки
1. Клонируйте репозиторий и перейдите в его директорию:
   ```sh
   git clone git@github.com:nir0k/yatube_project.git
   cd yatube_project
   ```
2. Установите и активируйте виртуальное окружение:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```
3. Установите зависимости из файла requirements.txt:
    ```sh
    python3 -m pip install --upgrade pip
    pip install -r requirements.txt
    ``` 
4. Выполните миграции и создайте суперпользователя:
    ```sh
    cd yatube
    python3 manage.py migrate
    python3 manage.py createsuperuser
    ```
- Запустите сервер разработки:
    ```sh
    python3 manage.py runserver
    ```

### Использование
- Просмотр постов: Откройте http://localhost:8000 для просмотра публикаций.
- Административная консоль: Для управления постами и группами используйте http://localhost:8000/admin.