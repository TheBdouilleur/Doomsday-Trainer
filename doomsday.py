import logging, time, random

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
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']




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

def randomDate():
    dateList = [str(random.randint(1,28)), str(random.choice(months)), str(random.randint(1582, 2300))] # (Start of Gregorian calendar, end of useful dates)
    date = ' '.join(dateList)
    return date

def askDate():
    ranDate = randomDate()
    t1 = time.perf_counter()
    a = input('What day was the {} ?'.format(ranDate))
    t = time.perf_counter() - t1
    r = dayFromDate(ranDate)
    
    if int(a) == r:
        print('Congrats! Ran in ', t)
        logging.info('New perf: {0} answered in {1} seconds!'.format(ranDate, t))
    else:
        print('False: real answer was', r)
        logging.info(' {0} False {1} in {2} seconds: real answer: {3}'.format(a, ranDate, t, r))

if __name__ == "__main__":
    print(dayFromDate('13 Dec 1672'))
    askDate()
