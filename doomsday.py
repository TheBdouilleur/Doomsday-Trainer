ctDict = { # Data gathered by Conway
    '15':3, 
    '16':2,
    '17':0,
    '18':5,
    '19':3,
    '20':2,
    '21':0,
    '22':5,
    '23':3,
}
mthDict = { # Data gathered by Conway
    'Jan':(3, 4), # (Non-leap year, leap year)
    'Feb':(28, 29),
    'Mar':(7,), # Trailing comma necessary for tuple
    'Apr':(4,),
    'May':(9,),
    'Jun':(6,),
    'Jul':(11,),
    'Aug':(8,),
    'Sep':(5,),
    'Oct':(10,),
    'Nov':(7,),
    'Dec':(12,)
}


def isLeapYear(year:int):
    if year%4 == 0:
        if year%100 == 0:
            if year%400 != 0:
                return False
            else: return True
        else: return True    
    else: return False

def dayFromDate(date:str):
    date = date.split(' ')
    yr = date[2]
    ct = yr[0:2]
    dc = int(yr[2:4])
    dy = int(date[0])
    mthDoomsday = mthDict[date[1]][-1] if isLeapYear(int(yr)) else mthDict[date[1]][0] 
    ctDoomsday = int(ctDict[ct])
    dmDifference = dy - mthDoomsday
    #FIXME. Currently supports only 4-digit-year dates
    dyOfWeek = (dmDifference + ctDoomsday + dc//12 + dc%12 + (dc%12)//4)%7 # Implementation of Conway's equation
    return dyOfWeek

    
if __name__ == "__main__":
    print(dayFromDate('13 Dec 1672'))
