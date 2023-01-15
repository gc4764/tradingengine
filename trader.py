import csv
import sys
import os
import argparse

# exchange  NSE BSE MCX NFO NCD
#instrument_type EQUITY FUTSTK etc
#scrip INFY HCLTECH BPCL
#entry LONG SHORT EXIT COVER
#price 
#stoploss
#target
#time_frame 5MIN, 15MIN, 1HOUR, 2HOUR, 4HOUR, DAILY, WEEKLY
#trade_type SCALPING INTRADAY SWING SHORT_TERM LONG_TERM 
#analysis FUNDAMENTAL TECHNICAL
#did_i_follow_my_rule YES NO
#why_am_i_traging_this "comment"

CLOSE_LOOP = -1
EXIT = -2

LONG = "LONG"
SHORT = "SHORT"
EXIT = "LONG EXIT"
COVER = "SHORT COVER"

def getInt(message):

    """Get int value from keyboard 
       covert it into int type
       keep trying untill get int value"""
    while True:
        try:
            int_number = int(input(message + " : "))
            return int_number
        except:
            print()
            print("Enter an integer number, try again")
            continue



def getFloat(message):

    """Get folat value from keyboard 
    covert it into int type
    keep trying untill get float value"""
    while True:
        try:
            float_number = float(input(message + " : "))
            return float_number
        except:
            print()
            print("Enter a float / number, try again")
            continue



def to05Tick(number):

    nu =  (round(number *200, -1)) / 200
    return nu



def to0025Tick(number):

    nu =  (round(number *4000, -1)) / 4000
    return nu



def intoCurrencyTick(price):

    if price is None:
        return None
    else:
        return to0025Tick(price)




def intoStockTick(price):

    if price is None:
        return None
    else:
        return to05Tick(price)



def intoIntTick(price):

    if price is None:
        return None
    else:
        return int(price)




def getLongEntryPrice():

    return getFloat("Enter Long Buy Price : ")




def getShortEntryPrice():

    return getFloat("Enter Short Sell Price : ")




def getLongSLPrice(buffer_percent = 0.05):

    triger = getFloat("Enter SL for Long ( sell Price ) : ")
    sl = triger * ( 1 - buffer_percent / 100)
    return triger, sl





def getShortSLPrice(buffer_percent = 0.05):

    triger = getFloat("Enter SL for Short ( buy Price ) : ")
    sl = triger *( 1 + buffer_percent / 100)
    return triger, sl
        



def getLongTargetPrice():

    return getFloat("Enter Target for Long ( sell Price ) : ")




def getShortTargetPrice():

    return getFloat("Enter Target for Short ( buy Price ) : ")





def riskForLong(long_price, sl_price):

    risk = long_price - sl_price
    percent = (risk * 100) / long_price
    return risk, percent





def riskForShort(short_price, sl_price):

    risk =  sl_price - short_price
    percent = (risk * 100) / short_price
    return risk, percent




def targetForLong(long_price, target_price):

    target = target_price - long_price
    percent = (target * 100) / long_price
    return target, percent




def targetForShort(short_price, target_price):

    target = short_price - target_price
    percent = (target * 100) / short_price
    return target, percent





def isValidSLForLong(long_price, 
                     sl_price, 
                     min_risk_percent, 
                     max_risk_percent):

    risk, risk_percent  = riskForLong(long_price = long_price, 
                                      sl_price = sl_price)
    if risk_percent < min_risk_percent:
        return False
    elif risk_percent > max_risk_percent:
        return False
    else:
        return True




def isValidSLForShort(short_price, 
                      sl_price, 
                      min_risk_percent, 
                      max_risk_percent):

    risk, risk_percent  = riskForShort(short_price = short_price, 
                                       sl_price = sl_price)
    if risk_percent < min_risk_percent:
        return False
    elif risk_percent > max_risk_percent:
        return False
    else:
        return True




def isValidTargetForLong(long_price, 
                         target_price, 
                         min_target_percent, 
                         max_target_percent):

    target, target_percent  = targetForLong(long_price = long_price, 
                                            target_price = target_price)
    if target_percent < min_target_percent:
        return False
    elif target_percent > max_target_percent:
        return False
    else:
        return True





def isValidTargetForShort(short_price, 
                          target_price, 
                          min_target_percent, 
                          max_target_percent):

    target, target_percent  = targetForShort(short_price = short_price, 
                                             target_price = target_price)
    if target_percent < min_target_percent:
        return False
    elif target_percent > max_target_percent:
        return False
    else:
        return True





