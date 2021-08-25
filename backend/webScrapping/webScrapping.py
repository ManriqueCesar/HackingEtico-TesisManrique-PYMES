#!/usr/bin/ebv python
#_*_ coding:utf8 _*_

# Cesar Manrique - Tesis 
#requests es una librería es dedicada especialmente al trabajo con peticiones HTTP
import requests
import dns.resolver
import argparse
import  urllib.request
import json
from bs4 import BeautifulSoup
from Wappalyzer import Wappalyzer, WebPage

parser = argparse.ArgumentParser(description="Detector de cabeceras- Manrique Cesar - Tesis II ")
parser.add_argument('-t','--target',help="Objetivo")
parser = parser.parse_args()
url = parser.target
def main ():
    if url:
        if (url.find("https") == -1):
            try:
                #obtener DNS
                a = dns.resolver.resolve(url,"A")
                for q in a:
                    print('DNS Obtenido:', q)
                #obtener localizacion
                urlLib = "https://ipinfo.io/"
                urlConsulta = urlLib + str(q) +"/json"
                v = urllib.request.urlopen(url)
                j = json.loads(v.read())
                for dato in j:
                    print(dato + " : " + j[dato])
                #obtener cabeceras
                newUrl = "https://" + url 
                urlRequest = requests.get(newUrl)
                cabeceras = dict(urlRequest.headers)
                for x in cabeceras:
                    print(x + " : " + cabeceras[x])
                #obtener wordpress Version
                cabecera = {'User-Agent':'Firefox'}
                peticion = requests.get(url=newUrl,headers= cabecera)
                soup = BeautifulSoup(peticion.text,'html.parser')
                for v in soup.find_all('meta'):
                    if v.get('name') == 'generator':
                        print('Version Wordpress: ' +v.get('content'))
                #obteniendo tecnologías con Wappalyzer
                wap = Wappalyzer.latest()
                web = WebPage.new_from_url(newUrl)
                tecnologias = wap.analyze(web)
                for t in tecnologias:
                    print("Tecnologia detectada: {}".format(t))
                #fuerza Bruta
                
            except:
                print("Ocurrio un error, intente nuevamente")
        else:
            # try:
                #obtener DNS
                urlSplitted = parser.target.split(sep="https://")
                a = dns.resolver.resolve(urlSplitted[1],"A")
                for q in a:
                    print('DNS Obtenido:', q)
                #obtener localizacion
                urlLib = "https://ipinfo.io/"
                urlConsulta = urlLib + str(q) +"/json"
                v = urllib.request.urlopen(urlConsulta)
                j = json.loads(v.read())
                for dato in j:
                    print(dato + " : " + j[dato])
                #obtener cabeceras
                url2 = requests.get(url=parser.target)
                cabeceras = dict(url2.headers)
                for x in cabeceras:
                    print(x + " : " + cabeceras[x])
                #obtener wordpress Version
                cabecera = {'User-Agent':'Firefox'}
                peticion = requests.get(url=url,headers= cabecera)
                soup = BeautifulSoup(peticion.text,'html.parser')
                for v in soup.find_all('meta'):
                    if v.get('name') == 'generator':
                        print('Version Wordpress: ' +v.get('content'))
                #obteniendo tecnologías con Wappalyzer
                wap = Wappalyzer.latest()
                web = WebPage.new_from_url(url)
                tecnologias = wap.analyze(web)
                for t in tecnologias:
                    print("Tecnologia detectada: {}".format(t))
            # except:
            #     print("Ocurrio un error, intente nuevamente")
    else:
        print("No hay objetivo") 

if __name__ =='__main__':
        main()