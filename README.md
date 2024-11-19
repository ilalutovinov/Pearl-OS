<h1 align="center">Welcome to the project Pearl OS! <img src="https://media.giphy.com/media/hvRJCLFzcasrR4ia7z/giphy.gif" width="40"></h1>
<br />

![Без названия (49)](documents/Без%20названия%20(49).png)

<br />

```bash
Pearl OS/                        # Главная папка проекта
│
├── templates/                    # Папка для HTML-шаблонов
│   ├── accounts/                 # Шаблоны для приложения аккаунтов
│   │   ├── create-account.html   # Страница регистрации
│   │   └── login.html            # Страница логина
│   │
│   ├── pages/                    # Папка для отдельных статических страниц
│   │   ├── 404.html              # Страница ошибки 404
│   │   ├── blank.html            # Пустая страница
│   │   ├── buttons.html          # Страница с кнопками
│   │   ├── cards.html            # Страница с карточками
│   │   ├── charts.html           # Страница с графиками
│   │   ├── forms.html            # Страница с формами
│   │   ├── modals.html           # Страница с модальными окнами
│   │   └── tables.html           # Страница с таблицами
│   │
│   └── index.html                # Главная страница
│
├── static/                       # Папка для статических файлов
│   ├── assets/                   # Статические ресурсы (CSS, JS, изображения)
│   │   ├── css/                  # CSS файлы
│   │   │   ├── tailwind.css      # Основной CSS файл
│   │   │   └── tailwind.output.css # Скомпилированный CSS файл
│   │   │
│   │   ├── js/                   # JS файлы
│   │   │   ├── charts-bars.js    # Скрипт для диаграмм в виде столбцов
│   │   │   ├── charts-lines.js   # Скрипт для линейных диаграмм
│   │   │   └── charts-pie.js     # Скрипт для круговых диаграмм
│   │   │
│   │   └── img/                  # Изображения для проекта
│   │       ├── login-office.jpeg      # Изображение для страницы логина
│   │       ├── create-account-office.jpeg # Изображение для страницы регистрации
│   │       └── dashboard.png     # Изображение для панели управления
│
├── dashboard/                    # Приложение для основной панели управления
│   ├── __init__.py               # Инициализация приложения
│   ├── settings.py               # Настройки проекта
│   ├── urls.py                   # Главная конфигурация URL-ов
│   ├── wsgi.py                   # Для деплоя через WSGI
│   └── asgi.py                   # Для асинхронного деплоя
│
├── manage.py                     # Скрипт для управления проектом (миграции, запуск сервера и т.п.)

```
