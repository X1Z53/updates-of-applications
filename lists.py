full_list = {
    'Programs': {
        'Archivators':                   {
            '7-Zip':                     ['https://www.7-zip.org', '', '.NewsText', 1],
                                         #['https://1progs.ru/7-zip/', 'https://www.7-zip.org', '.entry-title', 1],
            'WinRAR':                    ['https://www.win-rar.com/latestnews.html?&L=0', 'https://www.win-rar.com/predownload.html?&L=0', '.news-list-item', 2]},
        'Browsers':                      {
            'Google Chrome':             ['https://www.whatismybrowser.com/guides/the-latest-version/chrome', 'https://www.google.ru/chrome/', 'td+td'],
            'Microsoft Edge':            ['https://www.whatismybrowser.com/guides/the-latest-version/edge', 'https://www.microsoft.com/ru-ru/edge', 'td+td'],
            'Mozilla Firefox':           ['https://www.mozilla.org/en-US/firefox/notes/', 'https://www.mozilla.org/en-US/firefox/new/', '.c-release-version'],
            'Opera':                     ['https://www.whatismybrowser.com/guides/the-latest-version/opera', 'https://www.opera.com/browsers/opera', 'td+td'],        
            'Yandex Browser':            ['https://browser.yandex.ru/', '', '.page__version']},
        'Cheat Engine':                  ['https://www.cheatengine.org/downloads.php', '', '.download_link', -1],
        'Cloud Storage':                 {
            'Google Drive':              ['https://support.google.com/a/answer/7577057?hl=en', 'https://www.google.ru/drive/download/', 'em', -1],
            'TeraBox':                   ['https://www.terabox.com/russian/terabox-cloud-storage-for-pc-free-download', '', '.text', 2, 3, -18, '：'],
            'Yandex Disk':               ['https://ru.freedownloadmanager.org/Windows-PC/Yandex-Disk-FREE.html', 'https://disk.yandex.ru/promo/download', '.quick_specs div+div+div+div span+span', None, None, -5]},
        'Code Editors':                  {
            'Sublime Text':              ['https://www.sublimetext.com/download', '', '.latest', 2],
            'Visual Studio Code':        ['https://code.visualstudio.com/updates/', 'https://code.visualstudio.com/', 'strong', 1]},
        'Download Managers':             {
            'Internet Download Manager': ['https://www.internetdownloadmanager.com/news.html', 'https://rsload.net/soft/manager/8294-internet-download-manager.html', 'h3~h3', True, 4],
            'Xtreme Download Manager':   ['https://xtremedownloadmanager.com/#downloads', '', '.table tr+tr']},
        'Graphical Editors':             {
            'Adobe Photoshop':           ['https://1progs.ru/adobe-photoshop-2022/', '', '.entry-title', 3, 1],
            'CorelDRAW Graphics Suite':  ['https://1progs.ru/coreldraw-graphics-suite-aktivaciya/', '', '.entry-title', 4, 1]},
        'Music editors':                 {
            'Avid Sibelius':             ['https://1progs.ru/avid-sibelius/', '', '.entry-title', True, 2],
            'MuseScore':                 ['https://musescore.org/ru/download', '', 'strong', 5],
            'Reaper':                    ['https://www.reaper.fm/', 'https://www.reaper.fm/download.php', '.hdrbottom', 1, '', -1, '', {
                'ASIO4ALL':              ['https://www.asio4all.org/', '', 'tr', 1],
                'MAudioPlugins':         ['https://www.meldaproduction.com/downloads', '', 'h2', 1],
                'Native Access':         ['https://ru.freedownloadmanager.org/Windows-PC/Native-Instruments-Native-Access-FREE.html', 'https://www.native-instruments.com/en/specials/native-access/', '.quick_specs div+div+div+div+div span+span'],
                'Voxengo SPAN':          ['https://ru.freedownloadmanager.org/Windows-PC/Voxengo-SPAN-FREE.html', 'https://www.voxengo.com/product/span/', '.quick_specs div+div+div+div+div span+span']}]},
        'Office packs':                  {
            'Apache OpenOffice':         ['https://www.openoffice.org/download/index.html', '', '#announce', -1],
            'LibreOffice':               ['https://www.libreoffice.org/download/download/', '', '.dl_version_number'],
            'Microsoft Office':          ['https://docs.microsoft.com/en-us/officeupdates/current-channel-preview', 'https://repack.me/software/repacks/office/274-microsoft-office-2021.html', 'em', 1]},
        'Portable':                      {
            'AnyDesk':                   ['https://anydesk.com/en/downloads/windows', '', '.d-block', 0, 1],
            'Autoruns':                  ['https://docs.microsoft.com/en-us/sysinternals/downloads/autoruns', '', '.content', 3, 1],
            'CPU-Z':                     ['https://www.cpuid.com/softwares/cpu-z.html', '', '.subtitle', 1],
            'IconsExtract':              ['https://www.nirsoft.net/utils/iconsext.html', '', '.utilcaption', 1, 1],
            'MuseScore':                 ['https://musescore.org/ru/download', '', 'strong', 5],
            'Process Hacker':            ['https://processhacker.sourceforge.io/downloads.php', '', 'h1', True, 2],
            'TeamViewer':                ['https://www.teamviewer.com/en/download/windows/', '', '.wpb_text_column+.wpb_text_column+.wpb_text_column', 2],
            'Ventoy':                    ['https://github.com/ventoy/Ventoy/releases', '', '.ml-1.wb-break-all', 0, 1],
            'Visual Studio Code':        ['https://code.visualstudio.com/updates/', 'https://code.visualstudio.com/', 'strong', 1],
            'Windows ISO Downloader':    ['https://www.heidoc.net/joomla/technology-science/microsoft/67-microsoft-windows-and-office-iso-download-tool', '', '.pagenavcounter+p+p+p', 3],
            'WizTree':                   ['https://diskanalyzer.com/download', '', '.orange.btn + .orange.btn', 3]},
        'Python':                        ['https://www.python.org/downloads/', '', '.button', 2],
        'qBittorrent':                   ['https://www.qbittorrent.org/news.php', 'https://www.qbittorrent.org/download.php', 'h3', -2, 1],
        'Realtek Audio Driver':          ['https://www.softportal.com/software-5574-realtek-hd-audio-codec-driver.html', 'https://www.realtek.com/en/component/zoo/category/pc-audio-codecs-high-definition-audio-codecs-software', 'table tr+tr+tr td+td'],
        'Remote Access':                 {
            'AnyDesk':                   ['https://anydesk.com/en/downloads/windows', '', '.d-block', 0, 1],
            'TeamViewer':                ['https://www.teamviewer.com/en/download/windows/', '', '.wpb_text_column+.wpb_text_column+.wpb_text_column', 2]},
        'Steam':                         ['https://ru.freedownloadmanager.org/Windows-PC/Steam-FREE.html', 'https://store.steampowered.com/about/', '.quick_specs div+div+div+div span+span'],
        'System Analysis':               {
            'CPU-Z':                     ['https://www.cpuid.com/softwares/cpu-z.html', '', '.subtitle', 1],
            'Fraps':                     ['https://fraps.com/download.php', '', 'h3', 1],
            'Process Hacker':            ['https://processhacker.sourceforge.io/downloads.php', '', 'h1', True, 2],
            'WizTree':                   ['https://diskanalyzer.com/download', '', '.orange.btn', 3]},
        'Video Editors':                 {
            'Adobe Premiere Pro':        ['https://1progs.ru/adobe-premiere-pro-cc-klyuch-6/', '', '.entry-title', 4, 1],
            'Movavi Video Editor Plus':  #['https://www.movavi.ru/video-editor-plus/whats-new.html', 'https://1progs.ru/movavi-video-editor-klyuch-aktivacii/', '.h3.font-weight-bold', 1]},
                                         ['https://1progs.ru/movavi-video-editor-klyuch-aktivacii/', '', '.entry-title', 4]},
        'Virtualization':                {
            'QEMU':                      ['https://www.qemu.org/', 'https://www.qemu.org/download/#windows', 'strong'],
            'VirtualBox':                ['https://www.virtualbox.org/wiki/Downloads', '', 'h3', 1]},
        'VPN':                           {
            'ProtonVPN':                 ['https://github.com/ProtonVPN/win-app/releases', 'https://github.com/ProtonVPN/win-app/releases', '.ml-1.wb-break-all'],
            'Psiphon':                   ['https://1progs.ru/psiphon/', '', '.entry-title', 1],
            'Windscribe':                ['https://windscribe.com/changelog/windows', 'https://windscribe.com/install/desktop/windows', '.release>h3>a', None, 1]},
        'uTorrent':                      ['https://blog.utorrent.com/releases/windows/', 'https://www.utorrent.com/desktop/', 'a', 1],
        'uTorrent Web':                  ['https://blog.utorrent.com/releases/windows-web/', 'https://www.utorrent.com/web/', 'a', 2]
    },

    'Games': {
        'Assassin\'s Creed':                               {
            'Assassin\'s Creed Director\'s Cut Edition':   ['https://byrut.org/5460-assassins-creed-directors-cut-edition-pcs.html', '', '.subhname', 1],
            'Assassin\'s Creed 2 Deluxe Edition':          ['https://byrut.org/4232-assassins-creed-2-deluxe-edition-pc.html', '', '.subhname', 1],
            'Assassin\'s Creed Brotherhood':               ['https://byrut.org/1187-assassins-creed-brotherhood.html', '', '.subhname', 1],
            'Assassin\'s Creed Revelations':               ['https://byrut.org/5489-assassins-creed-revelations-pcs.html', '', '.subhname', 1],
            'Assassin\'s Creed 3 Remastered + Liberation': ['https://byrut.org/2856-assassins-creed-iii-remastered-repack-by-xatab.html', '', '.subhname', 1]},
        'The Sims 4':                                      ['https://byrut.org/608-sims-4-repack-by-xatab-to.html', '', '.subhname', 1]
    },

    'OSs': {
        'Arch Linux':         ['https://archlinux.org/download/', '', '#arch-downloads ul', 2],
        'Ubuntu':             {
            'Ubuntu Desktop': ['https://releases.ubuntu.com/', '', '.p-list__item', True, 1, -1],
            'Ubuntu Server':  ['https://releases.ubuntu.com/', '', '.p-list__item', True, 1, -1]},
        'MS-DOS':             {
            'MS-DOS 1':       ['https://winworldpc.com/download/37f6b264-9097-11e9-ab10-fa163e9022f0', '', 'h1', 1]}
    }
}

parametrs_list = ['url', 'download_link', 'content', 'word', 'slice_start', 'slice_end', 'split_symbol', 'addons']
