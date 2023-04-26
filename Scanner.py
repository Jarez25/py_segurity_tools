import sys
import socket

objeto = socket.gethostbyname(input('insertar la IP \n'))

print('escaneando la IP ' +  objeto)


try:
    for port in range(1,150):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        r = s.connect_ex((objeto, port))
        if resultado == 0:
            print('El puerto {} esta abierto'.format(port))
        s.close()
except:
    print('\n salida...')
    sys.exit(0)