def isValidSLTargetForLong(long_price, 
                           sl_price, 
                           target_price, 
                           min_risk_percent, 
                           max_risk_percent, 
                           min_target_percent, 
                           max_target_percent):

    is_sl_valid = isValidSLForLong(long_price = long_price, 
                                   sl_price = sl_price, 
                                   min_risk_percent = min_risk_percent,
                                   max_risk_percent = max_risk_percent)
    is_target_valid = isValidTargetForLong(long_price = long_price, 
                                           target_price = tatget_price, 
                                           min_target_percent = min_target_percent, 
                                           max_target_percent = max_target_percent)
    if is_sl_valid and is_target_valid:
        return True
    else:
        return False





def isValidSLTargetForShort(short_price, 
                            sl_price, 
                            target_price, 
                            min_risk_percent, 
                            max_risk_percent, 
                            min_target_percent, 
                            max_target_percent):

    is_sl_valid = isValidSLForShort(short_price = short_price, 
                                    sl_price = sl_price, 
                                    min_risk_percent = min_risk_percent, 
                                    max_risk_percent = max_risk_peecent)
    is_target_valid = isValidTargetForShort(short_price = short_price, 
                                            target_price = target_price, 
                                            min_target_percent = min_target_percent, 
                                            max_target_percent = max_target_percent)
    if is_sl_valid and is_target_valid:
        return True
    else:
        return False





def getEntrySLPriceForLong(buffer_percent = 0.05, 
                           min_risk_percent = 0.5, 
                           max_risk_percent = 1.0):

    long_price = getLongEntryPrice()
    while True:
        triger, sl_price = getLongSLPrice(buffer_percent = buffer_percent)
        if isValidSLForLong(long_price = long_price, 
                            sl_price = triger,
                            min_risk_percent = min_risk_percent,
                            max_risk_percent = max_risk_percent):
            return long_price, triger, sl_price
        else:
            min_sl = long_price * (1 - min_risk_percent / 100)
            max_sl = long_price * (1 - max_risk_percent / 100)
            print("Enter sl between : {} and {} ".format(min_sl, max_sl))
            continue
    return long_price, triger, sl_price







def getEntrySLPriceForShort(buffer_percent = 0.05, 
                           min_risk_percent = 0.5, 
                           max_risk_percent = 1.0):

    short_price = getShortEntryPrice()
    while True:
        triger, sl_price = getShortSLPrice(buffer_percent = buffer_percent)
        if isValidSLForShort(short_price = short_price, 
                            sl_price = triger,
                            min_risk_percent = min_risk_percent,
                            max_risk_percent = max_risk_percent):
            return short_price, triger, sl_price
        else:
            min_sl = short_price * (1 + min_risk_percent / 100)
            max_sl = short_price * (1 + max_risk_percent / 100)
            print("Enter sl between : {} and {} ".format(min_sl, max_sl))
            continue
    return short_price, triger, sl_price





def getEntrySLTargetPriceForLong(buffer_percent = 0.05, 
                                 min_risk_percent = 0.5, 
                                 max_risk_percent = 1.0,
                                 min_target_percent = 1.0,
                                 max_target_percent = 3.0):

    long_price = getLongEntryPrice()
    while True:
        triger, sl_price = getLongSLPrice(buffer_percent = buffer_percent)
        if isValidSLForLong(long_price = long_price, 
                            sl_price = triger,
                            min_risk_percent = min_risk_percent,
                            max_risk_percent = max_risk_percent):
            break
        else:
            min_sl = long_price * (1 - min_risk_percent / 100)
            max_sl = long_price * (1 - max_risk_percent / 100)
            print("Enter sl between : {} and {} ".format(min_sl, max_sl))
            continue

    while True:
        target = getLongTargetPrice()
        if isValidTargetForLong(long_price = long_price,
                                target_price = target_price,
                                min_target_percent = min_target_percent,
                                max_target_percent = max_target_percent):
            break
        else:
            min_target = long_price * ( 1 + min_target_percent / 100)
            max_target = long_price * ( 1 + max_target_percent / 100)
            print("Enter target between : {} and {} ".format(min_target, max_target))
            continue
    return long_price, triger, sl_price, target_price






def getEntrySLTargetPriceForShort(buffer_percent = 0.05, 
                                 min_risk_percent = 0.5, 
                                 max_risk_percent = 1.0,
                                 min_target_percent = 1.0,
                                 max_target_percent = 3.0):

    short_price = getShortEntryPrice()
    while True:
        triger, sl_price = getShortSLPrice(buffer_percent = buffer_percent)
        if isValidSLForShort(short_price = short_price, 
                            sl_price = triger,
                            min_risk_percent = min_risk_percent,
                            max_risk_percent = max_risk_percent):
            break
        else:
            min_sl = short_price * (1 + min_risk_percent / 100)
            max_sl = short_price * (1 + max_risk_percent / 100)
            print("Enter sl between : {} and {} ".format(min_sl, max_sl))
            continue

    while True:
        target = getShortTargetPrice()
        if isValidTargetForShort(short_price = short_price,
                                target_price = target_price,
                                min_target_percent = min_target_percent,
                                max_target_percent = max_target_percent):
            break
        else:
            min_target = short_price * ( 1 - min_target_percent / 100)
            max_target = short_price * ( 1 - max_target_percent / 100)
            print("Enter target between : {} and {} ".format(min_target, max_target))
            continue
    return short_price, triger, sl_price, target_price



