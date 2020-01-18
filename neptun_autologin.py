#!/usr/bin/env python3

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import getpass

usernameString = input('username: ')
passwordString = getpass.getpass('password: ') #password ide jön
neptun_szerverek = input('neptun szerverek száma: ')


for i in range(1,int(neptun_szerverek)+1):

      url = ("https://www-"+str(i)+ ".neptun.unideb.hu/hallgato/login.aspx")
      browser = webdriver.Chrome(ChromeDriverManager().install()) # webbrowser tipusa
      browser.get(url)

      username = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'user')))
      username.send_keys(usernameString)
      password = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'pwd')))
      password.send_keys(passwordString)
      button = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'btnSubmit')))
      button.click()

      print("Belépés a NEPTUN-ba...")
      # Belépés a tárgyak menübe
      targyak = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'mb1_Targyak')))
      targyak.click()
      print("Belépés a tárgyak menübe...")

      #Belépés a tárgyfelvétel menübe
      targyfelvet = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'mb1_Targyak_Targyfelvetel')))
      targyfelvet.click()
      print("Belépés a tárgyfelvétel menübe...")

      #Tárgyak listázására kattintás
      targyak_listazasa = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'upFilter_expandedsearchbutton')))
      targyak_listazasa.click()
      print("Tárgyak listázására kattintás...")






