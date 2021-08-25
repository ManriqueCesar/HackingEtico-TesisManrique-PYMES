#!/usr/bin/env python
#_*_ coding: utf8 _*_

import mechanize
from bs4 import BeautifulSoup

nav = mechanize.Browser()
nav.set_handle_robots(False)
nav.set_handle_equiv(False)
nav.addheaders = [('User-Agent','Firefox')]
nav.open("http://testphp.vulnweb.com/login.php")
nav.select_form(nr=0)

nav['uname'] = 'test'
nav['pass'] = 'test'

nav.submit()

nav.open("http://testphp.vulnweb.com/guestbook.php")
for f in nav.forms():
    print(f)
nav.select_form(nr=0)

# nav['update'] = "'"

# nav.submit()
# soup = BeautifulSoup(nav.response().read(),'html5lib')
# print(soup.pre.string)