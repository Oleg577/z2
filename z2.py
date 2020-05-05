from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
#import pandas as pd
#import numpy as np
import sqlite3
import csv
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import openpyxl


class Main(Frame):
    def __init__(self, root):
        super().__init__(root)
        self.in_m()

    def in_m(self):
        self.bt1 = Button(self, text="Автоматические выключатели\n модульного исполнения ", width=40, height=5, bg='#18e0ff',
                          command=self.ok1).grid(row=1, column=0)
        self.bt2 = Button(self, text="Трансформаторы тока ", width=40,height=5, bg='#18e0ff',
                          command=self.ok2).grid(row=2, column=0)
        self.bt3 =Button(self, text="Амперметры", width=40,height=5, command=self.ok3).grid(row=3, column=0)
        self.bt4 = Button(self, text="Вольтметры", width=40, height=5, command=self.ok4).grid(row=4, column=0)
        self.bt5 = Button(self, text="Счетчики\nМногофункциональные измерители", width=40, height=5, command=self.ok5).grid(row=5, column=0)
        self.bt6 = Button(self, text="Автоматические выключатели\nзащиты двигателя\nтипа GV", width=40, height=5, bg='#18e0ff', command=self.ok6).grid(row=1, column=1)
        self.bt7 = Button(self, text="Контакторы", width=40, height=5, bg='#18e0ff', command=self.ok7).grid(row=2, column=1)
        self.bt8 = Button(self, text="Тепловые реле", width=40, height=5, command=self.ok8).grid(row=3, column=1)
        self.bt9 = Button(self, text="Клеммники", width=40, height=5, bg='#18e0ff', command=self.ok9).grid(row=4, column=1)
        self.bt10 = Button(self, text="Корпуса типа ЩРН\n (Металлические)", width=40, height=5, bg='#18e0ff', command=self.ok10).grid(row=5, column=1)
        self.bt11 = Button(self, text="Автоматические выключателти\n в литом корпусе", width=40, height=5, bg='#18e0ff', command=self.ok11).grid(row=1, column=3)
        self.bt12 = Button(self, text="Хорошо известная всем хрень", width=40, height=5).grid(row=2, column=3)
        self.bt13 = Button(self, text="Дифференцивльный автоматические\nвыключатели", width=40, height=5,  bg='#18e0ff', command=self.ok13).grid(row=3, column=3)
        self.bt14 = Button(self, text="Устройства дифференциальной защиты\nУЗО", width=40, height=5, bg='#18e0ff', command=self.ok14).grid(row=4, column=3)
        self.bt15 = Button(self, text="Корпуса типа ЩМП", width=40, height=5, command=self.ok15).grid(row=5, column=3)

    def ok1(self):
        Podbor1()
    def ok2(self):
        Podbor2()
    def ok3(self):
        Podbor3()
    def ok4(self):
        Podbor4()
    def ok5(self):
        Podbor5()
    def ok6(self):
        Podbor6()
    def ok7(self):
        Podbor7()
    def ok8(self):
        Podbor8()
    def ok9(self):
        Podbor9()
    def ok10(self):
        Podbor10()
    def ok11(self):
        Podbor11()
    def ok13(self):
        Podbor13()
    def ok14(self):
        Podbor14()
    def ok15(self):
        Podbor15()



    def ЭК(self):
        Запрос_в_магазин()



class Запрос_в_магазин():
    def __init__(self):
        driver = webdriver.Chrome()
        driver.get(
            "https://www.smart-shop.pro/cgi-bin/display2.exe/main.mml?IsThruLetter=yes&wintoopen=registration.mml")
        time.sleep(1)
        driver.switch_to.frame('loginingo')
        elem = driver.find_element_by_xpath("//*[@id='cust']")
        elem.clear()
        elem.send_keys('059398')
        elem1 = driver.find_element_by_xpath("//*[@id='custpersonalcode']")
        elem1.clear()
        elem1.send_keys('EU396906')
        time.sleep(1)
        # driver.switch_to.frame('loginingo')
        driver.find_element_by_xpath('/html/body/table/tbody/tr/td[2]/table/tbody/tr/td/form/div[1]/a').click()
        time.sleep(3)
        driver.switch_to.frame('catalog')
        driver.find_element_by_xpath('//*[@id="m_searchetimTest"]').click()
        #time.sleep(2)
        #driver.get("https://www.smart-shop.pro/cgi-bin/display2.exe/main.mml")
        #driver.switch_to.frame('rightside')
        # elem2=driver.find_element_by_xpath('//*[@id="rightside"]')
        #time.sleep(2)
        # elem2 = driver.find_element_by_xpath('//*[@id="search_form"]/input[4]')
        #wb = openpyxl.load_workbook('Запрос в магазин.xlsx')
        #sheet = wb.get_sheet_by_name("Лист1")
        # elem2 = driver.find_element_by_xpath('//*[@id="search_form"]/input[4]')




class Podbor1(Toplevel):
    def __init__(self):
        super().__init__(root)
        self.ok11()


        self.lb1_1 = Label(self, text="Укажите дополнительные параметры ").grid(row=0, column=0, columnspan=5, sticky=S)
        self.lb1_11 = Label(self, text="Количество полюсов ").grid(row=1, column=0)
        self.c1_1 = ttk.Combobox(self, value=('1', '2', '3', '4'))
        self.c1_1.grid(row=2, column=0, pady=10)
        self.lb1_12 = Label(self, text="Кривая отключения ").grid(row=1, column=1)
        self.c1_2 = ttk.Combobox(self, value=('B', 'C', 'D', 'Z', 'K', 'L'))
        self.c1_2.grid(row=2, column=1)
        self.lb1_13 = Label(self, text="Номинальный ток, А").grid(row=1, column=2)
        self.c1_3 = ttk.Combobox(self, value=('0,5','1','1,6','2','3','4','6','8' ,'10','12,5', '13','16','20','25','32','40','50','63','80','100','125'))
        self.c1_3.grid(row=2, column=2)
        self.lb1_14 = Label(self, text="Тип тока (AC/DC)").grid(row=1, column=3)
        self.c1_4 = ttk.Combobox(self, value=('AC','DC'))
        self.c1_4.grid(row=2, column=3)
        self.lb1_15 = Label(self, text="Откл. способность, кА").grid(row=1, column=4)
        self.c1_5 = ttk.Combobox(self, value=('4,5', '6', '10', '15', '25'))
        self.c1_5.grid(row=2, column=4)
        self.lb1_17 = Button(self, text="Фильтр по производителю", bg='#BEF781', width=22, command=self.db1_7).grid(row=1, column=6)
        self.c1_7 = ttk.Combobox(self, value=('SHN', 'LS', 'KUR', 'IEK', 'EKF', 'ELVERT', 'TDM', 'OEZ', 'CHINT'))
        self.c1_7.grid(row=2, column=6)


        self.b1_11 = Button(self, text="Показать из базы", width=22, bg='#BEF781', command=self.db1_1).grid(row=3, column=6)
        self.b1_12 = Button(self, text="Удалить выбранное", width=22,command=self.db1_2).grid(row=4, column=6)
        self.b1_13 = Button(self, text="Сохранить", width=22,command=self.db1_3).grid(row=5, column=6)
        self.b1_14 = Button(self,text="Запрос в ЭК", width=22, command=self.ЭК).grid(row=6, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=7,column=6)
        self.rez = ttk.Button(self, width=22).grid(row=8, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=9, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=10, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=11, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=12, column=6)

        self.tree1 = ttk.Treeview(self, columns=('1v1', '1v2', '1v3', '1v4', '1v5', '1v6'), height=15,
                                  show='headings')
        self.tree1.column('1v1', width=1, anchor=CENTER)
        self.tree1.column('1v2', width=180)
        self.tree1.column('1v3', width=574)
        self.tree1.column('1v4', width=45, anchor=CENTER)
        self.tree1.column('1v5', width=75, anchor=CENTER)
        self.tree1.column('1v6', width=95, anchor=CENTER)
        self.tree1.grid(row=3, columnspan=5, rowspan=10)

        self.tree1.heading('1v1', text='Кл.')
        self.tree1.heading('1v2', text='Артикул')
        self.tree1.heading('1v3', text='Наименование материала')
        self.tree1.heading('1v4', text='Ед.\nизм')
        self.tree1.heading('1v5', text='Кол.')
        self.tree1.heading('1v6', text='Цена')

        scr1 = ttk.Scrollbar(self, orient='vertical', command=self.tree1.yview)
        scr1.grid(row=3, column=5, sticky=N + S, rowspan=10)
        self.tree1.configure(yscrollcommand=scr1.set)

        self.b1_21 = Button(self, text="Показать склад", width=22, bg='#FAAC58', command=self.db1_4).grid(row=13, column=6)
        self.b1_22 = Button(self, text="Удалить выбранное", width=22, command=self.db1_5).grid(row=14, column=6)
        self.b1_23 =Button(self, text="Сохранить", width=22,command=self.db1_9).grid(row=15, column=6) #ttk.Button(self, width=22).grid(row=15, column=6)
        self.b1_24 =ttk.Button(self, width=22).grid(row=16, column=6) #Button(self,text="Запрос в ЭК", width=22).grid(row=16, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=17, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=18, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=19, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=20, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=21, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=22, column=6)


        self.tree2 = ttk.Treeview(self, columns=('2v1', '2v2', '2v3', '2v4', '2v5','2v6'), height=15,
                                  show='headings')
        self.tree2.column('2v1', width=1, anchor=CENTER)
        self.tree2.column('2v2', width=180)
        self.tree2.column('2v3', width=574)
        self.tree2.column('2v4', width=45, anchor=CENTER)
        self.tree2.column('2v5', width=75, anchor=CENTER)
        self.tree2.column('2v6', width=95, anchor=CENTER)
        self.tree2.grid(row=13, columnspan=5, rowspan=10)

        self.tree2.heading('2v1', text='Кл.')
        self.tree2.heading('2v2', text='Артикул')
        self.tree2.heading('2v3', text='Наименование материала')
        self.tree2.heading('2v4', text='Ед.\nизм')
        self.tree2.heading('2v5', text='Кол.\nсклад')
        self.tree2.heading('2v6', text='Цена')

        scr2 = ttk.Scrollbar(self, orient='vertical', command=self.tree1.yview)
        scr2.grid(row=13, column=5, sticky=N + S, rowspan=10)
        self.tree2.configure(yscrollcommand=scr2.set)

    def db1_1(self):
            cs1 = self.c1_1.get()
            cs2 = self.c1_2.get()
            cs3 = self.c1_3.get()
            cs4 = self.c1_4.get()
            cs5 = self.c1_5.get()
            cs6 = cs1 + cs2 + cs3 + cs4 + cs5
            global row,sq11

            if int(cs1) > 0:

                self.conn = sqlite3.connect('s28b')
                self.cursor = self.conn.cursor()
                self.cursor.execute("SELECT * FROM МА_Б WHERE Ключ =:ID ORDER BY Цена", {"ID": cs6})
                sq11 = self.cursor.fetchall()
                for row in sq11:
                    self.tree1.insert("", END, values=row)


    def db1_2(self):
        item = self.tree1.selection()[0]
        self.tree1.delete(item)


    def db1_3(self):
        names = ["Ключ", "Артикул", "Наименование", "Ед.изм", " ", "Цена"]
        with open("Ответ Базы.csv", "w", newline='') as f:
             writer = csv.writer(f, delimiter=';')
             writer.writerow(names)

             for product in sq11:
                writer.writerow(product)

    def db1_4(self):
        global sq12
        cs1 = self.c1_1.get()
        cs2 = self.c1_2.get()
        cs3 = self.c1_3.get()
        cs4 = self.c1_4.get()
        cs5 = self.c1_5.get()
        cs6 = cs1 + cs2 + cs3 + cs4 + cs5

        if int(cs1) > 0:
            self.conn = sqlite3.connect('s28b')
            self.cursor = self.conn.cursor()
            self.cursor.execute("SELECT * FROM МА_С WHERE Ключ =:ID ORDER BY Цена", {"ID": cs6})
            sq12 = self.cursor.fetchall()
            for row in sq12:
                self.tree2.insert("", END, values=row)


    def db1_5(self):
        item = self.tree2.selection()[0]
        self.tree2.delete(item)

    def db1_7(self):
        cs1 = self.c1_1.get()
        cs2 = self.c1_2.get()
        cs3 = self.c1_3.get()
        cs4 = self.c1_4.get()
        cs5 = self.c1_5.get()
        cs6 = cs1 + cs2 + cs3 + cs4 + cs5
        cs7 = self.c1_7.get()

         #self.cursor.execute("SELECT * FROM МА_Б WHERE Ключ =:ID AND  Наименование_материала LIKE '%SHN%'  ",{"ID": cs6})  and cs7 == "SHN"

        if int(cs1) > 0:

            self.conn = sqlite3.connect('s28b')
            self.cursor = self.conn.cursor()
            self.cursor.execute("SELECT * FROM МА_Б WHERE Ключ =? AND  Артикул LIKE ('%' || ? || '%')",
                                (cs6,cs7))
            sq11 = self.cursor.fetchall()
            for row in sq11:
                self.tree1.insert("", END, values=row)
            print(sq11)

    def db1_9(self):
        names = ["Ключ", "Артикул", "Наименование", "Ед.изм.", "Доступно ", "Цена"]
        with open("Ответ Склада.csv", "w", newline='') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow(names)

            for product in sq12:
                writer.writerow(product)

    def ЭК(self):
        Запрос_в_магазин()

    def ok11(self):
        self.title('Автоматические выключатели\n модульного исполнения ')
        self.geometry('1170x750+300+80')
        self.resizable(False, False)

