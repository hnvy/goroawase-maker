# Goroawase is a Japanese mnemonic system used to memorise numbers. You probably need to speak some Japanese in order to find this helpful. But,
# for my Japanese friends out there, here you go.
# The idea stemmed from this website: http://www2u.biglobe.ne.jp/~b-jack/bn/pken.html. However, it had few things which
# I thought could be changed to my liking:
# 1. Maximum number of digits to be entered is 11.
# 2. The way the website splits long numbers is not random.
# 3. I wanted to add my own data.
# 4. It is online. If the website owner takes the website down, we will never be able to enjoy it again.
# 
# Thankfully, the owner has made the data publicly available. I am truly grateful for that: http://www2u.biglobe.ne.jp/~b-jack/d-m.html. I wanted to
# donate, but I couldn't find my way around the website (if you figure it out, please let me know).
# 
# Last but not least, there is another nice Goroawase website: https://seoi.net/goro/.


# * Start

import re
import random
import sys
import os


# * Initialise

filename = os.path.join(sys.path[0],'CombinedData.txt')

# * This function is the one which will find the correct line in the file.
def finder():
	global chosen_number

	segmented_number = []
	match = None

	for line in lines:
		# Match the search term in the line using RegEx
		match = re.search(r'\b{}\b'.format(chosen_number), line)
		# If there is a match, print the line and stop searching
		if match:
			print(line)
			break

	if match == None:
		while len(chosen_number) > 0:
			length = random.randint(1, 4) # This will (randomly) break down your long number into smaller pieces
			segmented_number.append(chosen_number[:length])
			chosen_number = chosen_number[length:]

		number_of_segments = len(segmented_number)
		goroawase_list = segmented_number

		print(f"No match found! Here are the truncated pieces: {segmented_number}\n")

		for line in lines:
			for i in range(number_of_segments):
				match = re.search(r'\b{}\b'.format(segmented_number[i]), line)
				if match:
					goroawase_list[i] = line

		for goroawase in goroawase_list:
			print(goroawase)


# * Run, run, run, RUN!

with open(filename, 'r', encoding="utf8") as f:
	lines = f.readlines()

	if len(sys.argv) > 1:
		chosen_number = sys.argv[1]
		finder()

	else:
		print("""
	You can use the command line to enter a number for creating Goroawase:
		python goroawase_maker.py [number]

	Alternatively, you can run the program and then follow the prompt:
		python goroawase_maker.py
	""")
		while True:
			chosen_number = input("Enter number to get the Goroawase: ")
			finder()
