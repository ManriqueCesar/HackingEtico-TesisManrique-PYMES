#!/usr/bin/env python
#_*_ coding: utf8 _*_

import os
from bs4 import BeautifulSoup
import argparse

parser = argparse.ArgumentParser(description="Whois- Manrique Cesar - Tesis II ")

def get_whois(url):
	command = "whois " + url
	process = os.popen(command)
	results = str(process.read())
	return results

print(get_whois('google.com'))