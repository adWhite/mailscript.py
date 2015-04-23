#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil
import errno

config_file = 'clients.txt'

f = open(config_file, 'r')
clients = [x.rstrip() for x in f.readlines() if x]

def copy_directory(src, dest):
    try:
        shutil.copytree(src, dest)
    except OSError as e:
        if e.errno == errno.ENOTDIR:
            shutil.copy(src, dest)
        else:
            print 'Directory not copied. Error: {0}'.format(e)

def copy_content(src, dest):
    try:
        shutil.copy(src, dest)
    except Exception, e:
        print 'Error: {0}'.format(e)

def main():
    for index, client in enumerate(clients):
        client = client.split(', ')
        for email in client[1:]:
            path = '{0}/{1}/Maildir/.OldInbox'.format(client[0], email)
            if not os.path.exists(path):
                print 'folder doesn\'t exist, copying OldMailTemplate to Maildir/.OldInbox'

                copy_directory('OldMailTemplate', path)

                try:
                    # comeauxdds.com/ryan2/Maildir/cur
                    src = os.path.join(client[0], email, 'Maildir', 'cur')

                    # comeauxdds.com/ryan2/Maildir/.OldInbox/cur
                    dest = os.path.join(path, 'cur')

                    print 'Copying files from {0} to {1}'.format(src, dest)

                    # cp -r src/* dest
                    os.system('cp -r {0}/* {1}'.format(src, dest))
                except Exception, e:
                    print 'Error: {0}, deleting folder'.format(e)
                    shutil.rmtree(path)

            else:
                print 'folder inside {0} already exists!'.format(email)
            
if __name__ == '__main__':
    main()
