# open() 함수를 사용하여 csv 파일을 읽기 위한 file 객체를 생성
with open('.\\191222\\grade.csv', 'r', encoding='euc-kr') as file:
    # 파일의 각 로우를 원소로 갖는 리스트 생성
    # readlines() 함수를 사용하여 파일의 내용을 리스트 형태로 가져옴
    csv_list = file.readlines()
    # 읽어 들인 행의 수(리스트의 원소 수) 만큼 반복
    for i, v in enumerate(csv_list):
        # 읽어 들인 csv 파일의 0번째 행은 '이름, 국어, 영어, 수학' 이라는 제목이므로
        # 처리에서 제외시켜야 된다.
        if i > 0:
            # 현재 행의 내용을 콤마를 기준으로 잘라서 리스트로 변환
            # ex> '비실이, 75, 60, 50'.split(',') -> ['비실이', '75', '60', '50']
            item = v.strip().split(',')
            print(item)
    print('-' * 10)
