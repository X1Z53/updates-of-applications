from classes import Program
import os
from lists import parametrs_list
from sys import platform
from progress.bar import Bar


def configure_list(unconfigured_list):
    full_list = {}

    for name, current_values in unconfigured_list.items():
        if type(current_values) == dict:
            full_list[name] = configure_list(current_values)
        else:
            parametrs = {}

            for value, parametr in zip(current_values, parametrs_list[:len(current_values)]):
                if parametr == 'addons' and value: parametrs[parametr] = configure_list(value)
                elif value: parametrs[parametr] = value

            full_list[name] = parametrs

    return full_list

def creating_objects(items_list, downloaded_versions, section=''):
    full_list = {}

    bar = Bar('Scanning updates for ' + section, max=len(items_list))
    
    for item_name, parametrs in items_list.items():
        if 'url' not in list(parametrs.keys()):
            item = creating_objects(parametrs, downloaded_versions)
        else:
            item = Program(item_name, downloaded_versions, parametrs)
        
            if item.parametrs and item.addons: item.addons = creating_objects(item.addons, downloaded_versions)

        if section: bar.next()
        full_list[item_name] = item

    if section: print()
    return full_list


def show_versions(section_list, prefix_number=0):
    for number, item in enumerate(section_list.items()):
        if hasattr(item[1], 'name'):
            item = item[1]
            print(f'{"  " * prefix_number}{number+1}. {item.name}: {item.downloaded_version} {f"(New version - {item.current_version})" if item.have_update else ""}')
            if hasattr(item, 'addons') and item.addons: show_versions(item.addons, prefix_number+1)
        else:
            print(f'{"  " * prefix_number}{number+1}. {item[0]}:')
            show_versions(item[1], prefix_number+1)


def get_downloaded_versions(sections):
    path_separator = ['/', '\\'][platform=='win32']
    root = path_separator.join(os.path.abspath(__file__).split(path_separator)[:-2]) + path_separator + 'All'
    downloaded_versions = scan(root)
    return downloaded_versions

def scan(root):
    full_list = {}
    for path, folders, files in os.walk(root):
        if '_' in path: continue
        for file in files:
            name, version = file.split(').')[0].split(' (')
            full_list[name] = version

    return full_list

def for_update(full_list):
    update_list = []
    for item in full_list.values():
        if not hasattr(item, 'name'): [update_list.append(i) for i in for_update(item)]
        elif item.have_update: update_list.append(item)
    return update_list

def show_updates(full_list):
    update_list = for_update(full_list)
    
    if update_list and input('\nShow update links? [Y/N] ').lower() == 'y':
        for number, item in enumerate(update_list):
            print(f'{number+1}. {item.name} {item.current_version} - {item.download_link}')