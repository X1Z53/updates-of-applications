'''
    The main script
    Run this file and follow the instractions
'''
import json

from functions import create_objects, get_downloaded_versions,\
    configure_list, show_versions, show_updates

full_list = json.load(open('list.json', 'r', encoding='utf-8'))

print('Scanning a downloaded files...')
downloaded_versions = get_downloaded_versions()

for section, items in full_list.items():
    full_list[section] = create_objects(
        configure_list(items), downloaded_versions, section)

show_versions(full_list)

show_updates(full_list)

input('\nPress <Enter> to exit')
