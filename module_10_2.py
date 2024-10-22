from threading import Thread
from time import sleep


class Knight(Thread):

    def __init__(self, name, power):
        self.kname = name
        self.power = power
        super().__init__()

    def run(self):
        print(f'{self.kname}, на нас напали!')
        vragi = 100
        days = 0
        while vragi > 0:
            sleep(1)
            days += 1
            vragi -= self.power
            if vragi < 0:
                vragi = 0
            print(f'{self.kname} сражается {days}..., осталось {vragi} воинов.')
        print(f'{self.kname} одержал победу спустя {days} дней(дня)!')

if __name__ == '__main__':

    knight1 = Knight('Sir Lancelot', 10)
    knight2 = Knight("Sir Galahad", 20)

    knight1.start()
    knight2.start()

    knight1.join()
    knight2.join()
    print('Все битвы завершены! Враг разгромлен!')


