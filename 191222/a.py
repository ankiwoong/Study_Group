grade_dic = {
    '이름': ['노진구', '이슬이', '비실이', '퉁퉁이', '도라에몽'],
    '국어': [98, 88, 92, 63, 100],
    '영어': [76, 90, 70, 60, 50],
    '수학': [88, 62, 88, 31, 76],
    '과학': [64, 72, 45, 70, 88]
}

with open('./quiz_grade.csv', 'w', encoding='utf-8') as file:
    keys = grade_dic.keys()
    file.write(','.join(keys) + '\n')
    for i in range(5):
        arr = []
        for key in keys:
            arr.append(str(grade_dic[key][i]))
        file.write(','.join(arr) + '\n')
