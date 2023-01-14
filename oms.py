





def placeLongLimitOrder(rms_obj, broker_api_obj, exchange, scrip, price, stop_loss, target, time_frame, message):
    if rms.isTodayLossLimitReached():
        print("Today Loss Limit Reached. No Trade For today")
    else:
        opened,postion_type, qty =  rms_obj.isPositionOpened(exchange, scrip):
        if opened
            print("{position_type} positon is already opened in {exchange}:{scrip} with {qty}")

        else:
            pending, order_type, qty = rms_obj.isAnyPendingOrder(exchange, scrip)
            if pending:
                print("{order_type} order is Already pending in {exchange}:{scrip} with {qty}")
            else:
                qty = rms_obj.getLongQty(long_price, stop_loss)
                if qty ≤ 0:
                    print("Can not open long position in {exchange}:{scrip} with {qty}")
                else:
                    data = broker_api_obj.placeLimitOrder()
                    updateOrderBook(data)


def modifyLongLimitOrderById(order_id, new_buy_price, message):
    pass

def modifyLongLimitOrderByScrip(exchange, scrip, message):
    pass

def cancelLongPendingOrderById(order_id, message):
    pass

def cancelLongPendingOrderByScrip(exchange, scrip, message):
    pass

def cancelAllLongPendingOrder(message):
    pass

def cancellAllOrder(message):
    pass


def exitLongPositionAtLimit(exchange, scrip, sell_price, message):
    pass

def exitLongPositionAtMarket(exchange, scrip, message):
    pass


def exitAllLongPosition(message):
    pass


def exitAllPosition(message):
    pass

