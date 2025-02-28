# SSHealth
 SecureCRT Session Health Checker

This script will iterate through your SecureCRT sessions, test SSH to each session, and output results to a .csv file. Helpful to identify sessions where SSH or authentication is not working.

### SecureCRT Session Folder
You must update the ```dir_path``` variable to your SecureCRT Sessions folder. This can be found in SecureCRT by going to the Options Menu and then Global Options. Under General there is Configuration Paths that will show your Configuration Folder, just add the Sessions folder to the path name.


### Requirements
Tested on Python 3.13.2, SecureCRT 9.6.1
Requires netmiko installed via pip