# demowebshop_test

## О проекте
Проект автоматизации тестирования сайта [Demo Web Shop](https://demowebshop.tricentis.com/).  
В рамках проекта реализованы следующие тесты:

1. **Проверка логина** – тестирует возможность авторизации пользователя.
2. **Проверка изменения реквизитов клиента** – тестирует возможность изменения личных данных пользователя.

Проект построен с использованием **Page Object Model (POM)** для удобного и поддерживаемого взаимодействия с элементами страницы.

---
## Стек технологий

- Python 3.13
- Pytest
- Selenium
- Docker + Docker Compose
- Allure (для отчётов)

---
## Структура проекта
```
demowebshop_test/
├── .github/
│ └── workflows/
│        └──Dockerfile
├── base/
│ ├── base_page.py
│ └── base_test.py
├── config/
│ ├── data.py
│ └── links.py
├── pages/
│ ├── customer_page.py
│ ├── login_page.py
│ └── main_page.py
├── tests/│ 
│ └── test_customer_account.py
├── conftest.py
├── Dockerfile
├── docker-compose.yml
├── pytest.ini
├── requirements.txt
└── README.md
```
## Установка и запуск локально

1. Клонируем репозиторий:
```bash
git clone https://github.com/mycrossstitch/demowebshop_test.git
cd demowebshop_test
```
2. Устанавливаем зависимости:
```bash 
pip install -r requirements.txt
```
3. Создаем локальный .env (пример)
```
EMAIL = email@gmail.com
PASSWORD = password
NEW_EMAIL = email_new@gmail.com
NEW_FIRST_NAME = Иван
NEW_LAST_NAME = Иванов
NEW_GENDER = male
```
4. Запуск тестов:
```bash 
pytest --alluredir=allure-results
```
5. Генерация отчёта Allure:
```bash 
allure generate allure-results --clean -o allure-report
allure open allure-report
```
## Запуск через Docker
```bash
docker compose build
docker compose run regression /bin/sh -c "pytest --alluredir=allure-results"
docker compose run regression /bin/sh -c "allure generate allure-results --clean -o allure-report"
docker compose run regression /bin/sh -c "allure open allure-report"
```
## Настройка переменных окружения
Для тестов используются следующие переменные (например, для авторизации и изменения данных пользователя):
```
EMAIL
PASSWORD
NEW_EMAIL
NEW_FIRST_NAME
NEW_LAST_NAME
NEW_GENDER
```
В GitHub Actions они передаются через secrets.

## CI / GitHub Actions

В репозитории настроен workflow, который при "Run workflow":
1. Запускает тесты в Docker.
2. Генерирует Allure-отчёт.
3. Публикует отчёт на GitHub Pages.