#!/usr/bin/env /usr/bin/python3

import ssl
import urllib.request
from sys import argv
from os.path import isfile, exists, join, islink
from os import mkdir, chdir, symlink, unlink, walk, readlink

from urllib.request import urlretrieve
from pprint import pprint
from re import match as re_match
from hashlib import file_digest


class FSUpdater(object):
    def __init__(self):
        self.__brepoDF = 'https://sourceforge.net/projects/fs-arch-unoffocial/files'
        self.__repo_name = 'fs-repo'
        self.__SLinkF = {self.__repo_name + '.db': self.__repo_name + '.db.tar.zst', self.__repo_name + '.db.sig': self.__repo_name + '.db.tar.zst.sig',
                         self.__repo_name + '.files': self.__repo_name + '.files.tar.zst', self.__repo_name + '.files.sig': self.__repo_name + '.files.tar.zst.sig', }
        self.__repo_dir = join(argv[1], self.__repo_name)
        self.__FileLists = {'file': {}, 'disk': {}}
        self.__repo_dir_folder = 'x64'

    def __checkDir(self):
        if not exists(self.__repo_dir):
            mkdir(self.__repo_dir)
            mkdir(join(self.__repo_dir, 'x64'))

    def __verifyHashDL(self, **kwargs):
        hsum = kwargs['hash_sum']
        hs_result = False

        with open(kwargs['dloaded_file'], 'rb') as dloaded_file:
            if file_digest(dloaded_file, 'sha512').hexdigest() == hsum:
                hs_result = True

        return hs_result

    def __dloadFile(self, **kwargs):
        context = ssl.create_default_context()

        try:
            with urllib.request.urlopen(kwargs['sourceUrl'], context=context) as response:
                total_size = int(response.getheader('Content-Length', 0))
                block_size = 8192
                downloaded = 0

                with open(kwargs['targetFile'], 'wb') as out_file:
                    while True:
                        buffer = response.read(block_size)
                        if not buffer:
                            break

                        out_file.write(buffer)
                        downloaded += len(buffer)

                        if total_size > 0:
                            percent = downloaded / total_size * 100
                            print(f"\rDownloading: {percent:.2f}%", end='')
                        else:
                            print(
                                f"\rDownloaded: {downloaded} bytes", end='')
        except:
            pass

    def __check_set_sl(self):
        chdir(join(self.__repo_dir, self.__repo_dir_folder))

        for sfl in self.__SLinkF.keys():

            if not exists(join(self.__repo_dir, self.__repo_dir_folder, sfl)):

                symlink(target_is_directory=False,
                        src=self.__SLinkF[sfl], dst=sfl)

            else:
                if islink(join(self.__repo_dir, self.__repo_dir_folder, sfl)):
                    linked_file = readlink(
                        join(self.__repo_dir, self.__repo_dir_folder, sfl))

                    if linked_file != self.__SLinkF[sfl]:
                        unlink(sfl)
                        symlink(target_is_directory=False,
                                src=self.__SLinkF[sfl], dst=sfl)

    def __dsync_files(self):
        chdir(self.__repo_dir)
        txt_files_content = None

        # updated copy files.txt file with all the hashes need to be downloaded
        if exists(join(self.__repo_dir, 'files.txt')):
            unlink(join(self.__repo_dir, 'files.txt'))

        try:
            urlretrieve(join(self.__brepoDF, 'files.txt',
                        'download'), 'files.txt')
        except:
            pass

        if exists(join(self.__repo_dir, 'files.txt')):
            with (open(join(self.__repo_dir, 'files.txt'), 'r')) as fhash_line:
                txt_files_content = fhash_line.readlines()

            for txt_file_line in txt_files_content:
                tfl_m = re_match(
                    r'^(.*)\ \ (.*\.(zst|sig|db|old|files|tar\.bz2))', txt_file_line)
                if tfl_m is not None:
                    self.__FileLists['file'][tfl_m.group(2)] = tfl_m.group(1)

            # pprint(self.__FileLists)

            for root, dirs, files in walk(join(self.__repo_dir, 'x64')):
                # x64 folder is empty
                if len(files) == 0:
                    for ftd in self.__FileLists['file'].keys():
                        success_hash = False

                        try:
                            # urlretrieve(join(self.__brepoDF, ftd, 'download'), join(self.__repo_dir, ftd))
                            while not success_hash:
                                if exists(join(self.__repo_dir, ftd)):
                                    unlink(join(self.__repo_dir, ftd))

                                self.__dloadFile(sourceUrl=join(self.__brepoDF, ftd, 'download'), targetFile=join(
                                    self.__repo_dir, ftd))

                                success_hash = self.__verifyHashDL(dloaded_file=join(
                                    self.__repo_dir, ftd), hash_sum=self.__FileLists['file'][ftd])

                        except:
                            pass

                #  directory is not empty, we syncronize 1-Way
                else:
                    # from the folder we take symbolic links away
                    sd_to_d = []
                    for slf in self.__SLinkF.keys():
                        if slf in files:
                            file_idx = (files.index(slf))
                            del files[file_idx]

                    for sdfile in files:
                        if self.__repo_dir_folder + '/' + sdfile not in self.__FileLists['file'].keys():
                            sd_to_d.append(sdfile)

                    # delete files not in files.txt mentioned
                    if len(sd_to_d) > 0:
                        for sdx in sd_to_d:
                            ftd = files.index(sdx)
                            del files[ftd]
                            unlink(
                                join(self.__repo_dir, self.__repo_dir_folder, sdx))

                    # now we syncronize
                    for slf in self.__FileLists['file']:

                        #  if not exist
                        if not exists(join(self.__repo_dir, slf)):
                            self.__dloadFile(sourceUrl=join(
                                self.__brepoDF, slf, 'download'), targetFile=join(self.__repo_dir, slf))

                        # if exist and wrong hash
                        else:
                            if not self.__verifyHashDL(dloaded_file=join(self.__repo_dir, slf), hash_sum=self.__FileLists['file'][slf]):
                                unlink(
                                    join(self.__repo_dir, self.__repo_dir_folder, slf))

                                self.__dloadFile(sourceUrl=join(
                                    self.__brepoDF, slf, 'download'), targetFile=join(self.__repo_dir, slf))

                # check the necessary symbolic links

    def __create_pacman_section(self):
        if not exists(join(self.__repo_dir, 'pacman_repo.txt')):
            with open(join(self.__repo_dir, 'pacman_repo.txt'), 'w') as fsrf:
                fsrf.write('[' + self.__repo_name + ']' + '\n' +
                           'Server = file://' + self.__repo_dir + '/' + self.__repo_dir_folder + '\n')

    def ex_tasks(self):
        task_list = {'checkdir': self.__checkDir, 'ds_files': self.__dsync_files,
                     'checksetsl': self.__check_set_sl, 'create_pacman_section': self.__create_pacman_section}
        for stask in task_list:
            task_list[stask]()


if __name__ == '__main__':
    FSUObj = FSUpdater()
    FSUObj.ex_tasks()


