from time import sleep
from threading import Thread,Lock

class Account(object):
    def __init__(self):
        self._balance = 0
        self._lock = Lock()
    
    @property
    def balance(self):
        return self._balance
    
    def deposit(self,money):
        #先获取锁才能执行后续的代码
        self._lock.acquire()
        try:
            new_balance = money + self._balance
            sleep(0.1)
            self._balance = new_balance
        finally:
            self._lock.release()
       
    
class AddMoneyThread(Thread):
    def __init__(self,account,money):
        super().__init__()
        self._account = account
        self._money = money
    
    def run(self):
        self._account.deposit(self._money,)

def main():
    account = Account()
    threads = []

    for _ in range(100):
        t = AddMoneyThread(account,1)
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    print("账户余额为：%d" %account.balance)
    
if __name__ == '__main__':
    main()