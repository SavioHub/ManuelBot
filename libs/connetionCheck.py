# interpop@interpop.com.br

import socket

def isConneted():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    try:
        ok = s.connect_ex(('www.google.com', 80))

        if(ok == 0):
            return True
    except:
        pass

    s.close()
    return False
        

print("Tem Internet" if isConneted() else "nao Tem internet")