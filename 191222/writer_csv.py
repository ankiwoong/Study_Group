# 한 반의 성적표 데이터 예시
grade = [
    {'name': '노진구', 'kor': 10, 'eng': 30, 'math': 20},
    {'name': '비실이', 'kor': 75, 'eng': 60, 'math': 50},
    {'name': '퉁퉁이', 'kor': 13, 'eng': 55, 'math': 40}
]

# 한 줄의 내용을 구성하기 위한 문자열 템플릿
word_template = '{0}, {1}, {2}, {3}\n'

# CSV 파일 저장 위한 file 객체 생성
# CSV 경우 euc-kr 형식 / utf-8 형식
with open('.\\191222\\grade.csv', 'w', encoding='euc-kr') as file:
    # 첫 줄에 각 항목의 컬럼 기록
    file.write('이름, 국어, 영어, 수학\n')

    # 각 데이터를 한 줄씩 콤마로 구분하여 기록
    for item in grade:
        template = word_template.format(
            item['name'], item['kor'], item['eng'], item['math'])
        file.write(template)