def getPrice(buffer_percent = 0.05,                     
             min_risk_percent = 0.5,
             max_risk_percent = 1.0,
             min_target_percent = 1.0,
             max_target_percent = 3.0):

    order_type = getOrderType()

    if order_type == LONG:
        # order_type, long_price, triger, sl_price, target
        return order_type, getEntrySLTargetPriceForLong(buffer_percent = 0.05,
                                                        min_risk_percent = 0.5,
                                                        max_risk_percent = 1.0,
                                                        min_target_percent = 1.0,
                                                        max_target_percent = 3.0)
    elif order_type == SHORT:
        return order_type, getEntrySLTargetPriceForShort(buffer_percent = 0.05,
                                                        min_risk_percent = 0.5,
                                                        max_risk_percent = 1.0,
                                                        min_target_percent = 1.0,
                                                        max_target_percent = 3.0)
    elif order_type == LONG_SL:
        #order_type, _ , triger, sl_price, _
        pass
    elif order_type == SHORT_SL:
        pass
    elif order_type == LONG_TARGET:
        #order_type, _ , _ , _ , target
        pass
    elif order_type == SHORT_TARGET:
        pass
    elif order_type == LONG_SL_TARGET:
        #order_type, _ , triger, sl_price, target
        pass
    elif order_type == SHORT_SL_TARGET:
        pass
    else:
        print()





def createOrder():
    #
    exchange, instrument_type, scrip = getScrip(file_of_scrip, scrip_name)
    order_type, price, triger, sl_price, target = getPrice(buffer_percent = 0.05,
                                                           min_risk_percent = 0.5,
                                                           max_risk_percent = 1.0,
                                                           min_target_percent = 1.0,
                                                           max_target_percent = 3.0)
    time_frame = getTimeFrame()
    trade_type = getTradeType()
    analysis_type = getAnalysisType()
    is_based_on_rule = getIsBasedOnRule()
    note = getNote()

    #retrun all variable


def toUpperCase(list_of_string):
    #done
    data = []
    if type(list_of_string) == list:
        for item in list_of_string:
            data.append(toUpperCase(item))
        return data
    elif type(list_of_string) == set:
        list_of_string = list(list_of_string)
        return toUpperCase(list_of_string)
    elif type(list_of_string) == tuple:
        list_of_string = list(list_of_string)
        return toUpperCase(list_of_string)  
    elif type(list_of_string) == str:
        return  str.upper(list_of_string)
    elif type(list_of_string) == int:
        return  list_of_string
    else:
        print("unknown data type, can not UPERCASE")
        return  list_of_string



def getExchange():
    #
    exchanges = ["nse","bse","ncd","nfo","mcx"]
    exchange = toUpperCase(getChoice(exchanges))
    print(exchange)
    return exchange

