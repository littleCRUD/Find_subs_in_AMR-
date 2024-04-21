from telnetlib import Telnet
import sys
import os
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
import core
from config import config

sys.path.insert(1, os.path.join(sys.path[0], ".."))


def start() -> None:
    """Функция формирует подключение по telnet к сетевому элементу,
    запускает сбор статистики и сохраняет данные в файл"""
    connect = Telnet(config.host)
    with connect as conn:
        conn.read_until(b"ENTER USERNAME <")
        conn.write(core.to_bytes(config.user))
        conn.read_until(b"ENTER PASSWORD <")
        conn.write(core.to_bytes(config.passw))
        conn.write(b"\r")
        amr = core.AMR(conn)
        amr.save_data_sub()
        print(f"Временем {datetime.now().hour}:00 данные добавлены успешно")


sched = BackgroundScheduler()  # подключаем шедулер

sched.add_job(start, "cron", hour="*", minute="1", id="job-1")
# добавляем задачу на сбор статискики каждый час

sched.add_job(core.send_mail, "cron", hour="*", minute="5", id="job-2")
# добавляем задачу на отправку email с собранной

sched.start()


if __name__ == "__main__":
    go = input()
