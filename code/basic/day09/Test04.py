from time import time, localtime, sleep


class Clock(object):

    def __init__(self, hour, minute, second):
        self._hour = hour
        self._minute = minute
        self._second = second

    @classmethod
    def now(cls):
        now_time = localtime(time())
        return cls(now_time.tm_hour, now_time.tm_min, now_time.tm_sec)

    def run(self):
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._hour += 1
                self._minute = 0
                if self._hour == 24:
                    self._hour = 0
    
    def show(self):
        """
        显示时间
        """
        return '%02d:%02d:%02d'%(self._hour, self._minute, self._second)


def main():
    clock = Clock.now()
    while(True):
        clock.run()
        sleep(1)
        print(clock.show())

if __name__ == '__main__':
    main()
