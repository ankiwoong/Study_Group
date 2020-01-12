from pandas import DataFrame
from Data import grade_list
from Data import grade_dic

# 인덱스와 컬럼이름 모두 지정
columns_name = ['국어', '영어', '수학', '과학']
index_name = ['노진구', '이슬이', '비실이', '퉁퉁이', '도라에몽']
df = DataFrame(grade_list, index=index_name, columns=columns_name)
print(df)
