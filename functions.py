'''
    Functions
'''

from os import walk
from os.path import abspath
from sys import platform
from progress.bar import Bar

from classes import Program

parametrs_list = ['url', 'download_link', 'content',
                  'word', 'slice_start', 'slice_end', 'split_symbol']


def configure_list(unconfigured_list) -> dict:
    '''
    Formating received list
    '''

    full_list = {}

    for name, current_values in unconfigured_list.items():
        if isinstance(current_values, dict):
            full_list[name] = configure_list(current_values)
        else:
            parametrs = {}

            for value, parametr in zip(current_values, parametrs_list[:len(current_values)]):
                if value:
                    parametrs[parametr] = value

            full_list[name] = parametrs

    return full_list


def create_objects(items_list, downloaded_versions, section=''):
    full_list = {}
    progress_bar = Bar('Scanning updates for ' + section, max=len(items_list))

    for item_name, parametrs in items_list.items():
        if 'url' not in list(parametrs.keys()):
            item = create_objects(parametrs, downloaded_versions)
        else:
            item = Program(item_name, downloaded_versions, parametrs)

        if section:
            progress_bar.next()

        full_list[item_name] = item

    if section:
        print()
    return full_list


def show_versions(section_list, prefix_number=0):
    '''
    Printng results
    '''
    for number, item in enumerate(section_list.items()):
        if hasattr(item[1], 'name'):
            item = item[1]
            print(f'{"  " * prefix_number}{number+1}. {item.name}: {item.downloaded_version} {f"(Error: {item.error})" if item.error else f"(New version: {item.current_version})" if item.have_update else ""}')

        else:
            print(f'{"  " * prefix_number}{number+1}. {item[0]}:')
            show_versions(item[1], prefix_number+1)


def get_downloaded_versions():
    path_separator = ['/', '\\'][platform == 'win32']
    root = path_separator.join(abspath(__file__).split(
        path_separator)[:-2]) + path_separator + 'All'
    downloaded_list = {}
    walk_list = walk(root)

    for path, _, files in walk_list:
        if '_' in path:
            continue
        for file in files:
            name, version = file.split(').')[0].split(' (', 1)
            downloaded_list[name] = version

    return downloaded_list


def for_update(full_list):
    update_list = []
    for item in full_list.values():
        if not hasattr(item, 'name'):
            for i in for_update(item):
                update_list.append(i)
        elif item.have_update:
            update_list.append(item)

    return update_list


def show_updates(full_list):
    '''
    Print result update links
    '''
    update_list = for_update(full_list)

    if update_list and input('\nShow update links? [Y/N] ').lower() != 'n':
        for number, item in enumerate(update_list):
            print(
                f'{number+1}. {item.name} ({item.current_version}) - {item.download_link}')
