from time import sleep

class Clock(object):
    
    def __init__(self, second, minute, hour):
        self._second = second
        self._minute = minute
        self._hour = hour
    
    def run(self):
        #走字
        self._second += 1
        if self._second >= 59:
            self._minute += 1
            self._second = 0
            if self._minute >= 59:
                self._hour += 1
                self._minute = 0
                if self._hour == 24:
                    _hour = 0