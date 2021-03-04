# Проект CatBot

CatBot - это бот для Telegram, который присылает пользователю котиков.

## Установка

1. Клонируйте репозиторий с github
2. Создайте виртуальное окружение
3. Установите зависимости `pip install -r requirements.txt`
4. Создайте файл `settings.py`
5. Впишите в settings.py переменные:
```
API_KEY = 'API-ключ бота'
USER_EMOJI = [':simple_smile:',':kissing_heart:',
              ':stuck_out_tongue_closed_eyes:',':smiling_imp:',
              ':heart:',':hankey:',':facepunch:']
```
6. Запустите бота командой `python bot.py`