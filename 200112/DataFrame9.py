from pandas import DataFrame
from Data import grade_dic

# 데이터프레임 생성
df = DataFrame(grade_dic, index=['노진구', '이슬이', '비실이', '퉁퉁이', '도라에몽'])

# 열을 기준으로 데이터 타입 확인
print(df.dtypes)
