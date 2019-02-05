class chart(object):

    def __init__(self,date,open,high,low,close,volume,unadjustedVolume,change,changePercent,vwap,label,chaneOverTime):
        self.date = date
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume
        self.unadjustedVolume = unadjustedVolume
        self.change = change
        self.changePercent = changePercent
        self.vwap = vwap
        self.label = label
        self.changeOverTime = chaneOverTime


    def get_date(self):
        return self.date
    def get_open(self):
        return self.open
    def get_high(self):
        return self.high
    def get_low(self):
        return self.low
    def get_close(self):
        return self.close
    def get_volume(self):
        return self.volume
    def get_unadjustedVolume(self):
        return self.unadjustedVolume
    def get_change(self):
        return self.change
    def get_changePercent(self):
        return self.changePercent
    def get_vwap(self):
        return self.vwap
    def get_label(self):
        return self.label
    def get_changeOverTime(self):
        return self.changeOverTime