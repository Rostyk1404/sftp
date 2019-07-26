For creating messenger which using access an SFTP server I used Release 0.2.9 PySftp. 
If you would like to use the same library you have to do several 
things. You have to install PySftp you can do it with this command:

$ python -m pip install pysftp # type it in prompt or Pycharm terminal

For more information, you may check this link: 
https://buildmedia.readthedocs.org/media/pdf/pysftp/latest/pysftp.pdf

After you installed Pysftp you must import that module. You must write just: 
import pysftp then you have to: input hostname, username and password. 
After that, your personal information will be saved in MongoDB.

Then you must create a connection for that operation you can use context manager 
and it will look at this: 
with pysftp.Connection(host=hostname, username=username, password=password) as sftp:

Then I wrote While True, is a while loop that will loop forever as the evaluated condition is always met, 
always True.

You can use some commands to navigate and get some information: 
"pwd" - will show you in which directory you are in; 
"ls" - will show you what files are in the directory you are in; 
"cd" - use this command to go to a directory; 
"cd.." - to go back from a folder to the folder; 
"copy" - to copy files through the command line; 
"exit" - closes the connection and cleans up; 
"users" - return list of all users which is in databases; 
"kill -u" - current command delete user from databases; 
"create -u" - create user with unique field hostname for example: 
    "create -u hostname, username, password" .