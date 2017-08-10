#!/usr/bin/python 
import os
from shutil import copyfile

altran_ssh_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDpHoRgkmKvLbkZV/1w5hWhtIF0yk4rVuy8d4d3B++Frz9eUKvEgXv9H1D5ZllS4OOA1S1TsmGBfUtL7vXPgfZHXlteI3XnU/V6kb8YvHFvuQ6PZAuo2yZp+mqWyBy0vANAbBLMZ6kY0JbyvaqejFIU5MxaTITdNXj7nMF31o5Qg0IgAQwzJz/01aDXuon5vgfRIKZaMJjh9cuBjpiln8rrLZBrWLorFt5b3bmjfiLxf7BwQTvGDDzso8opAD/coTwISIp6BfbmgRHnyJ3bQcuyey4+g87uy7pMISn1k8nTT9M34WjNPuB7ud/MVQWtkm6URw7FiZJgp1B+JQfa1JOF jvalderrama@jvalderrama"

def create_ssh_key():
	if altran_ssh_key not in open('/home/vagrant/.ssh/authorized_keys').read():
		with open("/home/vagrant/.ssh/authorized_keys", "a") as auth_file:
			auth_file.write(altran_ssh_key)

def create_root_ssh_key_and_let_root_access():
#	os.system("cat /dev/zero | ssh-keygen -q -N ")
	try:
		os.mkdir("/root/.ssh", 0755)
	except:
		print "File exists"
	copyfile("/home/vagrant/.ssh/authorized_keys","/root/.ssh/authorized_keys")




#resolve_by_hostname()
create_ssh_key()
create_root_ssh_key_and_let_root_access()
#install_httplib2()

