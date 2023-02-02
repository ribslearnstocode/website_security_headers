import requests


def scan_xxss(website):
		target=website
		response = requests.get(website)
		"""config failure if X-XSS-Protection header is not present"""
		global list
		list=[  ]
		server=response.headers["Server"]
		list.append("Server is: {}".format(server))
		try:
			if response.headers["X-XSS-Protection"]:
				list.append("[+] X-XSS-Protection : pass")
		except KeyError:
			list.append("[-] X-XSS-Protection header not present : fail!")
			 
		
		
		try:
			if response.headers["X-Content-Type-Options"].lower() == "nosniff":
				list.append("[+] X-Content-Type-Options : pass")
			else:
				list.append("[-] X-Content-Type-Options header not set correctly :fail!")
		except KeyError:
			list.append("[-] X-Content-Type-Options header not present :fail!")	


		try:
			if "deny" in response.headers["X-Frame-Options"].lower():
				list.append("[+] X-Frame-Options :pass")
			elif "sameorigin" in response.headers["X-Frame-Options"].lower():
				list.append("[+] X-Frame-Options :pass")
			else:
				list.append("[-] X-Frame-Options header not set correctly :fail!")
		except KeyError:
			list.append("[-] X-Frame-Options header not present :fail!")


		try:
			if response.headers["Strict-Transport-Security"]:
				list.append("[+] Strict-Transport-Security, :pass")
		except KeyError:
			list.append("[-] Strict-Transport-Security header not present :fail!")
			
		try:
			if response.headers["Content-Security-Policy"]:
				list.append("[+] Content-Security-Policy :pass")
		except KeyError:
			list.append("[-] Content-Security-Policy header not present :fail!")
		
		return list

def run_program(url):
	global security_headers
	security_headers=url
	return scan_xxss(security_headers)
