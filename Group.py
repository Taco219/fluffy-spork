import re

informatieAnalist = []
businessIntelligenceConsultant = []
businessConsultant = []
manager = []
zzp = []
docent = []
overig = []

newFile = open("overige.csv","w+")
sorted = open("gesoorteerd.csv","w+")

def checkStrings(strings, checkLine):
    for s in strings:
        if s.lower() in checkLine.lower():
            return True
    return False

with open('eindResultaat.csv') as fp:
    for line in fp:
        if checkStrings(["analist", 'Analyst'], line):
            informatieAnalist.append(line)
        elif checkStrings(['teacher', 'docent','Teacher','Docent'], line):
            docent.append(line)
        elif checkStrings(["Manager", "Accountmanager", 'Managing', 'ceo', 'founder', 'eigenaar', 'owner'], line):
            manager.append(line)
        elif checkStrings(["Intelligence Consultant","consultant"], line):
            businessIntelligenceConsultant.append(line)
        elif checkStrings(["Business Consultant", "Consultant", "Scrum", "Business"], line):
            businessConsultant.append(line)
        elif checkStrings(['engineer', 'Development', 'Web Developer', 'Database', 'sql','test','auditor'], line):
            zzp.append(line)
        else:
            overig.append(line)
            newFile.write(line)

    for analist in informatieAnalist:
        an = re.sub(';.*?;', ';Informatie analist;', analist, flags=re.DOTALL)
        sorted.write(an)
    for bic in businessIntelligenceConsultant:
        bc = re.sub(';.*?;', ';Business intelligence consultant;', bic, flags=re.DOTALL)
        sorted.write(bc)
    for buc in businessConsultant:
        bu = re.sub(';.*?;', ';Business consultant;', buc, flags=re.DOTALL)
        sorted.write(bu)
    for man in manager:
        ma = re.sub(';.*?;', ';Manager;', man, flags=re.DOTALL)
        sorted.write(ma)
    for zp in zzp:
        z = re.sub(';.*?;', ';Zzp;', zp, flags=re.DOTALL)
        sorted.write(z)
    for doc in docent:
        d = re.sub(';.*?;', ';Docent;', doc, flags=re.DOTALL)
        sorted.write(d)
    for oth in overig:
        o = re.sub(';.*?;', ';Overig;', oth, flags=re.DOTALL)
        sorted.write(o)
