import distutils.core
from os import path
import re

include_folder = 'slides'
include_template = '{}.md'
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

            matches = include_regex.findall(text) #save matches to print them
            text = include_regex.sub(processIncludeMatch, text)

            fout.write(text)

            if matches is not None:
                for match in matches:
                    print('>> File {} included'.format(include_template.format(match)))
    print('{} file processed.'.format(in_file))
    print('All done!')

def processIncludeMatch(match):
    return includeFile(match.group(1))

def includeFile(name):
    filename = path.join(include_folder, include_template.format(name))

    with open(filename, 'r') as f:
        return f.read()


main()
