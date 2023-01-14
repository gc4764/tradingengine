import math

MAX_RISK_PERCENT = 4

class RMS:
    def __init__(self, capital, mtf = False,leverage = 1, risk_percent = 1, rrr = 3):
        self.mtf = mtf
        self.leverage = leverage
        self.capital = capital
        if self.mtf:
            self.margin = capital * self.leverage
        else:
            self.margin = capital

        if risk_percent > MAX_RISK_PERCENT:
            self.risk_percent = MAX_RISK_PERCENT
        else :
            self.risk_percent = risk_percent    
        self.rrr = rrr

    def updateCapital(self, capital):
        self.capital = capital
        if self.mtf:
            self.margin = capital * self.leverage
        else :
            self.margin = capital

    def setMaxLoss(self,max_loss):
        self.max_loss = max_loss

    def getMaxLoss(self):
        return self.max_loss

    def setMaxProfit(self, max_profit):
        self.max_profit = max_profit


    def getMaxProfit(self):
        return self.max_profit

    def setMaxOpenPositions(self, max_open_positions):
        self.max_open_positions = max_open_positions

    def getMaxOpenPositions(self):
        return self.max_open_positions

    def setMTFOn(self):
        self.mtf = True

    def setMTFOff(self):
        self.mtf = False

    def updateLeverage(self, leverage):
        self.leversge = leverage


    def updateMaxRiskPercent(self, risk_percent):
        if risk_percent > MAX_RISK_PERCENT:
            self.risk_percent = MAX_RISK_PERCENT
        else :
            self.risk_percent = risk_percent

    def updateRRR(self, rrr):
        self.rrr = rrr

    def getRiskValue(self):
        return self.margin * self.risk_percent / 100

    def getLongQty(self, long_price, sl_price):
        self.long_price = long_price
        self.long_sl_price = sl_price
        self.long_risk_per_scrip = self.long_price - self.long_sl_price

        if self.long_price ≤ self.long_sl_price:
            print("Sl price is above buying price")
            return None
        qty = self.getRiskValue() / self.long_risk_per_scrip
        return math.floor(qty)

    def getLongTarget(self):
        return self.rrr * self.long_risk_per_scrip + self.long_price


    def getLongRiskPercent(self):
        return self.long_risk_per_scrip * 100 / self.long_price

    def getLongTargetPercent(self):
        return self.getLongRiskPercent() * self.rrr




if __name__ == "__main__":
    rms = RMS(