class Podbor2(Toplevel):
        def __init__(self):
            super().__init__(root)
            self.ok21()

            self.lb2_1 = Label(self, text="Укажите дополнительные параметры ")
            self.lb2_1.grid(row=0, column=0, columnspan=5, sticky=S)

            self.lb2_11 = Label(self, text="Ток первичной обмотки, А").grid(row=1, column=0)
            self.c2_1 = ttk.Combobox(self, value=('100', '150', '200', '250', '300', '400', '500', '600', '750', '800', '1000','1500'
                                                  , '2000', '2500', '3000', '4000', '5000', '6000'))
            self.c2_1.grid(row=2, column=0, pady=10)
            self.lb2_12 = Label(self, text="Ток вторичной обмотки, А ").grid(row=1, column=1)
            self.c2_2 = ttk.Combobox(self, value=('1', '5'))
            self.c2_2.grid(row=2, column=1)
            self.lb2_13 = Label(self, text="Класс точности").grid(row=1, column=2)
            self.c2_3 = ttk.Combobox(self, value=('0,1','0,2', '0,2S', '0,5', '0,5S', '1'))
            self.c2_3.grid(row=2, column=2)
            self.lb2_14 = Label(self).grid(row=1, column=3)
            self.c2_4 = ttk.Button(self, width=20).grid(row=2, column=3)
            self.lb2_15 = Label(self).grid(row=1, column=4)
            self.c2_5 = ttk.Button(self, width=20).grid(row=2, column=4)
            self.lb2_16 = Button(self, text="Фильтр по производителю", width=22 , bg='#BEF781', command=self.db2_7).grid(row=1, column=6)
            self.c2_7 = ttk.Combobox(self, value=('SHN', 'ETM', 'KUR', 'IEK', 'EKF', 'ELVERT', 'TDM'))
            self.c2_7.grid(row=2, column=6)

            self.b2_11 = Button(self, text="Показать из базы", width=22, bg='#BEF781', command=self.db2_1).grid(row=3,
                                                                                                                column=6)
            self.b2_12 = Button(self, text="Удалить выбранное", width=22, command=self.db2_2).grid(row=4, column=6)
            self.b2_13 = Button(self, text="Сохранить", width=22, command=self.db2_3).grid(row=5, column=6)
            self.b2_14 = Button(self, text="Запрос в ЭК", width=22, command=self.ЭК).grid(row=6, column=6)
            self.rez = ttk.Button(self, width=22).grid(row=7, column=6)
            self.rez = ttk.Button(self, width=22).grid(row=8, column=6)
            self.rez = ttk.Button(self, width=22).grid(row=9, column=6)
            self.rez = ttk.Button(self, width=22).grid(row=10, column=6)
            self.rez = ttk.Button(self, width=22).grid(row=11, column=6)
            self.rez = ttk.Button(self, width=22).grid(row=12, column=6)

            self.tree1 = ttk.Treeview(self, columns=('1v1', '1v2', '1v3', '1v4', '1v5', '1v6'), height=15,
                                      show='headings')
            self.tree1.column('1v1', width=1, anchor=CENTER)
            self.tree1.column('1v2', width=180)
            self.tree1.column('1v3', width=574)
            self.tree1.column('1v4', width=45, anchor=CENTER)
            self.tree1.column('1v5', width=75, anchor=CENTER)
            self.tree1.column('1v6', width=95, anchor=CENTER)
            self.tree1.grid(row=3, columnspan=5, rowspan=10)

            self.tree1.heading('1v1', text='Кл.')
            self.tree1.heading('1v2', text='Артикул')
            self.tree1.heading('1v3', text='Наименование материала')
            self.tree1.heading('1v4', text='Ед.\nизм')
            self.tree1.heading('1v5', text='Кол.')
            self.tree1.heading('1v6', text='Цена')

            scr1 = ttk.Scrollbar(self, orient='vertical', command=self.tree1.yview)
            scr1.grid(row=3, column=5, sticky=N + S, rowspan=10)
            self.tree1.configure(yscrollcommand=scr1.set)

            self.b2_21 = Button(self, text="Показать склад", width=22, bg='#FAAC58', command=self.db2_4).grid(row=13,
                                                                                                              column=6)
            self.b2_22 = Button(self, text="Удалить выбранное", width=22, command=self.db2_5).grid(row=14, column=6)
            self.b2_23 = Button(self, text="Сохранить", width=22, command=self.db2_9).grid(row=15, column=6)
            self.b2_24 = ttk.Button(self, width=22).grid(row=16, column=6)#Button(self, text="Запрос в ЭК", width=22, command=self.ЭК).grid(row=16, column=6)
            self.rez = ttk.Button(self, width=22).grid(row=17, column=6)
            self.rez = ttk.Button(self, width=22).grid(row=18, column=6)
            self.rez = ttk.Button(self, width=22).grid(row=19, column=6)
            self.rez = ttk.Button(self, width=22).grid(row=20, column=6)
            self.rez = ttk.Button(self, width=22).grid(row=21, column=6)
            self.rez = ttk.Button(self, width=22).grid(row=22, column=6)

            self.tree2 = ttk.Treeview(self, columns=('2v1', '2v2', '2v3', '2v4', '2v5', '2v6'), height=15,
                                      show='headings')
            self.tree2.column('2v1', width=1, anchor=CENTER)
            self.tree2.column('2v2', width=180)
            self.tree2.column('2v3', width=574)
            self.tree2.column('2v4', width=45, anchor=CENTER)
            self.tree2.column('2v5', width=75, anchor=CENTER)
            self.tree2.column('2v6', width=95, anchor=CENTER)
            self.tree2.grid(row=13, columnspan=5, rowspan=10)

            self.tree2.heading('2v1', text='Кл.')
            self.tree2.heading('2v2', text='Артикул')
            self.tree2.heading('2v3', text='Наименование материала')
            self.tree2.heading('2v4', text='Ед.\nизм')
            self.tree2.heading('2v5', text='Кол.\nсклад')
            self.tree2.heading('2v6', text='Цена')

            scr2 = ttk.Scrollbar(self, orient='vertical', command=self.tree1.yview)
            scr2.grid(row=13, column=5, sticky=N + S, rowspan=10)
            self.tree2.configure(yscrollcommand=scr2.set)

        def db2_1(self): # ПОКАЗТЬ БАЗУ. ОКНО 1
            cs1 = self.c2_1.get()
            cs2 = self.c2_2.get()
            cs3 = self.c2_3.get()
            cs6 = cs1 + cs2 + cs3
            global sq21

            if int(cs1) > 0:
                self.conn = sqlite3.connect('s28b')
                self.cursor = self.conn.cursor()
                self.cursor.execute("SELECT * FROM МА_Б WHERE Ключ =:ID ORDER BY Цена", {"ID": cs6})
                sq21 = self.cursor.fetchall()
                for row in sq21:
                    self.tree1.insert("", END, values=row)

        def db2_2(self): #УДАЛИТЬ ВЫБРАННЫЙ ЭЛЕМЕНТ ОКНО 1
            item = self.tree1.selection()[0]
            self.tree1.delete(item)

        def db2_3(self): #СОХРАНИТЬ СПЕЦИФИКАЦИЮ ОКНО 1
            names = ["Ключ", "Артикул", "Наименование", "Ед.изм.", " ", "Цена"]
            with open("Ответ Базы.csv", "w", newline='') as f:
                writer = csv.writer(f, delimiter=';')
                writer.writerow(names)

                for product in sq21:
                    writer.writerow(product)


        def db2_4(self): # ПОКАЗТЬ СКЛАД. ОКНО 2
            global sq22

            cs1 = self.c2_1.get()
            cs2 = self.c2_2.get()
            cs3 = self.c2_3.get()
            cs6 = cs1 + cs2 + cs3

            if int(cs1) > 0:
                self.conn = sqlite3.connect('s28b')
                self.cursor = self.conn.cursor()
                self.cursor.execute("SELECT * FROM МА_С WHERE Ключ =:ID ORDER BY Цена", {"ID":cs6})

                sq22 = self.cursor.fetchall()
                for row in sq22:
                    self.tree2.insert("", END, values=row)


        def db2_5(self):  #УДАЛИТЬ ВЫБРАННЫЙ ЭЛЕМЕНТ ОКНО 2
            item = self.tree2.selection()[0]
            self.tree2.delete(item)

        def db2_7(self): #ФИЛЬТР ПО ПРОИЗВОДИТЕЛЮ. ОКНО 1
            cs1 = self.c2_1.get()
            cs2 = self.c2_2.get()
            cs3 = self.c2_3.get()
            cs6 = cs1 + cs2 + cs3
            cs7 = self.c2_7.get()

            if int(cs1) > 0:

                self.conn = sqlite3.connect('s28b')
                self.cursor = self.conn.cursor()
                self.cursor.execute("SELECT * FROM МА_Б WHERE Ключ =? AND  Артикул LIKE ('%' || ? || '%')",
                                    (cs6, cs7))
                sq21 = self.cursor.fetchall()
                for row in sq21:
                    self.tree1.insert("", END, values=row)


        def db2_9(self): #СОХРАНИТЬ СКЛАД
            names = ["Ключ", "Артикул", "Наименование", "Ед.изм.", "Доступно ", "Цена"]
            with open("Ответ Склада.csv", "w", newline='') as f:
                writer = csv.writer(f, delimiter=';')
                writer.writerow(names)

                for product in sq22:
                    writer.writerow(product)

        def ЭК(self):
            Запрос_в_магазин()


        def ok21(self):
            self.title('Трансформаторы тока')
            self.geometry('1170x750+300+80')
            self.resizable(False, False)

