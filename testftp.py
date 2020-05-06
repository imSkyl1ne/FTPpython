#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

from ftplib import FTP
from getpass import getpass

ftp = FTP('192.168.1.203')
login=input("login ? ")
mdp=getpass("mdp ? ")
ftp.login(user=login,passwd=mdp)
ftp.cwd('/home/user')

etat=ftp.getwelcome()
print("Etat:",etat)

rep=ftp.dir()
print(rep)

choix=input("que souhaitez vous faire ? (entrez le num puis enter) \n 1:créer un repertoire \n 2:supprimer un repertoire \n 3:renomer un fichier ou dossier \n")
if choix=="1":
        dirname1 = input('taper le nom du repertoire à créer: ')
        newrep= ftp.mkd(dirname1)
if choix=="2":
        dirname2 = input('taper le nom du repertoire à supprimer: ')
        delrep= ftp.rmd(dirname2)
if choix=="3":
        filename_before = input('taper le nom du fichier ou repertoire à renommer: ')
        filename_after = input('le renommer en: ')
        rename= ftp.rename(filename_before,filename_after)
