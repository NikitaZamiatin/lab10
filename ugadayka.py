import random
import logging

logging.basicConfig(filename='game_log.txt', level=logging.INFO,
                    format='%(asctime)s %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

N = int(input("Введите число N (натуральное число): "))
k = int(input("Введите число попыток (натуральное число): "))

logging.info("Начало игры. N: %d Попытки: %d", N, k)

secret_number = random.randint(1, N)
logging.info("Загаданное число: %d", secret_number)

control = 0

for i in range(k):
    try:
        guess = int(input("Введите число от 1 до {}: ".format(N)))
        logging.info("Попытка ввода: %d", guess)

        if guess == secret_number:
            print("Вы угадали!")
            logging.info("Игра окончена. Результат: угадали")
            break

        if guess < secret_number:
            print("Больше")
            control += 1
            logging.info("Игра продолжается. Результат: больше")

        if guess > secret_number:
            print("Меньше")
            control += 1
            logging.info("Игра продолжается. Результат: меньше")

    except ValueError:
        print("Введите целое число!")

if control == k:
    print("Попытки закончились. Загаданное число: {}".format(secret_number))
    logging.info("Игра окончена. Результат: попытки закончились")