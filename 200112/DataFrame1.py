from pandas import DataFrame
from Data import grade_list
from Data import grade_dic

# List -> DataFrame
# None(값이 없음) -> NaN
df = DataFrame(grade_list)
print(df)
