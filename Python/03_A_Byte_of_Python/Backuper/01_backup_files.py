''' Backup files

This program backup files from list to folder from settings.ini file'''

import os
import configparser
import subprocess, shlex
import datetime
import zipfile

script_dir = os.path.dirname(os.path.realpath(__file__))

settings = configparser.ConfigParser()
settings.read(script_dir + '\\' + 'settings.ini','UTF-8')

Backup_folder = settings['DEFAULT']['Backup_folder'].replace('"','')
wr = settings['DEFAULT']['winrar_path'].replace('"','')
make_one_archive = settings.getboolean('DEFAULT', 'make_one_archive')
archive_program = settings.get('DEFAULT', 'archive_program')


# read list of files
p_file = open(script_dir + '\\' + 'files_and_folders.txt', mode='r', encoding='UTF-8')

lines = []
for line in p_file:
    clear_line = line.replace('\n','').replace('\r','').replace('"','').replace('\'','')
    if clear_line.strip() != '':
        lines.append(clear_line.strip())


if make_one_archive:
    arch_name = "Backup_" + datetime.datetime.now().replace(microsecond=0).strftime('%Y-%m-%d_%H-%M-%S')
    output_file = Backup_folder + '\\' + arch_name
    input_files = ' '.join(lines)
    input_files_qu = ' '.join(lines)
    

    if archive_program == 'WinRar':
        mycmd = '"' + wr + '"' +  ' a -ep1 ' + output_file + ' ' + input_files
        subprocess.run(shlex.split(mycmd))

    elif archive_program == 'Zip':
        with zipfile.ZipFile((output_file + '.zip').replace('\\', os.path.altsep), mode='w') as myzip:
            for input_file in lines:
                for root, subFolder, files in os.walk(input_file):
                    myzip.write(root)
                    
                    for subFolder_1 in subFolder:
                        sf = str(os.path.join(root,subFolder_1))
                        myzip.write(sf)  
  
                    for item in files:
                        fileNamePath = str(os.path.join(root,item))
                        myzip.write(fileNamePath)


if not make_one_archive:
    for folder in lines:
        arch_name = str(folder).replace('"','').split('\\')[-1] + " " + datetime.datetime.now().replace(microsecond=0).strftime('%Y-%m-%d_%H-%M-%S')
        output_file = Backup_folder + '\\' + arch_name
        input_file = '"' + str(folder).replace('"','') + '"'

        if archive_program == 'WinRar':
            mycmd = '"' + wr + '"' +  ' a -ep1 "' + output_file + '" ' + input_file
            subprocess.run(shlex.split(mycmd))
        
        elif archive_program == 'Zip':
            with zipfile.ZipFile((output_file + '.zip').replace('\\', os.path.altsep), mode='w') as myzip:
                for root, subFolder, files in os.walk(folder):
                    myzip.write(root)
                    
                    for subFolder_1 in subFolder:
                        sf = str(os.path.join(root,subFolder_1))
                        myzip.write(sf)  
                            
                    for item in files:
                        fileNamePath = str(os.path.join(root,item))
                        myzip.write(fileNamePath)

pass
