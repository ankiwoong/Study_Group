from pandas import DataFrame
from Data import grade_dic

df = DataFrame(grade_dic, index=['노진구', '이슬이', '비실이', '퉁퉁이', '도라에몽'])

# 현장에서 데이터는 몇 만건 이상의 대량의 데이터
# 모두 출력해서 일일이 확인은 불가능함
# 그러므로 데이터 일부분만 출력해서 확인

# 전체에 대한 처음 2줄만 추출
# 파라미터가 없을 경우 5줄이 기본
top_data = df.head()
print(top_data)
print('-' * 30)

top_data2 = df.head(2)
print(top_data2)