class Podbor6(Toplevel):
    def __init__(self):
        super().__init__(root)
        self.ok61()

        self.lb6_1 = Label(self, text="Укажите дополнительные параметры ").grid(row=0, column=0, columnspan=5, sticky=S)
        self.lb6_11 = Label(self, text="Номинальный ток, А").grid(row=1, column=0)
        self.c6_1 = ttk.Combobox(self, value=('0,16', '0,25','0,4', '0,6', '1', '1,6', '2,5', '4','6','8', '10', '12,5', '16',
                                              '18', '20', '25', '32', '40', '50', '63', '80', '100', '125', '160'))
        self.c6_1.grid(row=2, column=0, pady=10)
        self.lb6_12 = Label(self, text="Наличие теплового\n расцепителя").grid(row=1, column=1)
        self.c6_2 = ttk.Combobox(self, value=('Да', 'Нет'))
        self.c6_2.grid(row=2, column=1)
        self.lb6_13 = Label(self, text="Совместимость с выносной\n рукояткой").grid(row=1, column=2)
        self.c6_3 = ttk.Combobox (self,  value=('Да', 'Нет'))
        self.c6_3.grid(row=2, column=2)
        self.lb6_14 = Label(self).grid(row=1, column=3)
        self.c6_4 = ttk.Button(self, width=20).grid(row=2, column=3)
        self.lb6_15 = Label(self).grid(row=1, column=4)
        self.c6_5 = ttk.Button(self, width=20).grid(row=2, column=4)
        self.lb6_17 = Button(self, text="Фильтр по производителю", bg='#BEF781', width=22, command=self.db6_7).grid(row=1, column=6)
        self.c6_7 = ttk.Combobox(self, value=('SHN', 'LS', 'KUR', 'IEK', 'EKF', 'ELVERT', 'TDM', 'OEZ', 'CHINT'))
        self.c6_7.grid(row=2, column=6)

        self.b6_11 = Button(self, text="Показать из базы", width=22, bg='#BEF781', command=self.db6_1).grid(row=3,
                                                                                                            column=6)
        self.b6_12 = Button(self, text="Удалить выбранное", width=22, command=self.db6_2).grid(row=4, column=6)
        self.b6_13 = Button(self, text="Сохранить", width=22, command=self.db6_3).grid(row=5, column=6)
        self.b6_14 = Button(self, text="Запрос в ЭК", width=22, command=self.ЭК).grid(row=6, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=7, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=8, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=9, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=10, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=11, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=12, column=6)

        self.tree1 = ttk.Treeview(self, columns=('1v1', '1v2', '1v3', '1v4', '1v5', '1v6'), height=15,
                                  show='headings')
        self.tree1.column('1v1', width=1, anchor=CENTER)
        self.tree1.column('1v2', width=180)
        self.tree1.column('1v3', width=574)
        self.tree1.column('1v4', width=45, anchor=CENTER)
        self.tree1.column('1v5', width=75, anchor=CENTER)
        self.tree1.column('1v6', width=95, anchor=CENTER)
        self.tree1.grid(row=3, columnspan=5, rowspan=10)

        self.tree1.heading('1v1', text='Кл.')
        self.tree1.heading('1v2', text='Артикул')
        self.tree1.heading('1v3', text='Наименование материала')
        self.tree1.heading('1v4', text='Ед.\nизм')
        self.tree1.heading('1v5', text='Кол.')
        self.tree1.heading('1v6', text='Цена')

        scr1 = ttk.Scrollbar(self, orient='vertical', command=self.tree1.yview)
        scr1.grid(row=3, column=5, sticky=N + S, rowspan=10)
        self.tree1.configure(yscrollcommand=scr1.set)

        self.b6_21 = Button(self, text="Показать склад", width=22, bg='#FAAC58', command=self.db6_4).grid(row=13,
                                                                                                          column=6)
        self.b6_22 = Button(self, text="Удалить выбранное", width=22, command=self.db6_5).grid(row=14, column=6)
        self.b6_23 = Button(self, text="Сохранить", width=22, command=self.db6_9).grid(row=15, column=6)
        self.b6_24 = ttk.Button(self, width=22).grid(row=16,
                                                     column=6)  # Button(self, text="Запрос в ЭК", width=22, command=self.ЭК).grid(row=16, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=17, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=18, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=19, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=20, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=21, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=22, column=6)

        self.tree2 = ttk.Treeview(self, columns=('2v1', '2v2', '2v3', '2v4', '2v5', '2v6'), height=15,
                                  show='headings')
        self.tree2.column('2v1', width=1, anchor=CENTER)
        self.tree2.column('2v2', width=180)
        self.tree2.column('2v3', width=574)
        self.tree2.column('2v4', width=45, anchor=CENTER)
        self.tree2.column('2v5', width=75, anchor=CENTER)
        self.tree2.column('2v6', width=95, anchor=CENTER)
        self.tree2.grid(row=13, columnspan=5, rowspan=10)

        self.tree2.heading('2v1', text='Кл.')
        self.tree2.heading('2v2', text='Артикул')
        self.tree2.heading('2v3', text='Наименование материала')
        self.tree2.heading('2v4', text='Ед.\nизм')
        self.tree2.heading('2v5', text='Кол.\nсклад')
        self.tree2.heading('2v6', text='Цена')

        scr2 = ttk.Scrollbar(self, orient='vertical', command=self.tree1.yview)
        scr2.grid(row=13, column=5, sticky=N + S, rowspan=10)
        self.tree2.configure(yscrollcommand=scr2.set)


        #self.lb6_18 = Label(self,
                            #text="Примечание. Автоматические выключатели производства ИЕК, ЕКФ,"
                                 #" а также бюджетный Schneider не имеют возможности установки выносных поворотных рукояток")
        #self.lb6_18.grid(row=14, column=0, columnspan=6, pady=5)

    def db6_1(self): # ПОКАЗТЬ БАЗУ. ОКНО 1
            cs1 = self.c6_1.get()
            cs21 = self.c6_2.get()
            if cs21 == "Да":
                cs2 = "D"
            elif cs21 == "Нет":
                cs2 = "N"
            cs31 = self.c6_3.get()
            if cs31 == "Да":
                cs3 = "D"
            elif cs31 == "Нет":
                cs3 = "N"
            #cs4 = self.c6_4.get()
            #cs5 = self.c6_5.get()
            cs6 = cs1 + cs2 + cs3 #+ cs4 + cs5
            global row,sq61

            #if int(cs1) != 0:

            self.conn = sqlite3.connect('s28b')
            self.cursor = self.conn.cursor()
            self.cursor.execute("SELECT * FROM МА_Б WHERE Ключ =:ID ORDER BY Цена  ", {"ID": cs6})
            sq61 = self.cursor.fetchall()
            for row in sq61:
                self.tree1.insert("", END, values=row)


    def db6_2(self): #УДАЛИТЬ ВЫБРАННЫЙ ЭЛЕМЕНТ ОКНО 1
        item = self.tree1.selection()[0]
        self.tree1.delete(item)

    def db6_3(self):  # СОХРАНИТЬ СПЕЦИФИКАЦИЮ ОКНО 1
        names = ["Ключ", "Артикул", "Наименование", "Ед.изм.", " ", "Цена"]
        with open("Ответ Базы.csv", "w", newline='') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow(names)

            for product in sq61:
                writer.writerow(product)

    def db6_4(self):# ПОКАЗТЬ СКЛАД. ОКНО 2
        global sq62

        cs1 = self.c6_1.get()
        cs21 = self.c6_2.get()
        if cs21 == "Да":
            cs2 = "D"
        elif cs21 == "Нет":
            cs2 = "N"
        cs31 = self.c6_3.get()
        if cs31 == "Да":
            cs3 = "D"
        elif cs31 == "Нет":
            cs3 = "N"
        cs6 = cs1 + cs2 + cs3

        self.conn = sqlite3.connect('s28b')
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT * FROM МА_С WHERE Ключ =:ID ORDER BY Цена", {"ID": cs6})
        sq62 = self.cursor.fetchall()
        for row in sq62:
            self.tree2.insert("", END, values=row)


    def db6_5(self): #УДАЛИТЬ ВЫБРАННЫЙ ЭЛЕМЕНТ ОКНО 2
        item = self.tree2.selection()[0]
        self.tree2.delete(item)

    def db6_7(self): #ФИЛЬТР ПО ПРОИЗВОДИТЕЛЮ. ОКНО 1
        cs1 = self.c6_1.get()
        cs21 = self.c6_2.get()
        if cs21 == "Да":
            cs2 = "D"
        elif cs21 == "Нет":
            cs2 = "N"
        cs31 = self.c6_3.get()
        if cs31 == "Да":
            cs3 = "D"
        elif cs31 == "Нет":
            cs3 = "N"
        # cs4 = self.c6_4.get()
        # cs5 = self.c6_5.get()
        cs6 = cs1 + cs2 + cs3  # + cs4 + cs5

        cs7 = self.c6_7.get()

        if int(cs1) > 0:

            self.conn = sqlite3.connect('s28b')
            self.cursor = self.conn.cursor()
            self.cursor.execute("SELECT * FROM МА_Б WHERE Ключ =? AND  Артикул LIKE ('%' || ? || '%')",
                                (cs6, cs7))
            sq61 = self.cursor.fetchall()
            for row in sq61:
                self.tree1.insert("", END, values=row)

    def db6_9(self):  # СОХРАНИТЬ СКЛАД
        names = ["Ключ", "Артикул", "Наименование", "Ед.изм.", "Доступно ", "Цена"]
        with open("Ответ Склада.csv", "w", newline='') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow(names)

            for product in sq62:
                writer.writerow(product)

    def ЭК(self):
        Запрос_в_магазин()

    def ok61(self):
        self.title('Автоматические выключатели\n модульного исполнения ')
        self.geometry('1170x800+300+80')
        self.resizable(False, False)

class Podbor7(Toplevel):
    def __init__(self):
        super().__init__(root)
        self.ok71()

        self.lb7_1 = Label(self, text="Укажите дополнительные параметры ")
        self.lb7_1.grid(row=0, column=0, columnspan=5, sticky=S)

        self.lb7_11 = Label(self, text="Количество полюсов ")
        self.lb7_11.grid(row=1, column=0)
        self.c7_1 = ttk.Combobox(self, value=('3', '4', '2', '1'))
        self.c7_1.grid(row=2, column=0, pady=10)

        self.lb7_12 = Label(self, text="Номинальный ток, А ")
        self.lb7_12.grid(row=1, column=1)
        self.c7_2 = ttk.Combobox(self, value=('6', '9', '10', '12', '18', '22','25', '32', '38', '40', '65', '80', '95', '115', '120','150', '160','185', '200', '250','265','300', '320','400', '630'))
        self.c7_2.grid(row=2, column=1)

        self.lb7_13 = Label(self, text="Тип тока (AC/DC)")
        self.lb7_13.grid(row=1, column=2)
        self.c7_3 = ttk.Combobox(self, value=(
        'AC', 'DC'))
        self.c7_3.grid(row=2, column=2)

        self.lb7_14 = Label(self, text="Напряжение катушки, В")
        self.lb7_14.grid(row=1, column=3)
        self.c7_4 = ttk.Combobox(self, value=('220', '24', '380', '110', '48', '12'))
        self.c7_4.grid(row=2, column=3)

        self.lb7_15 = Label(self)
        self.lb7_15.grid(row=1, column=4)
        self.c7_5 = ttk.Button(self, width=20)
        self.c7_5.grid(row=2, column=4)



        self.lb7_16 = Button(self, text="Фильтр по производителю", width=22, bg='#BEF781', command=self.db7_7)
        self.lb7_16.grid(row=1, column=6)
        self.c7_7 = ttk.Combobox(self, value=('SHN','LS', 'ETM', 'KUR', 'IEK', 'EKF', 'ELVERT', 'TDM'))
        self.c7_7.grid(row=2, column=6)

        self.b7_11 = Button(self, text="Показать из базы", width=22, bg='#BEF781', command=self.db7_1).grid(row=3,
                                                                                                            column=6)
        self.b7_12 = Button(self, text="Удалить выбранное", width=22, command=self.db7_2).grid(row=4, column=6)
        self.b7_13 = Button(self, text="Сохранить", width=22, command=self.db7_3).grid(row=5, column=6)
        self.b7_14 = Button(self, text="Запрос в ЭК", width=22, command=self.ЭК).grid(row=6, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=7, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=8, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=9, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=10, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=11, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=12, column=6)

        self.tree1 = ttk.Treeview(self, columns=('1v1', '1v2', '1v3', '1v4', '1v5', '1v6'), height=15,
                                  show='headings')
        self.tree1.column('1v1', width=1, anchor=CENTER)
        self.tree1.column('1v2', width=180)
        self.tree1.column('1v3', width=574)
        self.tree1.column('1v4', width=45, anchor=CENTER)
        self.tree1.column('1v5', width=75, anchor=CENTER)
        self.tree1.column('1v6', width=95, anchor=CENTER)
        self.tree1.grid(row=3, columnspan=5, rowspan=10)

        self.tree1.heading('1v1', text='Кл.')
        self.tree1.heading('1v2', text='Артикул')
        self.tree1.heading('1v3', text='Наименование материала')
        self.tree1.heading('1v4', text='Ед.\nизм')
        self.tree1.heading('1v5', text='Кол.')
        self.tree1.heading('1v6', text='Цена')

        scr1 = ttk.Scrollbar(self, orient='vertical', command=self.tree1.yview)
        scr1.grid(row=3, column=5, sticky=N + S, rowspan=10)
        self.tree1.configure(yscrollcommand=scr1.set)

        self.b7_21 = Button(self, text="Показать склад", width=22, bg='#FAAC58', command=self.db7_4).grid(row=13,
                                                                                                          column=6)
        self.b7_22 = Button(self, text="Удалить выбранное", width=22, command=self.db7_5).grid(row=14, column=6)
        self.b7_23 = Button(self, text="Сохранить", width=22, command=self.db7_9).grid(row=15, column=6)
        self.b7_24 = ttk.Button(self, width=22).grid(row=16,
                                                     column=6)  # Button(self, text="Запрос в ЭК", width=22, command=self.ЭК).grid(row=16, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=17, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=18, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=19, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=20, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=21, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=22, column=6)

        self.tree2 = ttk.Treeview(self, columns=('2v1', '2v2', '2v3', '2v4', '2v5', '2v6'), height=15,
                                  show='headings')
        self.tree2.column('2v1', width=1, anchor=CENTER)
        self.tree2.column('2v2', width=180)
        self.tree2.column('2v3', width=574)
        self.tree2.column('2v4', width=45, anchor=CENTER)
        self.tree2.column('2v5', width=75, anchor=CENTER)
        self.tree2.column('2v6', width=95, anchor=CENTER)
        self.tree2.grid(row=13, columnspan=5, rowspan=10)

        self.tree2.heading('2v1', text='Кл.')
        self.tree2.heading('2v2', text='Артикул')
        self.tree2.heading('2v3', text='Наименование материала')
        self.tree2.heading('2v4', text='Ед.\nизм')
        self.tree2.heading('2v5', text='Кол.\nсклад')
        self.tree2.heading('2v6', text='Цена')

        scr2 = ttk.Scrollbar(self, orient='vertical', command=self.tree1.yview)
        scr2.grid(row=13, column=5, sticky=N + S, rowspan=10)
        self.tree2.configure(yscrollcommand=scr2.set)


    def db7_1(self): # ПОКАЗТЬ БАЗУ. ОКНО 1
        cs1 = self.c7_1.get()
        cs2 = self.c7_2.get()
        cs3 = self.c7_3.get()
        cs4 = self.c7_4.get()
        cs6 = cs1 + cs2 + cs3 + cs4
        global sq71

        if int(cs1) > 0:
            self.conn = sqlite3.connect('s28b')
            self.cursor = self.conn.cursor()
            self.cursor.execute("SELECT * FROM МА_Б WHERE Ключ =:ID ORDER BY Цена", {"ID": cs6})
            sq71 = self.cursor.fetchall()
            for row in sq71:
                self.tree1.insert("", END, values=row)

    def db7_2(self): #УДАЛИТЬ ВЫБРАННЫЙ ЭЛЕМЕНТ ОКНО 1
        item = self.tree1.selection()[0]
        self.tree1.delete(item)


    def db7_3(self): # СОХРАНИТЬ СПЕЦИФИКАЦИЮ ОКНО 1
        names = ["Ключ", "Артикул", "Наименование", "Ед.изм.", " ", "Цена"]
        with open("Ответ Базы.csv", "w", newline='') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow(names)

            for product in sq71:
                writer.writerow(product)

    def db7_4(self): # ПОКАЗТЬ СКЛАД. ОКНО 2
        global sq72

        cs1 = self.c7_1.get()
        cs2 = self.c7_2.get()
        cs3 = self.c7_3.get()
        cs4 = self.c7_4.get()
        cs6 = cs1 + cs2 + cs3 + cs4

        if int(cs1) > 0:
            self.conn = sqlite3.connect('s28b')
            self.cursor = self.conn.cursor()
            self.cursor.execute("SELECT * FROM МА_С WHERE Ключ =:ID ORDER BY Цена", {"ID": cs6})
            sq72 = self.cursor.fetchall()
            for row in sq72:
                self.tree2.insert("", END, values=row)

    def db7_5(self): #УДАЛИТЬ ВЫБРАННЫЙ ЭЛЕМЕНТ ОКНО 2
        item = self.tree2.selection()[0]
        self.tree2.delete(item)

    def db7_7(self): #ФИЛЬТР ПО ПРОИЗВОДИТЕЛЮ. ОКНО 1
        cs1 = self.c7_1.get()
        cs2 = self.c7_2.get()
        cs3 = self.c7_3.get()
        cs4 = self.c7_4.get()
        cs6 = cs1 + cs2 + cs3 + cs4
        cs7 = self.c7_7.get()

        if int(cs1) > 0:

            self.conn = sqlite3.connect('s28b')
            self.cursor = self.conn.cursor()
            self.cursor.execute("SELECT * FROM МА_Б WHERE Ключ =? AND  Артикул LIKE ('%' || ? || '%')",
                                (cs6, cs7))
            sq71 = self.cursor.fetchall()
            for row in sq71:
                self.tree1.insert("", END, values=row)

    def db7_9(self):  # СОХРАНИТЬ СКЛАД
        names = ["Ключ", "Артикул", "Наименование", "Ед.изм.", "Доступно ", "Цена"]
        with open("Ответ Склада.csv", "w", newline='') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow(names)

            for product in sq72:
                writer.writerow(product)

    def ЭК(self):
        Запрос_в_магазин()



    def ok71(self):
        self.title('Контакторы')
        self.geometry('1170x750+300+80')
        self.resizable(False, False)

