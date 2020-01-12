from pandas import DataFrame
from Data import grade_list
from Data import grade_dic

# 딕셔너리를 통한 데이터 프레임 생성
# 딕셔너리의 key = DataFarme의 컬럼(열)
df = DataFrame(grade_dic)
print(df)