from progress.bar import IncrementalBar     # pip install progress
from fpdf import FPDF                       # pip install fpdf
from PyPDF2 import PdfFileMerger            # pip install PyPDF2
from PIL import Image                       # pip install Pillow
import argparse                             # pip install argparse
import qprompt                              # pip install qprompt

from os.path import join
from glob import glob
from time import sleep
import datetime as dt
import platform
import os
import os.path


def pdf_merge(args, name, step, total):
    dpi = 100

    merger = PdfFileMerger(strict=False)

    error_count = 0
    temp_file_list = []

    bar = IncrementalBar("%02d/%02d" % (step, total),
                         max=len(args), fill='@', suffix='%(percent)d%%')

    for i, item in enumerate(args):
        # 경로를 절대경로로 변환
        item = os.path.abspath(item)

        # 파일이름과 확장자 분리
        filename, extenstion = os.path.splitext(item)
        extenstion = extenstion.lower()

        # 원소가 이미지인 경우 pdf로 변환
        if extenstion in [".jpg", ".png"]:
            temp = "%s_temp.pdf" % filename
            pdf = FPDF('P', 'mm', 'A4')
            pdf.add_page()

            im = Image.open(item)
            width, height = im.size
            im.close()

            width = (width * dpi) / 25.4
            height = (height * dpi) / 25.4
            scalex = 210 / width
            scaley = 297 / height

            if scalex < scaley:
                scale = scalex
            else:
                scale = scaley

            if scale > 1:
                scale = 1

            resize_width = scale * width
            resize_height = scale * height

            x = (210-resize_width) // 2
            y = (297-resize_height) // 2

            if x < 0:
                x = 0
            if y < 0:
                y = 0
            # print(x)
            # print(y)
            # print(resize_width)
            # print(resize_height)

            pdf.image(item, x, y, resize_width, resize_height)
            pdf.output(temp, "F")
            temp_file_list.append(temp)
            merger.append(temp)
        else:
            merger.append(item)

        bar.next()
        sleep(0.1)

    merger.write(name)
    merger.close()

    for k in temp_file_list:
        os.remove(k)

    bar.finish()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser._action_groups.pop()
    required = parser.add_argument_group('필수 파라미터')
    optional = parser.add_argument_group('옵션값')
    optional.add_argument('-o', '--output', help='생성될 파일의 경로')
    optional.add_argument(
        '-i', '--input', help='입력할 파일이나 폴더의 경로. 복수 지정시 콤마로 구분')
    optional.add_argument('-d', '--dir', help='작업폴더')
    optional.add_argument(
        '-g', '--group', help='입력파일들을 묶을 그룹 수. 빈 값이거나 0인 경우 단일 파일로 생성함')
    args = parser.parse_args()

    if not args.output:
        args.output = dt.datetime.now().strftime("%Y%m%d%H%M%S")

    if not args.dir:
        args.dir = os.getcwd()

    if platform.system() == 'Windows':
        args.dir = args.dir.replace("/", "\\")

    print("[Wording Dir] ", args.dir)

    if args.input:
        source = args.input.split(",")

        for i, v in enumerate(source):
            source[i] = os.path.join(args.dir, v)
    else:
        if not os.path.isdir(args.dir):
            print("[Error] Path is not found")
            quit()

        source = [args.dir]

    if os.path.isdir(source[0]):
        del(source[0])

        for ext in ('*.gif', '*.png', '*.jpg', '*.pdf'):
            source.extend(glob(os.path.join(args.dir, ext)))

    if not source:
        print("[Error] 처리할 파일들을 찾을 수 없습니다.")
        quit()

    source.sort()

    if not args.group:
        group = len(source)
    else:
        group = int(args.group)

    p = args.output.rfind(".")
    if p > -1:
        ext = args.output[p:]
        if (ext != ".pdf"):
            args.output += ".pdf"
    else:
        args.output += ".pdf"

    output = os.path.join(args.dir, args.output)
    # print(output)

    x, y = divmod(len(source), group)

    if (y > 0):
        x += 1

    print(" " + "-" * 50)
    print(" 총 %d개의 pdf 파일을 생성합니다." % x)
    print(" " + "-" * 50)
    print()

    for i in range(0, x):
        j = i*group
        k = j+group
        merge = source[j:k]

        if x > 1:
            filename, file_extension = os.path.splitext(output)
            save = "%s_%03d.pdf" % (filename, i+1)
        else:
            save = output

        pdf_merge(merge, save, i+1, x)

    print()
    print(" " + "-" * 50)
    print(" 작업이 완료되었습니다.")
    print(" " + "-" * 50)
