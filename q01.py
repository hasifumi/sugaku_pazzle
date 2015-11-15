# -*- coding: utf-8 -*-

def isKaibun(words):
    lst = str(int(words))
    if int(lst) == int(lst[::-1]):
        return True
    else:
        return False

i = 11
while True:
    if isKaibun(i) and isKaibun(format(i, 'b')) and isKaibun(oct(i)):
        print str(i) + ", " + str(format(i, 'b')) + ", " + str(oct(i))
        break
    else:
        print str(i)
    i += 2
