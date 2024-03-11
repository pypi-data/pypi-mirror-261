```
                        ==-------:       .:-===-:.  ..-------: ..................      .-*#######
                        =======--.           .......::..::::...:::::::...               .+#######
                        ---=====-:          ...::::::::::...:::::::::::::::..            :+######
                        --==-===:        ..:::::::::::::::::::::::::::::::::::.           :+#####
                        =-====-:       ..::::::::::.::::::::::::::::::::::::::::..         :+####
                        =====-.       ..::::::::::..::::::::::::::::::::::::::::::..        -+###
                        =====.       ..:::::::::::..::::::::::::-:::::::::::::::::::..      .=*##
                        ====:      ...:::::::::::: .:::::::::::::--::::::::::::..:::::.      -*##
                        ===-.     ...::::::::::::- :::::::::::::::-=::::::::::::.::::::...   .+*#
                        ===:.    ...:::::.::::::=- .:::::::::::::::-=-:::::::::::.::::::.::.. -+#
                        ===..  ....:::::.::::::==- .::::::::::::::::-==::..::::::.::::::..:...=*#
hashirkz                -=-.......::::::.:::::-=+=. :::::::-::::::::::-==-:.:::::..:::::...  .+##
doujindown-0.0.3        =--:.::...::::::.::::==+++- .::::::--:::::::::.:-==-:......:::::.    -*##
..  .. ..  .. ..  ..    ===-.    .:---::.:::=+=+++=-...::::-==-:.:::::.. ...  .....:::::.   .=###
  ..     ..     ..      ::::.     :----:.::--:.-----=-::::--=====-:::::.      -==:.:::::.   -+###
..  .. ..  .. ..  ..       .:..   .----:......      -===================-.  .:===........   -*###
                          .-==-.   :----:.====:.   .=+==================--------:..::...   .:+###
                        ---===-.    :----:-====----==+==================--------..::...  ....-*##
                        -=====-.:.   .:---::-====-=======================------....... .......-*#
                        ----::.:==-.   .::::::---=============================-:..:::......:...-+
                        :...:::====-:....::::..:--==++==========-------=-====-:..::::......::...:
                        ...--:==-===+:::::--::..:--======--::.................. .::::. ...:::::..
                        .::-=-==:=#*-.:::::::::.......::.   .  ............    .:::::. ...::::::.
                        ::-+**++==*=.::::.::::::::-=-       . . ............. .:::::.. ....::::::
                        ==-:-+*###+..:::::.::::::::::         . ...........  .:::::::..-=:.::::::
                        ====-::+##+ .::::::.::::::::..           .........  .......... .==:.:::::

site              nsfw    working
----------------  ------  ---------
ww7.manganelo.tv  n       y
hitomi.la         y       n

gh: https://github.com/hashirkz/doujindown
pypi: https://pypi.org/project/doujindown/
```

