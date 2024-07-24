import paramiko

# przesyłanie pliku na serwer
transport = paramiko.Transport('example.com, 22')
transport.connect(username='username', password='password')
sftp = paramiko.SFTPClient.from_transport(transport)

local_path = 'C:\\Users\\'
remote_path = ''
sftp.put(local_path + '', remote_path)

sftp.close()
transport.close()


# pobieranie pliku z serwera
# Tworzenie obiektu Transport
transport = paramiko.Transport(('example.com', 22))

# Łączenie się z serwerem
transport.connect(username='your_username', password='your_password')

# Tworzenie obiektu SFTP
sftp = paramiko.SFTPClient.from_transport(transport)

# Pobieranie pliku z serwera
remote_path = '/path/to/remote/file.txt'
local_path = '/path/to/local/file.txt'
sftp.get(remote_path, local_path)

# Zamykanie połączenia SFTP
sftp.close()

# Zamykanie transportu
transport.close()


# przesyłanie plików za pomocą SCP
from paramiko import SSHClient
from scp import SCPClient

# Tworzenie obiektu SSHClient
ssh = SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='example.com', username='your_username', password='your_password')

# Tworzenie obiektu SCPClient
scp = SCPClient(ssh.get_transport())

# Przesyłanie pliku
scp.put('/path/to/local/file.txt', '/path/to/remote/file.txt')

# Pobieranie pliku
scp.get('/path/to/remote/file.txt', '/path/to/local/file.txt')

# Zamykanie połączenia SCP
scp.close()
