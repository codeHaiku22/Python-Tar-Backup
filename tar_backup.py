#!/usr/bin/python3
import datetime, os, subprocess, sys

exitCode = os.system('sh /home/dgrewal/bin/tar/mount_repo.sh')                                      #using os.system for shelling

if exitCode != 0:
    print("Unable to mount archive repo.\nExit code = ", exitCode)
    sys.exit()

drive = input("Which drive should the backup occur on [u/e]? ").strip()
drive = drive.lower()

if drive != 'u' and drive != 'e':
    quit()

today = datetime.datetime.now()
directory = '/mnt/' + drive + '/backups/tar'
archiveFile = (today.strftime("%Y%m%d")) + ".tar.gz"
path = directory + os.sep + archiveFile

make_tar = subprocess.run(["tar", "-cvzf", path, "-X", "excludes.txt", '/mnt/c/Users/dgrewal/'])    #using subprocess.run for shelling

if make_tar.returncode != 0:
    print("Unable to create archive file: " + path + "\nExit code = ", make_tar.returncode)
    sys.exit()

print("\n[ List of archive files in", directory, ": ]")
list_files = subprocess.run(["ls", "-lh", directory])                                               #using subprocess.run for shelling

if list_files.returncode != 0:
    print("Unable to list files in archive repo.\nExit code = ", list_files.returncode)
    sys.exit()

deleteYN = input("\nWould you like to delete an existing archive? [y/N]: ").strip()
deleteYN = deleteYN.lower()

if deleteYN == 'y' or deleteYN == 'yes':
    deleteFile = input("Enter the filename to be deleted: ").strip()
    path = directory + os.sep + deleteFile
    if os.path.exists(path):
        os.remove(path)
    else:
        print("That file does not exist.")
    subprocess.run(["echo", "\n", "[ List of archive files in", directory, ": ]"])
    list_files = subprocess.run(["ls", "-lh", directory])
