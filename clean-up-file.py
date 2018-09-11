# coding=utf-8
newFile = open("eindResultaat.csv","w+")

remove = ['| LinkedIn', '| …', ', …"' , '"']

def rreplace(s, old, new, occurrence):
    li = s.rsplit(old, occurrence)
    return new.join(li)

with open('LinkedIn BI Alumni Fontys - Resultaten (1).csv') as fp:
    for line in fp:
        for r in remove:
            line = line.replace(r, "")
        line = line.replace('-', ';', 1)
        line = rreplace(line, '-', ';', 1)

        if line.count(';') == 2:
            newFile.write(line)