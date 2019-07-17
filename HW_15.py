"""

15 .כתוב פונקציה המקבלת כפרמטר שם קובץ )בקובץ יהיו רק מספרים ]כל מספר בשורה נפרדת[ (.
הפונקציה תוסיף לאותו הקובץ מספר שהוא סכום כל המספרים שהיו בקובץ

"""


def sumFile(fileName):
    sum = 0
    with open("c:/python/" + fileName, 'r+') as f1:
        for num in f1:
            sum += int(num)
        f1.write("\n"+str(sum))

sumFile("test_1.txt")
