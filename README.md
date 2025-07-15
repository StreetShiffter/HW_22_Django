![Django](https://www.djangoproject.com/s/img/logos/django-logo-negative.svg )
<h3 style="background: linear-gradient(257deg, Gold, green); -webkit-background-clip: text; color: transparent;">
  Проект ОНЛАЙН МАГАЗИН на django "
</h3> 

# 🔖 Описание проекта:

Данный проект является интернет-магазином


# 🔧 Установка компонентов:


1. Создайте проект и установите poetry:


```pip install --user poetry```


2. Установите инструменты для реализации магазина

[![Django](https://img.shields.io/badge/Django-3.2.0-%2311677A?logo=django&logoColor=white&style=flat&labelColor=black)]( https://www.djangoproject.com/ )

КОМАНДЫ ДЛЯ ЗАПУСКА ФРЕЙМВОРКА И ПРИЛОЖЕНИЯ
```
poetry add django # Установка 
django-admin startproject config . # Старт нового проекта
django-admin startproject myproject # Старт нового приложения

```

# ✒️ Использование
Основное использование приложения запускается из файла *manage.py*

⚠️ ВАЖНО ⚠️
```
python manage.py runserver 8080 # Запуск сервера
CTRL+С # Отключение сервера
```
### 🌐 Пример страниц:

![Главная стhаница](./image/home.jpg)
![Cтhаница_rjynfrns](./image/contacts.jpg)

# Структура проекта
```
HW_22_Django/
├── 📁 catalog/ # Приложение Django
│ ├── 📁 migrations/ # Миграции базы данных
│ ├── 📁 templates/ # Шаблоны HTML
│ │ ├── 📊 category.html
│ │ ├── 📊 contacts.html
│ │ └── 📊 home.html
│ │ └── 📊 order.html 
│ ├── 📝 init .py # Пустой файл, обязательный для Python
│ ├── 📝 admin.py # Настройки админки Django
│ ├── 📝 apps.py # Конфигурация приложения
│ ├── 📝 models.py # Модели данных
│ ├── 📝 tests.py # Тесты
│ ├── 📝 urls.py # URL-маршруты приложения
│ └── 📝 views.py # Вьюхи (представления)
├── 📁 config/ # Корневые настройки проекта
│ ├── 📝 init .py # Пустой файл, обязательный для Python
│ ├── 📝 asgi.py # Настройки ASGI (асинхронный сервер)
│ ├── 📝 settings.py # Основные настройки проекта
│ ├── 📝 urls.py # Глобальные URL-маршруты
│ └── 📝 wsgi.py # Настройки WSGI (синхронный сервер)
├── 📁 static/ # Статические файлы (CSS, JS, изображения)
├── 📄 .flake8 # Настройки flake8 (статический анализатор кода)
├── 📄 .gitignore # Файл игнорирования Git
├── 📄 db.sqlite3 # База данных SQLite
├── 📝 manage.py # Утилита управления проектом Django
├── 📄 poetry.lock # Зависимости Poetry
└── 📄 pyproject.toml # Конфигурация Poetry
```

# 📝 Документация 

Для получения дополнительной информации обратитесь к [документации](https://api.hh.ru/openapi/redoc#section)
