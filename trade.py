




def main():
    today  = getTodayDayOfWeek()
    if today == SAT or today == SUN :
        print("Today is {today} . Market is not open")
        return -1

    else:
        holiday = isTodayHoliday()
        if holiday:
            print("Today is Holiday. Market is not open")
            return -2
        else:
            trade.run()

