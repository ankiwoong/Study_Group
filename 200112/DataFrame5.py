from pandas import DataFrame
from Data import grade_list
from Data import grade_dic

# 각각의 데이터 열의 값 조회
# 컬럼 이름이 지정되면 번호로 접근할 수 없다.
columns_name = ['국어', '영어', '수학', '과학']
df = DataFrame(grade_list, columns=columns_name)

print(df['국어'])
print('-' * 30)
print(df['영어'])
