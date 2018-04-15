from datetime import date

class Data(object):
    """description of class"""
    def __init__(self,dictionary, **kwargs):
        #['Nazwa', 'ID', 'Cena', 'Pozycja', 'Poziom', 'Opis', 'Nr Zamówienia']
        self.name=dictionary['Nazwa']
        self.id=dictionary['ID']
        self.price=dictionary['Cena']
        self.rank=dictionary['Pozycja']
        self.level=dictionary['Poziom']
        self.description=dictionary['Opis']
        self.no_order=dictionary['Nr Zamówienia']
        self.dates=[]
        for key in dictionary:
            if InsertFieldToDates(dictionary,key):
                self.dates.append(key)

    def __str__(self):
        ret= ('Nazwa: '+ str(self.name) + ' ID: ' + str(self.id) + ' Cena: '+ str(self.price)
             + ' Pozycja: ' + str(self.rank) + ' Poziom: ' +  str(self.level) + ' Opis: '+ str(self.description)
             + ' Nr Zamówienia: '+ str(self.no_order) +'\n' + "Daty: "+ str(self.dates))
        return ret

    def AvgCost(self):
        days=0
        for two_dates in self.dates:
            beg_date,end_date=SplitToTwoDates(two_dates)
            d1 = date(GetYear(beg_date), GetMonth(beg_date), GetDay(beg_date))
            d2 = date(GetYear(end_date), GetMonth(end_date), GetDay(end_date))
            delta = d2 - d1
            days+=int(delta.days)
        if days == 0:
            return "BRAK KOSZTOW"
        return self.price/days

def InsertFieldToDates(dictionary, key):
    if IsHeaderDate(key) and (dictionary[key] != '-' or len(dictionary[key]) <=3) and dictionary[key] is not None:
        return True
    return False

def IsHeaderDate(field):
    string=str(field)
    if len(string) != len('01.01.2017-15.01.2017'):
        return False
    if string[10] != '-':
        return False
    first_date, second_date=SplitToTwoDates(string)
    if not IfStringLooksLikeDate(first_date):
        return False
    if not IfStringLooksLikeDate(second_date):
        return False
    return True


def IfStringLooksLikeDate(mydate):
    if len(mydate)<10:
        return False
    try:
        if  mydate[2] != '.' or mydate[5] != '.':
            return False
        d = date(GetYear(mydate), GetMonth(mydate), GetDay(mydate))
    except ValueError:
        return False
    return True

def GetDay(mydate):
    return int(mydate[:2])

def GetMonth(mydate):
    return int(mydate[3:5])

def GetYear(mydate):
    return int(mydate[6:])

def SplitToTwoDates(mydate):
    first_date=mydate[:len('01.01.2017')]
    second_date=mydate[len('01.01.2017-'):]
    return first_date, second_date
