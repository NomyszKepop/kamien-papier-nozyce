import random

print("Witaj w grze Kamień-Papier-Nożyce!")
player_name = input("Podaj swoje imię: ")

player_score = 0
pc_score = 0
rounds_to_win = 3

while player_score < rounds_to_win and pc_score < rounds_to_win:
    print(f"\nWynik: {player_name}: {player_score}  PC: {pc_score}")
    player_choice = input("Wybierz kamień (k), papier (p) lub nożyce (n): ").lower()

    if player_choice not in ["k", "p", "n"]:
        print("Niepoprawny wybór! Spróbuj jeszcze raz.")
        continue

    pc_choice = random.choice(["k", "p", "n"])

    print(f"{player_name}: {player_choice} vs PC: {pc_choice}")

    if player_choice == pc_choice:
        print("Remis!")
    elif (player_choice == "k" and pc_choice == "n") or (player_choice == "p" and pc_choice == "k") or (
            player_choice == "n" and pc_choice == "p"):
        print(f"{player_name} wygrywa rundę!")
        player_score += 1
    else:
        print("PC wygrywa rundę!")
        pc_score += 1

if player_score > pc_score:
    print(f"\nGratulacje, {player_name} wygrywasz grę!")
else:
    print("\nPC wygrywa grę!")