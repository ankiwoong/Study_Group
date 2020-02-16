# 한글 폰트 사용 확인
import os
import sys
from matplotlib import font_manager

# 시스템 폴더 스캔
font_manager._rebuild()

# 폰트 리스트 가져오기
# windows
if sys.platform == 'win32':
    # 시스템 글꼴 목록 리스트화
    font_list = font_manager.findSystemFonts()

    # 이름순 정렬
    font_list.sort()

    for file_path in font_list:
        # 폰트 속성 조회
        font_attribute = font_manager.FontProperties(fname=file_path)
        print('폰트 속성 : ' + str(font_attribute))

        # 폰트 이름 조회
        font_name = font_attribute.get_name()
        print('폰트 이름 : ' + str(font_name))

        # 폰트 파일 경로 + 폰트 이름 출력
        print('폰트 파일 경로 : %s >> 폰트 이름 : %s' % (file_path, font_name))
# mac os
else:
    # 설정파일 위치 조회
    cont_file_path = mpl.matplotlib_fname()
    print('설정 파일 위치 : ' + cont_file_path)

    # 설정파일 폴더 조회
    cont_file_dir = os.path.dirname(cont_file_path)
    print('설정 폴더 위치 : ' + cont_file_dir)

    # 폴더 경로 조합
    font_path = cont_file_dir + '/font/ttf'
    print('폰트 폴더 위치 : ' + font_path)

    # 폰트 폴더 오픈
    font_dir_open = 'open ' + font_path
    os.system(font_dir_open)
