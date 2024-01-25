import random
import logging
from datetime import datetime

# Настройка логгера
logging.basicConfig(filename='game_log.log', level=logging.INFO)


def log_info(message):
    """Функция для логирования информации."""
    logging.info(f"{datetime.now()} - INFO - {message}")


def input_with_validation(prompt, validation_func):
    """Функция для получения ввода от пользователя с проверкой."""
    while True:
        try:
            value = int(input(prompt))
            if validation_func(value):
                return value
            else:
                print("Введенное значение не проходит проверку, попробуйте еще раз.")
        except ValueError:
            print("Некорректный ввод, пожалуйста введите число.")


def play_game(max_number, max_attempts):
    """Основная функция игры."""
    secret_number = random.randint(1, max_number)
    log_info(f"Загаданное число: {secret_number}")

    for attempt in range(max_attempts):
        guess = input_with_validation(f"Попытка {attempt + 1}/{max_attempts}. Введите число от 1 до {max_number}: ",
                                      lambda x: 1 <= x <= max_number)
        log_info(f"Попытка пользователя: {guess}")

        if guess == secret_number:
            print("Вы угадали!")
            log_info("Пользователь угадал число.")
            return
        elif guess < secret_number:
            print("Загаданное число больше.")
            log_info("Пользователь ввел число меньше загаданного.")
        else:
            print("Загаданное число меньше.")
            log_info("Пользователь ввел число больше загаданного.")

    print("Попытки закончились.")
    log_info("Попытки пользователя закончились.")


def main():
    """Основная функция для запуска игры."""
    print("Добро пожаловать в игру 'Угадай число'!")

    N = input_with_validation("Введите максимальное число N: ", lambda x: x > 0)
    k = input_with_validation("Введите количество попыток k: ", lambda x: x > 0)

    log_info(f"Входные данные: N={N}, k={k}")

    play_game(N, k)


if __name__ == "__main__":
    main()
