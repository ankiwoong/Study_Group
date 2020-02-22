# pandas 패키지의 기능들을 사용하기 위해서 import
import pandas as pd
from print_df import print_df
import matplotlib.pyplot as plt

# CSV(comma separated values)
# TSV(tab separated values)
# Data들이 comma / tap 으로 구분된 파일
# data/gapminder.tsv 파일을 오픈
# separator : 쉼표(,) / 탭(\t)
# csv 또는 tsv 파일을 읽어서 dataframe 객체를 리턴하는 함수
# Dataframe : 액셀의 표(테이블) 형식의 데이터
df = pd.read_csv(
    '\\python_StudyGroup\\200223\\ch3\\Data\\gapminder.tsv', sep='\t')

# pandas.DataFrame의 함수 , 속성
# print_df(df.head(5))    # DataFrame 첫부분(5개) 출력
# print_df(df.tail(5))    # DataFrame 끝부분(5개) 출력
# print('shape:', df.shape)   # Table의 행(row) / 열(column)의 갯수 출력
# print(df.columns)   # Table의 열(column) 이름 출력

col = []
for c in df.columns:
    col.append(c)

# print(col)


# print(df.dtypes)    # 각 열(columns)의 있는 데이터 타입 출력

# df.info()   # DataFrame의 정보(행 / 열 / 데이터 타입 ...) 출력

# 열(colums) 단위의 데이터 추출
countries = df['continent']  # Table에서 continent만 추출 출력
print(countries)
'''
# series : 1차원 배열
print(type(countries))
print(countries.head())
print(countries.tail())
# DataFrame에서 관심있는 column(열)들로만 이루어진 부분집합
# DataFrame : 2차원 배열
subset_df = df[['country', 'year', 'lifeExp']]
print(type(subset_df))
print_df(subset_df.head())
print_df(subset_df.tail())
# 행(row) 단위의  데이터 추출
# df.loc['Label(행의 이름)']
# df.iloc['Index(행의 인덱스)']
print(df.loc[0])
print(type(df.loc[0]))
print(df.iloc[0])
print(type(df.iloc[0]))
# DataFrame에서 여러개의 row(행)을 추출
# df.loc[['행의 인덱스들의 리스트']]
print_df(df.loc[[0, 1, 2]])  # 인덱스 번호 부여
print_df(df.loc[840:851])   # 인덱스 번호 배열 부여
# DataFrame에서 특정 Cell(셀)에 있는 데이터
# df.loc[row(행) 이름, column(열) 이름]
print(df.loc[851, 'pop'])
# 행 번호 840 ~ 851까지의 pop 열 의 Data만 추출
korea_pop = df.loc[840:851, 'pop']
print(korea_pop)
# 행 번호 840 ~ 851 까지의 'country', 'year', 'pop' 열들의 데이터 추출
korea_year_pop = df.loc[840:851, ['country', 'year', 'pop']]
print_df(korea_year_pop)
# 년도별 기대수명의 평균값
# 1> DataFrame에서 연도별로 그룹을 만듬
grouped_year = df.groupby('year')
print(type(grouped_year))
print(grouped_year)
# 2> 그룹화된 DataFrame에서 평균값을 계산할 컬럼(lifeExp)를 추출
grouped_year_lifeExp = grouped_year['lifeExp']
print(type(grouped_year_lifeExp))
print(grouped_year_lifeExp)
# 3> 추출된 컬럼의 평균을 계산
mean = grouped_year_lifeExp.mean()
print(mean)
# 1 ~ 3 단계를 한줄형식으로
print(df.groupby('year')['lifeExp'].mean())
# 전체 인구의 기대수명의 평균값
print(df['lifeExp'].mean())
# 연도별 인구수의 평균(10의 7승으로 나옴(e+))
print(df.groupby('year')['pop'].mean())
# 연도별, 대륙별 기대수명의 평균
# df.groupby(그룹으로 묶을 컬럼들의 배열)
print(df.groupby(['year', 'continent'])['lifeExp'].mean())  # 그룹 기준 년도 > 국가
print(df.groupby(['continent', 'year'])['lifeExp'].mean())  # 그룹 기준 국가 > 년도
# 연도별 기대 수명, 인구수의 평균
print_df(df.groupby('year')[['lifeExp', 'pop']].mean())
# 연도별 기대 수명, GDP의 평균
print_df(df.groupby('year')[['lifeExp', 'gdpPercap']].mean())
# 연도별 대륙별 기대 수명, GDP의 평균
print(df.groupby(['year', 'continent'])[['year', 'gdpPercap']].mean())
# 연도별 기대 수명의 평균값 그래프
year_lifeExp_mean = df.groupby('year')['lifeExp'].mean()
plt.plot(year_lifeExp_mean)
plt.show()

# gapminder 데이터 프레임에서 나라이름이 'Korea, Rep'만 추출
# 데이터프레임 안에 True False 1차원 배열을 주어서 True에 만족하는 것만 출력
print_df(df[df['country'] == 'Korea, Rep.'])
'''