class Podbor8(Toplevel):
    def __init__(self):
        super().__init__(root)
        self.ok81()

        self.lb8_1 = Label(self, text="Укажите дополнительные параметры ")
        self.lb8_1.grid(row=0, column=0, columnspan=5, sticky=S)

        self.lb8_11 = Label(self, text="Номинальный ток, А")
        self.lb8_11.grid(row=1, column=0)
        self.c8_1 = ttk.Combobox(self, value=('0,65', '1', '2,5', '4', '6', '8', '10', '14', '19', '25', '32', '40', '50', '63', '80'))
        self.c8_1.grid(row=2, column=0, pady=10)

        self.lb8_12 = Label(self)
        self.lb8_12.grid(row=1, column=1)
        self.c8_2 = ttk.Button(self, width=20)
        self.c8_2.grid(row=2, column=1)

        self.lb8_13 = Label(self)
        self.lb8_13.grid(row=1, column=2)
        self.c8_3 = ttk.Button(self, width=20)
        self.c8_3.grid(row=2, column=2)

        self.lb8_14 = Label(self)
        self.lb8_14.grid(row=1, column=3)
        self.c8_4 = ttk.Button(self, width=20)
        self.c8_4.grid(row=2, column=3)

        self.lb8_15 = Label(self)
        self.lb8_15.grid(row=1, column=4)
        self.c8_5 = ttk.Button(self, width=20)
        self.c8_5.grid(row=2, column=4)



        self.lb8_16 = Button(self, text="Фильтр по производителю", width=22, bg='#BEF781', command=self.db8_7)
        self.lb8_16.grid(row=1, column=6)
        self.c8_7 = ttk.Combobox(self, value=('SHN', 'ETM', 'KUR', 'IEK', 'EKF', 'ELVERT', 'TDM'))
        self.c8_7.grid(row=2, column=6)

        self.b8_11 = Button(self, text="Показать из базы", width=22, bg='#BEF781', command=self.db8_1).grid(row=3,
                                                                                                            column=6)
        self.b8_12 = Button(self, text="Удалить выбранное", width=22, command=self.db8_2).grid(row=4, column=6)
        self.b8_13 = Button(self, text="Сохранить", width=22, command=self.db8_3).grid(row=5, column=6)
        self.b8_14 = Button(self, text="Запрос в ЭК", width=22, command=self.ЭК).grid(row=6, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=7, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=8, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=9, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=10, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=11, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=12, column=6)

        self.tree1 = ttk.Treeview(self, columns=('1v1', '1v2', '1v3', '1v4', '1v5', '1v6'), height=15,
                                  show='headings')
        self.tree1.column('1v1', width=1, anchor=CENTER)
        self.tree1.column('1v2', width=180)
        self.tree1.column('1v3', width=574)
        self.tree1.column('1v4', width=45, anchor=CENTER)
        self.tree1.column('1v5', width=75, anchor=CENTER)
        self.tree1.column('1v6', width=95, anchor=CENTER)
        self.tree1.grid(row=3, columnspan=5, rowspan=10)

        self.tree1.heading('1v1', text='Кл.')
        self.tree1.heading('1v2', text='Артикул')
        self.tree1.heading('1v3', text='Наименование материала')
        self.tree1.heading('1v4', text='Ед.\nизм')
        self.tree1.heading('1v5', text='Кол.')
        self.tree1.heading('1v6', text='Цена')

        scr1 = ttk.Scrollbar(self, orient='vertical', command=self.tree1.yview)
        scr1.grid(row=3, column=5, sticky=N + S, rowspan=10)
        self.tree1.configure(yscrollcommand=scr1.set)

        self.b7_21 = Button(self, text="Показать склад", width=22, bg='#FAAC58', command=self.db8_4).grid(row=13,
                                                                                                          column=6)
        self.b7_22 = Button(self, text="Удалить выбранное", width=22, command=self.db8_5).grid(row=14, column=6)
        self.b7_23 = Button(self, text="Сохранить", width=22, command=self.db8_9).grid(row=15, column=6)
        self.b7_24 = ttk.Button(self, width=22).grid(row=16,
                                                     column=6)  # Button(self, text="Запрос в ЭК", width=22, command=self.ЭК).grid(row=16, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=17, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=18, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=19, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=20, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=21, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=22, column=6)

        self.tree2 = ttk.Treeview(self, columns=('2v1', '2v2', '2v3', '2v4', '2v5', '2v6'), height=15,
                                  show='headings')
        self.tree2.column('2v1', width=1, anchor=CENTER)
        self.tree2.column('2v2', width=180)
        self.tree2.column('2v3', width=574)
        self.tree2.column('2v4', width=45, anchor=CENTER)
        self.tree2.column('2v5', width=75, anchor=CENTER)
        self.tree2.column('2v6', width=95, anchor=CENTER)
        self.tree2.grid(row=13, columnspan=5, rowspan=10)

        self.tree2.heading('2v1', text='Кл.')
        self.tree2.heading('2v2', text='Артикул')
        self.tree2.heading('2v3', text='Наименование материала')
        self.tree2.heading('2v4', text='Ед.\nизм')
        self.tree2.heading('2v5', text='Кол.\nсклад')
        self.tree2.heading('2v6', text='Цена')

        scr2 = ttk.Scrollbar(self, orient='vertical', command=self.tree1.yview)
        scr2.grid(row=13, column=5, sticky=N + S, rowspan=10)
        self.tree2.configure(yscrollcommand=scr2.set)


    def db8_1(self): # ПОКАЗТЬ БАЗУ. ОКНО 1
        cs1 = self.c8_1.get()
        #cs2 = self.c8_2.get()
        #cs3 = self.c8_3.get()
        #cs4 = self.c8_4.get()
        cs6 = cs1 # + cs2 + cs3 + cs4
        global sq81

        if int(cs1) > 0:
            self.conn = sqlite3.connect('s28b')
            self.cursor = self.conn.cursor()
            self.cursor.execute("SELECT * FROM МА_Б WHERE Ключ =:ID ORDER BY Цена", {"ID": cs6})
            sq81 = self.cursor.fetchall()
            for row in sq81:
                self.tree1.insert("", END, values=row)


    def db8_2(self):
        item = self.tree1.selection()[0]
        self.tree1.delete(item)


    def db8_3(self): # СОХРАНИТЬ СПЕЦИФИКАЦИЮ ОКНО 1
        names = ["Ключ", "Артикул", "Наименование", "Ед.изм.", " ", "Цена"]
        with open("Ответ Базы.csv", "w", newline='') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow(names)

            for product in sq81:
                writer.writerow(product)

    def db8_4(self):# ПОКАЗТЬ СКЛАД. ОКНО 2
        global sq82

        cs1 = self.c8_1.get()
        #cs2 = self.c8_2.get()
        #cs3 = self.c8_3.get()
        #cs4 = self.c8_4.get()
        cs6 = cs1 #+ cs2 + cs3 + cs4

        if int(cs1) > 0:
            self.conn = sqlite3.connect('s28b')
            self.cursor = self.conn.cursor()
            self.cursor.execute("SELECT * FROM МА_С WHERE Ключ =:ID ORDER BY Цена", {"ID": cs6})
            sq82 = self.cursor.fetchall()
            for row in sq82:
                self.tree2.insert("", END, values=row)

    def db8_5(self):
        item = self.tree2.selection()[0]
        self.tree2.delete(item)

    def db8_7(self): #ФИЛЬТР ПО ПРОИЗВОДИТЕЛЮ. ОКНО 1
        cs1 = self.c8_1.get()
        #cs2 = self.c8_2.get()
        #cs3 = self.c8_3.get()
        #cs4 = self.c8_4.get()
        cs6 = cs1 # + cs2 + cs3 + cs4
        cs7 = self.c8_7.get()

        if int(cs1) > 0:

            self.conn = sqlite3.connect('s28b')
            self.cursor = self.conn.cursor()
            self.cursor.execute("SELECT * FROM МА_Б WHERE Ключ =? AND  Артикул LIKE ('%' || ? || '%')",
                                (cs6, cs7))
            sq81 = self.cursor.fetchall()
            for row in sq81:
                self.tree1.insert("", END, values=row)



    def db8_9(self):  # СОХРАНИТЬ СКЛАД
        names = ["Ключ", "Артикул", "Наименование", "Ед.изм.", "Доступно ", "Цена"]
        with open("Ответ Склада.csv", "w", newline='') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow(names)

            for product in sq82:
                writer.writerow(product)

    def ЭК(self):
        Запрос_в_магазин()


    def ok81(self):
        self.title('Контакторы')
        self.geometry('1170x750+300+80')
        self.resizable(False, False)

