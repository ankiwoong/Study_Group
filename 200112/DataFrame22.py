from pandas import DataFrame
from Data import grade_dic

# 데이터프레임 생성
df = DataFrame(grade_dic, index=['노진구', '이슬이', '비실이', '퉁퉁이', '도라에몽'])

# 전치(가로와 세로가 바뀐 형태) 구하기
df_t = df.T
print(df_t)
