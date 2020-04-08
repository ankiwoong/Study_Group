import re
import pyperclip        # pip install pyperclip

'''
대표이사 : 권봉석, 배두용   사업자등록번호 : 107-86-14075   통신판매업신고번호 : 제1997-00084호   대표번호 : 02-3777-1114
주소 : 서울시 영등포구 여의대로 128 LG트윈타워   제품 및 서비스 문의 : 1544-7777 서비스이메일 : lgservice@lg.kr

중에 이메일 주소만 가져오고 싶으면 전체 복사후 아래 코드 실행 후 붙여넣기
'''

# Create email regex.
email_regex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+      # username
    @                      # @symbol
    [a-zA-Z0-9.-]+         # domain name
    (\.[a-zA-Z]{2,4}){1,2} # dot-something
    )''', re.VERBOSE)


def find_match_list():
    # Find the text that matches the email pattern in the copied contents of the clipboard.
    text = pyperclip.paste()

    matches = []

    for email in email_regex.findall(text):
        matches.append(email[0])

    return matches


def copy_result_to_clipboard(matches):
    # Copy results to the clipboard.
    if len(matches) > 0:
        pyperclip.copy('\n'.join(matches))
        print('클립보드에 복사되었습니다.')
    else:
        print('메칭되는 패턴이 없습니다.')


def main():
    matches = find_match_list()
    copy_result_to_clipboard(matches)


main()
