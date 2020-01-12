from pandas import DataFrame
from Data import grade_dic

df = DataFrame(grade_dic, index=['노진구', '이슬이', '비실이', '퉁퉁이', '도라에몽'])

# 전체 요약정보
tsi = df.describe()

# 요약정보 타입
print(type(tsi))

# 요약정보
print(tsi)
