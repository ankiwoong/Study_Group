from pandas import DataFrame
from Data import grade_dic

# 데이터프레임 생성
df = DataFrame(grade_dic, index=['노진구', '이슬이', '비실이', '퉁퉁이', '도라에몽'])

# DataFrame에서 Index(행) 이름만 추출
print(df.index)             # 객체 형식
print(list(df.index))       # 리스트 변환
