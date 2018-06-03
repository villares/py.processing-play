# JDF's timer thread example (from https://github.com/jdf/Processing.py-Bugs/issues/217 )

import threading
import time

class Timer(threading.Thread):
    def __init__(self, sleep, func):
        """ execute func(params) every 'sleep' seconds """
        self.func = func
        self.sleep = sleep
        threading.Thread.__init__(self, name="PeriodicExecutor")
        self.setDaemon(1)

    def run(self):
        while 1:
            time.sleep(self.sleep)
            self.func()

def setup():
    global t
    t = Timer(.8, doSomething)
    t.start()

def doSomething():
    println(millis())
