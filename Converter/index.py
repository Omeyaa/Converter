import base64
import hashlib
import os
import time


def main():
	while True:
		en = """
|-------------------------------------|
|           ENCRYPT TEXT              |
|-------------------------------------|
		"""
		de = """
|-------------------------------------|
|           DECRYPT TEXT              |
|-------------------------------------|
		"""
		banner = """        	      ,____
                      |---.\\
              ___     |    `         Omeyaa
             / .-\  ./=)
            |  |"|_/\/|
            ;  |-;| /_|         REAP THE REWARDS
           / \_| |/ \ |
          /      \/\( |         Author : Romeo
          |   /  |` ) |         Description : Converter
          /   \ _/    |         Grettings : Python Developer
         /--._/  \    |
         `/|)    |    /
           /     |   |
         .'      |   |
        /         \  |
       (_.-.__.__./  /

			"""
		a = ['Base64','Base16','Base32','ASCII85','Hexadecimal','Binary']
		n = 1
		print(banner)
		for i in a:
			time.sleep(0.5)
			print(" [{}] {} Encoder".format(int(n),i))
			n+=1
		a = """\n [1] Encode
 [2] Decode
 [3] Back
 """
		choice = int(input("\n Enter your choice : "))
		if choice == 1:
			os.system('cls')
			while True:
				print(banner)
				print(a)
				c = int(input("\n Enter Number : "))
				if c == 1:
					while True:
						os.system('cls')
						print(banner)
						print(en)
						q1 = input("\n Type String to Encode into Base64 : ")
						q1 = q1.encode('UTF-8')
						q1 = base64.b64encode(q1)
						print(" Encode : "+str(q1))
						input(" Press Enter to Continue...")
						os.system('cls')
						break
					continue
				elif c ==2:
					while True:
						os.system("cls")
						print(banner)
						print(de)
						q1 = input("\n Type Base64 to Decode into String : ")
						q1 = q1.encode('UTF-8')
						q1 = base64.b64decode(q1)
						print(" Decode : "+str(q1))
						input(" Press Enter to Continue...")
						os.system('cls')
						break
					continue
				elif c == 3:
					os.system('cls')
					break
				else:
					print(banner)
					print("\n Invalid Number")
				continue

		elif choice == 2:
			while True:
				os.system('cls')
				print(banner)				
				print(a)
				c = int(input("\n Enter Number : "))
				if c == 1:
					while True:
						os.system('cls')
						print(banner)
						print(en)
						q1 = input("\n Type String to Encode into Base16 : ")
						q1 = q1.encode('utf-8')
						q1 = base64.b16encode(q1)
						print(" Encode : {}".format(q1))
						input(" Press Enter to Continue...")
						break
					continue				
				elif c == 2:
					while True:
						os.system('cls')
						print(banner)
						print(de)
						q1 = input("\n Type Base32 to Decode into String : ")
						q1 = q1.encode('UTF-8')
						q1 = base64.b16decode(q1)
						print(" Decode : {}".format(q1))
						input(" Press Enter to Continue...")
						break
					continue
				elif c == 3:
					os.system('cls')
					break
				else:
					os.system('cls')
					print(banner)
					print("\n Invalid Number")
				continue

		elif choice == 3:
			while True:
				os.system('cls')
				print(banner)
				print(a)
				c = int(input("\n Enter Number : "))
				if c == 1:
					while True:
						os.system('cls')
						print(banner)
						print(en)
						q1 = input("\n Type String to Encode into Base32 : ")
						q1 = q1.encode('utf-8')
						q1 = base64.b32encode(q1)
						print(" Encode : {}".format(q1))
						input("Press Enter to continue...")
						break
					continue
				elif c == 2:
					while True:
						os.system('cls')
						print(banner)
						print(de)
						q1 = input(" Type Base32 to Decode into String : ")
						q1 = q1.encode('utf-8')
						q1 = base64.b32decode(q1)
						print(" Decode : {}".format(q1))
						input(" Press Enter to continue...")
						break
					continue
				elif c == 3:
					os.system('cls')
					break
				else:
					os.system('cls')
					print("\n Invalid Number")
				continue
		elif choice == 4:
			while True:
				os.system('cls')
				print(banner)
				print(a)
				c = int(input("\n Enter Number : "))
				if c == 1:
					while True:
						os.system('cls')
						print(banner)
						print(en)
						q1 = input(" Type String to Encode into ASCII85 : ")
						q1 = q1.encode('UTF-8')
						q1 = base64.a85encode(q1)
						print(" Encode : {}".format(q1))
						input(" Press Enter to Continue...")
						break
					continue
				elif c == 2:
					while True:
						os.system('cls')
						print(banner)
						print(de)
						q1 = input(" Type ASCII85 to Decode into String : ")
						q1 = q1.encode('UTF-8')
						q1 = base64.a85decode(q1)
						print(" Decode : {}".format(q1))
						input(" Press Enter to continue...")
						break
					continue
				elif c == 3:
					os.system('cls')
					break
				else:
					print(" Invalid Number") 
				continue

		elif choice == 5:
			while True:
				os.system('cls')
				print(banner)
				print(a)
				c = int(input(" Enter Number : "))
				if c == 1:
					while True:
						os.system('cls')
						print(banner)
						print(en)
						q1 = input(" Type String to Encode into Hexadecimal : ")
						print(" Encode :",end=" ")
						for i in q1:
							print(hex(ord(i)),end=" ")						
						input("\n Press Enter to continue...")
						break
					continue
				elif c == 2:
					while True:
						os.system('cls')
						print(banner)
						print(de)
						q1 = input(" Type Hexadecimal to Decode into String : ").split()
						print(" Decode :",end=" ")
						for i in q1:
							print(chr(int(i,16)),end="")
						input("\n Press Enter to continue...")
						break
					continue
				elif c == 3:
					os.system('cls')
					break
				else:
					print(" Invalid Number")

		elif choice == 6:
			while True:
				os.system('cls')
				print(banner)
				print(a)
				c = int(input(" Enter Number : "))
				if c == 1:
					while True:
						os.system('cls')
						print(banner)
						print(en)
						q1 = input(" Enter String to convert into Binary : ")
						print(" Encode :",end=" ")
						for i in q1:
							print(bin(ord(i)),end=" ")
						input("\n Press Enter to continue...")
						break
					continue
				elif c == 2:
					while True:
						os.system('cls')
						print(banner)
						print(de)
						q1 = input(" Enter Binary to convert into String : ").split()
						print(" Decode : ",end="")
						for i in q1:
							print(chr(int(i,2)),end="")
						input("\n Press Enter to continue...")
						break
					continue
				elif c == 3:
					os.system('cls')
					break
				else:
					print(" Invalid Number")
				continue

if __name__ == '__main__':
	main()