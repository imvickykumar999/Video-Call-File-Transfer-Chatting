import socket
import os, tqdm
import shutil

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 1024 * 4 #4KB

def send_file(filename, host, port):
    filesize = os.path.getsize(filename)
    s = socket.socket()
    print(f"[+] Connecting to {host}:{port}")
    s.connect((host, port))
    print("[+] Connected.")

    s.send(f"{filename}{SEPARATOR}{filesize}".encode())
    progress = tqdm.tqdm(range(filesize), f"Sending {filename}",
    unit="B", unit_scale=True, unit_divisor=1024)

    with open(filename, "rb") as f:
        for _ in progress:
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                break
            s.sendall(bytes_read)
    s.close()

if __name__ == "__main__":

    hostip = input('\nEnter Host IP : ')
    print("\n...to send multiple files, keep all in folder, create it's zip file")
    file = input("\nPaste ...file, folder, or zipped file's path : ")

    if os.path.isdir(file):
        shutil.make_archive(file, 'zip', file)

        file += '.zip'
        send_file(file, hostip, 5001)
        os.remove(file)

    else:
        send_file(file, hostip, 5001)
