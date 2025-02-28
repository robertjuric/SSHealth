import csv
from pathlib import Path
from netmiko.exceptions import NetMikoTimeoutException
from netmiko.exceptions import AuthenticationException
from netmiko.exceptions import SSHException
from netmiko import ConnectHandler

# SecureCRT Session Directory
# For windows use forward slashes in path
dir_path = "C:/Users/robert.juric/DropBox/SecureCRT/Sessions"

# Authentication Options
# 
# Script Stored Credentials
# To use stored credentials in the script, uncomment the following section, and comment the encryption section
#ssh_user = "dummy"
#ssh_pass = "notagoodidea"
#
# Encrypted Credentials


def read_sessions(sdir):
	return_dict = dict()
	pathlist = Path(sdir).rglob('*.ini')
	for path in pathlist:
	    path_in_str = str(path)
	    if not '__' in path_in_str and not 'Default' in path_in_str:
	    	stringlist = path_in_str.split("\\")
	    	file_name = stringlist[-1]
	    	filelist = file_name.split(".")
	    	session_name = filelist[0]
	    	try:
	    		with open(path_in_str, 'r') as file:
	    			for line in file:
	    				if 'S:"Hostname"' in line:
	    					linelist = line.split("=")
	    					host_name = linelist[-1].strip('\n')
	    					return_dict.update({session_name: host_name})
	    	except:
	    		print("Not found")
	return(return_dict)

sessions = read_sessions(dir_path)
filename = 'results.csv'
for session, hostname in sessions.items():
	print(f"Testing:  {hostname}")
	device = {
		"device_type": "cisco_ios",
		"host":hostname,
		"username":ssh_user,
		"password":ssh_pass,
	}
	try:
		net_connect = ConnectHandler(**device)
		net_connect.disconnect()
		with open(filename, 'a', newline='') as file:
			writer = csv.writer(file)
			writer.writerow([session, hostname, "Success"])
	except AuthenticationException:
		with open(filename, 'a', newline='') as file:
			writer = csv.writer(file)
			writer.writerow([session, hostname, "Authentication Failed"])
	except NetMikoTimeoutException:
		with open(filename, 'a', newline='') as file:
			writer = csv.writer(file)
			writer.writerow([session, hostname, "SSH Timed Out"])
	except SSHException as e:
		with open(filename, 'a', newline='') as file:
			writer = csv.writer(file)
			writer.writerow([session, hostname, "SSH Exception"])
	except EOFError:
		with open(filename, 'a', newline='') as file:
			writer = csv.writer(file)
			writer.writerow([session, hostname, "EOF Error"])
	except Exception as e:
		with open(filename, 'a', newline='') as file:
			writer = csv.writer(file)
			writer.writerow([session, hostname, "General Exception"])
