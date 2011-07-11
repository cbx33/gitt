import subprocess
import sys

BASE="/tmp/gitcreate"

class command:
	
	command = None
	real_command = None
	date = None
	com_id = None
	output = None
	
	def __init__(self, com_id, command, date=None):
		self.set_com_id(com_id)
		self.set_command(command)
		the_command = self.command.replace("git", "git --no-pager")
		if (date!=None):
			self.set_date(date)
			the_command = the_command + ' --date="' + self.date + '"'
		self.real_command = the_command
		
	def set_com_id(self, com_id):
		self.com_id = com_id

	def set_command(self, command):
		self.command = command
	
	def set_date(self, date):
		self.date = date
		
	def set_output(self, output):
		self.output = output

a = command(1,'mkdir coderepo')
b = command(2,'mkdir coderepo', 'Thu, 07 Apr 2005 22:13:13 +0200')

print b.date

commands = [
command(1,'mkdir coderepo'),
command(2,'cd coderepo/'),
command(3,'git init'),
command(4,'touch my_first_committed_file'),
command(5,'git add my_first_committed_file'),
command(6,'git commit -m "My First Ever Commit"', date='Thu, 07 Apr 2005 22:13:13 +0200'),
command(7,'echo "Change1" > my_first_committed_file'),
command(8,'touch my_second_committed_file'),
command(9,'touch my_third_committed_file'),
command(10,'git status'),
command(11,'git add my_first_committed_file'),
command(12,'echo "Change1" > my_second_committed_file'),
command(13,'git add my_second_committed_file'),
command(14,'git status'),
command(15,'echo "Change2" >> my_second_committed_file'),
command(16,'git status'),
command(17,'git commit -m "Made a few changes to first and second files"'),
command(18,'git status'),
command(19,'git commit -a -m "Finished adding initial files"'),
command(20,'git status'),
command(21,'git add my_third_committed_file'),
command(22,'git status'),
command(23,'git reset my_third_committed_file'),
command(24,'git status'),
]

for command in commands:
	print command.com_id, command.command
	
	proc = subprocess.Popen(command.command, shell=True, cwd=BASE, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
	outer = proc.stdout.read()
	outer += proc.stderr.read()
	command.set_output = outer
	f = open("outputs/" + str(command.com_id) + ".txt", "w")
	f.write(outer)
	f.close()
	
