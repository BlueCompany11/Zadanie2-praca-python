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
        try:
            days=0
            for two_dates in self.dates:
                beg_date,end_date=SplitToTwoDates(two_dates)
                d1 = date(GetYear(beg_date), GetMonth(beg_date), GetDay(beg_date))
                d2 = date(GetYear(end_date), GetMonth(end_date), GetDay(end_date))
                delta = d2 - d1
                days+=int(delta.days)
            if days == 0:
                return "BRAK"
            return self.price/days
        except ValueError:
            return 'Format daty jest niepoprawny'



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


def IfStringLooksLikeDate(date):
	try:
		if not 0<GetDay(date)<=31:
			return False
		if not 0<GetMonth(date)<=12:
			return False
		if not 1900<=GetYear(date):
			return False
		if not date[3] == '.' and date[6] == '.':
			return False
	except ValueError:
		return False
	return True

def GetDay(date):
    return int(date[:2])

def GetMonth(date):
    return int(date[3:5])

def GetYear(date):
    return int(date[6:])

def SplitToTwoDates(date):
    first_date=date[:len('01.01.2017')]
    second_date=date[len('01.01.2017-'):]
    return first_date, second_date
