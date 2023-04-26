import sys
import socket as so

objetivo = so.gethostbyname(input("Inserta la direcion IP para escaner los puertos:"))

print('escaneando objetivo' +  objetivo)

try:
    for port in range(1,150):
        s = so.socket(so.AF_INET, so.SOCK_STREAM)
        so.setdefaulttimeout(1)
        resul = s.connect_ex((objetivo, port))
        if resul == 0:
            print('El puerto {} esta abierto'.format(port))
        s.close()
except:
    print('\n saliendo...')
    sys.exit(0) 