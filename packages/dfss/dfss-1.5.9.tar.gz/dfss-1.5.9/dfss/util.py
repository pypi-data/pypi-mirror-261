import paramiko
from progressbar import ProgressBar, Percentage, Bar, FileTransferSpeed, ETA
import socket
import time
from datetime import datetime
import stat
import base64
import os
import io
import sys
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed

output_buffer = io.StringIO()
error_buffer = io.StringIO()

def lock_output(lock):
    if lock is True:
        sys.stdout = output_buffer
        sys.stderr = error_buffer
    else:
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__

def lock_output_clear():
    output_buffer.truncate(0)
    error_buffer.truncate(0)

def test_ping(host, port):
    try:
        start_time = time.time()
        with socket.create_connection((host, port), timeout=3) as connection:
            pass
        end_time = time.time()
        rtt = (end_time - start_time) * 1000
        return rtt
    except Exception as e:
        print("Error: ", str(e))
        return -1

def speed_sftp(host, port, username, password, timeout = 0.5):
    transport = paramiko.Transport((host, port))
    download_data_ok = 0
    file_content = io.BytesIO()
    lock_output(True)
    def sftpget(x, y):
        lock_output(True)
        try:
            sftp.getfo(x, y)
        except Exception as e:
            pass
    try:
        transport.connect(username=username, password=password)
        sftp = paramiko.SFTPClient.from_transport(transport)
        th = threading.Thread(target=sftpget, args=(".speed", file_content))
        th.start()
        th.join(timeout)
        sftp.close()
        transport.close()
        download_data_ok = 1
    except Exception as e:
        print('Error: ', e)
    finally:
        try:
            transport.close()
        except Exception as e:
            print('Error: ', e)
    lock_output(False)
    lock_output_clear()
    data_size = file_content.getbuffer().nbytes
    return data_size if download_data_ok == 1 else 0

def is_remote_directory(remote_path, sftp):
    try:
        remote_attributes = sftp.stat(remote_path)
        return stat.S_ISDIR(remote_attributes.st_mode)
    except Exception as e:
        print('Failed to determine directory:', str(e))
        return False


def is_remote_reg(remote_path, sftp):
    try:
        remote_attributes = sftp.stat(remote_path)
        return stat.S_ISREG(remote_attributes.st_mode)
    except Exception as e:
        print('Failed to determine reg file:', str(e))
        return False

def is_sftp_supported(index, server):
    host, port, user, passwd, _ = server
    is_sftp = True
    if test_ping(host, port) == -1:
        return (index, False)
    transport = paramiko.Transport((host, port))
    try:
        transport.connect(username=user, password=passwd)
        sftp = paramiko.SFTPClient.from_transport(transport)
        if is_remote_reg('.sophgo', sftp) is False:
            is_sftp = False
        sftp.close()
        transport.close()
    except Exception as e:
        is_sftp = False
    finally:
        try:
            transport.close()
        except Exception as e:
            pass
    return (index, is_sftp)


def format_file_size(file_size_bytes):
    if file_size_bytes < 1024:
        return "{} B".format(file_size_bytes)
    elif file_size_bytes < 1024 ** 2:
        return "{:.2f} KB".format(file_size_bytes / 1024)
    elif file_size_bytes < 1024 ** 3:
        return "{:.2f} MB".format(file_size_bytes / (1024 ** 2))
    elif file_size_bytes < 1024 ** 4:
        return "{:.2f} GB".format(file_size_bytes / (1024 ** 3))
    else:
        return "{:.2f} TB".format(file_size_bytes / (1024 ** 4))

def get_server_info(username):
    server_info = {'hostname':None,'port':None,'username':None,'password':None}
    if username.startswith('sophgo'):
        # HDK account
        server_info['hostname'] = "219.142.246.77"
        server_info['port'] = 18822
        server_info['username'] = username
    else:
        # SDK account
        server_list = [
            ("172.26.175.10", 32022, 'oponIn', 'oponIn', 0),
            ("172.26.13.58", 12022, 'oponIn', 'oponIn', 0),
            ("172.26.166.66", 22022, 'oponIn', 'oponIn', 0),
            ("106.37.111.20", 32022, 'open', 'open', 0),
        ]
        async_res = 0
        lock_output(True)
        with ThreadPoolExecutor(max_workers=10) as t:
            async_res = [t.submit(is_sftp_supported, index, server) for index, server in enumerate(server_list)]
        lock_output(False)
        lock_output_clear()
        for future in as_completed(async_res):
            (index, is_sftp) = future.result()
            if is_sftp is True:
                ip, port_to_check, user, passwd, _ = server_list[index]
                speed = speed_sftp(ip, port_to_check, user, passwd)
                print("connection scheme {} speed: {} B".format(index, speed))
                server_list[index] = (ip, port_to_check, user, passwd, speed)
        sorted_server_list = sorted(server_list, key=lambda x: x[-1], reverse = True)
        host, port, user, passwd, speed = sorted_server_list[0]
        if speed != 0:
            server_info['hostname'] = host
            server_info['port'] = port
            server_info['username'] = user
            server_info['password'] = passwd
    if server_info['hostname'] is not None:
        print('using ip: ', server_info['hostname'])
    return server_info

