import socket as so

hostname = so.gethostname()
ip = so.gethostbyname(hostname)

print('El numero ip de tu ordenador es: ' +  hostname)
print('Tu Dirrecion IP es: ' + ip)