class Podbor9(Toplevel):
    def __init__(self):
        super().__init__(root)
        self.ok91()

        self.lb9_1 = Label(self, text="Укажите дополнительные параметры ")
        self.lb9_1.grid(row=0, column=0, columnspan=5, sticky=S)

        self.lb9_11 = Label(self, text="Сечение")
        self.lb9_11.grid(row=1, column=0)
        self.c9_1 = ttk.Combobox(self, value=('2,5', '4', '6', '10', '16', '25', '35', '50', '70', '95', '150', '240'))
        self.c9_1.grid(row=2, column=0, pady=10)

        self.lb9_12 = Label(self, text="Тип зажима")
        self.lb9_12.grid(row=1, column=1)
        self.c9_2 = ttk.Combobox(self, value=('Bинтовой', 'Пружинный'))
        self.c9_2.grid(row=2, column=1)

        self.lb9_13 = Label(self, text="Количесвто рядов")
        self.lb9_13.grid(row=1, column=2)
        self.c9_3 = ttk.Combobox(self, value=('1','2','3','3+PE'))
        self.c9_3.grid(row=2, column=2)

        self.lb9_14 = Label(self, text="Цвет")
        self.lb9_14.grid(row=1, column=3)
        self.c9_4 = ttk.Combobox(self, value=('Серый','Бежевый',"Синий","Желто_зеленый"))
        self.c9_4.grid(row=2, column=3)

        self.lb9_15 = Label(self)
        self.lb9_15.grid(row=1, column=4)
        self.c9_5 = ttk.Button(self, width=20)
        self.c9_5.grid(row=2, column=4)

        self.lb9_17 = Button(self, text="Фильтр по производителю", bg='#BEF781', width=22, command=self.db9_7)
        self.lb9_17.grid(row=1, column=6)
        self.c9_7 = ttk.Combobox(self, value=('KLEMSAN', 'CONTACLIP', 'PHOENIX', 'IEK', 'EKF', 'ELVERT', 'TDM', 'SHN', 'CHINT'))
        self.c9_7.grid(row=2, column=6)

        self.b9_11 = Button(self, text="Показать из базы", width=22, bg='#BEF781', command=self.db9_1).grid(row=3,
                                                                                                            column=6)
        self.b9_12 = Button(self, text="Удалить выбранное", width=22, command=self.db9_2).grid(row=4, column=6)
        self.b9_13 = Button(self, text="Сохранить", width=22, command=self.db9_3).grid(row=5, column=6)
        self.b9_14 = Button(self, text="Запрос в ЭК", width=22, command=self.ЭК).grid(row=6, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=7, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=8, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=9, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=10, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=11, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=12, column=6)

        self.tree1 = ttk.Treeview(self, columns=('1v1', '1v2', '1v3', '1v4', '1v5', '1v6'), height=15,
                                  show='headings')
        self.tree1.column('1v1', width=1, anchor=CENTER)
        self.tree1.column('1v2', width=180)
        self.tree1.column('1v3', width=574)
        self.tree1.column('1v4', width=45, anchor=CENTER)
        self.tree1.column('1v5', width=75, anchor=CENTER)
        self.tree1.column('1v6', width=95, anchor=CENTER)
        self.tree1.grid(row=3, columnspan=5, rowspan=10)

        self.tree1.heading('1v1', text='Кл.')
        self.tree1.heading('1v2', text='Артикул')
        self.tree1.heading('1v3', text='Наименование материала')
        self.tree1.heading('1v4', text='Ед.\nизм')
        self.tree1.heading('1v5', text='Кол.')
        self.tree1.heading('1v6', text='Цена')

        scr1 = ttk.Scrollbar(self, orient='vertical', command=self.tree1.yview)
        scr1.grid(row=3, column=5, sticky=N + S, rowspan=10)
        self.tree1.configure(yscrollcommand=scr1.set)

        self.b9_21 = Button(self, text="Показать склад", width=22, bg='#FAAC58', command=self.db9_4).grid(row=13,
                                                                                                          column=6)
        self.b9_22 = Button(self, text="Удалить выбранное", width=22, command=self.db9_5).grid(row=14, column=6)
        self.b9_23 = Button(self, text="Сохранить", width=22, command=self.db9_9).grid(row=15, column=6)
        self.b9_24 = ttk.Button(self, width=22).grid(row=16,
                                                     column=6)  # Button(self, text="Запрос в ЭК", width=22, command=self.ЭК).grid(row=16, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=17, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=18, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=19, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=20, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=21, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=22, column=6)

        self.tree2 = ttk.Treeview(self, columns=('2v1', '2v2', '2v3', '2v4', '2v5', '2v6'), height=15,
                                  show='headings')
        self.tree2.column('2v1', width=1, anchor=CENTER)
        self.tree2.column('2v2', width=180)
        self.tree2.column('2v3', width=574)
        self.tree2.column('2v4', width=45, anchor=CENTER)
        self.tree2.column('2v5', width=75, anchor=CENTER)
        self.tree2.column('2v6', width=95, anchor=CENTER)
        self.tree2.grid(row=13, columnspan=5, rowspan=10)

        self.tree2.heading('2v1', text='Кл.')
        self.tree2.heading('2v2', text='Артикул')
        self.tree2.heading('2v3', text='Наименование материала')
        self.tree2.heading('2v4', text='Ед.\nизм')
        self.tree2.heading('2v5', text='Кол.\nсклад')
        self.tree2.heading('2v6', text='Цена')

        scr2 = ttk.Scrollbar(self, orient='vertical', command=self.tree1.yview)
        scr2.grid(row=13, column=5, sticky=N + S, rowspan=10)
        self.tree2.configure(yscrollcommand=scr2.set)

    def db9_1(self): # ПОКАЗТЬ БАЗУ. ОКНО 1
            cs11 = self.c9_1.get()
            if cs11 == '2,5':
                cs1 = '2'
            else:
                cs1=cs11
            cs21 = self.c9_2.get()
            if cs21 == 'Bинтовой':
                cs2 = "V"
            elif cs21 == 'Пружинный':
                cs2 = 'P'
            cs3 = self.c9_3.get()
            cs41 = self.c9_4.get()
            if cs41 == 'Серый':
                cs4 = 'CE'
            elif cs41 == 'Бежевый':
                cs4 = 'BE'
            elif cs41 == 'Синий':
                cs4 = 'BU'
            elif cs41 == 'Желто_зеленый':
                cs4 = 'PE'
            cs6 = cs1 + cs2 + cs3 + cs4

            print(cs6)
            global row, sq91

            if int(cs1) > 0:

                self.conn = sqlite3.connect('s28b')
                self.cursor = self.conn.cursor()
                self.cursor.execute("SELECT * FROM МА_Б WHERE Ключ =:ID ORDER BY Цена  ", {"ID": cs6})
                sq91 = self.cursor.fetchall()
                for row in sq91:
                    self.tree1.insert("", END, values=row)


    def db9_2(self): #УДАЛИТЬ ВЫБРАННЫЙ ЭЛЕМЕНТ ОКНО 1
        item = self.tree1.selection()[0]
        self.tree1.delete(item)


    def db9_3(self): #СОХРАНИТЬ СПЕЦИФИКАЦИЮ ОКНО 1
            names = ["Ключ", "Артикул", "Наименование", "Ед.изм.", " ", "Цена"]
            with open("Ответ Базы.csv", "w", newline='') as f:
                writer = csv.writer(f, delimiter=';')
                writer.writerow(names)

                for product in sq91:
                    writer.writerow(product)

    def db9_4(self): # ПОКАЗТЬ СКЛАД. ОКНО 2
        global sq92
        cs11 = self.c9_1.get()
        if cs11 == '2,5':
            cs1 = '2'
        else:
            cs1 = cs11
        cs21 = self.c9_2.get()
        if cs21 == 'Bинтовой':
            cs2 = "V"
        elif cs21 == 'Пружинный':
            cs2 = 'P'
        cs3 = self.c9_3.get()
        cs41 = self.c9_4.get()
        if cs41 == 'Серый':
            cs4 = 'CE'
        elif cs41 == 'Бежевый':
            cs4 = 'BE'
        elif cs41 == 'Синий':
            cs4 = 'BU'
        elif cs41 == 'Желто_зеленый':
            cs4 = 'PE'
        cs6 = cs1 + cs2 + cs3 + cs4

        if int(cs1) > 0:
            self.conn = sqlite3.connect('s28b')
            self.cursor = self.conn.cursor()
            self.cursor.execute("SELECT * FROM МА_С WHERE Ключ =:ID ORDER BY Цена", {"ID": cs6})
            sq92 = self.cursor.fetchall()
            for row in sq92:
                self.tree2.insert("", END, values=row)


    def db9_5(self): #УДАЛИТЬ ВЫБРАННЫЙ ЭЛЕМЕНТ ОКНО 5
        item = self.tree2.selection()[0]
        self.tree2.delete(item)

    def db9_7(self): #ФИЛЬТР ПО ПРОИЗВОДИТЕЛЮ. ОКНО 1
        cs11 = self.c9_1.get()
        if cs11 == '2,5':
            cs1 = '2'
        else:
            cs1 = cs11
        cs21 = self.c9_2.get()
        if cs21 == 'Bинтовой':
            cs2 = "V"
        elif cs21 == 'Пружинный':
            cs2 = 'P'
        cs3 = self.c9_3.get()
        cs41 = self.c9_4.get()
        if cs41 == 'Серый':
            cs4 = 'CE'
        elif cs41 == 'Бежевый':
            cs4 = 'BE'
        elif cs41 == 'Синий':
            cs4 = 'BU'
        elif cs41 == 'Желто_зеленый':
            cs4 = 'PE'
        cs6 = cs1 + cs2 + cs3 + cs4
        cs7 = self.c9_7.get()
        print(cs6)

        if int(cs1) > 0:

            self.conn = sqlite3.connect('s28b')
            self.cursor = self.conn.cursor()
            self.cursor.execute("SELECT * FROM МА_Б WHERE Ключ =? AND  Артикул LIKE ('%' || ? || '%')",
                                (cs6, cs7))
            sq91 = self.cursor.fetchall()
            for row in sq91:
                self.tree1.insert("", END, values=row)

    def db9_9(self):  # СОХРАНИТЬ СКЛАД
        names = ["Ключ", "Артикул", "Наименование", "Ед.изм.", "Доступно ", "Цена"]
        with open("Ответ Склада.csv", "w", newline='') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow(names)

            for product in sq92:
                writer.writerow(product)

    def ЭК(self):
        Запрос_в_магазин()




    def ok91(self):
        self.title('Автоматические выключатели\n модульного исполнения ')
        self.geometry('1170x750+300+80')
        self.resizable(False, False)

class Podbor10(Toplevel):
    def __init__(self):
        super().__init__(root)
        self.ok101()

        self.lb10_1 = Label(self, text="Укажите дополнительные параметры ")
        self.lb10_1.grid(row=0, column=0, columnspan=5, sticky=S)

        self.lb10_11 = Label(self, text="Количество модулей")
        self.lb10_11.grid(row=1, column=0)
        self.c10_1 = ttk.Combobox(self, value=(
        '9', '12', '15', '18', '24', '36', '2X24', '48', '54','60', '2X36', '72', '90', '2X48'))
        self.c10_1.grid(row=2, column=0, pady=10)

        self.lb10_12 = Label(self, text="Форма исполнения")
        self.lb10_12.grid(row=1, column=1)
        self.c10_2 = ttk.Combobox(self, value=('Навесной', 'Встраиваемый'))
        self.c10_2.grid(row=2, column=1)

        self.lb10_13 = Label(self, text="Степень защиты, iP")
        self.lb10_13.grid(row=1, column=2)
        self.c10_3 = ttk.Combobox(self, value=('30', '31', '54'))
        self.c10_3.grid(row=2, column=2)

        self.lb10_14 = Label(self)#, text="Цвет (RAL)")
        self.lb10_14.grid(row=1, column=3)
        self.c10_4 = ttk.Button(self, width=20)#, value=('7035', '7032'))
        self.c10_4.grid(row=2, column=3)

        self.lb10_15 = Label(self)
        self.lb10_15.grid(row=1, column=4)
        self.c10_5 = ttk.Button(self, width=20)
        self.c10_5.grid(row=2, column=4)

        self.b10_11 = Button(self, text="Показать из базы", width=22, bg='#BEF781', command=self.db10_1).grid(row=3,
                                                                                                            column=6)
        self.b10_12 = Button(self, text="Удалить выбранное", width=22, command=self.db10_2).grid(row=4, column=6)
        self.b10_13 = Button(self, text="Сохранить", width=22, command=self.db10_3).grid(row=5, column=6)
        self.b10_14 = Button(self, text="Запрос в ЭК", width=22, command=self.ЭК).grid(row=6, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=7, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=8, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=9, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=10, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=11, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=12, column=6)

        self.tree1 = ttk.Treeview(self, columns=('1v1', '1v2', '1v3', '1v4', '1v5', '1v6'), height=15,
                                  show='headings')
        self.tree1.column('1v1', width=1, anchor=CENTER)
        self.tree1.column('1v2', width=180)
        self.tree1.column('1v3', width=574)
        self.tree1.column('1v4', width=45, anchor=CENTER)
        self.tree1.column('1v5', width=75, anchor=CENTER)
        self.tree1.column('1v6', width=95, anchor=CENTER)
        self.tree1.grid(row=3, columnspan=5, rowspan=10)

        self.tree1.heading('1v1', text='Кл.')
        self.tree1.heading('1v2', text='Артикул')
        self.tree1.heading('1v3', text='Наименование материала')
        self.tree1.heading('1v4', text='Ед.\nизм')
        self.tree1.heading('1v5', text='Кол.')
        self.tree1.heading('1v6', text='Цена')

        scr1 = ttk.Scrollbar(self, orient='vertical', command=self.tree1.yview)
        scr1.grid(row=3, column=5, sticky=N + S, rowspan=10)
        self.tree1.configure(yscrollcommand=scr1.set)

        self.b9_21 = Button(self, text="Показать склад", width=22, bg='#FAAC58', command=self.db10_4).grid(row=13,
                                                                                                          column=6)
        self.b9_22 = Button(self, text="Удалить выбранное", width=22, command=self.db10_5).grid(row=14, column=6)
        self.b9_23 = Button(self, text="Сохранить", width=22, command=self.db10_9).grid(row=15, column=6)
        self.b9_24 = ttk.Button(self, width=22).grid(row=16,
                                                     column=6)  # Button(self, text="Запрос в ЭК", width=22, command=self.ЭК).grid(row=16, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=17, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=18, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=19, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=20, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=21, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=22, column=6)

        self.tree2 = ttk.Treeview(self, columns=('2v1', '2v2', '2v3', '2v4', '2v5', '2v6'), height=15,
                                  show='headings')
        self.tree2.column('2v1', width=1, anchor=CENTER)
        self.tree2.column('2v2', width=180)
        self.tree2.column('2v3', width=574)
        self.tree2.column('2v4', width=45, anchor=CENTER)
        self.tree2.column('2v5', width=75, anchor=CENTER)
        self.tree2.column('2v6', width=95, anchor=CENTER)
        self.tree2.grid(row=13, columnspan=5, rowspan=10)

        self.tree2.heading('2v1', text='Кл.')
        self.tree2.heading('2v2', text='Артикул')
        self.tree2.heading('2v3', text='Наименование материала')
        self.tree2.heading('2v4', text='Ед.\nизм')
        self.tree2.heading('2v5', text='Кол.\nсклад')
        self.tree2.heading('2v6', text='Цена')

        scr2 = ttk.Scrollbar(self, orient='vertical', command=self.tree1.yview)
        scr2.grid(row=13, column=5, sticky=N + S, rowspan=10)
        self.tree2.configure(yscrollcommand=scr2.set)

    def db10_1(self): # ПОКАЗТЬ БАЗУ. ОКНО 1
        global row, sq101
        cs1 = self.c10_1.get()
        cs21 = self.c10_2.get()
        global sq101
        if cs21 == "Навесной":
            cs2 = "N"
        else:
            cs21 == "Встраиваемый"
            cs2 = "V"
        cs3 = self.c10_3.get()
        #cs4 = self.c10_4.get()

        cs6 = cs1 + cs2 + cs3 #+ cs4
        print(cs6)

        if int(cs3) > 0:
            self.conn = sqlite3.connect('s28b')
            self.cursor = self.conn.cursor()
            self.cursor.execute("SELECT * FROM МА_Б WHERE Ключ =:ID ORDER BY Цена", {"ID": cs6})
            sq101 = self.cursor.fetchall()
            for row in sq101:
                self.tree1.insert("", END, values=row)

    def db10_2(self): #УДАЛИТЬ ВЫБРАННЫЙ ЭЛЕМЕНТ ОКНО 1
        item = self.tree1.selection()[0]
        self.tree1.delete(item)


    def db10_3(self): #СОХРАНИТЬ СПЕЦИФИКАЦИЮ ОКНО 1
            names = ["Ключ", "Артикул", "Наименование", "Ед.изм.", " ", "Цена"]
            with open("Ответ Базы.csv", "w", newline='') as f:
                writer = csv.writer(f, delimiter=';')
                writer.writerow(names)

                for product in sq101:
                    writer.writerow(product)


    def db10_4(self): # ПОКАЗТЬ СКЛАД. ОКНО 2
        global row, sq102
        cs1 = self.c10_1.get()
        cs21 = self.c10_2.get()
        if cs21 == "Навесной":
            cs2 = "N"
        else:
            cs21 == "Встраиваемый"
            cs2 = "V"
        cs3 = self.c10_3.get()
        #cs4 = self.c10_4.get()

        cs6 = cs1 + cs2 + cs3 #+ cs4
        print(cs6)

        if int(cs3) > 0:
            self.conn = sqlite3.connect('s28b')
            self.cursor = self.conn.cursor()
            self.cursor.execute("SELECT * FROM МА_С WHERE Ключ =:ID ORDER BY Цена", {"ID": cs6})
            sq102 = self.cursor.fetchall()
            for row in sq102:
                self.tree2.insert("", END, values=row)

    def db10_5(self): #УДАЛИТЬ ВЫБРАННЫЙ ЭЛЕМЕНТ ОКНО 2
        item = self.tree2.selection()[0]
        self.tree2.delete(item)

    def db10_9(self):  # СОХРАНИТЬ СКЛАД
        names = ["Ключ", "Артикул", "Наименование", "Ед.изм.", "Доступно ", "Цена"]
        with open("Ответ Склада.csv", "w", newline='') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow(names)

            for product in sq102:
                writer.writerow(product)

    def ЭК(self):
        Запрос_в_магазин()



    def ok101(self):
        self.title('Корпуса типа ЩРН (Металлические)')
        self.geometry('1170x750+300+80')
        self.resizable(False, False)

