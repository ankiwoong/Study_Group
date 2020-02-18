from matplotlib import pyplot as plt

# 전역 설정
plt.rcParams["font.family"] = 'NanumGothic'
plt.rcParams["font.size"] = 12
plt.rcParams["figure.figsize"] = (10, 10)

# 표시할 데이터 설정
# 총 합이 100이 아닐 경우 자동으로 비율을 계산
ratio = [73360, 52218, 45746, 33219, 30563]

# 라벨
label = ['삼성전자', '화웨이', '애플', '샤오미', '오포']

# 색상
color = ['#ff6600', '#ff0fff', '#ffff00', '#00ffff', '#0032ff']

# 확대비율
explodes = [0.0, 0.0, 0.0, 0.2, 0.1]

# 그래프 설정
plt.figure()

# 그래프 제목
plt.title('2018년 3분기 제조사별 스마트폰 출하량')

# 파이그래프 표시
# explode -> 중심으로부터 얼마만큼 떨어지는지 표현
# autopc -> 미설정 시 수치값 표시 안함
# startangle -> 기본값 0도
# shadow -> True 경우 그림자 표시
# 각 항목은 반시계 방향으로 회전하면서 배치
plt.pie(ratio, labels=label, colors=color, explode=explodes,
        autopct='%0.2f%%', shadow=False, startangle=90)

# 그래프 보이기
plt.show()

# 그래프 종료
plt.close()
