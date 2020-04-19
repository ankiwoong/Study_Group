# 딕셔너리를 사용ㅎㄴ 가위바위보
import random

rps = ["가위", "바위", "보"]

results = {
    ("가위","보"): True,
    ("가위","바위"): False,
    ("바위","가위"): True,
    ("바위","보"): False,
    ("보","바위"): True,
    ("보","가위"): False
}

while True:
    player = input("가위 / 바위 / 보 / 끝 : ")
    computer = random.choice(rps)

    if player == "끝":
        break

    print(player, computer)

    if player == computer:
        print("비겼어요!")
    elif results[(player, computer)]:
        print("이겼어요!")
    else:
        print("졌어요!")