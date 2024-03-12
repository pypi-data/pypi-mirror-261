# scraper for https://hitomi.la
import pandas as pd
from doujindown.text_cleaning import *
from doujindown.read_serialized import *
from doujindown.scrapers.abstract_scraper import abstract_scraper

import os
import shutil
from glob import glob
import datetime

from abstract_scraper import abstract_scraper

class hitomi_scraper(abstract_scraper):
    def __init__(self, _headers: dict=None, _cookies: dict=None, wait_rl: int=2, _domain: str='https://hitomi.la'):
        super().__init__(_headers, _cookies, wait_rl)
        self._DOMAIN = _domain
        self._SEARCH_ENDPOINT = f'{_domain}/search.html?'

    # search for query at website search endpoint
    def search(
        self, 
        q: str='', 
        max_pgs: int = 5, 
        save: bool=False,
        manga_title_css: str='.gallery-content .dj, .manga h1 a',
        pgs_css: str='.page-top ul li') -> pd.DataFrame:
        
        last_pg = max_pgs
        pg = 0
        while pg < max_pgs and pg < last_pg:
            url = f'{self._SEARCH_ENDPOINT}{q}#{pg+1}'
            soup = self.soupify(url, show_soup=True)
            if pg == 0:
                print(len(list(soup.select(pgs_css))))
                last_pg = int(soup.select(pgs_css)[-1].text)
            print(f'SEARCHING: pg:{pg+1}/{last_pg} at {url}')
            titles = list(map(lambda e : e.text, soup.select(manga_title_css)))
            links = list(map(lambda e : f'{self._DOMAIN}{e["href"]}', soup.select(manga_title_css)))
            pg += 1

            for title, link in zip(titles, links):
                mangas.append({
                    'manga_title': title,
                    'manga_link': link})
            

        mangas = pd.DataFrame(mangas).astype(str).drop_duplicates()
        print(f'num results: {len(mangas)}\n{mangas}\n')

        if save:
            formatted_date = datetime.date.today().strftime('%m_%d_%Y')
            savep = f'{os.path.basename(self._DOMAIN).split(".")[0]}{formatted_date}'
            print(f'saving to {savep}')
            mangas.to_csv(savep, index=False)

        return mangas

    # download imgs/pgs to pdf from chapter link
    def download_chapter(
        self, 
        link: str, 
        save_dir: str='',
        wait_for_default: int=0,
        format:str='zip',
        ch_num: str='',
        use_cbz: bool=True,
        imgs_css: str='img.img-loading') -> None:
        pass


    # view chapter list
    def chapters(
        self, 
        link: str, 
        save: bool=False,
        chapters_css: str='.row-content-chapter .a-h .chapter-name',
        num_views_css: str='.row-content-chapter .a-h .chapter-view',
        date_css: str='.row-content-chapter .a-h .chapter-time',
        manga_title_css: str='.story-info-right h1') -> pd.DataFrame:
        pass

if __name__ == '__main__':
    hitomi = hitomi_scraper()

    hitomi.search('kyockcho')