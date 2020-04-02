import doomsday, logging, time, random

logging.basicConfig(filename='average.log', level=logging.DEBUG)

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


def randomDate():
    dateList = [str(random.randint(1,28)), str(random.choice(months)), str(random.randint(1582, 2300))] # (Start of Gregorian calendar, end of useful dates)
    date = ' '.join(dateList)
    return date

def askDate():
    ranDate = randomDate()
    t1 = time.perf_counter()
    a = input('What day was the {} ?'.format(ranDate))
    t = time.perf_counter() - t1
    r = doomsday.dayFromDate(ranDate)
    
    if int(a) == r:
        print('Congrats! Ran in ', t)
        logging.info('New perf: {0} answered in {1} seconds!'.format(ranDate, t))
    else:
        print('False: real answer was', r)
        logging.info(' {0} False {1} in {2} seconds: real answer: {3}'.format(a, ranDate, t, r))

if __name__ == "__main__":
    askDate()