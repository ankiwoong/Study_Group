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

# 컬럼명 변경
df.rename(
    columns={
        'car_vs_people': '차 대 사람', 'car_vs_car': '차 대 차', 'car_only': '차량 단독',
    }, inplace=True
)

print_df(df)

# 전역 설정
plt.rcParams["font.family"] = 'NanumGothic'         # 한글 폰트
plt.rcParams["font.size"] = 12                      # 폰트 사이즈
plt.rcParams["figure.figsize"] = (12, 8)           # 그래프 사이즈
'''
막대 상자 그래프
'''
# x 축 배열 생성
x = np.arange(len(year))
# print(x)
'''
특정 컬럼 생성
'''
# df['차 대 사람'].plot.bar()
# plt.grid()
# plt.title('차 대 사람 교통사고 변화율')
# plt.ylabel('교통사고 수')
# plt.xticks(x, year)
# plt.show()
# plt.close()

'''
전체 컬럼 생성
'''
df.plot.bar()
plt.grid()
plt.title('차 대 사람 교통사고 변화율')
plt.ylabel('교통사고 수')
plt.xticks(x, year)
plt.show()
plt.close()
