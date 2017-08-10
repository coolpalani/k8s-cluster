#!/usr/bin/python 
import os
from shutil import copyfile

altran_ssh_key = "put-you-id_rsa-key here"

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

