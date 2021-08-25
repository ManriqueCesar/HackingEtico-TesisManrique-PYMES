#!/usr/bin/env python
#_*_ coding: utf8 _*_

from Wappalyzer import Wappalyzer, WebPage
import argparse


parser = argparse.ArgumentParser(description="Wappalyzer- Manrique Cesar - Tesis II ")

def main():
	wap = Wappalyzer.latest()
	web = WebPage.new_from_url('https://www.example.com')
	tecnologias = wap.analyze(web)
	for t in tecnologias:
		print("Tecnologia detectada: {}".format(t))

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print("Saliendo")
		exit()