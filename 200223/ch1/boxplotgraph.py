from matplotlib import pyplot as plt
from print_df import print_df
from pandas import DataFrame
from sample_data import traffic

# 데이터 수집
df = DataFrame(traffic)
# print_df(df)

# 데이터 전처리
# '년'에 대한 컬럼 추출
year = list(df['year'])
# print(year)

# 빈 딕셔너리 생성
new_name = {}

# '년' 리스트에 대해 반복
for i, v in enumerate(year):
    # 빈 딕셔너리에 {인덱스번호(i) : 값(v)} 형식으로 넣음
    new_name[i] = v
# print(new_name)

# 데이터 프레임의 인덱스 변경
df.rename(index=new_name, inplace=True)

# 기존의 '년' 컬럼 삭제
df.drop('year', axis=1, inplace=True)

# 컬럼명 변경
df.rename(
    columns={
        'car_vs_people': '차 대 사람', 'car_vs_car': '차 대 차', 'car_only': '차량 단독',
    }, inplace=True
)
# print_df(df)

# 상자 그림
# 전역 설정
plt.rcParams["font.family"] = 'NanumGothic'         # 한글 폰트
plt.rcParams["font.size"] = 12                      # 폰트 사이즈
plt.rcParams["figure.figsize"] = (12, 8)           # 그래프 사이즈

# 그래프 설정
plt.figure()

# df.boxplot('차 대 사람')
# df.boxplot(['차 대 사람', '차 대 차'])
df.boxplot()

plt.title('2005년 ~ 2017년 유형별 교통 사고 현황')

plt.ylabel('교통사고 수')

plt.show()

plt.close()
