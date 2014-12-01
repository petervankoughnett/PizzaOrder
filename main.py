#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2014 Peter VK <peter@peter-Inspiron-560>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  



	
from selenium import webdriver
	
email = 'pizzabuyer1@gmail.com'
password = 'Pizzapizza123'
	
driver = webdriver.Firefox()
url='http://order.papajohns.com/signin.html'
driver.get(url)

driver.switch_to.frame("signInFrame")
element_userName=driver.find_element_by_id("userName")
element_userName.send_keys(email)
element_password=driver.find_element_by_id("pwd")
element_password.send_keys(password)
driver.find_element_by_id('btnModalSignIn').click()

driver.get('http://order.papajohns.com/order.html')

	
	##path_to_chromedriver = '/usr/lib/chromium-browser/chromedriver' #change path as needed
	#browser = webdriver.Chrome(executable_path = path_to_chromedriver)####
