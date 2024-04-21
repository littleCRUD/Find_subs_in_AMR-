### Find subscribers in AMR
---

__Описание__:
> Скрипт для сбора статистики по абонентам операторов связи, находящихся в роуминге. С записью данных в xlsx файл в заданный период времени и отправкой актуальной статистики по email 

__Библиотеки__:
* python-dotenv
* telnetlib
* datetime
* apscheduler
* email
* openpyxl
* smtplib

__Содержания файла .env__
```USER = 'логин для авторизации на оборудовании с которого снимается статистика'
PASSW = 'пароль для авторизации на оборудовании с которого снимается статистика'
HOST = 'host оборудования'
SERVER = 'адрес сервера SMTP'
PORT = 'порт SMTP'
```
__Описание папки config__

В файлы _Opeartor.txt_ записать _global title_ оператора, абонентов которого требуется найти на сетевом элементе 
в формате:
* +7999 *** ** **
* +7899 *** ** **

__Каждый  _global title_ с новой строки__

---