def download_file_from_sophon_sftp(remote_path, local_path):
    server_info = get_server_info('open')
    
    if server_info['hostname'] is None or server_info['port'] is None \
        or server_info['username'] is None or server_info['password'] is None:
        print("No available servers found.")
        return False
    try:
        transport = paramiko.Transport((server_info['hostname'], server_info['port']))
        transport.connect(username=server_info['username'], password=server_info['password'])
        sftp = paramiko.SFTPClient.from_transport(transport)

        if is_remote_directory(remote_path, sftp) is True:
            print("cannot find aim")
            return False
        local_path = os.path.normpath(local_path)
        local_item = os.path.basename(remote_path)
        if os.path.isdir(local_path) is True:
            local_path = os.path.join(local_path, local_item)
        directory = os.path.dirname(local_path)
        if os.path.isdir(directory) is False:
            os.makedirs(directory)
        remote_file_size = sftp.stat(remote_path).st_size
        print('download file from', remote_path, '->', local_path, ', size:',
              format_file_size(remote_file_size), '...')
        widgets = [ETA(), ' | ', Percentage(), Bar(), FileTransferSpeed()]
        pbar = ProgressBar(widgets=widgets, maxval=remote_file_size).start()

        def progress_callback(x, y):
            pbar.update(x)
        sftp.get(remote_path, local_path, callback=progress_callback)
        pbar.finish()
        sftp.close()
        transport.close()
        return True
    except Exception as e:
        print('An error occurred in get file:', str(e))
        return False


def upload_file_to_sophon_sftp(remote_path, local_path):
    server_info = get_server_info('open')
    server_info['username'] = 'customerUploadAccount'
    server_info['password'] = '1QQHJONFflnI2BLsxUvA'

    if server_info['hostname'] is None or server_info['port'] is None or server_info['username'] is None or server_info['password'] is None:
        print("No available servers found.")
        return False
    try:
        transport = paramiko.Transport((server_info['hostname'], server_info['port']))
        transport.connect(username=server_info['username'], password=server_info['password'])
        sftp = paramiko.SFTPClient.from_transport(transport)
        local_path = os.path.normpath(local_path)
        if not os.path.isfile(local_path):
            print(local_path, 'is not a file.')
            exit(-1)
        remote_file_size = os.path.getsize(local_path)
        print('up file from', local_path, '-> open@sophgo.com:', remote_path, 'size:',
              format_file_size(remote_file_size), '...')
        widgets = [ETA(), ' | ', Percentage(), Bar(), FileTransferSpeed()]
        pbar = ProgressBar(widgets=widgets, maxval=remote_file_size).start()

        def progress_callback(x, y):
            pbar.update(x)
        decoded_bytes = base64.b64decode(remote_path)
        decoded_string = decoded_bytes.decode('utf-8')
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        remote_path = os.path.join(
            decoded_string, current_time + '_' + os.path.basename(local_path))
        sftp.put(local_path, remote_path,
                 callback=progress_callback, confirm=False)
        pbar.finish()
        sftp.close()
        transport.close()
        return True
    except Exception as e:
        print('An error occurred in up file:', str(e))
        return False

def sftp_login(username):
    print('Login sftp server by user: ', username)
    server_info = get_server_info(username)
    cmdstr = 'sftp -P '+ str(server_info['port'])+' '+ username +'@'+server_info['hostname']
    print('You can use this IP[{}] and port[{}] to login to the server through the SFTP client to download files.'.format(server_info['hostname'], server_info['port']))
    print('Currently trying to login using the sftp tool in the system ...')
    os.system(cmdstr)
    return True
