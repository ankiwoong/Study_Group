from pandas import DataFrame
from Data import grade_dic

df = DataFrame(grade_dic, index=['노진구', '이슬이', '비실이', '퉁퉁이', '도라에몽'])

# 요약정보 개별 조회
# 각 열 혹은 특정 열에 대해 NA(결측치)를 제외한 값의 수 반환
print(df.count())
print('-' * 30)
print(df['영어'].count())
