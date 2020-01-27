#Chloe Puckett
#Lab 10, COSC1336 MW18
#Creating a clock class, validating data, and strings in classes. 


class Clock():
    hour=12
    minute=00
    second=00
    def __init__(self,hr,mint,sec):
        if hr>=1 and hr<=24:
            self.__hour= hr
        else:
            self.__hour=Clock.hour
        if mint>=0 and mint<=60:
            self.__minute= mint
        else:
            self.__minute=Clock.minute
        if sec>=0 and sec<=60:
            self.__second= sec
        else:
            self.__second=Clock.second

    def getHour(self):
        return self.__hour
        
    def setHour(hr):
        self.__hour=hr

    def getMinute(self):
        return self.__minute
      
    def setMinute(self, minu):
        self.__minute=minu

    def getSecond(self):
        return self.__second

    def setSecond(self, sec):
        self.__second=sec

    def __str__(self):
        if self.__hour>=13:
            self.__hour=(self.__hour-12)
            return str("{hr:02}:{min:02}:{sec:02}".format(hr=self.__hour, min=self.__minute, sec=self.__second)+" PM")
        else:
            return str("{hr:02}:{min:02}:{sec:02}".format(hr=self.__hour, min=self.__minute, sec=self.__second)+" AM")



stopwatch= Clock(0, 0, 0)
print (stopwatch)
watch=Clock(10,30,0)
print (watch)
clock1=Clock(34,-100,4345)
print(clock1)
clock2=Clock(22,45,30)
print(clock2)
crazyClock=Clock(90,1000,-40)
print(crazyClock)
pmClock=Clock(16,61,32)
print(pmClock)
amClock=Clock(9,23,70)
print(amClock)


#Output:
##12:00:00 AM
##10:30:00 AM
##12:00:00 AM
##10:45:30 PM
##12:00:00 AM
##04:00:32 PM
##09:23:00 AM
##>>> 