def getAllInstrumentType(file, index):
    #
    instruments = []
    with open (file, "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for row in csv_reader:
            instruments.append(row[index])
    instrument_type =  list(set(instruments))
    return instrument_type

def getInstrument(file, instrument_index):
    #
    data = getChoice(getAllInstrumentType(file, instrument_index))
    print(data)
    return data

def getCSVDataFromFile(file):
    #
    data = []
    try:
        with open(file, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                data.append(row)
        return noneSafety(data)
    except:
        print("unable to open file : {}".format(file))
        sys.exit()

def noneSafety(data):
    #done
    if data is None:
        return False, data
    else:
        return True, data

def equalityTest(value1, value2):
    #done
    if toUpperCase(value1) == toUpperCase(value2):
        return True
    else:
        return False

def intoStandardString(data):
    if isString(data):
        return toUpperCase(data.strip())
    else:
        print("Not a string data")
        return data

def filterData(data, index1, value1, index2=None, value2=None, index3=None, value3=None):
    filtered_data = []
    if index3 == None:
        if index2 == None:
            for row in data:
                if equalityTest(row[index1], intoStandardString(value1)):
                    filtered_data.append(row)
            return noneSafety(filtered_data)
        else:
            for row in data:
                if equalityTest(row[index1], intoStandardString(value1)):
                    if equalityTest(row[index2], intoStandardString(value2)):
                        filtered_data.append(row)
            return noneSafety(filtered_data)
    else:
        for row in data:
            if equalityTest(row[index1], intoStandardString(value1)):
                if equalityTest(row[index2], intoStandardString(value2)):
                    if equalityTest(row[index3], intoStandardString(value3)):
                        filtered_data.append(row)
        return noneSafety(filtered_data)


def filterScrip(data, exchange_index, exchange, instrument_type_index, instrument_type, scrip_index, scrip):
    filtered_scrip_list = []
    ok, data_1 = filterData(data, exchange_index, exchange, instrument_type_index, instrument_type)
    if ok:
        for row in data_1:
            if intoStandardString(row[scrip_index]).startswith(intoStandardString(scrip)):
                filtered_scrip_list.append(row)
        if len(filtered_scrip_list) > 0:
            return True, filtered_scrip_list
        else:
            print("scrip not found , try again")
            return False, None




def isList(data):
    #done
    if type(data) == list:
        return True
    else:
        return False
def isString(data):
    #done
    if type(data) == str:
        return True
    else:
        return False

def isInt(data):
    #done
    if type(data) == int:
        return True
    else:
        return False

def isDict(data):
    #done
    if type(data) == dict:
        return True
    else :
        return False

def isTuple(data):
    #done
    if type(data) == tuple:
        return True
    else:
        return False

def isSet(data):
    #done
    if type(data) == set:
        return True
    else:
        return False


def isNone(data):
    #done
    if data is None:
        return True
    else:
        return False

def isNotNone(data):
    #done
    if data is not None:
        return True
    else:
        return False

def printInMultipleRows(data):
    #done
    i = 1
    for row in data:
        print(i, " => ", row)
        i = i + 1

def printInSingleRow(data):
    #done
    print(data)


def printDict(data):
    #done
    for key, value in zip(data.keys(), data.values()):
        print(key, " => ", value)

def printData(data):
    #done
    if isNotNone(data):
        if isList(data) or isTuple(data) or isSet(data):
            printInMultipleRows(data)
        elif isString(data) or isInt(data):
            printInSingleLine(data)
        elif isDict(data):
            printDict(data)
        else:
            print("unknown data type can not print")


def getScrip(file,exchange_index, instrument_type_index,scrip_index):
    exchange = getExchange()
    instrument_type = getInstrument(file, instrument_type_index)
    ok, raw_data = getCSVDataFromFile(file)
    if ok:
        while True:
            scrip = input("Enter scrip Name : ").upper().strip()
            if scrip is None:
               printData(raw_data)
            else:
                ok, filtered_scrip_list = filterScrip(raw_data, exchange_index, exchange, instrument_type_index, instrument_type, scrip_index, scrip)
                if ok:
                    printData(filtered_scrip_list)
                    #getChoice()




def makeChoice(choice_list):
    #done
    if type(choice_list) == list:
        choice_list.sort()
    elif type(choice_list) == set:
        choice_list = list(choice_list)
        choice_list.sort()
    elif type(choice_list) == dict:
        pass
    else:
        choice_list = list(choice_list)
        choice_list.sort()
    print("0 => Exit")
    incr  = 1
    for choice in choice_list:
        print(str(incr) ," => " ,  toUpperCase(choice))
        incr = incr + 1



def getActionChoice():
    #complete
    choice_list = ["To display all orders", "To add an order", "To search order", "To modify an order", "To delete an order"]
    getChoice(choice_list)


def getItemFromList(data, number):
    if number == 0:
        return CLOSE_LOOP
    else:
        try:
            return toUpperCase(data[number - 1])
        except:
            print("can not retrive item from list")
            return None


def getChoice(choice_list):
    #complete
    while True:
        print()
        print("-"*20)
        makeChoice(choice_list)
        max_number = len(choice_list)
        try:
            number = int(input("Enter your choice : "))
            if number < 0 or number > max_number:
                print("It should be between 0 and {}".format(max_number))
                print()
                continue
            else:
                return getItemFromList(choice_list, number)
        except:
            print()
            print("Enter a number, not a string ")
            continue

def displayAllRecords(file_name):
    #complete
    with open(file_name, 'r+') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            print(row)


def addRecord(file_name, data):
    #complete
    with open(file_name, "a+") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(data)


def action():
    choice = getChoice(5)

    if choice == 0:
        return 0
    elif choice == 1:
        displayAllRecord(file_name)
    elif choice == 2:
        ###
        addRecord(file_name)



def setUp():
    """Create / update file,
    download files"""


def trader():
    """Show option"""
    choice_list = []
    choice = getChoice(choice_list)


master_db = "scrip.csv"

#getAllInstrumentType(master_db,3)
#getInstrument(master_db, 3)

#0 exchange
#3 instrument
#5 scrip 
#scrip name

#getScrip(master_db,0, 3, 5)
#ins = getInstrument(master_db,3)
#print(ins)

ll = ["ab","cd","ef","gh"]

#ent = getEntry()
#print(ent)


print(to0025Tick(83.4842))
parser = argparse.ArgumentParser()

parser.add_argument("--getint", action="store_true")


args = parser.parse_args()

if args.getint:
    getInt("hell")

