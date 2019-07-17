"""

16 .כתוב פונקציה המקבלת כפרמטר: שם קובץ + מילה ומחזירה True אם המילה קיימת בקובץ,
אחרת מחזירה False

"""


def findWordFile(fileName,word):
    with open("c:/python/" + fileName) as f1:
        for line in f1:
            if word.lower() in list(line.lower().split()):
                return True
        else:
            return False


print(findWordFile("test_2.txt", "hello"))
print(findWordFile("test_2.txt", "blue"))
print(findWordFile("test_2.txt", "HeLlo"))
