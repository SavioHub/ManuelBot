import sys
from libs import connectionCheck
from libs import sendMail

count = 0
while True:
    if not connectionCheck.isConneted():
        count += 1
        if count == 100:
            print("sem internet")
            while True:
                if connectionCheck.isConneted():
                    sendMail.send()
                    count = 0
                    break
    else:
        count = 0