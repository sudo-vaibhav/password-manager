import sys
import pyperclip
import string
import random

def generate_password(length):
	return "".join([random.choice(string.ascii_letters+string.digits+string.punctuation) for _ in range(length)])
def save_dict_to_file(dic):
    f = open('passwords_file.txt','w')
    f.write(str(dic))
    f.close()

def load_dict_from_file():
    f = open('passwords_file.txt','r')
    data=f.read()
    f.close()
    return eval(data)

print("you just ran "+sys.argv[0]+" file in python3")

try:
	passwords=load_dict_from_file()
	print("passwords file loaded successfully")
except:
	passwords={}
	print("new passwords file had to be created")

if len(sys.argv)!=2:
	print("arguements not supplied properly, try again!!")
	sys.exit()
else:
	arguement=sys.argv[1]
	if arguement=="new" or arguement=="edit":
		key=input("enter service name: ").strip().lower()
		suggestion=input("Would you like a strong password suggestion? [y/n] : ")
		if suggestion=="y":
			length=int(input("Enter the length of password you want: "))
			password=generate_password(length)
			print("new password is {}".format(password))
			suggestion=input("would you like to use this as new password for {} ?[y/n]".format(key))
			if suggestion=='y':
				passwords[key]=password
				pyperclip.copy(password)
				print("new password has been saved and copied to clipboard")
				save_dict_to_file(passwords)
			else:
				password=input("enter password: ")
				passwords[key]=password
				pyperclip.copy(password)
				print("new password has been saved and copied to clipboard")
				save_dict_to_file(passwords)
		else:
			password=input("enter password: ")
			pyperclip.copy(password)
			passwords[key]=password
			print("new password has been saved and copied to clipboard")
			save_dict_to_file(passwords)
	elif arguement=="delete":
		key=input("enter the name of service whose password has to be deleted: ")
		if key in passwords.keys():
			del passwords[key]
			save_dict_to_file(passwords)
			print("password for {} deleted successfully".format(key))
		else:
			print("no such service found... please try again")
			sys.exit()
	elif arguement=="all":
		if passwords=={}:
			print("no passwords saved as of now!")
		else:
			print(*passwords.keys(),sep="\n")
	else:
		if arguement in passwords.keys():
			pyperclip.copy(passwords[arguement])
			print("password for {} copied to clipboard successfully".format(arguement))
		else:
			print("password for {} service not available... please try again".format(arguement))
			sys.exit()


