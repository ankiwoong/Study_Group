def welcome():
    print("이상한 나라에 오신 것을 환영합니다!")

welcome()

def welcome(name):
    print(name, "님 이상한 나라에 오신것을 환영합니다!")

welcome("엘리스")
welcome("도도새")

def draw_stars(num):
    print("*" * num)

draw_stars(3)
draw_stars(2)
draw_stars(1)

def concat(str1, str2):
    return(str1 + str2)

print(concat("빨주노초", "파남보"))

def sub_div(num1, num2):
    return(num1 - num2, num1 / num2)
print(sub_div(6, 3))

def judge_cards(name, num):
    for n in range(num):
        print(name, n + 1, "유죄!")

judge_cards("하트", 2)
judge_cards("클로버", 3)

import random
clovers = ["클로버1", "클로버2", "클로버3"]
print(random.choice(clovers))
print(random.sample(clovers, 2))

import random
print(random.choice([1, 2, 3]))
print(random.choice(range(1, 4)))
print(random.randint(1, 3))
print(random.randint(1, 4))

import random
name = input("당신의 이름을 입력하세요 : ")
birth_year = ["시끄러운", "푸른", "적색", "조용한", "웅크린", "백색", "지혜로운", "용감한", "날카로운", " 욕심많은"]
birth_month = ["늑대", "태양", "양", "매", "황소", "불꽃", "나무", "달빛", "말", "돼지", "하늘", "바람"]
birth_date = [
    "와(과) 함께 춤을", "의 기상", "은(는) 그림자속에", "", "", "", "의 환생", "의 죽음", "아래에서", "을(를) 보라",
    "이(가) 노래하다", "그림자", "의 일격", "에게 쫓기는 남자", "의 행진", "의 왕", "의 유령", "을(를) 죽인자",
    "은(는) 맨날 잠잔다.", "처럼", "의 파수꾼", "의 악마", "와(과) 같은 사나이", "을(를) 쓰러트린자", "의 혼",
    "은(는) 말이 없다."
]
random_name = random.choice(birth_year) + random.choice(birth_month) + random.choice(birth_date)
print(name, "당신의 과거 인디언 이름은", random_name, "라네.")