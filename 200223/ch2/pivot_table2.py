'''
Pandas와 Pivot의 연계
'''
from print_df import print_df
from pandas import DataFrame
from matplotlib import pyplot as plt
import numpy as np
from sample_data import traffic

# 데이터 수집
df = DataFrame(traffic)
# print_df(df)

# 데이터 전처리
# '년도'에 대한 컬럼만 리스트로 추출
year = list(df['year'])
# print_df(year)

# 빈 딕셔너리 생성
new_name = {}

# '년도' 리스트에 대해 반복
for i, v in enumerate(year):
    new_name[i] = v
# print(new_name)

# 데이터 프레임의 인덱스 변경
df.rename(index=new_name, inplace=True)

# 기존의 '년도' 컬럼은 삭제
df.drop('year', axis=1, inplace=True)

print_df(df)

# 전역 설정
plt.rcParams["font.family"] = 'NanumGothic'         # 한글 폰트
plt.rcParams["font.size"] = 12                      # 폰트 사이즈
plt.rcParams["figure.figsize"] = (12, 8)           # 그래프 사이즈
'''
상자 수염 그림
'''
'''
case 1
특정 컬럼 생성
'''
# plt.grid()
# df.boxplot('car_vs_people')
# plt.title('차 대 사람 교통사고 변화율')
# plt.ylabel('교통사고 수')
# plt.show()
# plt.close()
'''
case 2
복수 컬럼 생성
'''
# plt.grid()
# df.boxplot(['car_vs_people', 'car_vs_car'])
# plt.title('차 대 사람 / 차 대 차 교통사고 변화율')
# plt.ylabel('교통사고 수')
# plt.show()
# plt.close()
'''
case 3
전체 컬럼 생성
'''
plt.grid()
df.boxplot()
plt.title('2005년 ~ 2017년 유형별 교통 사고 현황')
plt.ylabel('교통사고 수')
plt.show()
plt.close()
