''' Backup files

This program backup files from list to folder from settings.ini file'''

import os
import configparser
import subprocess, shlex
import datetime

script_dir = os.path.dirname(os.path.realpath(__file__))

settings = configparser.ConfigParser()
settings.read(script_dir + '\\' + 'settings.ini','UTF-8')

Backup_folder = settings['DEFAULT']['Backup_folder'].replace('"','')
wr = settings['DEFAULT']['WinRar_path'].replace('"','')
make_one_archive = settings.getboolean('DEFAULT', 'make_one_archive')


# read list of files
p_file = open(script_dir + '\\' + 'files_and_folders.txt', mode='r', encoding='UTF-8')

lines = []
for line in p_file:
    clear_line = line.replace('\n','').replace('\r','').replace('"','').replace('\'','')
    if clear_line.strip() != '':
        lines.append('"' + clear_line.strip() + '"')


if make_one_archive:
    arch_name = "Backup_" + datetime.datetime.now().replace(microsecond=0).strftime('%Y-%m-%d_%H-%M-%S')
    output_file = '"' + Backup_folder + '\\' + arch_name + '"'
    input_files = ' '.join(lines)
    mycmd = '"' + wr + '"' +  ' a -ep1 ' + output_file + ' ' + input_files
    mycmd_2 = '"' + wr + '"' +  ' a -ep1 ' + output_file + ' ' + input_files    
    subprocess.run(shlex.split(mycmd))
else:
    for folder in lines:
        arch_name = str(folder).replace('"','').split('\\')[-1] + " " + datetime.datetime.now().replace(microsecond=0).strftime('%Y-%m-%d_%H-%M-%S')
        output_file = '"' + Backup_folder + '\\' + arch_name + '"'
        input_files = '"' + str(folder).replace('"','') + '"'
        mycmd = '"' + wr + '"' +  ' a -ep1 ' + output_file + ' ' + input_files
        subprocess.run(shlex.split(mycmd))

pass
