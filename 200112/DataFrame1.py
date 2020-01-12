from pandas import DataFrame
from Data import grade_list
from Data import grade_dic
from print_df import print_df

# List -> DataFrame
# None(값이 없음) -> NaN
# Missing
df = DataFrame(grade_list)
print(df)

# 출력 모듈 Testing
# 모듈 - prettytable
print_df(df)
