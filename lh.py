# -*- coding: utf-8 -*-
import sys
if sys.version_info[0] < 3:
    print ("Python 2 não é suportado, mn tenta o python3 :)")
    exit(0)
    
   
idioma = open("modulos/idioma.txt", "r+")
leitor = idioma.readlines()
analisa = len(leitor)
if not analisa:
	print ("[01] Português-Brasil")
	print ("[02] Español")
	print ("[03] English\n")
	print ("sei la mn escolhe ai")
	lingua_seleciona = input("Seleciona uma linguagem ai: ")
	if lingua_seleciona == "01" or lingua_seleciona == "1":
		idioma.write("pt")
		idioma.close()
		restart_program()
		pass

	elif lingua_seleciona == "02" or lingua_seleciona == "2":
		idioma.write("es")
		idioma.close()
		restart_program()
		pass

	elif lingua_seleciona == "03" or lingua_seleciona == "3":
		idioma.write("en")
		idioma.close()
		restart_program()
		pass

	else:
		os.system("clear")
		print ("Não foi selecionado uma opção correta, definindo para Português-Brasil")
		print ("No se seleccionó una opción correcta, estableciéndose como portugués-brasileño")
		print ("A correct option was not selected, setting to Portuguese-Brazilian\n")
		print ("Altere essa linguagem nas configurações")
		print ("Cambie este idioma en los ajustes")
		print ("Change this language in the settings")
		time.sleep(5)
		idioma.write("pt")
		idioma.close()
		restart_program()

pt = False
en = False
es = False
pt_check = "pt"
en_check = "en"
es_check = "es"

from var_pt import *
from var_en import *
from var_es import *

with open("modulos/idioma.txt", "r") as a:
	for linha in a:
		if pt_check.lower() == linha.lower().strip():
			pt = True
			#from var_pt import *
			pass
		elif en_check.lower() == linha.lower().strip():
			en = True
			#from var_en import *
			pass

		elif es_check.lower() == linha.lower().strip():
			es = True
			#from var_es import *
			pass
    
import os

banner()
print ('BEM VINDO AO SCRIPT LA LOS HERMANOS')

print ('OK VAMOS COMEÇAR')

import sqlite3

MASTER_PASSWORD = "los"

senha = input("Insira a senha: ")
if senha != MASTER_PASSWORD:
	print("senha correta ....: ")
	exit()

conn = loshermanos.connect('passwords.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    service TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);
''')

conn.close()






import os

print("olaaaaa amigos")

1 - ('https://github.com/Zian25/UniTools-Termux')   

1 - ('https://jornadadodev.com.br/cursos')


