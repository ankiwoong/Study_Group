# open() 함수를 사용하여 csv 파일을 읽기 위한 file 객체를 생성
with open('.\\191222\\grade.csv', 'r', encoding='euc-kr') as file:
    # 파일의 각 로우를 원소로 갖는 리스트 생성
    # readlines() 함수를 사용하여 파일의 내용을 리스트 형태로 가져옴
    csv_list = file.readlines()
    print(csv_list)
    print('-' * 10)
