# Script by T1OneB (Pavel)
# Срипт от T1OneB (Павел)

# импорт плагинов

import os
import config
from colorama import init, Fore
import random

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# имя

name = input("Укажите имя: ")

# возраст

age = input("Укажите ваш возраст: ")
print()

if int(age) <= 18:
	print("Ну ничего. Повзрослеешь...")
else:
	print("Уже большой!")
enter = input("Нажмите 'Enter' для продолжения...")
cls()

# вес

wight = input("Укажите ваш вес: ")
print()

if int(wight) <= 35:
    print("Кушай больше!")
else:
	print('Пора худеть!')
	
enter1 = input("Нажмите 'Enter' для продолжения...")

cls()

# карточка

print(Fore.BLUE + "Ваша карточка")
print(Fore.GREEN + "Имя: " + name)
print("Возраст: " + age)
print("Вес: " + wight)
print()
enter2 = input(Fore.RED + "Нажмите 'Enter' для продолжения...")
cls()