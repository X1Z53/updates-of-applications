from lists import full_list
from functions import *


print('Scanning a downloaded files...')
downloaded_versions = get_downloaded_versions(full_list.keys())

for section, items in full_list.items():
    full_list[section] = creating_objects(configure_list(items), downloaded_versions, section)

show_versions(full_list)

show_updates(full_list)

input('\nPress <Enter> to exit')
