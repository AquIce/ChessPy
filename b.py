from colorama import Fore, Back, Style
import os
import readchar

index = 0
ok = False
while not ok:
	os.system('clear')
	ok = False

	options = [
	 f"\t{Fore.MAGENTA}1{Style.RESET_ALL}", f"\t{Fore.MAGENTA}2{Style.RESET_ALL}", f"\t{Fore.MAGENTA}3{Style.RESET_ALL}",f"\t{Fore.MAGENTA}4{Style.RESET_ALL}",f"\t{Fore.MAGENTA}5{Style.RESET_ALL}",f"\t{Fore.MAGENTA}6{Style.RESET_ALL}\n"
	]

	for i in range(len(options)):
		if i == index:
			print(f"{Back.BLUE}", end="")
		print(options[i])

	if readchar.readkey() == readchar.key.DOWN:
		index += 1
		if index == len(options):
			index = 0
	elif readchar.readkey() == readchar.key.UP:
		index -= 1
		if index == -1:
			index = len(options) - 1
	if readchar.readkey() == readchar.key.ENTER:
		ok = True
	os.system('clear')
print('end')