#!/usr/bin/env python
#_*_ coding: utf8 _*_
#https://www.acerosymolduras.com/
#www.acerosymolduras.com/

import dns.resolver
import argparse

parser = argparse.ArgumentParser(description="DNS- Manrique Cesar - Tesis II ")
parser.add_argument('-t','--target',help="Objetivo")
parser = parser.parse_args()

def main():
	url = parser.target
	if (url.find("https") == -1): 
		print(url)
		try:
			a = dns.resolver.resolve(parser.target,"A")
			for q in a:
				print('El DNS Obtenido es:', q)
		except:
			print("No pude obtener la consulta")
	else:
		urlSplitted = parser.target.split(sep="https://")
		print(urlSplitted[1])
		try:
			a = dns.resolver.resolve(urlSplitted[1],"A")
			for q in a:
				print('El DNS Obtenido es:', q)
		except:
			print("No pude obtener la consulta")


	


if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()