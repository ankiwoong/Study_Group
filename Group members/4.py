import re
​
db = "1234"
password = input("기존 패스워드를 입력해주세요.")
​
if db == password:
    db = input("신규 패스워드를 입력해주세요.")
    # 숫자, 특수문자 각 1회 이상, 영문 2개 이상 사용하여 8자리 이상 입력(한글 X)
    p = re.compile(
        "^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$")
    m = p.search(db)
    if m:
        print("신규 비밀번호를 잘 저장했습니다.")
        print(db)
    else:
        print("신규 비밀번호 저장에 실패했습니다.")
else:
    print("잘못된 비밀번호입니다.")
