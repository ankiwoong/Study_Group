from pandas import DataFrame
from Data import grade_list
from Data import grade_dic

# 인덱스 이름을 지정한 데이터 프레임 생성
df = DataFrame(grade_dic, index=['노진구', '이슬이', '비실이', '퉁퉁이', '도라에몽'])
print(df)