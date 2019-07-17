"""
14 .כתוב תוכנית הקולטת מילים מהמשתמש. עד אשר תיקלט המילה ‘exit .‘כל מילה שנקלטה כתוב
לקובץ טקסט כלשהו. לאחר מכן הדפס את תכולת הקובץ
"""

with open("c:/python/test_1.txt", 'w+') as f1:
    while True:
        word = input("Please enter a word (exit to exit): ")
        if word.upper() == 'EXIT':
            break
        f1.write(word+"\n")
    f1.seek(0)
    for line in f1:
        print(line, end="")
