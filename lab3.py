import csv
import sys
import keyboard
import numpy as np
import pandas as pd


def open_group1():
	print("Виберіть спосіб виведення\n\
DataFrame Pandas -> Натисніть 1\n\
Звичайний -> Натисніть 2\n")

	while True:
		try:
			if keyboard.is_pressed('1'): #З використанням pandas
				data = df = pd.read_table('C:\python projects\group1.txt', delimiter=" ", header=None, encoding='utf-8')
				data.columns = ['Прізвище', "Ім'я", 'Середній бал']
				print ('______________KH-2-1______________\n')
				print(data)
				print ('__________________________________\n')
				break
			if keyboard.is_pressed('2'): #Звичайне зчитування та вивід інофрмації
				file1 = open("C:\python projects\group1.txt", "r", encoding='utf-8')
				print ('______________KH-2-1______________\n')
				while True:
					line = file1.readline()
					if not line:
						break
					print(line.strip())
				print ('____________________________\n')
				file1.close()
				break
		except:
			break


def open_group2():
	print("Виберіть спосіб виведення\n\
DataFrame Pandas -> Натисніть 1\n\
Звичайний -> Натисніть 2\n")

	while True:
		try:
			if keyboard.is_pressed('1'): #З використанням pandas
				data = df = pd.read_table('C:\python projects\group2.txt', delimiter=" ", header=None, encoding='utf-8')
				data.columns = ['Прізвище', "Ім'я", 'Середній бал']
				print ('______________KH-2-2______________\n')
				print(data)
				print ('__________________________________\n')
				break
			if keyboard.is_pressed('2'): #Звичайне зчитування та вивід інофрмації
				file1 = open("C:\python projects\group2.txt", "r", encoding='utf-8')
				print ('______________KH-2-2______________\n')
				while True:
					line = file1.readline()
					if not line:
						break
					print(line.strip())
				print ('____________________________\n')
				file1.close()
				break
		except:
			break

def addzap():
	print("Виберіть группу\n")
	while True:
		try:
			if keyboard.is_pressed('1'):
				add_to_file = open("C:\python projects\group1.txt", "a", encoding='utf-8')
				add_to_file.write("\n")
				add_to_file.write(input("Введіть студента -> "))
				add_to_file.close()
				print("Оновлений список:")
				file1 = open("C:\python projects\group1.txt", "r", encoding='utf-8')
				print ('______________KH-2-2______________\n')
				while True:
					line = file1.readline()
					if not line:
						break
					print(line.strip())
				print ('____________________________\n')
				file1.close()
				break
			if keyboard.is_pressed('2'):
				add_to_file = open("C:\python projects\group2.txt", "a", encoding='utf-8')
				add_to_file.write("\n")
				add_to_file.write(input("Введіть студента -> "))
				add_to_file.close()
				print("Оновлений список:")
				file1 = open("C:\python projects\group2.txt", "r", encoding='utf-8')
				print ('______________KH-2-2______________\n')
				while True:
					line = file1.readline()
					if not line:
						break
					print(line.strip())
				print ('____________________________\n')
				file1.close()
				break
		except:
			break

def search():
	print("Виберіть группу\n")
	while True:
		try:
			if keyboard.is_pressed('1'):
				name = input("Введіть прізвище студента -> ")
				in_file = open("C:\python projects\group1.txt", "r", encoding='utf-8')
				print ('______________KH-2-1______________\n')
				for line in in_file:
					if name in line:
						print (line)
				print ('__________________________________\n')
				break
			if keyboard.is_pressed('2'):
				name = input("Введіть прізвище студента -> ")
				in_file = open("C:\python projects\group2.txt", "r", encoding='utf-8')
				print ('______________KH-2-2______________\n')
				for line in in_file:
					if name in line:
						print (line)
				print ('__________________________________\n')
				break
		except:
			break

def sort():
	print("Виберіть группу\n")
	while True:
		try:
			if keyboard.is_pressed('1'):
				data = df = pd.read_table('C:\python projects\group1.txt', delimiter=" ", header=None, encoding='utf-8')
				data.columns = ['Прізвище', "Ім'я", 'Середній бал']
				print("Сортування за середнім балом")
				print ('______________KH-2-1______________\n')
				SortData = data.sort_values(by='Середній бал', ascending=False)
				print(SortData)
				print ('__________________________________\n')
				break
			if keyboard.is_pressed('2'):
				data = df = pd.read_table('C:\python projects\group2.txt', delimiter=" ", header=None, encoding='utf-8')
				data.columns = ['Прізвище', "Ім'я", 'Середній бал']
				print("Сортування за середнім балом")
				print ('______________KH-2-2______________\n')
				SortData = data.sort_values(by='Середній бал', ascending=False)
				print(SortData)
				print ('__________________________________\n')
				
				break
		except:
			break



print("\n 1 -> Группа КН-2-1\n\
 2 -> Группа КН-2-2\n\n\
 3 -> Вивести групу КН-2-1 \n\
 4 -> Вивести групу КН-2-2\n\
 5 -> Додати запис\n\
 6 -> Пошук\n\
 7 -> Сортування\n")


while True:
	try:
		if keyboard.is_pressed('3'):
			open_group1()
			break
		if keyboard.is_pressed('4'):
			open_group2()
			break
		if keyboard.is_pressed('5'):
			addzap()
			break
		if keyboard.is_pressed('6'):
			search()
			break
		if keyboard.is_pressed('7'):
			sort()
			break
	except:
		break


