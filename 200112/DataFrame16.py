from pandas import DataFrame
from Data import grade_dic

# 데이터프레임 생성
df = DataFrame(grade_dic, index=['노진구', '이슬이', '비실이', '퉁퉁이', '도라에몽'])

# 열 -> 행 순으로 접근
print('노진구의 국어 점수는 %d 점 입니다.' % df['국어']['노진구'])
