#### MAIN LIB ####

# -=-=-=-=-=-=-
VERSION = 'v1.1'

from colorama import init, Fore, Back, Style
import os
import sys
import requests

from lib.payload import *
init()
# -=-=-=-=-=-=-

## banner / start
def exit():
	os.system('clear')
	print(fr'''{Fore.YELLOW}
	.----------------------------.
	|                            |
	| {Fore.RESET}Thank you for using Lemon!{Fore.YELLOW} |
	|       {Fore.RESET}<3{Fore.YELLOW}                   |
	|          {Fore.RESET}-SpiceSouls{Fore.YELLOW}       |
	|                            |
	'----------------------------'

''')
	sys.exit()

def title(columns):
	width = 63
	if columns < 63:
		os.system('resize -s 40 63')
		offset = 0
	else:
		offset = columns - 63
		offset = offset // 2
	empty_offset = ' ' * offset
	os.system('clear')
	print(fr'''{Fore.GREEN}{Style.BRIGHT}
{empty_offset}▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
{empty_offset}█{Fore.YELLOW}  ___       _______  ___      ___     ______    _____  ___   {Fore.GREEN}█
{empty_offset}█{Fore.YELLOW} |"  |     /"     "||"  \    /"  |   /    " \  (\"   \|"  \  {Fore.GREEN}█
{empty_offset}█{Fore.YELLOW} ||  |    (: ______) \   \  //   |  // ____  \ |.\\   \    | {Fore.GREEN}█
{empty_offset}█{Fore.YELLOW} |:  |     \/    |   /\\  \/.    | /  /    ) :)|: \.   \\  | {Fore.GREEN}█
{empty_offset}█{Fore.YELLOW}  \  |___  // ___)_ |: \.        |(: (____/ // |.  \    \. | {Fore.GREEN}█
{empty_offset}█{Fore.YELLOW} ( \_|:  \(:      "||.  \    /:  | \        /  |    \    \ | {Fore.GREEN}█
{empty_offset}█{Fore.YELLOW}  \_______)\_______)|___|\__/|___|  \"_____/    \___|\____\) {Fore.GREEN}█
{empty_offset}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
{Style.RESET_ALL}''')

def intersection(message):
	try:
		columns, rows = os.get_terminal_size(0)
	except OSError:
		columns, rows = os.get_terminal_size(1)
	print('\n' + Style.BRIGHT + Fore.GREEN + '=' * columns + Fore.YELLOW)
	count = columns - len(message)
	count = count // 2
	print(' ' * count + message)
	print(Fore.GREEN + '=' * columns + Style.RESET_ALL)
def banner(message):
	try:
		columns, rows = os.get_terminal_size(0)
	except OSError:
		columns, rows = os.get_terminal_size(1)
	title(columns)

	intersection(message)
	print(fr'''
	      {Style.BRIGHT}{Fore.GREEN}[{Fore.YELLOW}01{Fore.GREEN}]{Style.RESET_ALL} Meterpreter Reverse TCP
	      {Style.BRIGHT}{Fore.GREEN}[{Fore.YELLOW}02{Fore.GREEN}]{Style.RESET_ALL} Meterpreter Bind TCP
              {Style.BRIGHT}{Fore.GREEN}[{Fore.YELLOW}03{Fore.GREEN}]{Style.RESET_ALL} Meterpreter Reverse HTTP
	      {Style.BRIGHT}{Fore.GREEN}[{Fore.YELLOW}04{Fore.GREEN}]{Style.RESET_ALL} Meterpreter Reverse HTTPS

	      {Style.BRIGHT}{Fore.GREEN}[{Fore.YELLOW}05{Fore.GREEN}]{Style.RESET_ALL} Bash Stager Reverse TCP
	      {Style.BRIGHT}{Fore.GREEN}[{Fore.YELLOW}06{Fore.GREEN}]{Style.RESET_ALL} Bash Stager Reverse UDP
	      {Style.BRIGHT}{Fore.GREEN}[{Fore.YELLOW}07{Fore.GREEN}]{Style.RESET_ALL} Powershell Stager Reverse TCP
              {Style.BRIGHT}{Fore.GREEN}[{Fore.YELLOW}08{Fore.GREEN}]{Style.RESET_ALL} Powershell Stager Bind TCP

	      {Style.BRIGHT}{Fore.GREEN}[{Fore.YELLOW}update{Fore.GREEN}]{Style.RESET_ALL} Check for an Update
	      {Style.BRIGHT}{Fore.GREEN}[{Fore.YELLOW}credits{Fore.GREEN}]{Style.RESET_ALL} Credits 2 The Dev
              {Style.BRIGHT}{Fore.GREEN}[{Fore.YELLOW}exit{Fore.GREEN}]{Style.RESET_ALL} Exit the script
''')
def update():
	response = requests.get("https://api.github.com/repos/spicesouls/lemon/releases/latest")
	if response.json()["name"] == VERSION:
		print(f"\nLemon {Fore.GREEN}is up to date!{Fore.RESET} ({VERSION})")
		input('Press ENTER To Continue...')
	else:
		print(f"\nLemon is {Fore.RED}NOT{Fore.RESET} up to date. (Current: {VERSION}, New: {response.json()['name']})\nDownload the Updated version at: {Style.BRIGHT}{Fore.GREEN}https://github.com/spicesouls/lemon{Style.RESET_ALL}")
		input('Press ENTER To Continue...')

