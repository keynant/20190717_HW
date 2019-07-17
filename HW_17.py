"""
17 .כתוב פונקציה המקבלת כפרמטר: שם קובץ מקור + שם קובץ יעד. הפונקצייה תעתיק את תכולת
קובץ המקור לקובץ היעד בסדר אותיות הפוך
"""


def copyFileReversed(ogFile, cpFile):
    with open('c:/python/' + ogFile) as f1:
        f2 = open('c:/python/' + cpFile, 'w')
        eof = f1.seek(0, 2)  # eof = end of file
        for index in range(eof, -1, -1):
            f1.seek(index)
            f2.write(f1.read(1))
        f2.close()


copyFileReversed('test_2.txt', 'test2 copy.txt')
