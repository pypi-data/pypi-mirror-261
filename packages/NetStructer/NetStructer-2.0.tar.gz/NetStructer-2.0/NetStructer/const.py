from cryptography.fernet import Fernet
from utlist import *
import requests , psutil as proc

def GenerateKey():
	'''
	Description:
		GenerateKey: generate a random key using crpytography
	Returns:
		None
	'''
	return Fernet.generate_key()
	
def PublicIp():
	'''
	Description:
		PublicIp : return the public ip of the network
	Returns:
		return the public ip of your wifi
	'''	
	try:
	
	except requests.exceptions.ConnectionError:
		raise ValueError('You are not online -__-')
	
	
def LocalIp():
	for x,y in proc.net_if_addrs().items():
		for z in y:
			if z.address.startswith('192.168'):
				return z.address
	return ''