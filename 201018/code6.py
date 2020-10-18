from pytrends.request import TrendReq
import matplotlib.pyplot as plt
import pandas as pd
import os

# 검색 keyword, 검색 지역, 검색 기간 입력
keywords = ["현대 팰리세이드", "쌍용 렉스턴"]
local_area = "KR"
period = "2018-01-01 2018-12-31"

# Google Trend 접속 및 데이터 탑재
trend_obj = TrendReq()
trend_obj.build_payload(kw_list=keywords, timeframe=period, geo=local_area)
trend_df = trend_obj.interest_over_time()
trend_df = trend_df.reset_index()
trend_df["Date"] = trend_df["date"].dt.to_period(freq="W")
trend_df.set_index("Date", inplace=True)
trend_df.drop(["date", "isPartial"], axis=1, inplace=True)
# print(trend_df.head())

"""
                       현대 팰리세이드  쌍용 렉스턴
Date
2018-01-01/2018-01-07         0      53
2018-01-08/2018-01-14         0      18
2018-01-15/2018-01-21         0       9
2018-01-22/2018-01-28         0      37
2018-01-29/2018-02-04         0      28
"""

# 주가 데이터 - 야후 파이낸스에서 다운로드 받은 CSV 파일을 가져오기
hd = pd.read_csv("./data/005380.KS.csv", index_col=0, encoding="utf-8")  # 현대자동차
sy = pd.read_csv("./data/003620.KS.csv", index_col=0, encoding="utf-8")  # 쌍용자동차
# print(hd.head())
# print(sy.head())

"""
              Open    High     Low   Close  Adj Close   Volume
Date
2018-01-01  5120.0  5270.0  5120.0  5210.0     5210.0   609558
2018-01-08  5210.0  5590.0  5130.0  5330.0     5330.0  1641993
2018-01-15  5390.0  5460.0  5270.0  5330.0     5330.0  1079284
2018-01-22  5400.0  6070.0  5380.0  5980.0     5980.0  3332912
2018-01-29  6000.0  6160.0  5640.0  5920.0     5920.0  1740149

              Open    High     Low   Close  Adj Close   Volume
Date
2018-01-01  5120.0  5270.0  5120.0  5210.0     5210.0   609558
2018-01-08  5210.0  5590.0  5130.0  5330.0     5330.0  1641993
2018-01-15  5390.0  5460.0  5270.0  5330.0     5330.0  1079284
2018-01-22  5400.0  6070.0  5380.0  5980.0     5980.0  3332912
2018-01-29  6000.0  6160.0  5640.0  5920.0     5920.0  1740149
"""

# 주가 데이터 스케일 조정 (Min-Max 스케일 조정)
def min_max_scaler(x):
    return (x - x.min()) / (x.max() - x.min())


hd["Scaled_Adj"] = hd[["Adj Close"]].apply(min_max_scaler)
sy["Scaled_Adj"] = sy[["Adj Close"]].apply(min_max_scaler)
hd_df = hd.iloc[1:, :]
sy_df = sy.iloc[1:, :]
# print(hd_df.head())

"""
                Open      High       Low     Close      Adj Close   Volume  Scaled_Adj
Date
2018-01-08  148500.0  158000.0  147500.0  154000.0  148972.359375  2643772    0.875109
2018-01-15  154000.0  162000.0  151000.0  162000.0  156711.171875  2081097    0.992653
2018-01-22  162500.0  167500.0  149000.0  152500.0  147521.328125  3798731    0.853069
2018-01-29  153000.0  164000.0  152000.0  162500.0  157194.859375  3180636    1.000000
2018-02-05  162500.0  163500.0  153500.0  155000.0  149939.703125  3519128    0.889802
"""

trend_df.index = hd_df.index
print(trend_df.head())

"""
            현대 팰리세이드  쌍용 렉스턴
Date
2018-01-08         0      15
2018-01-15         0       8
2018-01-22         0       8
2018-01-29         0      31
2018-02-05         0       0
"""

final_data = pd.concat([trend_df, hd_df["Scaled_Adj"], sy_df["Scaled_Adj"]], axis=1)
final_data.columns = ["펠리세이드", "렉스턴", "현대_주가", "쌍용_주가"]
# print(final_data.head())

"""
            현대 팰리세이드  쌍용 렉스턴
Date
2018-01-08         0      15
2018-01-15         0       8
2018-01-22         0       8
2018-01-29         0      31
2018-02-05         0       0
            펠리세이드  렉스턴     현대_주가     쌍용_주가
Date
2018-01-08      0   15  0.875109  0.705882
2018-01-15      0    8  0.992653  0.705882
2018-01-22      0    8  0.853069  1.000000
2018-01-29      0   31  1.000000  0.972851
2018-02-05      0    0  0.889802  0.950226
"""

# matplotlib 한글 폰트 오류 문제 해결
from matplotlib import font_manager, rc

font_path = os.path.join(os.getcwd(), "data", "malgun.ttf")  # 폰트파일의 위치
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc("font", family=font_name)

# 그래프 출력 및 저장
plt.style.use("ggplot")
ax1 = final_data[["펠리세이드", "렉스턴"]].plot(kind="bar", figsize=(20, 10))
ax2 = ax1.twinx()
final_data[["현대_주가", "쌍용_주가"]].plot(ls="--", ax=ax2)
ax1.legend(loc="upper right")
ax2.legend(loc="upper center")
plt.title("구글 검색 트렌드와 주가의 관계", size=18)

output_filepath = os.path.join(os.getcwd(), "output", "google_trend_stock_price.png")
plt.savefig(output_filepath, dpi=300)

plt.show()