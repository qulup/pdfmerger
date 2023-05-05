import PyPDF2
import sys
import os
from colorama import Fore, Back, Style
import getpass

print()
print(Fore.BLUE)
print(' ______ _____   _______   ______                               ')
print('(_____ (____ \ (_______) |  ___ \                              ')
print(' _____) )   \ \ _____ ___| | _ | | ____  ____ ____  ____  ____ ')
print('|  ____/ |   | |  ___|___) || || |/ _  )/ ___) _  |/ _  )/ ___)')
print('| |    | |__/ /| |       | || || ( (/ /| |  ( ( | ( (/ /| |    ')
print('|_|    |_____/ |_|       |_||_||_|\____)_|   \_|| |\____)_|    ')
print('                                            (_____|            ' + Style.RESET_ALL)
print()

print('Hello ' + getpass.getuser() + '!')

merger = PyPDF2.PdfMerger()
desktop_path = '/Users/' + getpass.getuser() + '/Desktop/'
if not os.path.exists(desktop_path + '/MergeMe/'):
	os.mkdir(desktop_path + '/MergeMe/')
	print(Fore.RED)
	print('Please add all the PDFs you want to merge into the MergeMe folder on your Desktop.')
	input(Style.DIM + 'Press ENTER when you are ready ...' + Style.RESET_ALL)
thisdir = "/Users/oliver/Desktop/MergeMe/"
print()
print(Style.DIM + "Merging in alphabetical order ..." + Style.RESET_ALL)
print("")

for file in sorted(os.listdir(desktop_path + '/MergeMe/')):
	if file.endswith(".pdf"):
		print("-> ", file)
		merger.append(thisdir + file)

os.mkdir(desktop_path + '/MergeMe/Result')
merger.write(desktop_path + '/MergeMe/Result/Merged.pdf')
print(Fore.GREEN + "________________________________")
print("***** SUCCESSFULLY MERGED! *****")
print("––––––––––––––––––––––––––––––––")
print(Style.RESET_ALL + "Merged PDF: \n" + desktop_path + '/MergeMe/Result/Merged.pdf')
print()