def commandloop():
	while True:
		banner('MAIN MENU - SELECT AN OPTION')
		try:
			selection1 = input(f'{Style.BRIGHT}[{Fore.YELLOW}Lemon{Fore.RESET}]{Style.RESET_ALL} >> ')
		except KeyboardInterrupt:
			print(f'\nExit?\n\n{Style.BRIGHT}{Fore.YELLOW}[{Fore.GREEN}Y{Fore.YELLOW}]{Fore.RESET}/{Fore.YELLOW}[{Fore.RED}N{Fore.YELLOW}]{Style.RESET_ALL}\n ')
			exitc = input('>> ').upper()
			if exitc == 'Y':
				exit()
			else:
				break
		try:
			if selection1 == 'exit':
				exit()
			elif selection1 == 'update':
				update()
				break
			elif selection1 == 'credits':
				os.system('clear')
				print(fr'''
    {Style.BRIGHT}{Fore.RED}DEV {Fore.RESET}---{Fore.YELLOW} SPICESOULS
{Fore.BLUE}
beyondrootsec.wordpress.com
spicesouls.github.io
{Fore.GREEN}
SpiceSouls#2629
@SpicySoulsV
{Style.RESET_ALL}''')
				input('Press ENTER To Continue...')
				break
			poptions = {
	"1":"windowsARCHmeterpreter_reverse_tcp",
	"2":"windowsARCHmeterpreter_bind_tcp",
	"3":"windowsARCHmeterpreter_reverse_http",
	"4":"windowsARCHmeterpreter_reverse_https",
	"5":"cmd/unix/reverse_bash",
	"6":"cmd/unix/reverse_bash_udp",
	"7":"cmd/windows/powershell_reverse_tcp",
	"8":"cmd/windows/powershell_bind_tcp"
}
			try:
				msf_payload = poptions[str(selection1)]
			except KeyError:
				break
			intersection(f"PAYLOAD OPTIONS - {msf_payload.replace('ARCH', '/')}")
			workingpayload = payloadoptions(msf_payload)
			intersection(f"PAYLOAD GENERATION - {msf_payload.replace('ARCH', '/')}")
			workingpayload.generate()
			msfchoice = input(f'\nWould you like to get the MSF Console ready to handle connections? {Style.BRIGHT}[{Fore.GREEN}Y{Fore.RESET}]/[{Fore.RED}N{Fore.RESET}]{Style.RESET_ALL}\n>> ').upper()
			if msfchoice == 'Y':
				rfilepath = generateresource(workingpayload)
				os.system(f'msfconsole -r {rfilepath}')
		except KeyboardInterrupt:
			pass
		except ValueError:
			pass
