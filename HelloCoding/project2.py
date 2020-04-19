# while로 반복하는 가위바위보 게임
import random
rps = ["가위", "바위", "보"]

while True:
    player = input("가위 / 바위 / 보 / 끝 : ")
    computer = random.choice(rps)

    if player == "끝":
        break

    print(player, computer)

    if player == computer:
        print("비겼어요!")
    elif player == "가위":
        if computer == "바위":
            print("졌어요!")
        else:
            print("이겼어요!")
    elif player == "바위":
        if computer == "보":
            print("졌어요!")
        else:
            print("이겼어요!")
    elif player == "보":
        if computer == "가위":
            print("졌어요!")
        else:
            print("이겼어요!")