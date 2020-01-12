from pandas import DataFrame
from Data import grade_dic

# 데이터프레임 생성
df = DataFrame(grade_dic, index=['노진구', '이슬이', '비실이', '퉁퉁이', '도라에몽'])

# 특정 값 변경
# 행 우선 접근 방법으로만 가능
df.loc['이슬이', '수학'] = 99
print('이슬이의 변경된 수학 점수는 %d 점' % df.loc['이슬이', '수학'])
