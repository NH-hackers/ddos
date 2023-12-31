#!/bin/python3
from treq import get
from twisted.internet import reactor
import os

# This method is called whenever a response is recieved
def done(response):
   if response.code == 200:
       # do something with response
        reactor.stop()
def loop():
    while True:
        try:
            for i in range(100000):
                get("http://www.agveducation.com").addCallback(done)
            reactor.run()
        except:
            os.system('python3 api.py')
loop()
