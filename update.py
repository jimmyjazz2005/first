import os
def main():
	os.system('sudo apt-get update')
	os.system('sudo apt-get upgrade -y')
	os.system('sudo apt-get dist-upgrade -y')

if __name__ == "__main__":
	main()
