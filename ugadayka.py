import random
import logging

# Настройка логгера
logging.basicConfig(filename='game_log.txt', level=logging.INFO,
                    format='%(asctime)s %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

N = int(input("Введите число N: "))
k = int(input("Введите число k: "))

