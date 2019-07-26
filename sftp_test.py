import pysftp
from mongo_db.template import Templates


def sign_in():
    """
        Current function creating connection to SFTP server and inserting data into MongoDB
        Sample of connection :
        hostname = "yourhostname" # "192.168.0.110"
        username = "username" # the name of yours laptop, PC or virtual machine
        password = "password" # password of yours laptop, PC or virtual machine
    """
    hostname = input('input your hostname:')
    username = input('username:')
    password = input("password:")

    if hostname and username and password:
        Templates.creating_unique_field()
        Templates.create(hostname, username, password)

    with pysftp.Connection(host=hostname, username=username, password=password) as sftp:
        while True:
            stdin = input(f'{sftp.pwd}:')
            if stdin == 'pwd':
                print(sftp.pwd)
            elif stdin == 'ls':
                print(sftp.listdir(sftp.pwd))
            elif 'cd' in stdin:
                sftp.chdir(stdin.split()[1])
            elif 'cd ..' in stdin:
                sftp.cd()
            elif 'copy' in stdin:
                sftp.get(stdin.split()[1], preserve_mtime=True)
            elif stdin == 'exit':
                sftp.close()
            elif stdin == 'users':
                user_name = list(user.get('username') for user in Templates.get_all())
                host_name = list(host.get('hostname') for host in Templates.get_all())
                for el in list(zip(user_name, host_name)):
                    print(f'{el[0]}@{el[1]}')
            elif 'kill -u' in stdin:

                Templates.delete_user(stdin.split()[-1])
            elif 'create -u' in stdin:

                Templates.create(stdin.split()[2], stdin.split()[3], stdin.split()[4])
                Templates.creating_unique_field()


if __name__ == '__main__':
    print(sign_in())
