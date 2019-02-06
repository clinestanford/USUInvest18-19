
import datetime
class DateUtility:

    #Returns todays date with the passed minutes and hour in format hh:mm
    def TodaysDateWithHour(self,hour):
        try:
            x = datetime.datetime.now()
            x.hour = hour[0,2]
            x.minute = hour[3,2]
            return x
        except ValueError:
            print("Bad Hour input")
