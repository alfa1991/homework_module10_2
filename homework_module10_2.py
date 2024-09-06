import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = 100  # Общее количество врагов для всех рыцарей

    def run(self):
        days = 0
        print(f"{self.name}, на нас напали!")
        while self.enemies > 0:
            days += 1
            time.sleep(1)  # Имитация одного дня сражения
            self.enemies -= self.power
            remaining_enemies = max(0, self.enemies)
            print(f"{self.name}, сражается {days} день(дня)..., осталось {remaining_enemies} воинов.")
        print(f"{self.name} одержал победу спустя {days} дней(дня)!")


# Создаем и запускаем два потока для двух рыцарей
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

# Ожидаем завершения потоков
first_knight.join()
second_knight.join()

print("Все битвы закончились!")
