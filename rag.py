import sys
import os
from adventure import *

os.system("cls")
quests = []
answers = []
for task in tasks:
	quests.append(task[0])
	answers.append(task[1])

cur = -1
max = len(quests)

if len(quests) != len(answers):
	raise ValueError("Quests and answers must match!")

while cur < max:
	if cur == -1:
		#os.system('cls')
		print start
		raw_input("ENTER'a bas!")
		cur = cur + 1
	elif cur == -2:
		print defeat
		cur = -1
		raw_input("")
	else:
		print quests[cur]
		answer = raw_input("Yanit:")
		if answer == answers[cur]:
			cur = cur + 1
		elif answer.isspace() or answer == "":
			continue
		else:
			cur = -2

print end