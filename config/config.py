import os
from dotenv import load_dotenv


load_dotenv()

user = os.getenv("USER")
# логин для подключения к сетевому элементу, с которого будет собираться статистика

passw = os.getenv("PASSW")
# логин для подключения к сетевому элементу, с которого будет собираться статистика

port = os.getenv("PORT")  # # порт для SMTP
server = os.getenv("SERVER")  # адрес сервера для SMTP
host = os.getenv("HOST")  # ip host сетевого элемента
