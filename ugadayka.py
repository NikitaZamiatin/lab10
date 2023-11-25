import random
import logging

# Настройка логгера
logging.basicConfig(filename='game_log.txt', level=logging.INFO,
                    format='%(asctime)s %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

N = int(input("Введите число N: "))
k = int(input("Введите число k: "))

logging.info("Начало игры. N: %d, k: %d", N, k)

secret_number = random.randint(1, N)
logging.info("Загаданное число: %d", secret_number)

for i in range(k):
    try:
        guess = int(input("Введите число от 1 до %d: ", N))
        logging.info("Попытка ввода: %d", guess)

        if guess == secret_number:
            print("Вы угадали!")
            logging.info("Игра окончена. Результат: угадали")
            break

        if guess < secret_number:
            print("Меньше")
            logging.info("Игра продолжается. Результат: меньше")

        if guess > secret_number:
            print("Больше")
            logging.info("Игра продолжается. Результат: больше")

    except ValueError:
        print("Введите целое число!")