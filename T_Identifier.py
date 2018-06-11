import pyperclip
import re
raw_suspects = pyperclip.paste()

#Find the robot
robots = {}
data = re.compile('\w+').findall('Terminator')

# Write a textfile of the suspects who are robots
f = open("Suspects.txt", "w")
f.write(suspects_robots)
f.close()

#Send robots to clipboard
pyperclip.copy(suspects_robots)