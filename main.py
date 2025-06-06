#!/usr/bin/env python3
import tarfile
import os
import json
import sys
import subprocess as sp
import print_color as pc
import shutil

def unpack(package_name):
    try:
        file = tarfile.open(f'{package_name}.ula') 

        file.extractall('./pkg_cache', filter='data') 
        file.close()
    except:
        pc.print(f'No app with that name. EC: 10', tag='erros', tag_color='red', color='white')
        exit(10)

    pc.print('Unpacking app...')
    info_file = {}
    
    try:
        with open(f'./pkg_cache/{package_name}/package.json', 'r') as file:
            info_file_loaded = file.read()
            info_file = json.loads(info_file_loaded)
    
        pc.print(f'{info_file['name']} v{info_file['version']} unpacked!', tag='success', tag_color='green', color='white')
        pc.print(f'To run {info_file['name']} type "{sys.argv[0]} -r {info_file['name']}".', tag='info', tag_color='yellow', color='white')

    except:
        pc.print(f'There\'s not "package.json" file. EC: 11', tag='erros', tag_color='red', color='white')
        exit(11)

def run(package_name):
    old_dir = os.getcwd()
    os.chdir(f'./pkg_cache/{package_name}')
    sp.call(['sh', f'./start.sh'])
    os.chdir(old_dir)

def info(package_name):
    dlt_file = False
    if not os.path.exists(os.path.join(os.getcwd(), 'pkg_cache', package_name)):
        dlt_file = True
        try:
            file = tarfile.open(f'{package_name}.ula') 

            file.extractall('./pkg_cache', filter='data') 
            file.close()
        except:
            pc.print(f'No app with that name. EC: 10', tag='erros', tag_color='red', color='white')
            exit(10)

    pc.print('Unpacking app...')
    info_file = {}
    
    try:
        with open(f'./pkg_cache/{package_name}/package.json', 'r') as file:
            info_file_loaded = file.read()
            info_file = json.loads(info_file_loaded)
        
        print(f'App Information:\n\tName: {info_file['name']}\n\tVersion: {info_file['version']}\n\tAuthor: {info_file['author']}\n\tApp Format Version: {info_file['format-version']}')
    except:
        pc.print(f'There\'s not "package.json" file. EC: 11', tag='erros', tag_color='red', color='white')
        exit(11)

    if dlt_file:
        shutil.rmtree(f'./pkg_cache/{package_name}')


if __name__ == '__main__':
    if sys.argv[1] == '-u':
        if len(sys.argv[2]) > 0: unpack(sys.argv[2])
    elif sys.argv[1] == '-r':
        if len(sys.argv[2]) > 0: run(sys.argv[2])
    elif sys.argv[1] == '-ur':
        if len(sys.argv[2]) > 0: 
            unpack(sys.argv[2]) 
            run(sys.argv[2])
    elif sys.argv[1] == '-i':
        if len(sys.argv[2]) > 0: 
            info(sys.argv[2]) 
