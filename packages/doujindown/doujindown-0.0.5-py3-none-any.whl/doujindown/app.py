import urllib

import os
import sys
import argparse

from doujindown.scrapers.abstract_scraper import abstract_scraper
from doujindown.scrapers.manganelo import manganelo_scraper
from doujindown.text_cleaning import *
from doujindown.read_serialized import *

# GLOBAL PATHS
DOUJINDOWN = read_txt(rootp('./conf/doujindown.txt'))
WORKING = pretty_csv(rootp('./conf/working.csv'))
SETTINGS = read_yml(rootp('./conf/settings.yml'))
SITES = read_json(rootp('./conf/mirrors.json'))['sites']
MIRRORS = read_json(rootp('./conf/mirrors.json'))['mirrors']

VIOLET = '\033[38;5;105m'
CYAN = '\033[38;5;63m'
WHITE = '\033[0m'

# app pfp
HELP = 'see for more help:\ngithub: https://github.com/hashirkz/doujindown\npypi: https://pypi.org/project/doujindown/'
MSG = '\n' + VIOLET + DOUJINDOWN + CYAN + '\n\n' + WORKING + '\n\n' + '\n' + HELP + '\n' + WHITE
    
# main ineractive app function
def shell() -> int:
    yn = 'y'
    num = 0
    while yn in ['y', 'yes']:
        if num != 0:
            yn = input('CONTINUE y/n ? ').lower().strip()
            if yn not in ['y', 'yes']: return 0
            
        link = input('LINK TO CHAPTERS ?  ').lower().strip()
        download_range = input('CHAPTERS TO DOWNLOAD e.x 1-40 *default all ? ').lower().strip()
        
        
        # lookup domain in site_registry.json
        # pattern = r"https?://(www\.[a-zA-Z0-9.-]+).*"
        domain = urllib.parse.urlparse(link).netloc
        scraper = read_json('./registry.json').get(domain)

        # unable to find domain in the site registry
        if not scraper: 
            print(f'ERROR: unsupported link from: {domain}')
            return 1

        try:
            # if the lookup is successful create the scraper subclass object for whatever website link was
            # e.x user inputs ww7.manganelo.tv link then generate a manganelo_scraper object *factory design
            scraper = globals()[scraper]()
            scraper.download_chapters(link=link, download_range=download_range)

        except Exception as e:
            print(f'ERROR:\n{e}')
        
        num += 1

    return 0

def app() -> int:

    parser = argparse.ArgumentParser(
        prog="doujindown",
        description=MSG,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    # flag group for the desired function
    func = parser.add_mutually_exclusive_group(required=True)
    # parser.add_argument('-l', '--link', dest='link', help='chapter/series/search link', required=True)
    
    # SEARCH parsing
    func.add_argument('-s', '--search', help='search for manga')
    parser.add_argument('-q', '--query', required='--search' in sys.argv, help='query for manga')
    parser.add_argument('--max-pgs', dest='max_pgs', type=int, default=50, required='--search' in sys.argv, help='max_pgs to search manga')
    parser.add_argument('--save-searches', dest='save_searches', default=True, required='--search' in sys.argv, action='store_true', help='save searches to current working dir')
    
    # CHAPTER parsing
    func.add_argument('-c', '--chapter', help='download chapters from link')
    parser.add_argument('--save-dir-ch', dest='save_dir_ch', default='', required='--chapter' in sys.argv, help='directory to save chapter')

    # SERIES/ALL CHAPTERS parsing
    func.add_argument('-a', '--series', dest='series', help='series / all chapters link to download')
    parser.add_argument('--save-dir-series', dest='save_dir_series', default='', required='--series' in sys.argv, help='directory to save series to')
    parser.add_argument('-r', '--range', dest='range', default='-', required='--series' in sys.argv, help='directory to save series to')
    parser.add_argument('--wait-default', dest='wait_default', type=int, default=0, required='--series' in sys.argv, help='wait num mins before making new requests')
    

    # VIEW CHAPTERS parsing
    func.add_argument('--viewch', dest='viewch', help='view chapters for manga at link')
    parser.add_argument('--save-chapters', dest='save_chapters', default='--viewch' in sys.argv, action='store_true', help='save chapters to current working dir')
    
    # HEADERS COOKIES TO USE *may need these for some sites e.x hitomi.la nhentai.net etc
    parser.add_argument('--headers')
    parser.add_argument('--cookies')
    parser.add_argument('--wait-rl', dest='wait_rl', type=int, default=2)

    args = parser.parse_args()
    
    # error handling
    # no search/chapters/series flag
    if not args.search and not args.chapter and not args.series and not args.viewch:
        print(f'ERROR: bad command missing no -s|-c|-a was given. try doujindown --help for help')
        return 1
    
    if args.search: link = args.search
    if args.chapter: link = args.chapter
    if args.series: link = args.series
    if args.viewch: link = args.viewch
    
    host = urllib.parse.urlparse(link).netloc
    scraper_h = SITES.get(host)

    # bad host
    if not scraper_h: 
        print(f'ERROR: bad host not on mirror list: {host}')
        return 1
    
    # instantiate host site scraper polymorphically
    scraper = globals()[scraper_h](_headers=args.headers, _cookies=args.cookies, wait_rl=args.wait_rl)
    
    # SEARCH FUNCTION
    if args.search:
        scraper.search(q=args.query, max_pgs=args.max_pgs, save=args.save_searches)
        return 0

    # CHAPTER FUNCTION
    if args.chapter:
        scraper.download_chapter(link=link, save_dir=args.save_dir_ch)
        return 0
    
    # SERIES FUNCTION
    if args.series:
        scraper.download_chapters(link=link, save_dir=args.save_dir_series, download_range=args.range, wait_for_default=args.wait_default)
        return 0

    # VIEW CHAPTERS FUNCTION
    if args.viewch:
        scraper.chapters(link=link, save=args.save_chapters)
        return 0

if __name__ == '__main__':
    app()
