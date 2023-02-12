import random as rand
import sqlite3 as sql
import os
import pandas as pd
import openpyxl
from datetime import date


if os.path.exists('database.db')==False:

    con=sql.connect('database.db')
    cur=con.cursor()
    #cur.execute('CREATE TABLE arhiva(orginal,Klasifikaciska_oznaka,Naziv_dokumenta,broj_dokumenta,datum_nastanka)')
    cur.execute('''
        CREATE TABLE Arhiva(
        orginal CHAR(10),
        Klasifikacijska_oznaka INT,
        Naziv_dokumenta CHAR(245),
        broj_dokumenata INT,
        datum_nastanka DATE
        );
    ''')


choice=input('''Izaberite operaciju:
        1)Unesite podatke od kupca
        2)Conversion to excel
        3)Brisanje baze podataka
        Unesite broj od izbora: ''')

if choice=='1':
    nameOfCompany=str(input('Ime kompanije/korisnika: '))
    typeOfService=str(input('Naziv usluge: '))
    date=str(input('Datum nastanka dokumenta(npr.23.05.2023): '))
    yearOfDocument=input('Unesite godinu dokumenta(npr.za 2019 ide 19): ')
    numberOfDocument=str(rand.randint(1000000,9999999))
    numberOfDocument=f'{numberOfDocument}/{yearOfDocument}'
    namePlusType=f'{nameOfCompany} {typeOfService}'
    osnIliDod=input('Jeli dokument osnovna(19) ili dodatna(38): ')

    con=sql.connect('database.db')
    cur=con.cursor()
    cur.execute(f'''INSERT INTO arhiva VALUES('O',{osnIliDod},'{namePlusType}','{numberOfDocument}','{date}');''')
    con.commit()

elif choice=='2':
    con=sql.connect('database.db')
    df=pd.read_sql_query('SELECT * FROM Arhiva',con)
    df.to_excel(f'{date.today()}.xlsx')
    print('Baza podataka je spašena u excel')

elif choice=='3':
    os.remove('database.db')
    print('Baza podataka je izbrisana')