class Podbor11(Toplevel):

    def __init__(self):
        super().__init__(root)
        self.ok111()

        self.lb11_1 = Label(self, text="Укажите дополнительные параметры ")
        self.lb11_1.grid(row=0, column=0, columnspan=5, sticky=S)

        self.lb11_11 = Label(self, text="Количество полюсов")
        self.lb11_11.grid(row=1, column=0)
        self.c11_1 = ttk.Combobox(self, value=(
        '2', '3', '4'))
        self.c11_1.grid(row=2, column=0, pady=10)

        self.lb11_12 = Label(self, text="Тепловой расцепитель")
        self.lb11_12.grid(row=1, column=1)
        self.c11_2 = ttk.Combobox(self, value=('Фиксированный', 'Регулируемый'))
        self.c11_2.grid(row=2, column=1)

        self.lb11_13 = Label(self, text="Эл.магн. расцепитель")
        self.lb11_13.grid(row=1, column=2)
        self.c11_3 = ttk.Combobox(self, value=('Фиксированный', 'Регулируемый'))
        self.c11_3.grid(row=2, column=2)

        self.lb11_14 = Label(self, text="Номинальный ток, А")
        self.lb11_14.grid(row=1, column=3)
        self.c11_4 = ttk.Combobox(self, width=20, value=('10','16','25','32','40','50','63','80','100','125','160','200','250','315','320','400','500','630','800','1000'))
        self.c11_4.grid(row=2, column=3)

        self.lb11_15 = Label(self, text="Отключ. способность, кА")
        self.lb11_15.grid(row=1, column=4)
        self.c11_5 = ttk.Combobox(self, width=20, value=('6','7,5','10','14','18','20','25','30', '35','36', '40', '45', '50','65', '70','85','100','150'))
        self.c11_5.grid(row=2, column=4)

        self.lb2_16 = Button(self, text="Фильтр по производителю", width=22, bg='#BEF781', command=self.db11_7)
        self.lb2_16.grid(row=1, column=6)
        self.c11_7 = ttk.Combobox(self, value=('SHN','LS','IEK','TDM','ELVERT'))
        self.c11_7.grid(row=2, column=6)

        self.b11_11 = Button(self, text="Показать из базы", width=22, bg='#BEF781', command=self.db11_1).grid(row=3,
                                                                                                            column=6)
        self.b11_12 = Button(self, text="Удалить выбранное", width=22, command=self.db11_2).grid(row=4, column=6)
        self.b11_13 = Button(self, text="Сохранить", width=22, command=self.db11_3).grid(row=5, column=6)
        self.b11_14 = Button(self, text="Запрос в ЭК", width=22, command=self.ЭК).grid(row=6, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=7, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=8, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=9, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=10, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=11, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=12, column=6)

        self.tree1 = ttk.Treeview(self, columns=('1v1', '1v2', '1v3', '1v4', '1v5', '1v6'), height=15,
                                  show='headings')
        self.tree1.column('1v1', width=1, anchor=CENTER)
        self.tree1.column('1v2', width=180)
        self.tree1.column('1v3', width=574)
        self.tree1.column('1v4', width=45, anchor=CENTER)
        self.tree1.column('1v5', width=75, anchor=CENTER)
        self.tree1.column('1v6', width=95, anchor=CENTER)
        self.tree1.grid(row=3, columnspan=5, rowspan=10)

        self.tree1.heading('1v1', text='Кл.')
        self.tree1.heading('1v2', text='Артикул')
        self.tree1.heading('1v3', text='Наименование материала')
        self.tree1.heading('1v4', text='Ед.\nизм')
        self.tree1.heading('1v5', text='Кол.')
        self.tree1.heading('1v6', text='Цена')

        scr1 = ttk.Scrollbar(self, orient='vertical', command=self.tree1.yview)
        scr1.grid(row=3, column=5, sticky=N + S, rowspan=10)
        self.tree1.configure(yscrollcommand=scr1.set)

        self.b11_21 = Button(self, text="Показать склад", width=22, bg='#FAAC58', command=self.db11_4).grid(row=13,
                                                                                                          column=6)
        self.b11_22 = Button(self, text="Удалить выбранное", width=22, command=self.db11_5).grid(row=14, column=6)
        self.b11_23 = Button(self, text="Сохранить", width=22, command=self.db11_9).grid(row=15, column=6)
        self.b11_24 = ttk.Button(self, width=22).grid(row=16,
                                                     column=6)  # Button(self, text="Запрос в ЭК", width=22, command=self.ЭК).grid(row=16, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=17, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=18, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=19, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=20, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=21, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=22, column=6)

        self.tree2 = ttk.Treeview(self, columns=('2v1', '2v2', '2v3', '2v4', '2v5', '2v6'), height=15,
                                  show='headings')
        self.tree2.column('2v1', width=1, anchor=CENTER)
        self.tree2.column('2v2', width=180)
        self.tree2.column('2v3', width=574)
        self.tree2.column('2v4', width=45, anchor=CENTER)
        self.tree2.column('2v5', width=75, anchor=CENTER)
        self.tree2.column('2v6', width=95, anchor=CENTER)
        self.tree2.grid(row=13, columnspan=5, rowspan=10)

        self.tree2.heading('2v1', text='Кл.')
        self.tree2.heading('2v2', text='Артикул')
        self.tree2.heading('2v3', text='Наименование материала')
        self.tree2.heading('2v4', text='Ед.\nизм')
        self.tree2.heading('2v5', text='Кол.\nсклад')
        self.tree2.heading('2v6', text='Цена')

        scr2 = ttk.Scrollbar(self, orient='vertical', command=self.tree1.yview)
        scr2.grid(row=13, column=5, sticky=N + S, rowspan=10)
        self.tree2.configure(yscrollcommand=scr2.set)

    def db11_1(self): # ПОКАЗТЬ БАЗУ. ОКНО 1
        cs1 = self.c11_1.get()
        cs21 = self.c11_2.get()
        global sq111
        if cs21 == "Фиксированный":
            cs2 = "F"
        else:
            cs21 == "Регулируемый"
            cs2 = "R"
        cs31 = self.c11_3.get()
        if cs31 == "Фиксированный":
            cs3 = "F"
        else:
            cs31 == "Регулируемый"
            cs3 = "R"
        cs4 = self.c11_4.get()
        cs5 = self.c11_5.get()

        cs6 = cs1 + cs2 + cs3 + cs4 + cs5
        print(cs6)

        if int(cs1) > 0:
            self.conn = sqlite3.connect('s28b')
            self.cursor = self.conn.cursor()
            self.cursor.execute("SELECT * FROM МА_Б WHERE Ключ =:ID ORDER BY Цена", {"ID": cs6})
            sq111 = self.cursor.fetchall()
            for row in sq111:
                self.tree1.insert("", END, values=row)


    def db11_2(self): #УДАЛИТЬ ВЫБРАННЫЙ ЭЛЕМЕНТ ОКНО 1
        item = self.tree1.selection()[0]
        self.tree1.delete(item)


    def db11_3(self):# СОХРАНИТЬ СПЕЦИФИКАЦИЮ ОКНО 1
        names = ["Ключ", "Артикул", "Наименование", "Ед.изм.", " ", "Цена"]
        with open("Ответ Базы.csv", "w", newline='') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow(names)

            for product in sq111:
                writer.writerow(product)

    def db11_4(self): # ПОКАЗТЬ СКЛАД. ОКНО 2
        global sq112

        cs1 = self.c11_1.get()
        cs21 = self.c11_2.get()
        if cs21 == "Фиксированный":
            cs2 = "F"
        else:
            cs21 == "Регулируемый"
            cs2 = "R"
        cs31 = self.c11_3.get()
        if cs31 == "Фиксированный":
            cs3 = "F"
        else:
            cs31 == "Регулируемый"
            cs3 = "R"
        cs4 = self.c11_4.get()
        cs5 = self.c11_5.get()

        cs6 = cs1 + cs2 + cs3 + cs4 + cs5
        print(cs6)

        if int(cs1) > 0:
            self.conn = sqlite3.connect('s28b')
            self.cursor = self.conn.cursor()
            self.cursor.execute("SELECT * FROM МА_С WHERE Ключ =:ID ORDER BY Цена", {"ID": cs6})
            sq112 = self.cursor.fetchall()
            for row in sq112:
                self.tree2.insert("", END, values=row)

    def db11_5(self): #УДАЛИТЬ ВЫБРАННЫЙ ЭЛЕМЕНТ ОКНО 2
        item = self.tree2.selection()[0]
        self.tree2.delete(item)

    def db11_7(self): #ФИЛЬТР ПО ПРОИЗВОДИТЕЛЮ. ОКНО 1
        cs1 = self.c11_1.get()
        cs21 = self.c11_2.get()
        if cs21 == "Фиксированный":
            cs2 = "F"
        else:
            cs21 == "Регулируемый"
            cs2 = "R"
        cs31 = self.c11_3.get()
        if cs31 == "Фиксированный":
            cs3 = "F"
        else:
            cs31 == "Регулируемый"
            cs3 = "R"
        cs4 = self.c11_4.get()
        cs5 = self.c11_5.get()

        cs6 = cs1 + cs2 + cs3 + cs4 + cs5
        cs7 = self.c11_7.get()
        print(cs6)

        if int(cs1) > 0:

            self.conn = sqlite3.connect('s28b')
            self.cursor = self.conn.cursor()
            self.cursor.execute("SELECT * FROM МА_Б WHERE Ключ =? AND  Артикул LIKE ('%' || ? || '%')",
                                (cs6, cs7))
            sq111 = self.cursor.fetchall()
            for row in sq111:
                self.tree1.insert("", END, values=row)

    def db11_9(self):  # СОХРАНИТЬ СКЛАД
        names = ["Ключ", "Артикул", "Наименование", "Ед.изм.", "Доступно ", "Цена"]
        with open("Ответ Склада.csv", "w", newline='') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow(names)

            for product in sq112:
                writer.writerow(product)

    def ЭК(self):
        Запрос_в_магазин()

    def ok111(self):
        self.title('Автоматические выключателти\n в литом корпусе')
        self.geometry('1170x750+300+80')
        self.resizable(False, False)

