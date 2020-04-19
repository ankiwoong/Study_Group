# 리스트를 사용한 가위바위보

# 리스트에 가위,바위,보를 저장
rps = ["가위", "바위", "보"]

# 사용자와 컴퓨터가 rps를 선택
player = rps[1]
computer = rps[0]
print("사용자가 선택한 것은", player, "이며", "컴퓨터가 선택한것은", computer, "입니다.")

# player에 선택과 computer에 선택을 비교하여 승부 비교
if player == "가위" and computer == "가위":
    print("비겼어요!")
elif player == "가위" and computer == "바위":
    print("졌어요!")
elif player == "가위" and computer == "보":
    print("이겼어요!")
elif player == "바위" and computer == "가위":
    print("이겼어요!")
elif player == "바위" and computer == "바위":
    print("비겼어요!")
elif player == "바위" and computer == "보":
    print("졌어요!")
elif player == "보" and computer == "가위":
    print("졌어요!")
elif player == "보" and computer == "바위":
    print("이겼어요!!")
elif player == "바위" and computer == "보":
    print("비겼어요!")