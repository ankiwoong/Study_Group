grade_dic = {
    '이름': ['노진구', '이슬이', '비실이', '퉁퉁이', '도라에몽'],
    '국어': [98, 88, 92, 63, 100],
    '영어': [76, 90, 70, 60, 50],
    '수학': [88, 62, 88, 31, 76],
    '과학': [64, 72, 45, 70, 88]
}

word_template = '{0},{1},{2},{3},{4}\n'
keys = list(grade_dic.keys())

p = ','
title = p.join(keys)

with open('.\\191222\\quiz_grade.csv', 'w', encoding='euc-kr') as file:
    file.write(title + '\n')

    for i in range(len(grade_dic.values())):
        template = word_template.format(grade_dic['이름'][i], grade_dic['국어'][i],
                                        grade_dic['영어'][i], grade_dic['수학'][i],
                                        grade_dic['과학'][i])
        print(template)
        file.write(template)