## about
- command line app to download doujins + manga from many websites *manganelo.com hitomi.la etc 
- similar to [hdoujindownloader](https://github.com/HDoujinDownloader/HDoujinDownloader)
- for wsl2/unix/debian systems

### installation
```bash
pip install doujindown
```

#### usage
```
# read doujindown --help for more functionality
>> doujindown -a 'https://ww7.manganelo.tv/manga/manga-pd966360'

SEARCHING: https://ww7.manganelo.tv/manga/manga-pd966360
HTTP STATUS: 200

name: Mahou Shoujo Madoka★Magica
NUM RESULTS: 12
                                        chapter_title                                       chapter_link num_views upload_date
0   mahou_shoujo_madoka★magica:_vol.1_chapter_1_:_...  https://ww7.manganelo.tv/chapter/manga-pd96636...     29.9k   aug_25,19
1   mahou_shoujo_madoka★magica:_vol.1_chapter_2_:_...  https://ww7.manganelo.tv/chapter/manga-pd96636...     18.2k   aug_25,19
2   mahou_shoujo_madoka★magica:_vol.1_chapter_3_:_...  https://ww7.manganelo.tv/chapter/manga-pd96636...     16.6k   aug_25,19
3   mahou_shoujo_madoka★magica:_vol.1_chapter_4_:_...  https://ww7.manganelo.tv/chapter/manga-pd96636...     14.7k   aug_25,19
4   mahou_shoujo_madoka★magica:_vol.2_chapter_5_:_...  https://ww7.manganelo.tv/chapter/manga-pd96636...     14.1k   aug_25,19
5   mahou_shoujo_madoka★magica:_vol.2_chapter_6_:_...  https://ww7.manganelo.tv/chapter/manga-pd96636...     13.2k   aug_25,19
6   mahou_shoujo_madoka★magica:_vol.2_chapter_7_:_...  https://ww7.manganelo.tv/chapter/manga-pd96636...     13.1k   aug_25,19
7   mahou_shoujo_madoka★magica:_vol.2_chapter_8_:_...  https://ww7.manganelo.tv/chapter/manga-pd96636...     14.2k   aug_25,19
8   mahou_shoujo_madoka★magica:_vol.3_chapter_9_:_...  https://ww7.manganelo.tv/chapter/manga-pd96636...     15.5k   aug_25,19
9   mahou_shoujo_madoka★magica:_vol.3_chapter_10_:...  https://ww7.manganelo.tv/chapter/manga-pd96636...     13.9k   aug_25,19
10  mahou_shoujo_madoka★magica:_vol.3_chapter_11_:...  https://ww7.manganelo.tv/chapter/manga-pd96636...     14.2k   aug_25,19
11  mahou_shoujo_madoka★magica:_vol.3_chapter_12_:...  https://ww7.manganelo.tv/chapter/manga-pd96636...     22.4k   aug_25,19
SEARCHING CACHED FILES
saving to
downloading ch: 1/12

SEARCHING: https://ww7.manganelo.tv/chapter/manga-pd966360/chapter-1
HTTP STATUS: 200

CHAPTER NAME: Mahou Shoujo Madoka★Magica Vol.1 Chapter 1 : I Kind Of Saw Her In My Dream page 1 - Mangakakalot
NUM PGS FOUND: 43
creating directory: mahou_shoujo_madoka★magica in /mnt/c/users/hashi/documents/stuff_nh
downloading ch: 2/12

SEARCHING: https://ww7.manganelo.tv/chapter/manga-pd966360/chapter-2
HTTP STATUS: 200

CHAPTER NAME: Mahou Shoujo Madoka★Magica Vol.1 Chapter 2 : I Thought That It Would Be Really Nice page 1 - Mangakakalot
NUM PGS FOUND: 37


... skipping for readme.md but would go through ch 3-11 aswell ...


downloading ch: 11/12

SEARCHING: https://ww7.manganelo.tv/chapter/manga-pd966360/chapter-11
HTTP STATUS: 200

CHAPTER NAME: Mahou Shoujo Madoka★Magica Vol.3 Chapter 11 : The Only Way Left page 1 - Mangakakalot
NUM PGS FOUND: 37
downloading ch: 12/12

SEARCHING: https://ww7.manganelo.tv/chapter/manga-pd966360/chapter-12
HTTP STATUS: 200

CHAPTER NAME: Mahou Shoujo Madoka★Magica Vol.3 Chapter 12 : My Best Friend [End] page 1 - Mangakakalot
NUM PGS FOUND: 47
```

##### help
```
usage: doujindown [-h] [-s SEARCH] [-q QUERY] [--max-pgs MAX_PGS] [--save-searches] [-c CHAPTER] [--save-dir-ch SAVE_DIR_CH]
                   [-a SERIES] [--save-dir-series SAVE_DIR_SERIES] [-r RANGE] [--wait-default WAIT_DEFAULT] [--viewch VIEWCH]
                   [--save-chapters] [--headers HEADERS] [--cookies COOKIES] [--wait-rl WAIT_RL]

| order | flag              | function                                 |
| ----- | ----------------- | ---------------------------------------- |
| !     | -h \| --help      | show this help message and exit          |
| !     | -s \| --search    | search for manga                         |
| x     | -q \| --query     | query for manga                          |
| x     | --max-pgs         | max_pgs to search manga                  |
| x     | --save-searches   | save searches to current working dir     |
| !     | -c \| --chapter   | download chapters from link              |
| x     | --save-dir-ch     | directory to save chapter                |
| !     | -a \| --series    | series / all chapters link to download   |
| x     | --save-dir-series | directory to save series to              |
| x     | -r \| --range     | directory to save series to              |
| x     | --wait-default    | wait num mins before making new requests |
| !     | --viewch          | view chapters for manga at link          |
| x     | --save-chapters   | save chapters to current working dir     |
| ?     | --headers         | HEADERS                                  |
| ?     | --cookies         | COOKIES                                  |
| ?     | --wait-rl         | WAIT_RL                                  |
```