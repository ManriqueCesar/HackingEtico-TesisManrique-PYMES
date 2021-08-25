#!/usr/bin/env python
#_*_ coding: utf8 _*_
#Actualizado a Python 3
# Tesis - Manrique Cesar


import  urllib.request
import json
import argparse

parser = argparse.ArgumentParser(description="Geolocation- Manrique Cesar - Tesis II ")

def main():
	url = "https://ipinfo.io/66.225.201.119/json"
	v = urllib.request.urlopen(url)
	j = json.loads(v.read())

	for dato in j:
		print(dato + " : " + j[dato])


if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()