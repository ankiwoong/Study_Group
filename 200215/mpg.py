# 모듈 참조
from print_df import print_df
from pandas import ExcelFile
from pandas import DataFrame
from matplotlib import pyplot as plt
import numpy as np

# ---------------------------------------------------------
# 데이터 수집
# ---------------------------------------------------------
# 엑셀파일 읽기
xls_file = ExcelFile('C:\\python_StudyGroup\\200215\\data\\mpg.xlsx')

# 엑셀의 sheet 이름들 중에서 0번째 sheet를 dataframe으로 변환
df = xls_file.parse(xls_file.sheet_names[0], index_col=0)
# print_df(df.head())

# ---------------------------------------------------------
# 데이터 전처리
# ---------------------------------------------------------
# 각 컬럼명 변경
df.rename(
    columns={
        'manufacturer': '제조회사', 'model': '모델명', 'displ': '배기량', 'year': '생산년도', 'cyl': '실린더개수', 'trans': '변속기종류', 'drv': '구동방식', 'cty': '도시연비', 'hwy': '고속도로연비', 'fl': '연료종류', 'class': '자동자종류'
    }, inplace=True
)
# print_df(df)

# 평균연비 합격을 의미하는 '연비테스트'컬럼을 mpg 데이터에 추가
# 평균연비 20이상이면 '합격', 그렇지 않으면 '불합격'
# 도시연비, 고속도로 연비를 활용하여 평균연비 데이터 avg을 mpg 데이터에 추가
df['연비테스트'] = np.where((df['도시연비'] + df['고속도로연비']) / 2 >= 20, '합격', '불합격')
# print_df(df.head(10))

# 각 값별로 수량을 카운트하여 새로운 데이터 프레임 생성
count = df['연비테스트'].value_counts()
count_df = DataFrame(count)
print_df(count_df)

# ---------------------------------------------------------
# 데이터 정제
# ---------------------------------------------------------
# 결측치 여부 확인
empty_sum = df.isnull().sum()
# print_df(empty_sum)

# ---------------------------------------------------
# 데이터 시각화
# ---------------------------------------------------
# 그래프 만들기
plt.rcParams["font.family"] = 'NanumGothic'      # 한글 폰트 지정(나눔고딕)
plt.rcParams["font.size"] = 14                   # 그래프 폰트 사이즈(14)
plt.rcParams["figure.figsize"] = (10, 10)        # 그래프 사이즈(10 x 10)

# # 전체 컬럼에 대한 시각화
count_df['연비테스트'].plot.pie(autopct='%0.1f%%')  # autopct : 각 범주가 데이터에서 차지하는 비율
plt.title("연비테스트 합격 비율")                   # 그래프 제목
plt.savefig('mpg.png', dpi=200)                     # 그래프 저장
plt.show()                                          # 그래프 보기
plt.close()                                         # 그래프 종료