class Podbor13(Toplevel):

    def __init__(self):
            super().__init__(root)
            self.ok131()

            self.lb13_1 = Label(self, text="Укажите дополнительные параметры ")
            self.lb13_1.grid(row=0, column=0, columnspan=5, sticky=S)

            self.lb13_11 = Label(self, text="Количество полюсов")
            self.lb13_11.grid(row=1, column=0)
            self.c13_1 = ttk.Combobox(self, value=('2', '4',))
            self.c13_1.grid(row=2, column=0, pady=10)

            self.lb13_12 = Label(self, text=("Кривая отключения"))
            self.lb13_12.grid(row=1, column=1)
            self.c13_2 = ttk.Combobox(self, value=('C', 'B'))
            self.c13_2.grid(row=2, column=1)

            self.lb13_13 = Label(self, text=("Номинальный ток, А" ))
            self.lb13_13.grid(row=1, column=2)
            self.c13_3 = ttk.Combobox(self, value=('6','10', '16', '20', '25', '32', '40', '50', '63', '80', '100'))
            self.c13_3.grid(row=2, column=2)

            self.lb13_14 = Label(self, text = ("Ток утечки"))
            self.lb13_14.grid(row=1, column=3)
            self.c13_4 = ttk.Combobox(self, value=('30', '300', '100','10'))
            self.c13_4.grid(row=2, column=3)

            self.lb13_15 = Label(self, text="Тип защиты")
            self.lb13_15.grid(row=1, column=4)
            self.c13_5 = ttk.Combobox(self, value=('A', 'AC', 'ASi'))
            self.c13_5.grid(row=2, column=4)

            self.lb13_16 = Button(self, text="Фильтр по производителю", width=22, bg='#BEF781', command=self.db13_7)
            self.lb13_16.grid(row=1, column=6)
            self.c13_7 = ttk.Combobox(self, value=('SHN','LS', 'KUR', 'IEK', 'EKF', 'ELVERT', 'TDM'))
            self.c13_7.grid(row=2, column=6)

            self.b13_11 = Button(self, text="Показать из базы", width=22, bg='#BEF781', command=self.db13_1).grid(row=3,
                                                                                                                column=6)
            self.b13_12 = Button(self, text="Удалить выбранное", width=22, command=self.db13_2).grid(row=4, column=6)
            self.b13_13 = Button(self, text="Сохранить", width=22, command=self.db13_3).grid(row=5, column=6)
            self.b13_14 = Button(self, text="Запрос в ЭК", width=22, command=self.ЭК).grid(row=6, column=6)
            self.rez = ttk.Button(self, width=22).grid(row=7, column=6)
            self.rez = ttk.Button(self, width=22).grid(row=8, column=6)
            self.rez = ttk.Button(self, width=22).grid(row=9, column=6)
            self.rez = ttk.Button(self, width=22).grid(row=10, column=6)
            self.rez = ttk.Button(self, width=22).grid(row=11, column=6)
            self.rez = ttk.Button(self, width=22).grid(row=12, column=6)

            self.tree1 = ttk.Treeview(self, columns=('1v1', '1v2', '1v3', '1v4', '1v5', '1v6'), height=15,
                                      show='headings')
            self.tree1.column('1v1', width=1, anchor=CENTER)
            self.tree1.column('1v2', width=180)
            self.tree1.column('1v3', width=574)
            self.tree1.column('1v4', width=45, anchor=CENTER)
            self.tree1.column('1v5', width=75, anchor=CENTER)
            self.tree1.column('1v6', width=95, anchor=CENTER)
            self.tree1.grid(row=3, columnspan=5, rowspan=10)

            self.tree1.heading('1v1', text='Кл.')
            self.tree1.heading('1v2', text='Артикул')
            self.tree1.heading('1v3', text='Наименование материала')
            self.tree1.heading('1v4', text='Ед.\nизм')
            self.tree1.heading('1v5', text='Кол.')
            self.tree1.heading('1v6', text='Цена')

            scr1 = ttk.Scrollbar(self, orient='vertical', command=self.tree1.yview)
            scr1.grid(row=3, column=5, sticky=N + S, rowspan=10)
            self.tree1.configure(yscrollcommand=scr1.set)

            self.b13_21 = Button(self, text="Показать склад", width=22, bg='#FAAC58', command=self.db13_4).grid(row=13,
                                                                                                              column=6)
            self.b13_22 = Button(self, text="Удалить выбранное", width=22, command=self.db13_5).grid(row=14, column=6)
            self.b13_23 = Button(self, text="Сохранить", width=22, command=self.db13_9).grid(row=15, column=6)
            self.b13_24 = ttk.Button(self, width=22).grid(row=16,
                                                         column=6)  # Button(self, text="Запрос в ЭК", width=22, command=self.ЭК).grid(row=16, column=6)
            self.rez = ttk.Button(self, width=22).grid(row=17, column=6)
            self.rez = ttk.Button(self, width=22).grid(row=18, column=6)
            self.rez = ttk.Button(self, width=22).grid(row=19, column=6)
            self.rez = ttk.Button(self, width=22).grid(row=20, column=6)
            self.rez = ttk.Button(self, width=22).grid(row=21, column=6)
            self.rez = ttk.Button(self, width=22).grid(row=22, column=6)

            self.tree2 = ttk.Treeview(self, columns=('2v1', '2v2', '2v3', '2v4', '2v5', '2v6'), height=15,
                                      show='headings')
            self.tree2.column('2v1', width=1, anchor=CENTER)
            self.tree2.column('2v2', width=180)
            self.tree2.column('2v3', width=574)
            self.tree2.column('2v4', width=45, anchor=CENTER)
            self.tree2.column('2v5', width=75, anchor=CENTER)
            self.tree2.column('2v6', width=95, anchor=CENTER)
            self.tree2.grid(row=13, columnspan=5, rowspan=10)

            self.tree2.heading('2v1', text='Кл.')
            self.tree2.heading('2v2', text='Артикул')
            self.tree2.heading('2v3', text='Наименование материала')
            self.tree2.heading('2v4', text='Ед.\nизм')
            self.tree2.heading('2v5', text='Кол.\nсклад')
            self.tree2.heading('2v6', text='Цена')

            scr2 = ttk.Scrollbar(self, orient='vertical', command=self.tree1.yview)
            scr2.grid(row=13, column=5, sticky=N + S, rowspan=10)
            self.tree2.configure(yscrollcommand=scr2.set)


    def db13_1(self):
            cs1 = self.c13_1.get()
            cs2 = self.c13_2.get()
            cs3 = self.c13_3.get()
            cs4 = self.c13_4.get()
            cs5 = self.c13_5.get()
            cs6 = cs1 + cs2 + cs3 + cs4 + cs5
            global sq131

            if int(cs1) > 0:
                self.conn = sqlite3.connect('s28b')
                self.cursor = self.conn.cursor()
                self.cursor.execute("SELECT * FROM МА_Б WHERE Ключ =:ID ORDER BY Цена", {"ID": cs6})
                sq131 = self.cursor.fetchall()
                for row in sq131:
                    self.tree1.insert("", END, values=row)

    def db13_2(self): #УДАЛИТЬ ВЫБРАННЫЙ ЭЛЕМЕНТ ОКНО 1
            item = self.tree1.selection()[0]
            self.tree1.delete(item)


    def db13_3(self):# СОХРАНИТЬ СПЕЦИФИКАЦИЮ ОКНО 1
        names = ["Ключ", "Артикул", "Наименование", "Ед.изм.", " ", "Цена"]
        with open("Ответ Базы.csv", "w", newline='') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow(names)

            for product in sq131:
                writer.writerow(product)



    def db13_4(self):# ПОКАЗТЬ СКЛАД. ОКНО 2
        global sq132

        cs1 = self.c13_1.get()
        cs2 = self.c13_2.get()
        cs3 = self.c13_3.get()
        cs4 = self.c13_4.get()
        cs6 = cs1 + cs2 + cs3 + cs4

        if int(cs1) > 0:
            self.conn = sqlite3.connect('s28b')
            self.cursor = self.conn.cursor()
            self.cursor.execute("SELECT * FROM МА_С WHERE Ключ =:ID ORDER BY Цена", {"ID": cs6})
            sq132 = self.cursor.fetchall()
            for row in sq132:
                self.tree2.insert("", END, values=row)



    def db13_5(self):
            item = self.tree2.selection()[0]
            self.tree2.delete(item)

    def db13_7(self): #ФИЛЬТР ПО ПРОИЗВОДИТЕЛЮ. ОКНО 1
            cs1 = self.c13_1.get()
            cs2 = self.c13_2.get()
            cs3 = self.c13_3.get()
            cs4 = self.c13_4.get()
            cs5 = self.c13_5.get()
            cs6 = cs1 + cs2 + cs3 + cs4 + cs5
            cs7 = self.c13_7.get()

            if int(cs1) > 0:

                self.conn = sqlite3.connect('s28b')
                self.cursor = self.conn.cursor()
                self.cursor.execute("SELECT * FROM МА_Б WHERE Ключ =? AND  Артикул LIKE ('%' || ? || '%')",
                                    (cs6, cs7))
                sq131 = self.cursor.fetchall()
                for row in sq131:
                    self.tree1.insert("", END, values=row)

    def db13_9(self):  # СОХРАНИТЬ СКЛАД
        names = ["Ключ", "Артикул", "Наименование", "Ед.изм.", "Доступно ", "Цена"]
        with open("Ответ Склада.csv", "w", newline='') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow(names)

            for product in sq132:
                writer.writerow(product)

    def ЭК(self):
        Запрос_в_магазин()

    def ok131(self):
            self.title('Дифференцивльный автоматические\nвыключатели')
            self.geometry('1170x800+300+80')
            self.resizable(False, False)

class Podbor14(Toplevel):
        def __init__(self):
            super().__init__(root)
            self.ok141()

            self.lb14_1 = Label(self, text="Укажите дополнительные параметры ")
            self.lb14_1.grid(row=0, column=0, columnspan=5, sticky=S)

            self.lb14_11 = Label(self, text="Количество полюсов")
            self.lb14_11.grid(row=1, column=0)
            self.c14_1 = ttk.Combobox(self, value=('2', '4', ))
            self.c14_1.grid(row=2, column=0, pady=10)

            self.lb14_12 = Label(self, text="Номинальный ток, А ")
            self.lb14_12.grid(row=1, column=1)
            self.c14_2 = ttk.Combobox(self, value=('10', '16', '20', '25', '32', '40', '50', '63', '80', '100'))
            self.c14_2.grid(row=2, column=1)

            self.lb14_13 = Label(self, text="Ток утечки, А")
            self.lb14_13.grid(row=1, column=2)
            self.c14_3 = ttk.Combobox(self, value=('30', '300', '100', '10'))
            self.c14_3.grid(row=2, column=2)

            self.lb14_14 = Label(self, text="Тип защиты")
            self.lb14_14.grid(row=1, column=3)
            self.c14_4 = ttk.Combobox(self, value=('A', 'AC', 'ASi'))
            self.c14_4.grid(row=2, column=3)

            self.lb14_15 = Label(self)
            self.lb14_15.grid(row=1, column=4)
            self.c14_5 = ttk.Button(self, width=20)
            self.c14_5.grid(row=2, column=4)

            self.lb14_16 = Button(self, text="Фильтр по производителю", width=22, bg='#BEF781', command=self.db14_7)
            self.lb14_16.grid(row=1, column=6)
            self.c14_7 = ttk.Combobox(self, value=('SHN','LS', 'KUR', 'IEK', 'EKF', 'ELVERT', 'TDM'))
            self.c14_7.grid(row=2, column=6)

            self.b14_11 = Button(self, text="Показать из базы", width=22, bg='#BEF781', command=self.db14_1).grid(row=3,
                                                                                                                column=6)
            self.b14_12 = Button(self, text="Удалить выбранное", width=22, command=self.db14_2).grid(row=4, column=6)
            self.b14_13 = Button(self, text="Сохранить", width=22, command=self.db14_3).grid(row=5, column=6)
            self.b14_14 = Button(self, text="Запрос в ЭК", width=22, command=self.ЭК).grid(row=6, column=6)
            self.rez = ttk.Button(self, width=22).grid(row=7, column=6)
            self.rez = ttk.Button(self, width=22).grid(row=8, column=6)
            self.rez = ttk.Button(self, width=22).grid(row=9, column=6)
            self.rez = ttk.Button(self, width=22).grid(row=10, column=6)
            self.rez = ttk.Button(self, width=22).grid(row=11, column=6)
            self.rez = ttk.Button(self, width=22).grid(row=12, column=6)

            self.tree1 = ttk.Treeview(self, columns=('1v1', '1v2', '1v3', '1v4', '1v5', '1v6'), height=15,
                                      show='headings')
            self.tree1.column('1v1', width=1, anchor=CENTER)
            self.tree1.column('1v2', width=180)
            self.tree1.column('1v3', width=574)
            self.tree1.column('1v4', width=45, anchor=CENTER)
            self.tree1.column('1v5', width=75, anchor=CENTER)
            self.tree1.column('1v6', width=95, anchor=CENTER)
            self.tree1.grid(row=3, columnspan=5, rowspan=10)

            self.tree1.heading('1v1', text='Кл.')
            self.tree1.heading('1v2', text='Артикул')
            self.tree1.heading('1v3', text='Наименование материала')
            self.tree1.heading('1v4', text='Ед.\nизм')
            self.tree1.heading('1v5', text='Кол.')
            self.tree1.heading('1v6', text='Цена')

            scr1 = ttk.Scrollbar(self, orient='vertical', command=self.tree1.yview)
            scr1.grid(row=3, column=5, sticky=N + S, rowspan=10)
            self.tree1.configure(yscrollcommand=scr1.set)

            self.b14_21 = Button(self, text="Показать склад", width=22, bg='#FAAC58', command=self.db14_4).grid(row=13,
                                                                                                              column=6)
            self.b14_22 = Button(self, text="Удалить выбранное", width=22, command=self.db14_5).grid(row=14, column=6)
            self.b14_23 = Button(self, text="Сохранить", width=22, command=self.db14_9).grid(row=15, column=6)
            self.b14_24 = ttk.Button(self, width=22).grid(row=16,
                                                         column=6)  # Button(self, text="Запрос в ЭК", width=22, command=self.ЭК).grid(row=16, column=6)
            self.rez = ttk.Button(self, width=22).grid(row=17, column=6)
            self.rez = ttk.Button(self, width=22).grid(row=18, column=6)
            self.rez = ttk.Button(self, width=22).grid(row=19, column=6)
            self.rez = ttk.Button(self, width=22).grid(row=20, column=6)
            self.rez = ttk.Button(self, width=22).grid(row=21, column=6)
            self.rez = ttk.Button(self, width=22).grid(row=22, column=6)

            self.tree2 = ttk.Treeview(self, columns=('2v1', '2v2', '2v3', '2v4', '2v5', '2v6'), height=15,
                                      show='headings')
            self.tree2.column('2v1', width=1, anchor=CENTER)
            self.tree2.column('2v2', width=180)
            self.tree2.column('2v3', width=574)
            self.tree2.column('2v4', width=45, anchor=CENTER)
            self.tree2.column('2v5', width=75, anchor=CENTER)
            self.tree2.column('2v6', width=95, anchor=CENTER)
            self.tree2.grid(row=13, columnspan=5, rowspan=10)

            self.tree2.heading('2v1', text='Кл.')
            self.tree2.heading('2v2', text='Артикул')
            self.tree2.heading('2v3', text='Наименование материала')
            self.tree2.heading('2v4', text='Ед.\nизм')
            self.tree2.heading('2v5', text='Кол.\nсклад')
            self.tree2.heading('2v6', text='Цена')

            scr2 = ttk.Scrollbar(self, orient='vertical', command=self.tree1.yview)
            scr2.grid(row=13, column=5, sticky=N + S, rowspan=10)
            self.tree2.configure(yscrollcommand=scr2.set)


        def db14_1(self): # ПОКАЗТЬ БАЗУ. ОКНО 1
            cs1 = self.c14_1.get()
            cs2 = self.c14_2.get()
            cs3 = self.c14_3.get()
            cs4 = self.c14_4.get()
            cs6 = cs1 + cs2 + cs3 + cs4
            global sq141

            if int(cs1) > 0:
                self.conn = sqlite3.connect('s28b')
                self.cursor = self.conn.cursor()
                self.cursor.execute("SELECT * FROM МА_Б WHERE Ключ =:ID ORDER BY Цена", {"ID": cs6})
                sq141 = self.cursor.fetchall()
                for row in sq141:
                    self.tree1.insert("", END, values=row)


        def db14_2(self): #УДАЛИТЬ ВЫБРАННЫЙ ЭЛЕМЕНТ ОКНО 1
            item = self.tree1.selection()[0]
            self.tree1.delete(item)


        def db14_3(self):  # СОХРАНИТЬ СПЕЦИФИКАЦИЮ ОКНО 1
            names = ["Ключ", "Артикул", "Наименование", "Ед.изм.", " ", "Цена"]
            with open("Ответ Базы.csv", "w", newline='') as f:
                writer = csv.writer(f, delimiter=';')
                writer.writerow(names)

                for product in sq141:
                    writer.writerow(product)

        def db14_4(self): # ПОКАЗТЬ СКЛАД. ОКНО 2
            global sq142

            cs1 = self.c14_1.get()
            cs2 = self.c14_2.get()
            cs3 = self.c14_3.get()
            cs4 = self.c14_4.get()
            cs6 = cs1 + cs2 + cs3 +cs4

            if int(cs1) > 0:
                self.conn = sqlite3.connect('s28b')
                self.cursor = self.conn.cursor()
                self.cursor.execute("SELECT * FROM МА_С WHERE Ключ =:ID ORDER BY Цена", {"ID": cs6})
                sq142 = self.cursor.fetchall()
                for row in sq142:
                    self.tree2.insert("", END, values=row)

        def db14_5(self): #УДАЛИТЬ ВЫБРАННЫЙ ЭЛЕМЕНТ ОКНО 2
            item = self.tree2.selection()[0]
            self.tree2.delete(item)

        def db14_7(self): #ФИЛЬТР ПО ПРОИЗВОДИТЕЛЮ. ОКНО 1
            cs1 = self.c14_1.get()
            cs2 = self.c14_2.get()
            cs3 = self.c14_3.get()
            cs4 = self.c14_4.get()
            cs6 = cs1 + cs2 + cs3 + cs4
            cs7 = self.c14_7.get()

            if int(cs1) > 0:

                self.conn = sqlite3.connect('s28b')
                self.cursor = self.conn.cursor()
                self.cursor.execute("SELECT * FROM МА_Б WHERE Ключ =? AND  Артикул LIKE ('%' || ? || '%')",
                                    (cs6, cs7))
                sq141 = self.cursor.fetchall()
                for row in sq141:
                    self.tree1.insert("", END, values=row)

        def db14_9(self):  # СОХРАНИТЬ СКЛАД
            names = ["Ключ", "Артикул", "Наименование", "Ед.изм.", "Доступно ", "Цена"]
            with open("Ответ Склада.csv", "w", newline='') as f:
                writer = csv.writer(f, delimiter=';')
                writer.writerow(names)

                for product in sq142:
                    writer.writerow(product)

        def ЭК(self):
            Запрос_в_магазин()

        def ok141(self):
            self.title('Устройства дифференциальной защиты УЗО')
            self.geometry('1170x800+300+80')
            self.resizable(False, False)

