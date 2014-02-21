#!/usr/bin/python
import distutils.core
from os import path
import re

include_folder = 'slides'
include_templates = ['{}.html', '{}.md']
include_regex = re.compile('@@([a-zA-Z0-9-_]+)')

in_file = 'index.html'
out_folder = '../dist'
out_file_name = 'index.html'
dirs_to_copy = ['css', 'js', 'lib', 'plugin']

def main():
    print('Copying static directories...')
    for directory in dirs_to_copy:
        target = path.join(out_folder, directory)
        if path.exists(target):
            distutils.dir_util.remove_tree(target) #WARNING: THIS ACTUALLY REPLACES THE OLD ONE, SO BE CAREFUL
        distutils.dir_util.copy_tree(directory, target)
        print('{} copied'.format(directory))
    print('All copied.')

    print('Processing {} file...'.format(in_file))
    with open(path.join(out_folder, out_file_name), 'w+') as fout:
        with open(in_file, 'r') as fin:
            text = fin.read()

            text = include_regex.sub(processIncludeMatch, text)

            fout.write(text)

    print('{} file processed.'.format(in_file))
    print('All done!')

def processIncludeMatch(match):
    return includeFile(match.group(1))

def includeFile(name):
    filename = ''
    exists = False

    for template in include_templates:
        filename = path.join(include_folder, template.format(name))
        if path.isfile(filename):
            exists = True
            break

    if exists:
        print('>> File {} included'.format(filename))

        with open(filename, 'r') as f:
            return f.read()


main()
