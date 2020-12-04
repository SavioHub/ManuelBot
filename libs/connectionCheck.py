# interpop@interpop.com.br

import socket

def isConneted():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        if(s.connect_ex(('www.google.com', 80)) == 0):            
            return True
    except:
        pass

    s.close()
    return False
# while True:
#     print("connected" if isConneted() else "not connected")