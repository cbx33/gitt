import subprocess

BASE="/tmp/gitcreate"

commands = [
{'1':'mkdir coderepo'},
{'2':'cd coderepo/'},
{'3':'git init'},
{'4':'touch my_first_committed_file'},
{'5':'git add my_first_committed_file'},
{'6':'git commit -m "My First Ever Commit"'},
{'7':'echo "Change1" > my_first_committed_file'},
{'8':'touch my_second_committed_file'},
{'9':'touch my_third_committed_file'},
{'10':'git status'},
{'11':'git add my_first_committed_file'},
{'12':'echo "Change1" > my_second_committed_file'},
{'13':'git add my_second_committed_file'},
{'14':'git status'},
{'15':'echo "Change2" >> my_second_committed_file'},
{'16':'git status'},
{'17':'git commit -m "Made a few changes to first and second files"'},
{'18':'git status'},
{'19':'git commit -a -m "Finished adding initial files"'},
{'20':'git status'},
{'21':'git add my_third_committed_file'},
{'22':'git status'},
{'23':'git reset my_third_committed_file'},
{'24':'git status'},
]

for command in commands:
	print command.keys()[0], command[command.keys()[0]]
	the_command = command[command.keys()[0]].replace("git", "git --nopager")
	proc = subprocess.Popen(command[command.keys()[0]], shell=True, cwd=BASE, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
	outer = proc.stdout.read()
	outer += proc.stderr.read()
	f = open("outputs/" + command.keys()[0] + ".txt", "w")
	f.write(outer)
	f.close()
	
