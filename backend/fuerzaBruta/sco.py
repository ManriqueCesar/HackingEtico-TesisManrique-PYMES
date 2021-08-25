#!/usr/bin/env python
#_*_ coding: utf8 _*_

import socket
from bs4 import BeautifulSoup

s = socket.socket()
try:
	s.connect(("acerosymolduras.com",21))
	banner = s.recv(1024)
	print(banner)
except:
	print("Ocurrio un error en la conexion")