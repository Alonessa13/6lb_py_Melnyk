import random
def main():
    coins = random.randint(1, 1000)  # Генеруємо випадкову кількість монет
    print(f"Ви знайшли {coins} золотих монет!")
    try:
        people = input("Скільки людей у вашій команді? ")
        people = int(people)  # Перетворюємо введене значення в ціле число
        result = coins // people  # Ділимо монети порівну
        print(f"Кожен учасник отримує {result} монет.")
    except ValueError:
        print("Помилка! Потрібно ввести число.")
    except ZeroDivisionError:
        print("Помилка! Не можна ділити на нуль.")
    finally:
        print("Пригоди тривають!")
main()
