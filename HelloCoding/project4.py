# 함수를 넣은 가위바위보
import random

def compare(p_choice, c_choice):
    if p_choice == c_choice:
        print("비겼어요!")
    elif (p_choice - c_choice) % 3 == 1:
        print("이겼어요!")
    else:
        print("졌어요...")

while True:
    rps = ["가위", "바위", "보"]

    player = int(input("가위(0) / 바위(1) / 보(2) / 끝(-1) : "))

    computer = random.randint(0, 2)

    if player == -1:
        break
    print(rps[player], rps[computer])

    compare(player, computer)