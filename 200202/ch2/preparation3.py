from pandas import DataFrame
from Data import grade_dic
from print_df import print_df

df = DataFrame(grade_dic, index=['노진구', '이슬이', '비실이', '퉁퉁이', '도라에몽'])

# print_df(df)

# 다른 데이터 프레임 병합
# 제외된 열 -> NaN(결측치)
# sort -> 열을 이름순으로 정렬(기본값 : true)

df2 = DataFrame({'국어': 34, '수학': 40, '과학': 90}, index=['짱구'])
new_df = df.append(df2, sort=False)

print_df(new_df)
