import getpass

blue= '\33[94m'
lightblue = '\033[94m'
red = '\033[91m'
white = '\33[97m'
yellow = '\33[93m'
green = '\033[32m'
cyan  = "\033[96m"
end = '\033[0m'


#HEADER

print(green+"""\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n<<<<★★★★>>>> Hello, Guys! I am Sanaur Rahman Asif. Welcome To \'\'Root Of Cyber\'\' All in One Tool. If you want to use our Tools, You have to SignUp or Login in our tool<<<★★★★>>>                                 \n\n\n\n\n\n\n\n\n\n\n\n""")

#MAIN
#WHILE_INT
optcount=1
passcountn=1

#USER
while optcount<2:
	print(cyan+"""==» Select (1) if you want to SignUp and select (2) to Login from below.\n"""+red+"""Note: YOU WILL NIT BE ABLE TO OPEN 2 ACCOUNTS."""+yellow+"""\n\n\n  1)SignUp \n  2)Login"""+end)
	try:
		opt=int(input(blue+"\nSelect Your Option: "+yellow))
		if opt==1:
			unamen=str(input(blue+"\nEnter Your Name: "+yellow))
			while passcountn<2:
				passn=str(input(blue+"\nEnter a Password: "+yellow))
				passnc=str(input(blue+"\nEnter the Password Again: "+yellow))
				if passn==passnc:
					passcountn=2
				else:
					print(red+"\nPassword does not Matched. Try Again!"+end)
					passcountn-=1
			print(green+"\n\t★★★REGISTRATION COMPLETED!★★★   "+yellow+"\n\nNow select (2) from below to Login to your account: \n")
		elif opt==2:
			print(red+"\n\n\t\t   Server Upgrading...."+end)
			optcount=2
	except:
			print(red+"\nYou Have Entered a Wrong value. Please Enter 1 or 2 only. Try Again!\n"+end)
			optcount-=1
