from pandas import DataFrame
from Data import grade_list
from Data import grade_dic

# 컬럼(열) 이름을 지정하여 새로 생성
# 컬럼의 이름을 갖고 있는 리스트를 지정
columns_name = ['국어', '영어', '수학', '과학']
df = DataFrame(grade_list, columns=columns_name)
print(df)