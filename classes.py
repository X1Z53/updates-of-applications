import requests
from bs4 import BeautifulSoup as BS
from time import sleep


class Program:
    def __init__(self, name, downloaded_versions, parametrs=None):
        self.name            = name
        self.error           = ''
        self.current_version = 0

        if parametrs:
            self.url           = parametrs.setdefault('url',           '')
            self.download_link = parametrs.setdefault('download_link', self.url)
            self.content       = parametrs.setdefault('content',       '')
            self.word          = parametrs.setdefault('word',          0)
            self.slice_start   = parametrs.setdefault('slice_start',   None)
            self.slice_end     = parametrs.setdefault('slice_end',     None)
            self.split_symbol  = parametrs.setdefault('split_symbol',  None)
            self.addons        = parametrs.setdefault('addons',        {})
            
            self.current_version_check()
        else:
            self.error = 'No parametrs'
       
        self.downloaded_version = downloaded_versions[self.name.replace("'", '')] if self.name.replace("'", '') in downloaded_versions.keys() else 'Not Found'

        self.have_update = all((self.downloaded_version != self.current_version, not self.error))

    def current_version_check(self):
        try:
            session = requests.get(self.url)
        except:
            self.error = 'No response to the request'
        else:
            html = BS(session.text, 'html.parser')
            if type(self.content) == bool:
                self.error = 'Show HTML Code'
                self.current_version = html

            element_response = html.select(self.content)

            if all([self.content, element_response]):
                text = element_response[0].text.split(self.split_symbol)

                if type(self.word) != bool:
                    try:
                        self.current_version = text[self.word][self.slice_start:self.slice_end]
                    except:
                        self.error = f'Incorrect response or parametrs: {text, self.word, self.slice_start, self.slice_end}'
                else:
                    self.current_version = ' '.join(text[self.slice_start:self.slice_end])
            else:
                self.error = f'Incorrect response or parametrs: {self.content, element_response}'

        if self.error and not self.current_version: self.current_version = 0