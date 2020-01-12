from pandas import DataFrame
from Data import grade_list
from Data import grade_dic

# 인덱스(행) 이름을 지정하여 생성
# 인덱스의 이름을 갖고 있는 리스트를 지정
index_names = ['노진구', '이슬이', '비실이', '퉁퉁이', '도라에몽']
df = DataFrame(grade_list, index=index_names)
print(df)
