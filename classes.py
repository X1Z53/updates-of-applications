import requests
from bs4 import BeautifulSoup as BS


class Program:
    def __init__(self, name, downloaded_versions, parametrs):
        self.name      = name
        self.parametrs = parametrs or None

        if self.parametrs:
            self.url           = self.parametrs.setdefault('url',           '')
            self.download_link = self.parametrs.setdefault('download_link', self.url)
            self.content       = self.parametrs.setdefault('content',       '')
            self.word          = self.parametrs.setdefault('word',          0)
            self.slice_start   = self.parametrs.setdefault('slice_start',   None)
            self.slice_end     = self.parametrs.setdefault('slice_end',     None)
            self.split_symbol  = self.parametrs.setdefault('split_symbol',  None) 
            self.addons        = self.parametrs.setdefault('addons',        {})
            
            session = requests.get(self.url)
            html = BS(session.text, 'html.parser')
            if type(self.content) == bool: print(html)
            if type(self.word) != bool and self.content:
                self.current_version = html.select(self.content)[0].text.split(self.split_symbol)[self.word][self.slice_start:self.slice_end]
            elif self.content:
                self.current_version = ' '.join(html.select(self.content)[0].text.split(self.split_symbol)[self.slice_start:self.slice_end])
            else:
                self.current_version = 'Not Found'

            self.current_version = self.current_version.replace('(', '').replace(')', '')
        else:
            self.current_version = 'Not Found'
       
        self.downloaded_version = downloaded_versions[self.name.replace("'", '')] if self.name.replace("'", '') in downloaded_versions.keys() else 'Not Found'

        self.have_update = self.downloaded_version != self.current_version
