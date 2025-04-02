import random
def get_winner(player, computer):
    rules = {
        "камінь": ["ножиці", "ящірка"],
        "ножиці": ["папір", "ящірка"],
        "папір": ["камінь", "спок"],
        "ящірка": ["папір", "спок"],
        "спок": ["ножиці", "камінь"]
    }
    if player == computer:
        return "Нічия!"
    elif computer in rules.get(player, []):
        return "Ви перемогли!"
    else:
        return "Комп'ютер переміг!"
def main():
    choices = ["камінь", "ножиці", "папір", "ящірка", "спок"]
    computer_choice = random.choice(choices)
    print("Гра: Камінь-Ножиці-Папір-Ящірка-Спок!")
    print("Ваш варіант: камінь, ножиці, папір, ящірка, спок")
    try:
        player_choice = input("Ваш вибір: ").strip().lower()
        if player_choice not in choices:
            raise ValueError(
                "Неправильний вибір! Будь ласка, виберіть з доступних варіантів: камінь, ножиці, папір, ящірка, спок.")
        print(f"Комп'ютер обрав: {computer_choice}")
        print(get_winner(player_choice, computer_choice))
    except ValueError as e:
        print(e)
    finally:
        print("Гра завершена! Дякуємо за участь.")
if __name__ == "__main__":
    main()
