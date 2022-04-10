import subprocess
import os
print("проверка и устанрвка модулей...")
os.system("pip install rich")
os.system("pip install pyfiglet")
print("Выполнено")
import requests
import pyfiglet
from rich.console import Console
console = Console()
console.print("[magenta]" + pyfiglet.figlet_format("Wi-Fi Get Password", font="slant") + "[/magenta]")
console.print("[bold cyan] made by CLOTI (Xsarz)[/] [bold yellow]Telegram: t.me/DXsarz[/]")
def get_wifi_passwords():
	profiles_data = subprocess.check_output('netsh wlan show profiles').decode('Windows-1251').split('\n')
	profiles = [i.split(':')[1].strip() for i in profiles_data if '    ‚бҐ Їа®дЁ«Ё Ї®«м§®ў\xa0вҐ«Ґ©     ' in i]
	g = len(profiles)-1
	d = 1
	console.print("[bold green]Wi-fi сети на этом устройстве:[/]\n")
	for i in range(len(profiles)):
		console.print(f"{g}){profiles[g]}")
		g -=1
		d +=1
	while True:
		try:
			num = int(console.input("\n[bold yellow]Введите номер сети, чтобы получить информацию>> [/]"))
			if num > len(profiles):
				console.print("\n\n[bold red]Сеть под этим номером не найден![/]")
			else:
				break
		except:
			console.print("\n\n[bold red]Введите цифру![/]")

	try:
		profile_info = subprocess.check_output(f"netsh wlan show profile {profiles[num]} key=clear").decode('CP866')	
		console.print(profile_info)
		console.print('\n\n[bold cyan]Пароль от сети находится в поле "Содержимое ключа"[/]\n\n')
		name_file = f"{profiles[num]}_INFO"
		my_file = open(f"{name_file}.txt", "w+")
		my_file.write(str(profile_info))
		my_file.close()
		console.print(f'[bold green]Ифориация про эту сеть сохранена в файл [/]"{name_file}"')
	except:
		console.print("[bold red]Не удаётся получить информацию[/]")
get_wifi_passwords()