class Podbor15(Toplevel):
    def __init__(self):
        super().__init__(root)
        self.ok151()

        self.lb15_1 = Label(self, text="Укажите дополнительные параметры ")
        self.lb15_1.grid(row=0, column=0, columnspan=5, sticky=S)

        self.lb15_11 = Label(self, text="Габаритные размеры")
        self.lb15_11.grid(row=1, column=0)
        self.c15_1 = ttk.Combobox(self, value=(
        '~ 395х310х120', '~ 500х400х220', '~ 650х500х220', '~ 800х650х250', '~ 1000х650х250',
        '~ 1200х650х285', '~ 1400х800х300'))
        self.c15_1.grid(row=2, column=0, pady=10)

        self.lb15_12 = Label(self, text="Форма исполнения")
        self.lb15_12.grid(row=1, column=1)
        self.c15_2 = ttk.Combobox(self, value=('Навесной', 'Встраиваемый'))
        self.c15_2.grid(row=2, column=1)

        self.lb15_13 = Label(self, text="Степень защиты, iP")
        self.lb15_13.grid(row=1, column=2)
        self.c15_3 = ttk.Combobox(self, value=( '31', '54','65','66'))
        self.c15_3.grid(row=2, column=2)

        self.lb15_14 = Label(self,text="Климатическое исполнение")#, text="Цвет (RAL)")
        self.lb15_14.grid(row=1, column=3)
        self.c15_4 = ttk.Combobox(self, value=('УХЛ3', 'У2', 'УХЛ1','У1'))
        self.c15_4.grid(row=2, column=3)

        self.lb15_15 = Label(self)
        self.lb15_15.grid(row=1, column=4)
        self.c15_5 = ttk.Button(self, width=20)
        self.c15_5.grid(row=2, column=4)

        self.b15_11 = Button(self, text="Показать из базы", width=22, bg='#BEF781', command=self.db15_1).grid(row=3,
                                                                                                              column=6)
        self.b15_12 = Button(self, text="Удалить выбранное", width=22, command=self.db15_2).grid(row=4, column=6)
        self.b15_13 = Button(self, text="Сохранить", width=22, command=self.db15_3).grid(row=5, column=6)
        self.b15_14 = Button(self, text="Запрос в ЭК", width=22, command=self.ЭК).grid(row=6, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=7, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=8, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=9, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=10, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=11, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=12, column=6)

        self.tree1 = ttk.Treeview(self, columns=('1v1', '1v2', '1v3', '1v4', '1v5', '1v6'), height=15,
                                  show='headings')
        self.tree1.column('1v1', width=1, anchor=CENTER)
        self.tree1.column('1v2', width=180)
        self.tree1.column('1v3', width=574)
        self.tree1.column('1v4', width=45, anchor=CENTER)
        self.tree1.column('1v5', width=75, anchor=CENTER)
        self.tree1.column('1v6', width=95, anchor=CENTER)
        self.tree1.grid(row=3, columnspan=5, rowspan=10)

        self.tree1.heading('1v1', text='Кл.')
        self.tree1.heading('1v2', text='Артикул')
        self.tree1.heading('1v3', text='Наименование материала')
        self.tree1.heading('1v4', text='Ед.\nизм')
        self.tree1.heading('1v5', text='Кол.')
        self.tree1.heading('1v6', text='Цена')

        scr1 = ttk.Scrollbar(self, orient='vertical', command=self.tree1.yview)
        scr1.grid(row=3, column=5, sticky=N + S, rowspan=10)
        self.tree1.configure(yscrollcommand=scr1.set)

        self.b15_21 = Button(self, text="Показать склад", width=22, bg='#FAAC58', command=self.db15_4).grid(row=13,
                                                                                                            column=6)
        self.b15_22 = Button(self, text="Удалить выбранное", width=22, command=self.db15_5).grid(row=14, column=6)
        self.b15_23 = Button(self, text="Сохранить", width=22, command=self.db15_9).grid(row=15, column=6)
        self.b15_24 = ttk.Button(self, width=22).grid(row=16,
                                                      column=6)  # Button(self, text="Запрос в ЭК", width=22, command=self.ЭК).grid(row=16, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=17, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=18, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=19, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=20, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=21, column=6)
        self.rez = ttk.Button(self, width=22).grid(row=22, column=6)

        self.tree2 = ttk.Treeview(self, columns=('2v1', '2v2', '2v3', '2v4', '2v5', '2v6'), height=15,
                                  show='headings')
        self.tree2.column('2v1', width=1, anchor=CENTER)
        self.tree2.column('2v2', width=180)
        self.tree2.column('2v3', width=574)
        self.tree2.column('2v4', width=45, anchor=CENTER)
        self.tree2.column('2v5', width=75, anchor=CENTER)
        self.tree2.column('2v6', width=95, anchor=CENTER)
        self.tree2.grid(row=13, columnspan=5, rowspan=10)

        self.tree2.heading('2v1', text='Кл.')
        self.tree2.heading('2v2', text='Артикул')
        self.tree2.heading('2v3', text='Наименование материала')
        self.tree2.heading('2v4', text='Ед.\nизм')
        self.tree2.heading('2v5', text='Кол.\nсклад')
        self.tree2.heading('2v6', text='Цена')

        scr2 = ttk.Scrollbar(self, orient='vertical', command=self.tree1.yview)
        scr2.grid(row=13, column=5, sticky=N + S, rowspan=10)
        self.tree2.configure(yscrollcommand=scr2.set)

    def db15_1(self):
        cs11 = self.c15_1.get()
        if cs11 == "~ 395х310х120":
           cs1= "432"
        elif cs11 == "~ 500х400х220":
           cs1 = "542"
        elif cs11 == "~ 650х500х220":
           cs1 = "642"
        elif cs11 == "~ 800х650х250":
           cs1 = "843"
        elif cs11 == "~ 1000х650х285":
           cs1 = "1063"
        elif cs11 == "~ 1200х650х285":
           cs1 = "1263"
        elif cs11 == "~ 1400х800х300":
           cs1 = "1483"

        cs21 = self.c15_2.get()
        global sq151
        if cs21 == "Навесной":
            cs2 = "N"
        elif cs21 == "Встраиваемый":
            cs2 = "V"
        cs3 = self.c15_3.get()
        cs41 = self.c15_4.get()
        if cs41 == "УХЛ3":
           cs4= "UXL3"
        elif cs41 == "У2":
           cs4 = "U2"
        elif cs41 == "У2":
           cs4 = "642"
        elif cs41 == "УХЛ1":
           cs4 = "UXL1"
        elif cs41 == "У1":
           cs4 = "U1"

        cs6 = cs1 + cs2 + cs3 + cs4
        print(cs6)

        if int(cs3) > 0:
            self.conn = sqlite3.connect('s28b')
            self.cursor = self.conn.cursor()
            self.cursor.execute("SELECT * FROM МА_Б WHERE Ключ =:ID ORDER BY Цена", {"ID": cs6})
            sq151 = self.cursor.fetchall()
            for row in sq151:
                self.tree1.insert("", END, values=row)



    def db15_2(self): #УДАЛИТЬ ВЫБРАННЫЙ ЭЛЕМЕНТ ОКНО 1
        item = self.tree1.selection()[0]
        self.tree1.delete(item)


    def db15_3(self):# СОХРАНИТЬ СПЕЦИФИКАЦИЮ ОКНО 1

        names = ["Ключ", "Артикул", "Наименование", "Ед.изм.", " ", "Цена"]
        with open("Ответ Базы.csv", "w", newline='') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow(names)

            for product in sq151:
                writer.writerow(product)


    def db15_4(self): # ПОКАЗТЬ СКЛАД. ОКНО 2
        global sq152

        cs11 = self.c15_1.get()
        if cs11 == "~ 395х310х120":
            cs1 = "432"
        elif cs11 == "~ 500х400х220":
            cs1 = "542"
        elif cs11 == "~ 650х500х220":
            cs1 = "642"
        elif cs11 == "~ 800х650х250":
            cs1 = "843"
        elif cs11 == "~ 1000х650х285":
            cs1 = "1063"
        elif cs11 == "~ 1200х650х285":
            cs1 = "1263"
        elif cs11 == "~ 1400х800х300":
            cs1 = "1483"

        cs21 = self.c15_2.get()
        global sq151
        if cs21 == "Навесной":
            cs2 = "N"
        elif cs21 == "Встраиваемый":
            cs2 = "V"
        cs3 = self.c15_3.get()
        cs41 = self.c15_4.get()
        if cs41 == "УХЛ3":
            cs4 = "UXL3"
        elif cs41 == "У2":
            cs4 = "U2"
        elif cs41 == "У2":
            cs4 = "642"
        elif cs41 == "УХЛ1":
            cs4 = "UXL1"
        elif cs41 == "У1":
            cs4 = "U1"
        cs6 = cs1 + cs2 + cs3 + cs4
        print(cs6)

        if int(cs1) > 0:
            self.conn = sqlite3.connect('s28b')
            self.cursor = self.conn.cursor()
            self.cursor.execute("SELECT * FROM МА_С WHERE Ключ =:ID ORDER BY Цена", {"ID": cs6})
            sq152 = self.cursor.fetchall()
            for row in sq152:
                self.tree2.insert("", END, values=row)

    def db15_5(self): #УДАЛИТЬ ВЫБРАННЫЙ ЭЛЕМЕНТ ОКНО 2
        item = self.tree2.selection()[0]
        self.tree2.delete(item)

    def db15_7(self): #ФИЛЬТР ПО ПРОИЗВОДИТЕЛЮ. ОКНО 1
        cs1 = self.c15_1.get()
        cs2 = self.c15_2.get()
        cs3 = self.c15_3.get()
        cs4 = self.c15_4.get()
        cs6 = cs1 + cs2 + cs3 + cs4
        cs7 = self.c15_7.get()

        if int(cs1) > 0:

            self.conn = sqlite3.connect('s28b')
            self.cursor = self.conn.cursor()
            self.cursor.execute("SELECT * FROM МА_Б WHERE Ключ =? AND  Артикул LIKE ('%' || ? || '%')",
                                (cs6, cs7))
            sq151 = self.cursor.fetchall()
            for row in sq151:
                self.tree1.insert("", END, values=row)

    def db15_9(self):  # СОХРАНИТЬ СКЛАД
        names = ["Ключ", "Артикул", "Наименование", "Ед.изм.", "Доступно ", "Цена"]
        with open("Ответ Склада.csv", "w", newline='') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow(names)

            for product in sq152:
                writer.writerow(product)

    def ЭК(self):
        Запрос_в_магазин()


    def ok151(self):
        self.title('Корпуса типа ЩМП')
        self.geometry('1170x750+300+80')
        self.resizable(False, False)


if __name__ == "__main__":
    root = Tk()
   # db = DB()
    app = Main(root)
    app.grid()
    root.title("")
    root.geometry("870x430+520+200")
    root.resizable(False, False)
    root.mainloop()