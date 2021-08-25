#!/usr/bin/ebv python
#_*_ coding:utf8 _*_

# Cesar Manrique - Tesis 
#requests es una librería es dedicada especialmente al trabajo con peticiones HTTP
import requests
import argparse

parser = argparse.ArgumentParser(description="Detector de cabeceras- Manrique Cesar - Tesis II ")
parser.add_argument('-t','--target',help="Objetivo")
parser = parser.parse_args()
url = parser.target
def main ():
    if url:
        if (url.find("https") == -1):
            try:
                newUrl = "https://" + url 
                urlRequest = requests.get(newUrl)
                cabeceras = dict(urlRequest.headers)
                for x in cabeceras:
                    print(x + " : " + cabeceras[x])
            except:
                print("no se pudo conectar")
        else:
            try:
                url2 = requests.get(url=parser.target)
                #print(url.headers)
                cabeceras = dict(url2.headers)
                for x in cabeceras:
                    print(x + " : " + cabeceras[x])
            except:
                print("no se pudo conectar2")
    else:
        print("No hay objetivo") 

if __name__ =='__main__':
        main()