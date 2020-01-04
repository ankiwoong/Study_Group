grade_dic = {
    '이름': ['노진구', '이슬이', '비실이', '퉁퉁이', '도라에몽'],
    '국어': [98, 88, 92, 63, 100],
    '영어': [76, 90, 70, 60, 50],
    '수학': [88, 62, 88, 31, 76],
    '과학': [64, 72, 45, 70, 88]
}

# 한 줄에 대한 템플릿
word_template = '{0},{1},{2},{3},{4}\n'
# 딕셔너리의 키를 리스트로 변환
keys =

p = ','
# keys 리스트 사이에 쉼표를 넣어 문자열로 변환
title =

with open('.\\191222\\quiz_grade.csv', 'w', encoding='euc-kr') as file:
    # 첫 줄에 각 항목의 제목 기록
    file.write(title + '\n')

    # 각 데이터를 한 줄씩 콤마로 구분하여 기록
    for i in:
        template = word_template.format(grade_dic['이름'][i], grade_dic['국어'][i],
                                        grade_dic['영어'][i], grade_dic['수학'][i],
                                        grade_dic['과학'][i])
        file.write(template)
