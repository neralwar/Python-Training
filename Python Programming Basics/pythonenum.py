from enum import Enum
class Country(Enum):
    Afghanistan = 93
    Albania = 355
    plgeria = 213
    zndorra = 376
    Angola = 244
    Antarctica = 672

countrylist=[]
for n in (Country):
    countrylist.append(n.name)
countrylist.sort()
countrylist.reverse()
print(countrylist)