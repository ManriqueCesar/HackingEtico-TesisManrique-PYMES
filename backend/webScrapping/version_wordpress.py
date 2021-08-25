#!/usr/bin/ebv python
#_*_ coding:utf8 _*_

# Cesar Manrique - Tesis 

import requests 
from bs4 import BeautifulSoup
import argparse


parser = argparse.ArgumentParser(description="Wordpress version - Manrique Cesar - Tesis II ")
def main():
    url = "https://educamp.utec.edu.pe/"
    cabecera = {'User-Agent':'Firefox'}
    peticion = requests.get(url=url,headers= cabecera)
    soup = BeautifulSoup(peticion.text,'html.parser')
    for v in soup.find_all('meta'):
        if v.get('name') == 'generator':
            print('Version de Wordpress encontrada: ' +v.get('content'))

if __name__ == '__main__':
    try: 
        main()
    except KeyboardInterrupt:
        print("Saliendo")
        exit()