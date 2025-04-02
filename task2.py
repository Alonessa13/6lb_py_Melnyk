import random
def main():
    code = random.randint(100, 999)  # Генеруємо випадковий тризначний код
    attempts = 5  # Кількість спроб
    print("Вам потрібно зламати сейф! Введіть тризначний код.")
    while attempts > 0:
        try:
            guess = input("Введіть код: ")
            guess = int(guess)  # Перетворюємо введення на число
            if guess == code:
                print("Вітаємо! Ви зламали сейф!")
                return  # Вихід з функції при правильному вводі
            elif guess < code:
                print("Код більший.")
            else:
                print("Код менший.")
        except ValueError:
            print("Помилка! Потрібно ввести число.")
        attempts -= 1
        print(f"Залишилось спроб: {attempts}")
    print(f"Ви програли! Код сейфу був: {code}")
    print("Пригоди тривають!")
main()
