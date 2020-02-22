import pandas as pd
import matplotlib.pyplot as plt
from print_df import print_df

years = range(1880, 2011)
df_pieces = []  # 1880 ~ 2010년 까지의 데이터 프레임을 젖아할 리스트
for year in years:  # 1880 ~ 2010
    path = '\\Python\\GoottAcademy\\Study\\data\\yob%d.txt' % year  # 파일 이름
    df = pd.read_csv(path, header=None, names=[
                     'name', 'gender', 'born'], encoding='utf-8')
    df['year'] = year   # 데이터 프레임에 year 컬럼 추가
    df_pieces.append(df)    # 데이터 프레임들의 리스트

names = pd.concat(df_pieces, ignore_index=True)

# 가장 많이 작명한 이름들 - 이름의 트렌드
# ascending=False -> 내림차순


def get_top100(group):
    return group.sort_values(by='born', ascending=False)[:100]


# 연도 / 성별을 기준으로 그룹화 후 출력
grouped = names.groupby(['year', 'gender'])
top100 = grouped.apply(get_top100)

top100.reset_index(inplace=True, drop=True)

total_born_name = top100.pivot_table(
    'born', index='year', columns='name', aggfunc=sum)

subset = total_born_name[['Mary', 'Anna', 'John', 'William']]

boys = top100[top100.gender == 'M']

girl = top100[top100.gender == 'F']

df_boy = boys[boys.year == 1900]
print_df(df_boy)
