# -*- coding: utf-8 -*-

'''
Copyright (C) 2015                                                     

This program is free software: you can redistribute it and/or modify   
it under the terms of the GNU General Public License as published by   
the Free Software Foundation, either version 3 of the License, or      
(at your option) any later version.                                    

This program is distributed in the hope that it will be useful,        
but WITHOUT ANY WARRANTY; without even the implied warranty of         
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          
GNU General Public License for more details.                           

You should have received a copy of the GNU General Public License      
along with this program. If not, see <http://www.gnu.org/licenses/>  
'''

import os
import re
import sys
import urllib
import urllib2
import WebUtils
import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin
import xbmcvfs

##############################GLOBALS AND SETTINGS VARS#############################
searchQ = str('')
searchKW = str('')
sortBy = str('recent')
viewMode = 500
mysettings = xbmcaddon.Addon(id='plugin.video.GayHideout')
profile = mysettings.getAddonInfo('profile')
homep = mysettings.getAddonInfo('path')
webreq = WebUtils.BaseRequest(os.path.join(homep, 'cookies.lwp'))
#######################################URL TEMPLATES################################
redtube = 'http://www.redtube.com/redtube/gay'
xvideos = 'http://www.xvideos.com'
xhamster = 'http://xhamster.com'  # /?content=gay
xhamsteridx = xhamster + '/channels/new-amateur_gays-1.html'
vikiporn = 'http://www.vikiporn.com'
tube8 = 'http://www.tube8.com'
tube8g = tube8 + '/gay'
pornxs = 'http://pornxs.com'
pornxsg = 'http://pornxs.com/twink/sort-time/'
pornxsg1 = 'http://pornxs.com/amateur/sort-time/'
pornxsg2 = 'http://pornxs.com/piss/sort-time/'
pornhd = 'http://www.pornhd.com'
lubetube = 'http://lubetube.com/'
porncom = 'http://gay.porn.com'  # porncom = 'http://www.porn.com'
zbporn = 'http://zbporn.com'
yesxxx = 'http://www.yes.xxx/'
youjizz = 'http://www.youjizz.com'
motherless = 'http://motherless.com'
motherlessg = motherless + '/term/videos/gay?term=gay&type=videos&range=0&size=0&sort=date'
eporner = 'http://www.eporner.com'
epornerg = 'http://www.eporner.com/category/gay/PROD-home/1/'
tubepornclassic = 'http://www.tubepornclassic.com'
efukt = 'http://efukt.com/'
pornhub = 'http://pornhub.com'
pornsocket = 'http://pornsocket.com'
pornsocketg = 'http://www.pornsocket.com/categories-media/21-gay.html?display=list&filter_mediaType=4&limitstart=0&start=0'
hentaigasm = 'http://hentaigasm.com/'
ashemaletube = 'http://www.ashemaletube.com'
youporn = 'http://www.youporn.com'
youporng = 'http://www.youporngay.com'
heavyr = 'http://www.heavy-r.com'
japanesehd = 'http://jav720p.net'
gotporn = 'http://www.gotporn.com'
gotporng = gotporn + '/gay'
empflix = 'http://www.empflix.com'
txxx = 'http://www.txxx.com'
fantasti = 'http://fantasti.cc'
fantastig = fantasti + '/tag/gay/videos/'
fantastigc = fantasti + '/tag/gay/collections/'
upornia = 'http://upornia.com'
yespornplease = 'http://yespornplease.com'
###############################END OF URLS###############################
try:
    searchQ = mysettings.getSetting("lastsearch")
    searchKW = mysettings.getSetting("lastsearchKW")
    viewMode = mysettings.getSetting("viewmode")
    sortBy = mysettings.getSetting("sortby")
except:
    sortBy = 'recent'
    searchQ = ''
    searchKW = 'gay'
    viewMode = 500
    mysettings.setSetting('sortby', sortBy)
    mysettings.setSetting('lastsearch', searchQ)
    mysettings.setSetting('lastsearchKW', searchKW)
    mysettings.setSetting('viewmode', viewMode)
fanart = xbmc.translatePath(os.path.join(homep, 'fanart.jpg'))
icon = xbmc.translatePath(os.path.join(homep, 'icon.png'))
logos = xbmc.translatePath(os.path.join(homep, 'logos\\'))  # subfolder for logos


def menulist():
    try:
        homemenu = xbmc.translatePath(os.path.join(homep, 'resources', 'playlists', 'xxx_playlist.m3u'))
        if xbmcvfs.exists(homemenu):
            mainmenu = open(homemenu, 'r')
            content = mainmenu.read()
            mainmenu.close()
            match = re.compile('#.+,(.+?)\n(.+?)\n').findall(content)
            return match
        else:
            return None
    except:
        return None


def make_request(url):
    source = ""
    try:
        source = webreq.getSource(url)
        #req = urllib2.Request(url)
        #req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0')
        #response = urllib2.urlopen(req, timeout=60)
        #link = response.read()
        #response.close()
        return source
    except urllib2.URLError, e:
        print 'We failed to open "%s".' % url
        if hasattr(e, 'code'):
            print 'We failed with error code - %s.' % e.code
        elif hasattr(e, 'reason'):
            print 'We failed to reach a server.'
            print 'Reason: ', e.reason


def home():
    add_dir('[COLOR white]...[/COLOR] [COLOR pink]|<^ Home ^>|[/COLOR] [COLOR white]...[/COLOR]', '', None, icon,
            fanart)


def main():
    add_dir('Motherless [COLOR green] GAY[/COLOR]', motherlessg, 2, logos + 'motherless.png', fanart)
    add_dir('RedTube [COLOR yellow] GAY[/COLOR]', redtube + '/?page=1', 2, logos + 'redtube.png', fanart)
    add_dir('Xvideos [COLOR green] GAY[/COLOR]', xvideos, 2, logos + 'xvideos.png', fanart)
    add_dir('Tube8 [COLOR yellow] -searchnotgay[/COLOR]', tube8g + '/newest.html', 2, logos + 'tube8.png', fanart)
    add_dir('YouJizz [COLOR yellow] GAY[/COLOR]', youjizz + '/setFilter.php?filter=gay', 2, logos + 'youjizz.png',
            fanart)
    add_dir('YouPornGay [COLOR yellow] GAY[/COLOR]', youporng + '/browse/time/', 2, logos + 'youporn.png', fanart)
    add_dir('ZBPorn [COLOR yellow] GAY[/COLOR]', zbporn + '/categories/gays/', 2, logos + 'zbporn.png', fanart)
    add_dir('GayPornCom [COLOR yellow]-play in srch[/COLOR]', porncom + '/videos?p=1', 2, logos + 'porncom.png', fanart)
    add_dir('Fantasti.cc [COLOR yellow] -search,gay[/COLOR]', fantastig, 2, logos + 'fantasti.png', fanart)
    add_dir('PornHub [COLOR yellow] GAY[/COLOR]', pornhub + '/gayporn/video?page=1', 2, logos + 'pornhub.png', fanart)
    add_dir('Pornsocket [COLOR yellow]-NOsearch-[/COLOR]', pornsocketg, 2, logos + 'pornsocket.png', fanart)
    add_dir('Eporner [COLOR green] GAY[/COLOR]', epornerg, 2, logos + 'eporner.png', fanart)
    add_dir('Upornia [COLOR red] -NOindex,next-[/COLOR]', upornia + '/categories/gay/1/', 2, logos + 'upornia.png',
            fanart)
    add_dir('Gotporn [COLOR red]-cats,next,vidplay-[/COLOR]', gotporng + '/?sort=newest&page=1', 2,
            logos + 'gotporn.png', fanart)
    add_dir('xHamster [COLOR yellow] -[/COLOR]', xhamsteridx, 2, logos + 'xhamster.png', fanart)
    add_dir('Efukt [COLOR red] -NOgay-[/COLOR]', efukt, 2, logos + 'efukt.png', fanart)
    add_dir('Empflix [COLOR red]-NOgay,cats-[/COLOR]', empflix + '/browse.php?category=mr', 2, logos + 'empflix.png',
            fanart)
    add_dir('Heavy-R [COLOR red] -NOseach-[/COLOR]', heavyr + '/porn_videos/gay/', 2, logos + 'heavyr.png', fanart)
    add_dir('Txxx [COLOR yellow] -[/COLOR]', txxx + '/latest-updates/', 2, logos + 'txxx.png', fanart)
    add_dir('YesPornPlease [COLOR yellow] -[/COLOR]', yespornplease + '/?s=date', 2, logos + 'yespornplease.png',
            fanart)
    add_dir('PornXS [COLOR red] -NOcats,semigay-[/COLOR]', pornxsg, 2, logos + 'pornxs.png', fanart)
    add_dir('Yes XXX [COLOR red] -NOgay-[/COLOR]', yesxxx + '?s=recent', 2, logos + 'yes.png', fanart)
    add_dir('Tubepornclassic[COLOR yellow]-[/COLOR]', tubepornclassic + '/latest-updates/', 2, logos + 'tpc.png',
            fanart)
    #add_dir('ViKiPorn [COLOR yellow] -[/COLOR]', vikiporn + '/latest-updates/', 2, logos + 'vikiporn.png', fanart)
    #add_dir('Hentaigasm [COLOR yellow] -[/COLOR]', hentaigasm, 2, logos + 'hentaigasm.png', fanart)
    #add_dir('Jav720p [COLOR yellow] -[/COLOR]', japanesehd + '/jav-recent', 2, logos + 'j720p.png', fanart)
    add_dir('LubeTube [COLOR red] -NOgay-[/COLOR]', lubetube + '/', 2, logos + 'lubetube.png', fanart)
    add_dir('PornHD [COLOR red] -NOgay[/COLOR]', pornhd, 2, logos + 'pornhd.png', fanart)


def search():
    searchText = str('')
    searchQs = str('')
    try:
        searchKW = urllib.unquote_plus(mysettings.getSetting('lastsearchKW'))
        searchQs = urllib.unquote_plus(mysettings.getSetting('lastsearch'))
        if searchKW is not None and len(searchKW) > 1 and searchQs is not None and len(searchQs) > 1:
            searchText = str(searchKW + ' ' + searchQs).strip()
        elif searchKW is None or searchQs is None or len(searchKW) < 2 or len(searchQs) < 2:
            if searchKW is not None and len(searchKW) > 1:
                searchText = searchKW.replace('+', ' ')
            if searchQs is not None and len(searchQs) > 1:
                searchText += searchQs.replace('+', ' ')
        searchText = searchText.strip()
    except:
        searchText = searchKW + ' '
    try:
        if len(searchText) < 1 or searchText is None:
            searchText = ''
            mysettings.setSetting('lastsearchKW', 'gay')
        outmsg = str(
            'KEYWORD:[COLOR yellow]' + searchKW + '[/COLOR] AND [COLOR yellow]' + searchQs + '[/COLOR] |"' + searchText + '"|')
        keyb = xbmc.Keyboard(searchText.replace('+', ' '), outmsg)
        keyb.doModal()
        if (keyb.isConfirmed()):
            inputText = keyb.getText().replace(' ', '+')
            searchQ = inputText.replace(searchKW + '+', '').strip()
            mysettings.setSetting('lastsearch', searchQ)
            searchText = inputText
        if 'ashemaletube' in name:
            url = ashemaletube + '/search/' + searchText + '/page1.html'
            start(url)
        elif 'efukt' in name:
            url = efukt + '/search/' + searchText + '/'
            start(url)
        elif 'eporner' in name:
            url = eporner + '/search/' + searchText
            start(url)
        elif 'gotporn' in name:
            url = gotporng + '/results?sort=newest&search_query=' + searchText + '&page=1&src=ipt:b'
            # url = gotporn + '/results?search_query=' + searchText + '&src=ipt:b'
            start(url)
        elif 'hentaigasm' in name:
            url = hentaigasm + '/?s=' + searchText
            start(url)
        elif 'heavy-r' in name:
            url = heavyr + 'free_porn/' + searchText + '.html'
            start(url)
        elif 'jav720p' in name:
            url = japanesehd + '/search/' + searchText
            start(url)
        elif 'lubetube.com' in name:
            url = lubetube + 'search/title/' + searchText.replace('+', '_') + '/'
            start(url)
        elif 'motherless' in name:
            searchText = searchText.lstrip('gay+')
            if 'Groups' in name:
                url = motherless + '/search/groups?term=' + searchText + '&member=&sort=date&range=0&size=0'
                motherless_groups_cat(url)
            if 'Galleries' in name:
                url = motherless + '/search/Galleries?term=' + searchText + '&member=&sort=date&range=0&size=0'
                motherless_galeries_cat(url)
            else:
                url = motherless + '/term/videos/' + searchText
                # if searchText.find('gay+') == -1:
                #    url = motherless + '/term/videos/gay+' + searchText
                start(url)
        elif '.porn.com' in name:
            searchText = searchText.replace('gay+', '')
            url = porncom + '/videos/search?q=' + searchText
            start(url)
            # media_list(url)
        elif 'pornhd.com' in name:
            url = pornhd + '/search?search=' + searchText
            start(url)
        elif 'pornhub' in name:
            url = pornhub + '/video/search?search=' + searchText
            start(url)
        elif 'pornsocket' in name:
            url = pornsocket + '/media-gallery.html?filter_search=4&filter_tag=' + searchText + '&start=0&limitstart=0&display=list'
            start(url)
        elif 'pornxs' in name:
            url = pornxs + '/search.php?s=' + searchText
            start(url)
            # media_list(url)
        elif 'redtube.com' in name:
            url = redtube + '/?search=' + searchText
            start(url)
        elif 'tube8.com' in name:
            url = tube8 + '/searches.html?q=' + searchText
            start(url)
        elif 'tubepornclassic' in name:
            url = tubepornclassic + '/search/' + searchText + '/'
            start(url)
        elif 'vikiporn.com' in name:
            url = vikiporn + '/search/?q=' + searchText
            start(url)
            # media_list(url)
        elif 'xhamster.com' in name:
            url = xhamster + '/search.php?q=' + searchText + '&qcat=video'
            start(url)
        elif 'xvideos.com' in name:
            url = xvideos + '/?k=' + searchText
            start(url)
        elif 'yes.xxx' in name:
            url = yesxxx + '?s=search&search=' + searchText
            start(url)
        elif 'youjizz.com' in name:
            url = youjizz + '/srch.php?q=' + searchText
            start(url)
        elif 'youporn' in name:
            url = 'http://www.youporngay.com/search/?query=' + searchText
            start(url)
        elif 'zbporn' in name:
            url = zbporn + '/search/?q=' + searchText
            start(url)
        elif 'empflix' in name:
            url = empflix + '/search.php?what=' + searchText
            start(url)
        elif 'txxx' in name:
            url = txxx + '/search/?s=' + searchText
            start(url)
        elif 'fantasti' in name:
            url = fantasti + '/search/' + searchText + '/videos/'
            start(url)
        elif 'upornia' in name:
            url = upornia + '/search/?q=' + searchText
            start(url)
        elif 'yespornplease' in name:
            url = yespornplease + '/search?q=' + searchText
            start(url)
    except:
        pass


def nostart(url):
    if 'ashemaletube' in url:
        add_dir('[COLOR lightgreen]ashemaletube.com     [COLOR red]Search[/COLOR]', ashemaletube, 1,
                logos + 'ashemaletube.png', fanart)
        add_dir('[COLOR lime]Categories[/COLOR]', ashemaletube + '/tags/', 30, logos + 'ashemaletube.png', fanart)
        content = make_request(url)
        match = re.compile(
            '<div class="thumb vidItem" id=".+?">.+?<a href="([^"]*)">.+?src="([^"]*)" alt="([^"]*)".+?>([:\d]+)</span>',
            re.DOTALL).findall(content)
        for url, thumb, name, duration in match:
            name = name.replace('&amp;', '&')
            add_link(name + ' [COLOR lime](' + duration + ')[/COLOR]', url, 4, thumb, fanart)
        try:
            match = re.compile('<link rel="next" href="(.+?)" />').findall(content)
            add_dir('[COLOR blue]Next  Page  >>>>[/COLOR]', ashemaletube + match[0], 2, logos + 'pornhd.png', fanart)
        except:
            pass


def doEmpflix(url):
    content = make_request(url)
    add_dir('[COLOR lightgreen]empflix.com ...[COLOR red]SEARCH[/COLOR]...', empflix, 1, logos + 'empflix.png', fanart)
    add_dir('...[COLOR lime]Categories[/COLOR]...', empflix + '/categories.php', 45, logos + 'empflix.png', fanart)
    add_dir('...[COLOR yellow]Sorting[/COLOR]...', empflix + '/browse.php?category=mr', 46, logos + 'empflix.png',
            fanart)
    restr = r'<div id="remove(.+?)">.+?<a href="([^"]+)".+?><h2>(.+?)</h2>.+?<span class=\"duringTime\">([\d:]+)</span>.+?<img src="([^"]+)"'
    match = re.compile(restr, re.DOTALL).findall(content)
    try:
        for url, dummy, name, duration, thumb in match:
            url = 'http://player.empflix.com/video/' + url
            name = name.replace('&amp;', '&').replace('&quot;', '"').replace('&#39;', '\'')
            content2 = make_request(url)
            match = re.compile('flashvars\.config\s*=\s*escape\("([^"]*)"\);').findall(content2)
            for url in match:
                add_link(name + ' [COLOR lime](' + duration + ')[/COLOR]', url, 4, 'http:' + thumb, fanart)
            match = re.compile('href="([^"]+)">next &gt;&gt;</a>').findall(content)
            add_dir('[COLOR blue]Next  Page  >>>>[/COLOR]', empflix + '/' + match[0], 2, logos + 'empflix.png', fanart)
        return True
    except:
        return False


def doEfukt(url):
    content = make_request(url)
    try:
        add_dir('[COLOR lightgreen]efukt.com     [COLOR red]Search[/COLOR]', efukt, 1, logos + 'efukt.png', fanart)
        restr = r'<div class="thumb"><a href="([^"]+)"><img src="([^"]+)".+?l">([^>]+)</a></p>'
        match = re.compile(restr, re.DOTALL).findall(content)
        for url, thumb, name in match:
            add_link(name, efukt + url, 4, thumb, fanart)
        match = re.compile('<a href=".+?" style="color:#bf4616;">.+?</a><a href="([^"]+)">.+?</a>').findall(content)
        add_dir('[COLOR blue]Next  Page  >>>>[/COLOR]', efukt + match[0], 2, logos + 'efukt.png', fanart)
        return True
    except:
        return False


def doFantastiQueryUrl():
    qok = False
    querystr = 'gay'
    try:
        if searchKW is not None and searchQ is not None:
            if len(searchKW) > 1 and len(searchQ) > 1:
                querystr = '{0}+{1}'.format(searchKW, searchQ.replace(' ', '+'))
                qok = True
        if not qok:
            if searchKW is None or len(searchKW) < 2:
                if searchQ is not None and len(searchQ) > 1:
                    qok = True
                    querystr = searchQ.replace(' ', '+')
                elif searchKW is not None or len(searchKW) > 1:
                    qok = True
                    querystr = searchKW.replace(' ', '+')
                else:
                    querystr = 'gay'
                    qok = True
            else:
                if searchQ is not None and len(searchQ) > 1:
                    qok = True
                    querystr = searchQ.replace(' ', '+')
                else:
                    querystr = 'gay'
                    qok = True
    except:
        querystr = 'gay'
    # urlcoll = 'http://fantasti.cc/ajax/widgets/widget.php?media=videos&filters=upload_improved&sort=latest&pro=0&filter=4&q={0}&limit=100&page=1&tpl=user/videos_search_users.tpl&cache=5&pager=true&div=featured_videos&clear=true&q={0}'.format(querystr)
    # return 'http://fantasti.cc/ajax/widgets/widget.php?media=videos&filters=upload_improved&sort=latest&pro=0&filter=4&q={0}&limit=100&page=1&tpl=user/videos_search_users.tpl&cache=5&pager=true&div=featured_videos&clear=true&q={0}'.format('gay')
    return 'http://fantasti.cc/tag/gay/videos/'


def fatasti_sorting(url):
    home()
    content = make_request(url)
    if 'collections' in url:
        match = re.compile(
            'href="/videos/collections/popular([^"]*)" style=".+?">(Today|This Week|This Month|All Time)</a>',
            re.DOTALL).findall(content)
        for url, name in match:
            add_dir('Popular Videos ' + name, fantasti + '/category/gay/collections/' + url, 48,
                    logos + 'fantasti.png', fanart)  # '/videos/collections/popular'
    else:
        match = re.compile('<a href="(.+?)" style="color:#.+?">(today|this week|this month|all time)</a>',
                           re.DOTALL).findall(content)
        for url, name in match:
            add_dir('Popular Videos ' + name, fantasti + url, 2, logos + 'fantasti.png', fanart)


def fantasti_items(showTags=True):
    strSearch = '.[COLOR red]<: SEARCH [/COLOR]-[COLOR white]Fantasti.cc[/COLOR]- [COLOR red]:>[/COLOR].'
    strSort = '.[COLOR lime](_ SORT _)[/COLOR].'
    strTubelist = '.[COLOR orange](- TUBES -)[/COLOR].'
    strTag = '.[COLOR lime](= TAG [/COLOR]-[COLOR white]{0}[/COLOR]-[COLOR lime] =)[/COLOR].'
    fantastigtubebase = fantasti + '/tag/gay/videos/'
    add_dir(strSearch, fantasti, 1, logos + 'fantasti', fanart)
    add_dir(strSort, fantasti + '/videos/popular/today/', 2, logos + 'fantasti.png', fanart)
    if not showTags:
        pass
    else:
        add_dir(strTubelist, fantastigtubebase, 480, logos + 'fantasti.png', fanart)
        fantastigtagbase = fantasti + '/tag/{0}/videos/upcoming/'
        fantastitaglist = ['amateur+gay', 'gay+twink', 'gays', 'general+gay']
        for tagname in fantastitaglist:
            tagurl = fantastigtagbase.format(tagname)
            tagtitle = tagname.replace('+', ' ').title()
            add_dir(strTag.format(tagtitle), tagurl, 48, logos + 'fantasti.png', fanart)


def fantasti_collections(url):
    #home()
    #fantasti_items()
    content = str(make_request(url)).splitlines()
    html = ''
    for l in content:
        html += l.strip()
    vblocks = re.compile('<p style=.+?>.*?(<a.*?</a>).*?</p>', re.DOTALL).findall(html)
    for vid in vblocks:
        match = re.compile('<a href="([^"]+)"><img.+src="([^"]+)".+?alt="([^"]+)".+>', re.DOTALL).findall(vid)
        for vurl, vthumb, vname in match:
            add_link(vname, fantasti + vurl, 2, vthumb, fanart)


def fantasi_tubevids(url):
    #home()
    #fantasti_items()
    result = webreq.getThumbs(url)
    content = result.get('html')
    match = result.get('videos')
    for vurl, vthumb, vname in enumerate(match):
        add_link(vname, fantasti + vurl, 2, vthumb, fanart)
    #content = str(make_request(url)).splitlines()
    html = ''
    for l in content:
        html += l.strip()
        for vurl, vthumb, vname in match:
            add_link(vname, fantasti + vurl, 2, vthumb, fanart)
            # vblocks = re.compile('<p.*?(<a.*?<img.*?[^>]*?.*?</a>.*?)</p>', re.DOTALL).findall(content)
            # content = make_request(url)
            # match = re.compile(r'href="([^"]+)"><img.+src="([^"]+)".+?alt="([^"]+)".+>', re.DOTALL).findall(content)
            # for vurl, vthumb, vname in match:
            #    add_link(vname, fantasti + vurl, 4, vthumb, fanart)


def fantasti_tubesidx(url):
    home()
    fantasti_items(showTags=False)
    fantastigtubebase = fantasti + '/tag/gay/videos/'
    fantastitubelist = ['undefined/', 'xtube_gay/', 'xhamster/', 'hardsextube/', 'pornhub_gay/', 'redtube/', 'tnaflix/',
                        'xvideos/', 'you_porn/']
    strTube = '.[COLOR orange](- TUBE [/COLOR]-[COLOR white]{0}[/COLOR]-[COLOR orange] -)[/COLOR].'
    for cname in fantastitubelist:
        sname = str(cname).rstrip('/').title()
        add_dir(strTube.format(sname), fantastigtubebase + cname, 2, logos + 'fantasti.png', fanart)


def doFantasti(url):
    # home()
    xbmc.executebuiltin("Notification('FantastiCC URL', '{0}')".format(url))
    try:
        if 'tag' in url:
            if 'tube' in url or '/tag/gay/videos/':
                fantasi_tubevids(url)
            else:
                fantasti_collections(url)
        if 'search' in url:
            content = make_request(url)
            restr = r'href="([^"]+)".+?<img alt="([^"]+)"   src="([^"]+)".+?<span class="v_lenght">([\d:]+)</span>'
            match = re.compile(restr, re.DOTALL).findall(content)
            for url, name, thumb, duration in match:
                url = fantasti + url
                add_dir(name, url, 4, thumb, fanart)
        else:
            # fantasti_collections(url)
            content = make_request(url)
            # match = re.compile(r'href="([^"]+)"><img.+src="([^"]+)".+?alt="([^"]+)".+>', re.DOTALL).findall(content)
            # for vurl, vthumb, vname in match:
            #    add_link(vname, fantasti + vurl, 4, vthumb, fanart)
            match = re.compile('<a href="([^"]+)">next &gt;&gt').findall(content)
            add_dir('...[COLOR red]-->[/COLOR] [COLOR blue]Next Page[/COLOR] [COLOR red]-->[/COLOR]...',
                    fantasti + match[0], 2, logos + 'fantasti.png', fanart)
        return True
    except:
        return False


def doEporner(url):
    content = make_request(url)
    try:
        add_dir('[COLOR lightgreen]eporner.com [COLOR red]Search[/COLOR]', eporner, 1, logos + 'eporner.png', fanart)
        add_dir('[COLOR lime]Categories[/COLOR]', eporner + '/categories/', 21, logos + 'eporner.png', fanart)
        # match = re.compile('</div> <a href="/.+?/([^"]*)" title="(.+?)" id=".+?"> <div id=".+?"> <img id=".+?" src="(.+?)".+?<div class="mbtim">(.+?)</div>').findall(content)
        restr = r'<span>(.+?)</span></div> <a href="/.+?/([^"]*)" title="(.+?)".+?src="(.+?)".+?<div class="mbtim">(.+?)</div>'
        match = re.compile(restr, re.DOTALL).findall(content)
        for dummy, url, name, thumb, duration in match:
            add_link(name + ' [COLOR lime](' + duration + ')[/COLOR]', eporner + '/config5/' + url, 4, thumb, fanart)
        try:
            match = re.compile("<a href='([^']*)' title='Next page'>").findall(content)
            add_dir('[COLOR blue]Next  Page  >>>>[/COLOR]', eporner + match[0], 2, logos + 'eporner.png', fanart)
        except:
            match = re.compile('<a href="([^"]*)" title="Next page">').findall(content)
            add_dir('[COLOR blue]Next  Page  >>>>[/COLOR]', eporner + match[0], 2, logos + 'eporner.png', fanart)
        return True
    except:
        return False


def doPornhd(url):
    try:
        return True
    except:
        return False


def doLubetube(url):
    try:
        return True
    except:
        return False


def doPorncom(url):
    try:
        return True
    except:
        return False


def doMotherless(url):
    try:
        return True
    except:
        return False


def doRedtube(url):
    try:
        return True
    except:
        return False


def doVikiporn(url):
    try:
        return True
    except:
        return False


def doXhamster(url):
    try:
        return True
    except:
        return False


def doTube8(url):
    try:
        return True
    except:
        return False


def doZbporn(url):
    try:
        return True
    except:
        return False


def doPornhub(url):
    try:
        return True
    except:
        return False


def doPornsocket(url):
    try:
        return True
    except:
        return False


def doYoujizz(url):
    try:
        return True
    except:
        return False


def doYouporn(url):
    try:
        return True
    except:
        return False


def doheavyr(url):
    try:
        return True
    except:
        return False


def doJav720(url):
    try:
        return True
    except:
        return False


def doXvideos(url):
    try:
        return True
    except:
        return False


def doYesxxx(url):
    try:
        return True
    except:
        return False


def doTubepornclassic(url):
    try:
        return True
    except:
        return False


def doPornxs(url):
    try:
        return True
    except:
        return False


def doTxxx(url):
    try:
        return True
    except:
        return False


def doUpornia(url):
    try:
        return True
    except:
        return False


def doGotporn(url):
    try:
        return True
    except:
        return False


def doYespornplease(url):
    try:
        return True
    except:
        return False


def doTemplate(url):
    try:
        return True
    except:
        return False


def startNew(url):
    home()
    isok = True
    if 'empflix' in url:
        isok = doEmpflix(url)
    elif 'efukt' in url:
        isok = doEfukt(url)
    elif 'fantasti' in url:
        isok = doFantasti(url)
    elif 'eporner' in url:
        isok = doEporner(url)
    elif 'pornhd' in url:
        isok = doPornhd(url)
    elif 'lubetube' in url:
        isok = doLubetube(url)
    elif 'porn.com' in url:
        isok = doPorncom(url)
    elif 'motherless' in url:
        isok = doMotherless(url)
    elif 'redtube' in url:
        isok = doRedtube(url)
    elif 'viki' in url:
        isok = doVikiporn(url)
    elif 'xhamster' in url:
        isok = doXhamster(url)
    elif 'tube8' in url:
        isok = doTube8(url)
    elif 'zbporn' in url:
        isok = doZbporn(url)
    elif 'pornsocket' in url:
        isok = doPornsocket(url)
    elif 'youjizz' in url:
        isok = doYoujizz(url)
    elif 'youporn' in url:
        isok = doYouporn(url)
    elif 'heavy' in url:
        isok = doheavyr(url)
    elif 'jav720' in url:
        isok = doJav720(url)
    elif 'xvideo' in url:
        isok = doXvideos(url)
    elif 'yes.xxx' in url:
        isok = doYesxxx(url)
    elif 'tubepornclassic' in url:
        isok = doTubepornclassic(url)
    elif 'pornxs' in url:
        isok = doPornxs(url)
    elif 'txxx' in url:
        isok = doTxxx(url)
    elif 'upornia' in url:
        isok = doUpornia(url)
    elif 'gotporn' in url:
        isok = doGotporn(url)
    elif 'yespornplease' in url:
        isok = doYespornplease(url)
    else:
        isok = False
    ############# COMPLETED ALL SITE SPECIFIC PARSING ##################
    strurlmin = str(urllib.unquote(url.replace('http://', '').replace('www.', '').strip('/')))
    msgOut = str("Notification('Error', 'Failed to parse {0}')".format(strurlmin))
    if not isok:
        xbmc.executebuiltin(msgOut)
    xbmc.executebuiltin("Container.SetViewMode({0})".format(viewMode))


def start(url):
    home()
    isok = False
    if 'fantasti' in url:
        isok = doFantasti(url)
    elif 'efukt' in url:
        content = make_request(url)
        add_dir('[COLOR lightgreen]efukt.com     [COLOR red]Search[/COLOR]', efukt, 1, logos + 'efukt.png', fanart)
        match = re.compile('<div class="thumb"><a href="([^"]+)"><img src="([^"]+)".+?l">([^>]+)</a></p>',
                           re.DOTALL).findall(content)
        for url, thumb, name in match:
            add_link(name, efukt + url, 4, thumb, fanart)
        match = re.compile('<a href=".+?" style="color:#bf4616;">.+?</a><a href="([^"]+)">.+?</a>').findall(content)
        add_dir('[COLOR blue]Next  Page  >>>>[/COLOR]', efukt + match[0], 2, logos + 'efukt.png', fanart)
    elif 'eporner' in url:
        content = make_request(url)
        add_dir('[COLOR lightgreen]eporner.com     [COLOR red]Search[/COLOR]', eporner, 1, logos + 'eporner.png',
                fanart)
        add_dir('[COLOR lime]Categories[/COLOR]', eporner + '/categories/', 21, logos + 'eporner.png', fanart)
        # match = re.compile('</div> <a href="/.+?/([^"]*)" title="(.+?)" id=".+?"> <div id=".+?"> <img id=".+?" src="(.+?)".+?<div class="mbtim">(.+?)</div>').findall(content)
        match = re.compile(
            '<span>(.+?)</span></div> <a href="/.+?/([^"]*)" title="(.+?)".+?src="(.+?)".+?<div class="mbtim">(.+?)</div>',
            re.DOTALL).findall(content)
        for dummy, url, name, thumb, duration in match:
            add_link(name + ' [COLOR lime](' + duration + ')[/COLOR]', eporner + '/config5/' + url, 4, thumb, fanart)
        try:
            match = re.compile("<a href='([^']*)' title='Next page'>").findall(content)
            add_dir('[COLOR blue]Next  Page  >>>>[/COLOR]', eporner + match[0], 2, logos + 'eporner.png', fanart)
        except:
            match = re.compile('<a href="([^"]*)" title="Next page">').findall(content)
            add_dir('[COLOR blue]Next  Page  >>>>[/COLOR]', eporner + match[0], 2, logos + 'eporner.png', fanart)
    elif 'fantasti' in url:
        content = make_request(url)
        add_dir('[COLOR lightgreen]Fantastic.com     [COLOR red]Search[/COLOR]', fantasti, 1, logos + 'fantasti',
                fanart)
        add_dir('[COLOR lime]Collection[/COLOR]', fantasti + '/category/gay/collections/videos/', 48,
                logos + 'fantasti.png', fanart)  # '/videos/collections/popular/today/'
        add_dir('[COLOR lime]Sorting [/COLOR]', fantasti + '/videos/popular/today/', 49, logos + 'fantasti.png', fanart)
        if 'search' in url:
            match = re.compile(
                r'href="([^"]+)".+?<img alt="([^"]+)"   src="([^"]+)".+?<span class="v_lenght">([\d:]+)</span>',
                re.DOTALL).findall(content)
            for url, name, thumb, duration in match:
                url = fantasti + url
                add_dir(name, url, 4, thumb, fanart)
        else:
            match = re.compile(r'href="([^"]+)"><img src="([^"]+)".+?alt="([^"]+)"').findall(content)
            for url, thumb, name in match:
                url = fantasti + url
                add_link(name, url, 4, thumb, fanart)
        try:
            match = re.compile('<a href="([^"]+)">next &gt;&gt').findall(content)
            add_dir('[COLOR blue]Next  Page  >>>>[/COLOR]', fantasti + match[0], 2, logos + 'fantasti.png', fanart)
        except:
            pass
    elif 'gotporn' in url:
        content = make_request(url)
        add_dir('[COLOR lightgreen]gotporn.com     [COLOR red]Search[/COLOR]', gotporn, 1, logos + 'gotporn.png',
                fanart)
        add_dir('[COLOR lime]Categories[/COLOR]', gotporng + '/categories?src=hm', 40, logos + 'gotporn.png', fanart)
        add_dir('[COLOR lime]Change Content[/COLOR]', gotporn, 41, logos + 'gotporn.png', fanart)
        match = re.compile(
            r'<a class=".+?" href="([^"]+)".+?data-title="([^"]+)">.+?<span class="duration">.+?([\d:]+).+?</span>.+?<img src=\'(.+?)\'',
            re.DOTALL).findall(content)
        for url, name, duration, thumb in match:
            add_link(name + ' [COLOR lime](' + duration + ')[/COLOR]', url, 4, thumb, fanart)
        try:
            if "gay" in url:
                match = re.compile(
                    '<a href="([^"]+)" class="btn btn-secondary"><i class="icon icon-angle-right"></i></a>').findall(
                    content)
                add_dir('[COLOR blue]Next  Page  >>>>[/COLOR]', gotporng + '/gay/' + match[0], 2, logos + 'gotporn.png',
                        fanart)
            else:
                match = re.compile(
                    '<a href="([^"]+)" class="btn btn-secondary"><i class="icon icon-angle-right"></i></a>').findall(
                    content)
                add_dir('[COLOR blue]Next  Page  >>>>[/COLOR]', gotporn + match[0], 2, logos + 'gotporn.png', fanart)
        except:
            pass
    elif 'hentaigasm' in url:
        add_dir('[COLOR lime]hentaigasm     [COLOR red]Search[/COLOR]', hentaigasm, 1, logos + 'hentaigasm.png', fanart)
        add_dir('[COLOR lime]Categories[/COLOR]', hentaigasm, 29, logos + 'hentaigasm.png', fanart)
        content = make_request(url)
        match = re.compile('title="(.+?)" href="(.+?)">\s*\s*.+?\s*\s*.+?<img src="(.+?)"').findall(content)
        for name, url, thumb in match:
            thumb = thumb.replace(' ', '%20')
            if "Raw" in name:
                add_link('[COLOR lime] [Raw] [/COLOR]' + name, url, 4, thumb, fanart)
            else:
                add_link('[COLOR yellow] [Subbed] [/COLOR]' + name, url, 4, thumb, fanart)
        try:
            match = re.compile("<a href='([^']*)' class=\"next\">»").findall(content)
            add_dir('[COLOR blue]Next  Page  >>>>[/COLOR]', match[0], 2, logos + 'hentaigasm.png', fanart)
        except:
            pass
    elif 'heavy-r' in url:
        add_dir('[COLOR lightgreen]heavy-r       [COLOR red]Search[/COLOR]', heavyr, 1, logos + 'heavyr.png', fanart)
        add_dir('[COLOR lime]Categories[/COLOR]', heavyr + '/categories/', 33, logos + 'heavyr.png', fanart)
        content = make_request(url)
        match = re.compile(
            '<a href="([^"]+)" class="image">.+?<img src="([^"]+)".+?alt="([^"]+)".+?<span class="duration"><i class="fa fa-clock-o"></i> ([\d:]+)</span>',
            re.DOTALL).findall(content)
        for url, thumb, name, duration in match:
            add_link(name + ' [COLOR lime](' + duration + ')[/COLOR]', heavyr + url, 4, thumb, fanart)
        try:
            match = re.compile('<a href="([^"]*)">Next</a>').findall(content)
            add_dir('[COLOR blue]Next  Page  >>>>[/COLOR]', heavyr + match[0], 2, logos + 'heavyr.png', fanart)
        except:
            pass
    elif 'jav720p' in url:
        add_dir('[COLOR lightgreen]jav720p.net     [COLOR red]Search[/COLOR]', japanesehd, 1, logos + 'j720p.png',
                fanart)
        add_dir('[COLOR lime]Genres[/COLOR]', japanesehd + '/categories/genres', 34, logos + 'j720p.png', fanart)
        add_dir('[COLOR lime]Models[/COLOR]', japanesehd + '/categories/models', 35, logos + 'j720p.png', fanart)
        add_dir('[COLOR lime]Makers[/COLOR]', japanesehd + '/categories/makers', 36, logos + 'j720p.png', fanart)
        content = make_request(url)
        match = re.compile(
            'title=".+?"> <img src="([^"]*)" alt=".+?" title="([^"]*)"/> <div class=".+?"> </div> </a> <span class="duration">([^"]*)</span> <span class="quality">HD</span> </div> <div class="item-detail"> <h4><a href="([^"]*)"').findall(
            content)
        for thumb, name, duration, url in match:
            name = name.replace('&amp;', '&').replace('&quot;', '"').replace('&#39;', '\'')
            add_link(name + ' [COLOR lime](' + duration + ')[/COLOR]', url, 4, thumb, fanart)
        try:
            match = re.compile('<a href="([^"]*)" title="Next">Next</a></li><li>').findall(content)
            add_dir('[COLOR blue]Next  Page  >>>>[/COLOR]', match[0], 2, logos + 'j720p.png', fanart)
        except:
            pass
    elif 'lubetube' in url:
        content = make_request(url)
        add_dir('[COLOR lightgreen]lubetube.com     [COLOR red]Search[/COLOR]', lubetube, 1, logos + 'lubetube.png',
                fanart)
        add_dir('[COLOR lime]Categories[/COLOR]', lubetube + 'categories', 15, logos + 'lubetube.png', fanart)
        add_dir('[COLOR lime]Pornstars[/COLOR]', lubetube + 'pornstars', 12, logos + 'lubetube.png', fanart)
        match = re.compile('href="(.+?)" title="(.+?)"><img src="(.+?)".+?Length: (.+?)<').findall(content)
        for url, name, thumb, duration in match:
            add_link(name + '[COLOR lime] (' + duration + ')[/COLOR]', url, 4, thumb, fanart)
        try:
            match = re.compile('<a class="next" href="([^"]*)">Next</a>').findall(content)
            add_dir('[COLOR blue]Next  Page  >>>>[/COLOR]', lubetube + match[0], 2, logos + 'lubetube.png', fanart)
        except:
            pass
    elif 'motherless' in url:
        content = make_request(url)
        ###Search in def search(): and media_list(url)
        add_dir('[COLOR lightgreen]motherless.com     [COLOR red]Search[/COLOR]', motherless, 1,
                logos + 'motherless.png', fanart)
        ####Subfolders
        add_dir('[COLOR lime]Being watched now[/COLOR]', motherless + '/live/videos', 61, logos + 'motherless.png',
                fanart)
        add_dir('[COLOR lime]Sorting[/COLOR]', motherless + '/videos/', 44, logos + 'motherless.png', fanart)
        add_dir('[COLOR magenta]Galleries[/COLOR]', motherless + '/galleries/updated?page=1', 60,
                logos + 'motherless.png', fanart)
        add_dir('[COLOR magenta]Groups[/COLOR]', motherless + '/groups?s=u', 62, logos + 'motherless.png', fanart)
        ###sending video URL to resolve_url(url)
        match = re.compile(
            'data-frames="12">.+?<a href="([^"]+)".+?src="([^"]+)".+?alt="([^"]+)".+?caption left">([:\d]+)</div>',
            re.DOTALL).findall(content)
        for url, thumb, name, duration in match:
            name = name.replace('Shared by ', '').replace('&quot;', '"').replace('&#39;', '\'')
            if 'motherless' in url:
                add_link(name + ' [COLOR lime](' + duration + ')[/COLOR]', url, 4, thumb, fanart)
            else:
                add_link(name + ' [COLOR lime](' + duration + ')[/COLOR]', motherless + url, 4, thumb, fanart)
        ###Next Button
        try:
            match = re.compile('<a href="([^"]*)" class="pop" rel="[1-9999]">NEXT &raquo;</a></div>').findall(content)
            add_dir('[COLOR blue]Next  Page  >>>>[/COLOR]', motherless + match[0], 2, logos + 'motherless.png', fanart)
        except:
            pass
    elif '.porn.com' in url:
        content = make_request(url)
        add_dir('[COLOR lightblue]gay.porn.com     [COLOR red]Search[/COLOR]', porncom, 1, logos + 'porncom.png',
                fanart)
        add_dir('[COLOR lime]Categories[/COLOR]', porncom + '/categories', 14, logos + 'porncom.png', fanart)
        match = re.compile(
            '<a href=".+/videos/(.+?)" class=".+?"><img src="(.+?)" /><span class=".+?">.+?class="duration">(.+?)</.+?class="title">(.+?)</a>').findall(
            content)
        for url, thumb, duration, name in match:
            add_link(name + ' [COLOR lime](' + duration + ')[/COLOR]', porncom + '/videos/' + url, 4, thumb, fanart)
        try:
            match = re.compile('</span><a href="([^"]*)" class="btn nav">Next').findall(content)
            add_dir('[COLOR blue]Next  Page  >>>>[/COLOR]', porncom + match[0], 2, logos + 'porncom.png', fanart)
        except:
            pass
    elif 'pornhd' in url:
        add_dir('[COLOR lightgreen]pornhd.com     [COLOR red]Search[/COLOR]', pornhd, 1, logos + 'pornhd.png', fanart)
        add_dir('[COLOR lime]Categories[/COLOR]', pornhd + '/category', 19, logos + 'pornhd.png', fanart)
        add_dir('[COLOR lime]Pornstars[/COLOR]', pornhd + '/pornstars?order=video_count&gender=female', 20,
                logos + 'pornhd.png', fanart)
        content = make_request(url)
        match = re.compile(
            '<a class="thumb" href="(.+?)" >\s*<img class="lazy"\s*alt="(.+?)"\s*src=".+?"\s*data-original="(.+?)" width=".+?" height=".+?" />\s*<div class="meta transition">\s*<time>(.+?)</time>').findall(
            content)
        for url, name, thumb, duration in match:
            add_link(name + ' [COLOR lime](' + duration + ')[/COLOR]', pornhd + url, 4, thumb, fanart)
        try:
            match = re.compile('<link rel="next" href="([^"]*)" />').findall(content)
            add_dir('[COLOR blue]Next  Page  >>>>[/COLOR]', pornhd + match[0], 2, logos + 'pornhd.png', fanart)
        except:
            pass
    elif 'pornhub' in url:
        content = make_request(url)
        add_dir('[COLOR lightgreen]pornhub.com     [COLOR red]Search[/COLOR]', pornhub, 1, logos + 'pornhub.png',
                fanart)
        add_dir('[COLOR lime]Categories[/COLOR]', pornhub + '/categories', 25, logos + 'pornhub.png', fanart)
        match = re.compile(
            '<li class="videoblock.+?<a href="([^"]+)" title="([^"]+)".+?<var class="duration">([^<]+)<.*?data-mediumthumb="([^"]+)"',
            re.DOTALL).findall(content)
        for url, name, duration, thumb in match:
            add_link(name + ' [COLOR lime](' + duration + ')[/COLOR]', pornhub + url, 4, thumb, fanart)
        match = re.compile('<li class="page_next"><a href="([^"]+)" class="orangeButton">Next</a></li>',
                           re.DOTALL).findall(content)
        add_dir('[COLOR blue]Next  Page  >>>>[/COLOR]', pornhub + match[0].replace('&amp;', '&'), 2,
                logos + 'pornhub.png', fanart)
    elif 'pornsocket' in url:
        content = make_request(url)
        add_dir('[COLOR lightgreen]pornsocket.com ? [COLOR red]Search[/COLOR]', pornsocket, 1,
                logos + 'pornsocket.png', fanart)
        add_dir('[COLOR lime]Categories[/COLOR]', pornsocket + '/categories-media.html', 26, logos + 'pornsocket.png',
                fanart)
        match = re.compile(
            '<div class="media-duration">\s*([^<]+)</div>\s*<a href="([^"]+)"> <img src="([^"]+)" border="0" alt="([^"]+)"').findall(
            content)
        for duration, url, thumb, name in match:
            add_link(name + ' [COLOR lime](' + duration + ')[/COLOR]', pornsocket + url, 4, pornsocket + thumb, fanart)
        match = re.compile('><a title="Next" href="([^"]+)" class="pagenav">Next</a>', re.DOTALL).findall(content)
        add_dir('[COLOR blue]Next  Page  >>>>[/COLOR]', pornsocket + match[0].replace('&amp;', '&'), 2,
                logos + 'pornsocket.png', fanart)
    elif 'pornxs' in url:
        content = make_request(url)
        add_dir('[COLOR lightgreen]pornxs.com     [COLOR red]Search[/COLOR]', pornxs, 1, logos + 'pornxs.png', fanart)
        add_dir('[COLOR lime]TWINKS[/COLOR]', pornxsg, 2, logos + 'pornxs.png', fanart)
        add_dir('[COLOR lime]AMATEURS[/COLOR]', pornxsg1, 2, logos + 'pornxs.png', fanart)
        add_dir('[COLOR lime]PISS[/COLOR]', pornxsg2, 2, logos + 'pornxs.png', fanart)
        add_dir('[COLOR lime]Categories[/COLOR]', pornxs + '/categories.php', 39, logos + 'pornxs.png', fanart)
        match = re.compile(
            '<a href="([^"]+)"><div class="video-container".+?<img src="([^"]+)" alt="([^"]+)".+?</div><div class="time">([:\d]+)</div>',
            re.DOTALL).findall(content)
        for url, thumb, name, duration in match:
            add_link(name + ' [COLOR lime](' + duration + ')[/COLOR]', pornxs + url, 4, thumb, fanart)
        try:
            match = re.compile('<a class="pagination-next" href="([^"]*)"><span></span></a></li> ').findall(content)
            add_dir('[COLOR blue]Next  Page  >>>>[/COLOR]', pornxs + match[0], 2, logos + 'pornxs.png', fanart)
        except:
            pass
    elif 'redtube' in url:
        content = make_request(url)
        add_dir('[COLOR lightgreen]redtube.com     [COLOR red]Search[/COLOR]', redtube, 1, logos + 'redtube.png',
                fanart)
        add_dir('[COLOR lime]Channels[/COLOR]', redtube + '/channel', 10, logos + 'redtube.png', fanart)
        match = re.compile(
            'window.location.href =\'([^"]+)\'">([:\d]+)</span>.+?<img title="([^"]+)".+?data-src="([^"]+)"',
            re.DOTALL).findall(content)
        for url, duration, name, thumb in match:
            name = name.replace('&#39;', ' ').replace('&amp;', '&').replace('&quot;', '"').replace('	', '')
            add_link(name + ' [COLOR lime](' + duration + ')[/COLOR]', redtube + url, 4, thumb, fanart)
        try:
            match = re.compile('rel="next" href="([^"]+)">').findall(content)
            add_dir('[COLOR blue]Next  Page  >>>>[/COLOR]', match[0], 2, logos + 'redtube.png', fanart)
        except:
            pass
    elif 'tube8' in url:
        content = make_request(url)
        add_dir('[COLOR lightgreen]tube8.com     [COLOR red]Search[/COLOR]', tube8, 1, logos + 'tube8.png', fanart)
        add_dir('[COLOR lime]Categories[/COLOR]', tube8 + '/categories.html', 22, logos + 'tube8.png', fanart)
        match = re.compile(
            'class="thumb_box">.+?<a href="([^"]+)".+?src="([^"]+)" alt="([^"]+)".+?video_duration">([:\d]+)</div>',
            re.DOTALL).findall(content)
        for url, thumb, name, duration in match:
            add_link(name + ' [COLOR lime](' + duration + ')[/COLOR]', url, 4, thumb, fanart)
        match = re.compile('<link rel="next" href="([^"]*)">').findall(content)
        add_dir('[COLOR blue]Next  Page  >>>>[/COLOR]', match[0], 2, logos + 'tube8.png', fanart)
    elif 'tubepornclassic' in url:
        content = make_request(url)
        add_dir('[COLOR lightgreen]tubepornclassic     [COLOR red]Search[/COLOR]', tubepornclassic, 1,
                logos + 'tubepornclassic.png', fanart)
        add_dir('[COLOR lime]Categories[/COLOR]', tubepornclassic + '/categories/', 38, logos + 'tubepornclassic.png',
                fanart)
        match = re.compile(
            '<div class="item  ">.+?<a href="([^"]+)" title="([^"]+)".*?original="([^"]+)".*?duration">([^<]+)<',
            re.DOTALL).findall(content)
        for url, name, thumb, duration in match:
            add_link(name + ' [COLOR lime](' + duration + ')[/COLOR]', url, 4, thumb, fanart)
        try:
            match = re.compile(
                '<a href="([^"]*)" data-action=".+?" data-container-id=".+?" data-block-id=".+?" data-parameters=".+?" title=\"Next Page\">Next</a>').findall(
                content)
            add_dir('[COLOR blue]Next  Page  >>>>[/COLOR]', tubepornclassic + match[0], 2,
                    logos + 'tubepornclassic.png', fanart)
        except:
            pass
    elif 'txxx' in url:
        content = make_request(url)
        add_dir('[COLOR lightgreen]txxx   [COLOR red]Search[/COLOR]', txxx, 1, logos + 'txxx.png', fanart)
        add_dir('[COLOR lime]Categories[/COLOR]', 'http://m.txxx.com/categories/', 47, logos + 'txxx.png', fanart)
        match = re.compile(
            '<a href="([^"]+)" class="js-thumb-pagination".+?<img src="([^"]+)" alt="([^"]+)".+?<div class="thumb__duration">([^<]+)</div>',
            re.DOTALL).findall(content)
        for url, thumb, name, duration in match:
            add_link(name + ' [COLOR lime](' + duration + ')[/COLOR]', url, 4, thumb, fanart)
        try:
            match = re.compile('<a class=" btn btn--size--l btn--next" href="([^"]+)" title="Next Page"').findall(
                content)
            add_dir('[COLOR blue]Next  Page  >>>>[/COLOR]', txxx + match[0], 2, logos + 'txxx.png', fanart)
        except:
            pass
    elif 'upornia' in url:
        content = make_request(url)
        add_dir('[COLOR lightgreen]upornia   [COLOR red]Search[/COLOR]', upornia, 1, logos + 'upornia.png', fanart)
        add_dir('[COLOR lime]Categories[/COLOR]', upornia + '/categories/', 50, logos + 'upornia.png', fanart)
        add_dir('[COLOR lime]Models[/COLOR]', upornia + '/models/', 51, logos + 'upornia.png', fanart)
        match = re.compile(
            '<a class="thumbnail thumbnail-pagination" href="([^"]*)".+?<img src="([^"]+)" alt="([^"]+)">.+?<div class="thumbnail__info__right">.+?([:\d]+).+?</div>',
            re.DOTALL).findall(content)
        for url, thumb, name, duration in match:
            add_link(name + ' [COLOR lime](' + duration + ')[/COLOR]', url, 4, thumb, fanart)
        try:
            match = re.compile('<li class="next">.+?<a href="(.+?)"', re.DOTALL).findall(content)
            add_dir('[COLOR blue]Next  Page  >>>>[/COLOR]', upornia + match[0], 2, logos + 'upornia.png', fanart)
        except:
            pass
    elif 'vikiporn' in url:
        content = make_request(url)
        add_dir('[COLOR lightgreen]vikiporn.com     [COLOR red]Search[/COLOR]', vikiporn, 1, logos + 'vikiporn.png',
                fanart)
        add_dir('[COLOR lime]Categories[/COLOR]', vikiporn + '/categories/', 16, logos + 'vikiporn.png', fanart)
        match = re.compile(
            '<a href="(.+?)">\s*<div class=".+?">\s*<img style=".+?" class=".+?"  src=".+?" data-original="(.+?)" alt="(.+?)" onmouseover=".+?" onmouseout=".+?">\s*<span class=".+?">(.+?)</span>').findall(
            content)
        for url, thumb, name, duration in match:
            add_link(name + ' [COLOR lime](' + duration + ')[/COLOR]', url, 4, thumb, fanart)
        match = re.compile('<a href="([^"]*)">NEXT</a>').findall(content)
        add_dir('[COLOR blue]Next  Page  >>>>[/COLOR]', vikiporn + match[0], 2, logos + 'vikiporn.png', fanart)
    elif 'xhamster' in url:
        content = make_request(url)
        add_dir('[COLOR lightgreen]xhamster.com     [COLOR red]Search[/COLOR]', xhamster, 1, logos + 'xhamster.png',
                fanart)
        add_dir('[COLOR lime]Categories[/COLOR]', xhamster + '/channels.php', 17, logos + 'xhamster.png', fanart)
        add_dir('[COLOR lime]Rankings[/COLOR]', xhamster + '/rankings/weekly-top-viewed.html', 42,
                logos + 'xhamster.png', fanart)
        add_dir('[COLOR lime]Change Content[/COLOR]', xhamster, 24, logos + 'xhamster.png', fanart)
        match = re.compile(
            'href="([^"]*)" class=".+?"><img src=\'(.+?)\' class=\'.+?\' alt="(.+?)"/>.+?<b>(.+?)</b>').findall(content)
        for url, thumb, name, duration in match:
            name = name.replace('&amp;', '&').replace('&quot;', '"').replace('&#39;', '\'')
            if '?from=video_promo' in url:
                pass
            else:
                add_link(name + ' [COLOR lime](' + duration + ')[/COLOR]', url, 4, thumb, fanart)
        match = re.compile('<div id="cType"><div class="([^"]*)"></div>').findall(content)
        if "iconL iconTrans" in match:
            match = re.compile('<link rel="next" href="([^"]*)"><link rel="dns-prefetch"').findall(content)
            add_dir('[COLOR blue]Next  Page  >>>>[/COLOR]', match[0] + '?content=shemale', 2, logos + 'xhamster.png',
                    fanart)
        if "iconL iconGays" in match:
            match = re.compile('<link rel="next" href="([^"]*)"><link rel="dns-prefetch"').findall(content)
            add_dir('[COLOR blue]Next  Page  >>>>[/COLOR]', match[0] + '?content=gay', 2, logos + 'xhamster.png',
                    fanart)
        else:
            match = re.compile('<link rel="next" href="([^"]*)"><link rel="dns-prefetch"').findall(content)
            add_dir('[COLOR blue]Next  Page  >>>>[/COLOR]', match[0], 2, logos + 'xhamster.png', fanart)
    elif 'xvideos' in url:
        content = make_request(url)
        add_dir('[COLOR lightgreen]xvideos.com     [COLOR red]Search[/COLOR]', xvideos, 1, logos + 'xvideos.png',
                fanart)
        add_dir('[COLOR lime]Categories[/COLOR]', xvideos, 27, logos + 'xvideos.png', fanart)
        add_dir('[COLOR lime]Pornstars[/COLOR]', xvideos + '/pornstars', 32, logos + 'xvideos.png', fanart)
        match = re.compile('<a href="([^"]*)"><img src="([^"]*)".+? title="([^"]*)">.+?"duration">\(([^"]*)\)</span>',
                           re.DOTALL).findall(content)
        for url, thumb, name, duration in match:
            name = name.replace('&amp;', '&').replace('&quot;', '"').replace('&#39;', '`')
            add_link(name + ' [COLOR lime](' + duration + ')[/COLOR]', xvideos + url, 4, thumb, fanart)
        try:
            match = re.compile('<a href="([^"]*)" class=\"no-page\"').findall(content)
            add_dir('[COLOR blue]Next  Page  >>>>[/COLOR]', xvideos + match[0], 2, logos + 'xvideos.png', fanart)
        except:
            pass
    elif 'youjizz' in url:
        content = make_request(url)
        add_dir('[COLOR lightgreen]youjizz.com  [COLOR red]Search[/COLOR]', youjizz, 1, logos + 'youjizz.png', fanart)
        add_dir('[COLOR lime]Categories[/COLOR]', youjizz + '/newest-clips/1.html', 28, logos + 'youjizz.png', fanart)
        match = re.compile(
            '<a class="frame" href=\'([^\']+)\'.+?data-original="([^"]+)".+?<span id="title1">([^"]+)</span>.+?>([:\d]+)</span>',
            re.DOTALL).findall(content)
        for url, thumb, name, duration in match:
            add_link(name + ' [COLOR lime](' + duration + ')[/COLOR]', youjizz + url, 4, thumb, fanart)
        match = re.compile("<a href='([^']+)'>Next", re.DOTALL).findall(content)
        add_dir('[COLOR blue]Next  Page  >>>>[/COLOR]', youjizz + match[0], 2, logos + 'youjizz.png', fanart)
    elif 'youporn' in url:
        add_dir('[COLOR lightgreen]youporn.com  [COLOR red]Search[/COLOR]', youporn, 1, logos + 'youporn.png', fanart)
        add_dir('[COLOR lime]Categories[/COLOR]', youporng + '/categories/', 31, logos + 'youporn.png', fanart)
        add_dir('[COLOR lime]Sorting[/COLOR]', youporn, 43, logos + 'youporn.png', fanart)
        content = make_request(url)
        match = re.compile(
            '<a href="([^"]+)" class=\'video-box-image\' title="([^"]+)" >.+?<img src="([^"]+)".+?video-box-duration">.+?([:\d]+)	</span>',
            re.DOTALL).findall(content)
        for url, name, thumb, duration in match:
            add_link(name + ' [COLOR lime](' + duration + ')[/COLOR]', youporn + url, 4, thumb, fanart)
        try:
            match = re.compile('<link rel="next" href="([^"]*)" />').findall(content)
            add_dir('[COLOR blue]Next  Page  >>>>[/COLOR]', match[0], 2, logos + 'youporn.png', fanart)
        except:
            pass
    elif 'yespornplease' in url:
        content = make_request(url)
        add_dir('[COLOR lightgreen]yespornplease    [COLOR red]Search[/COLOR]', yespornplease, 1, logos + 'yespp.png',
                fanart)
        add_dir('[COLOR lime]Categories[/COLOR]', yespornplease + '/categories', 52, logos + 'yespp.png', fanart)
        if 'search' in url:
            match = re.compile(
                '<a style="text-decoration:none;" href="([^"]*)">.+?<img src="([^"]*)".+?alt="([^"]*)".+?<div class="duration">([:\d]+)</div>',
                re.DOTALL).findall(content)
            for url, thumb, name, duration in match:
                name = name.replace('&amp;', '&').replace('&quot;', '"').replace('&#39;', '\'').replace('	', '')
                add_link(name + '[COLOR lime] (' + duration + ')[/COLOR]', yespornplease + url, 4, thumb, fanart)
        else:
            match = re.compile(
                'class="video-link" href="([^"]*)">.+?<img src="([^"]*)".+?alt="([^"]*)".+?<div class="duration">([:\d]+)</div>',
                re.DOTALL).findall(content)
            for url, thumb, name, duration in match:
                name = name.replace('&amp;', '&').replace('&quot;', '"').replace('&#39;', '\'').replace('	', '')
                add_link(name + '[COLOR lime] (' + duration + ')[/COLOR]', yespornplease + url, 4, thumb, fanart)
        try:
            match = re.compile('<a href="(.+?)" class="prevnext">Next &raquo;</a></li>').findall(content)
            add_dir('[COLOR blue]Next  Page  >>>>[/COLOR]', yespornplease + match[0], 2, logos + 'yespp.png', fanart)
        except:
            pass
    elif 'yes.xxx' in url:
        content = make_request(url)
        add_dir('[COLOR lightgreen]yes.xxx    [COLOR red]Search[/COLOR]', yesxxx, 1, logos + 'yes.png', fanart)
        add_dir('[COLOR lime]Categories[/COLOR]', yesxxx + '?s=tags', 37, logos + 'yes.png', fanart)
        match = re.compile(
            'href="/([^"]*)" title="([^"]*)"><img src="([^"]*)" /><br></a></div><div class="dur">([:\d]+)</div>').findall(
            content)
        for url, name, thumb, duration in match:
            name = name.replace('&amp;', '&').replace('&quot;', '"').replace('&#39;', '\'').replace('	', '')
            add_link(name + '[COLOR lime] (' + duration + ')[/COLOR]', yesxxx + url, 4, thumb, fanart)
        match = re.compile('<li><a href="(.+?)">Next</a></li>').findall(content)
        add_dir('[COLOR blue]Next  Page  >>>>[/COLOR]', yesxxx + match[0], 2, logos + 'yes.png', fanart)
    elif 'zbporn' in url:
        content = make_request(url)
        add_dir('[COLOR lightgreen]zbporn.com    [COLOR red]Search[/COLOR]', zbporn, 1, logos + 'zbporn.png', fanart)
        add_dir('[COLOR lime]Categories[/COLOR]', zbporn + '/categories/', 23, logos + 'zbporn.png', fanart)
        match = re.compile(
            'href="([^"]*)" data-rt=".+?"><img src="([^"]+)" alt="([^"]+)">.+?<span class="length">([:\d]+)</span>',
            re.DOTALL).findall(content)
        for url, thumb, name, duration in match:
            add_link(name + ' [COLOR lime](' + duration + ')[/COLOR]', url, 4, thumb, fanart)
        match = re.compile('</li>\s*<li><a data-page=".+?" href="(.+?)">.+?</a></li>\s*<li><a').findall(content)
        add_dir('[COLOR blue]Next  Page  >>>>[/COLOR]', zbporn + match[0], 2, logos + 'zbporn.png', fanart)
    else:
        startNew(url)


def pornhd_categories(url):
    home()
    content = make_request(url)
    match = re.compile('<a href="([^"]*)">.+?alt="([^"]*)".+?data-original="([^"]*)"', re.DOTALL).findall(content)
    for url, name, thumb in match:
        add_dir(name, pornhd + url, 2, thumb, fanart)


def pornhd_pornstars(url):
    home()
    content = make_request(url)
    match = re.compile(
        'data-original="([^"]*)"\s*width=".+?"\s*height=".+?"\s*/>\s*</a>\s*<div class="info">\s*<a class="name" href="([^"]*)">\s*(.+?)\s*<').findall(
        content)
    for thumb, url, name in match:
        add_dir(name, pornhd + url, 2, thumb, fanart)
    match = re.compile('<link rel="next" href="([^"]*)" />').findall(content)
    add_dir('[COLOR blue]Next  Page  >>>>[/COLOR]', pornhd + match[0], 20, logos + 'pornhd.png', fanart)


def eporner_categories(url):
    home()
    content = make_request(url)
    match = re.compile('href="([^"]*)" title="([^"]*)"><img src="([^"]*)"').findall(content)
    for url, name, thumb in match:
        add_dir(name, eporner + url, 2, thumb, fanart)


def lubtetube_pornstars(url):
    home()
    content = make_request(url)
    match = re.compile('class="score">(.+?)</strong></span><a class="frame" href="/(.+?)"><img src="(.+?)" alt="(.+?)"',
                       re.DOTALL).findall(content)
    for duration, url, thumb, name in match:
        duration = duration.replace('<strong>', ' ')
        add_dir(name + ' [COLOR lime](' + duration + ')[/COLOR]', lubetube + url, 2, lubetube + thumb, fanart)
    try:
        match = re.compile('<a class="next" href="([^"]*)">Next</a>').findall(content)
        add_dir('[COLOR blue]Next  Page  >>>>[/COLOR]', lubetube + match[0], 12, logos + 'lubetube.png', fanart)
    except:
        pass


def lubetube_categories(url):
    home()
    content = make_request(url)
    match = re.compile('href="http://lubetube.com/search/adddate/cat/([^"]*)"><img src="(.+?)" alt="(.+?)"').findall(
        content)
    for url, thumb, name in match:
        add_dir(name, lubetube + 'search/adddate/cat/' + url, 2, logos + 'lubetube.png', fanart)


def porncom_channels_list(url):
    home()
    content = make_request(url)
    match = re.compile('href=".+/videos/(.+?)" title="(.+?)"').findall(content)[31:200]
    for url, name in match:
        add_dir(name, porncom + '/videos/' + url, 2, logos + 'porncom.png', fanart)


def motherless_galeries_cat(url):
    home()
    add_dir('[COLOR lightgreen]motherless.com Galleries    [COLOR red]Search[/COLOR]', motherless + '/search/Galleries',
            1, logos + 'motherless.png', fanart)
    content = make_request(url)
    match = re.compile('href="/G(.+?)".+?src="(.+?)".+?alt="(.+?)"', re.DOTALL).findall(content)
    for url, thumb, name in match:
        name = name.replace('&amp;', '&').replace('&quot;', '"').replace('&#39;', '\'')
        url = '/GV' + url
        add_dir(name, motherless + url, 2, thumb, fanart)
    match = re.compile('<a href="([^"]*)" class=".+?" rel="[1-9999]">NEXT &raquo;</a></div>').findall(content)
    add_dir('[COLOR blue]Next  Page  >>>>[/COLOR]', motherless + match[0], 60, logos + 'motherless.png', fanart)


def motherless_groups_cat(url):
    home()
    add_dir('[COLOR lightgreen]motherless.com Groups    [COLOR red]Search[/COLOR]', motherless + '/search/groups?term=',
            1, logos + 'motherless.png', fanart)
    content = make_request(url)
    match = re.compile('<a href="/g/(.+?)">.+?src="(.+?)".+?class="grunge motherless-red">.+?(.+?)</a>',
                       re.DOTALL).findall(content)
    for url, thumb, name in match:
        name = name.replace('&amp;', '&').replace('&quot;', '"').replace('&#39;', '\'').replace('  ', '')
        add_dir(name, motherless + '/gv/' + url, 2, thumb, fanart)
    match = re.compile('<a href="([^"]*)" class="pop" rel="[1-9999]">NEXT &raquo;</a></div>').findall(content)
    add_dir('[COLOR blue]Next  Page  >>>>[/COLOR]', motherless + match[0], 62, logos + 'motherless.png', fanart)


def motherless_being_watched_now(url):
    home()
    content = make_request(url)
    match = re.compile("<a href=\"(.+?)\" title=\"All Media\">").findall(content)
    add_dir('[COLOR lime]REFRESH[COLOR orange]  Page[COLOR red]  >>>>[/COLOR]', motherless + match[0], 61,
            logos + 'motherless.png', fanart)
    match = re.compile(
        'data-frames="12">.+?<a href="([^"]+)".+?src="([^"]+)".+?alt="([^"]+)".+?caption left">([:\d]+)</div>',
        re.DOTALL).findall(content)
    for url, thumb, name, duration in match:
        name = name.replace('&amp;', '&').replace('&quot;', '"').replace('&#39;', '\'')
        add_link(name + ' [COLOR lime](' + duration + ')[/COLOR]', url, 4, thumb, fanart)


def redtube_channels_list(url):
    home()
    content = make_request(url)
    match = re.compile('href="(.+?)" class="channels-list-img">\s*<img src="(.+?)" alt="(.+?)">').findall(content)
    for url, thumb, name in match:
        add_dir(name, redtube + url, 2, thumb, fanart)
    try:
        match = re.compile('rel="next" href="([^"]+)">').findall(content)
        add_dir('[COLOR blue]Next  Page  >>>>[/COLOR]', match[0], 11, logos + 'redtube.png', fanart)
    except:
        pass


def redtube_channels_cat(url):
    home()
    content = make_request(url)
    match = re.compile('href="/channel/(.+?)" title="(.+?)">').findall(content)
    for url, name in match:
        add_dir(name, redtube + '/channel/' + url, 11, logos + 'redtube.png', fanart)


def vikiporn_categories(url):
    home()
    content = make_request(url)
    match = re.compile('href="(.+?)">(.+?)<span>(\(\d+\))<').findall(content)[42:]
    for url, name, inum in match:
        inum = inum.replace(')', ' videos)')
        add_dir(name + '[COLOR lime] ' + inum + '[/COLOR]', url, 2, logos + 'vikiporn.png', fanart)


def xhamster_categories(url):
    home()
    content = make_request(url)
    match = re.compile('href="http://xhamster.com/channels/(.+?)">(.+?)<').findall(content)
    for url, name in match:
        name = name.replace('&amp;', '&').replace('&quot;', '"').replace('&#39;', '´')
        add_dir(name, xhamster + '/channels/' + url, 2, logos + 'xhamster.png', fanart)


def xhamster_content(url):
    home()
    content = make_request(url)
    match = re.compile("<a href=\"(.+?)\" hint='(.+?)'><div class='iconL").findall(content)
    for url, name in match:
        add_dir(name, url, 2, logos + 'xhamster.png', fanart)


def tube8_categories(url):
    home()
    content = make_request(url)
    match = re.compile('<a href="http://www.tube8.com/cat/([^"]*)">([^"]*)</a>\s*				</li>').findall(
        content)
    for url, name in match:
        add_dir(name, tube8 + '/cat/' + url, 2, logos + 'tube.png', fanart)


def zbporn_categories(url):
    home()
    content = make_request(url)
    match = re.compile('<a href="([^"]*)"><img src="([^"]*)" alt="([^"]*)"><span class="info">').findall(content)
    for url, thumb, name in match:
        add_dir(name, url, 2, thumb, fanart)


def pornhub_categories(url):
    home()
    content = make_request(url)
    match = re.compile('<div class="category-wrapper">.+?<a href="(.+?)"  alt="(.+?)">.+?<img src="(.+?)"',
                       re.DOTALL).findall(content)
    for url, name, thumb in match:
        add_dir(name, pornhub + url, 2, thumb, fanart)


def pornsocket_categories(url):
    home()
    content = make_request(url)
    match = re.compile('<a href="([^"]*)"> <img src="([^"]*)" border="0" alt="([^"]*)" class="media-thumb "').findall(
        content)
    for url, thumb, name in match:
        add_dir(name, pornsocket + url + '?filter_mediaType=4', 2, pornsocket + thumb, fanart)


def youjizz_categories(url):
    home()
    content = make_request(url)
    match = re.compile('<li><a target=\"_blank\" href="([^"]+)" >([^"]+)</a></li>').findall(content)
    for url, name in match:
        url = url.replace('High Definition', 'HighDefinition');
        add_dir(name, url, 2, logos + 'youjizz.png', fanart)


def hentaigasm_categories(url):
    home()
    content = make_request(url)
    match = re.compile("<a href='http://hentaigasm.com/tag/([^']+)'").findall(content)
    for url in match:
        name = url.replace('http://hentaigasm.com/tag/', '').replace('/', '')
        add_dir(name, 'http://hentaigasm.com/tag/' + url, 2, logos + 'hentaigasm.png', fanart)


def youporn_categories(url):
    home()
    content = make_request(url)
    match = re.compile('<a href="([^"]+)" class=".+?" onclick=".+?">\s*<img src="([^"]+)" alt="([^"]+)">').findall(
        content)
    for url, thumb, name in match:
        add_dir(name, youporng + url, 2, thumb, fanart)


def ashemaletube_categories(url):
    home()
    content = make_request(url)
    match = re.compile('Galleries" src="([^"]+)".+?href="/videos/([^"]+)/best-recent/">([^>]+)</a>', re.DOTALL).findall(
        content)
    for thumb, url, name in match:
        add_dir(name, ashemaletube + '/videos/' + url + '/newest/', 2, thumb, fanart)


def heavyr_categories(url):
    home()
    content = make_request(url)
    match = re.compile('<a href="([^"]+)" class="image">.+?<img src="([^"]+)" alt="([^"]+)', re.DOTALL).findall(content)
    for url, thumb, name in match:
        add_dir(name, heavyr + url, 2, heavyr + thumb, fanart)


def jav720p_categories(url):
    home()
    content = make_request(url)
    match = re.compile(
        '<div class="col-sm-4"> <h3 class="title-category"><a href="([^"]+)" title="All JAV Genre .+?">([^"]+)</a></h3> </div>',
        re.DOTALL).findall(content)
    for url, name in match:
        add_dir(name, url, 2, logos + 'j720p.png', fanart)


def jav720p_models(url):
    home()
    content = make_request(url)
    match = re.compile(
        '<div class="col-sm-4"> <h3 class="title-category"><a href="([^"]+)" title="All JAV Model .+?">([^"]+)</a></h3> </div>',
        re.DOTALL).findall(content)
    for url, name in match:
        add_dir(name, url, 2, logos + 'j720p.png', fanart)


def jav720p_makers(url):
    home()
    content = make_request(url)
    match = re.compile(
        '<div class="col-sm-4"> <h3 class="title-category"><a href="([^"]+)" title="All JAV maker .+?">([^"]+)</a></h3> </div>',
        re.DOTALL).findall(content)
    for url, name in match:
        add_dir(name, url, 2, logos + 'j720p.png', fanart)


def xvideos_categories(url):
    home()
    content = make_request(url)
    match = re.compile('<li><a href="(/c/\w+[-]\d+)" class="btn btn-default">([^"]+)<\/a></li>', re.DOTALL).findall(
        content)
    for url, name in match:
        add_dir(name, xvideos + url, 2, logos + 'xvideos.png', fanart)


def xvideos_pornstars(url):
    home()
    content = make_request(url)
    match = re.compile(
        'Url\(\'<img src="([^"]+)".+?<p class="profile-name"><a href="/pornstars-click/13/([^"]+)">([^"]+)</a></p><p',
        re.DOTALL).findall(content)
    for thumb, url, name in match:
        add_dir(name, xvideos + '/profiles/' + url + '/videos/', 2, thumb, fanart)
    try:
        match = re.compile('<a class="active" href=".+?">.+?</a></li><li><a href="([^"]+)">.+?</a></li><li>',
                           re.DOTALL).findall(content)
        add_dir('[COLOR blue]Next  Page  >>>>[/COLOR]', xvideos + match[0], 32, logos + 'xvideos.png', fanart)
    except:
        pass


def yesxxx_categories(url):
    home()
    content = make_request(url)
    match = re.compile('<a href="([^"]+)" title="([^"]+)"><img src="([^"]+)"', re.DOTALL).findall(content)
    for url, name, thumb in match:
        add_dir(name, yesxxx + url, 2, thumb, fanart)
    try:
        match = re.compile('<li><a href="([^"]+)">Next</a></li>', re.DOTALL).findall(content)
        add_dir('[COLOR blue]Next  Page  >>>>[/COLOR]', yesxxx + match[0], 37, logos + 'yes.png', fanart)
    except:
        pass


def tubepornclassic_categories(url):
    home()
    content = make_request(url)
    match = re.compile(
        'a class="item" href="([^"]+)" title="([^"]+)">.+?<img class="thumb" src="([^"]+)".+?<div class="videos">([^"]+)</div>',
        re.DOTALL).findall(content)
    for url, name, thumb, duration in match:
        add_dir(name + ' [COLOR lime](' + duration + ')[/COLOR]', url, 2, thumb, fanart)


def pornxs_categories(url):
    home()
    content = make_request(url)
    match = re.compile('<a href="([^"]+)">.+?/img/categories/(.+?).jpg.+?caption">([^"]+)</div>', re.DOTALL).findall(
        content)
    for url, thumb, name in match:
        name = name.replace(' ', '')
        add_dir(name, pornxs + url, 2, pornxs + '/img/categories/' + thumb + 'pornxs.jpg', fanart)


def gotporn_categories(url):
    home()
    content = make_request(url)
    match = re.compile(' <a class="category-list-item" href="([^"]+)">(.+?)<span>([^"]+)</span>', re.DOTALL).findall(
        content)
    for url, name, duration in match:
        name = name.replace(' ', '')
        add_dir(name + ' [COLOR lime](' + duration + ')[/COLOR]', url, 2, logos + 'gotporn.png', fanart)


def gotporn_content(url):
    home()
    content = make_request(url)
    match = re.compile('<a href="http://www.gotporn.com/browse-settings/(.+?)"').findall(content)
    for url in match:
        name = url
        name = name.replace('store?orientation=', '')
        add_dir(name, 'http://www.gotporn.com/browse-settings/' + url, 2, logos + 'gotporn.png', fanart)


def xhamster_rankigs(url):
    home()
    content = make_request(url)
    match = re.compile('<a href="([^"]+)" >(.+?)</a>', re.DOTALL).findall(content)
    for url, name in match:
        add_dir(name, url, 2, logos + 'xhamster.png', fanart)


def youporn_sorting(url):
    home()
    content = make_request(url)
    match = re.compile('href="([^"]+)">(Top.+?|Most.+?)</a></li>').findall(content)
    for url, name in match:
        add_dir(name, youporn + url, 2, logos + 'youporn.png', fanart)


def motherless_sorting(url):
    home()
    content = make_request(url)
    match = re.compile('<a href="([^"]+)" title=".+?">(Most.+?|Popular.+?)</a>').findall(content)
    for url, name in match:
        add_dir(name, motherless + url, 2, logos + 'motherless.png', fanart)


def emplix_categories(url):
    home()
    content = make_request(url)
    match = re.compile(
        '<span class="thumb2">.+?<a href="//www.empflix.com/categories/([^"]+)" class="floatLeft">.+?<img src="([^"]+)" alt="([^"]+)">',
        re.DOTALL).findall(content)
    for url, thumb, name in match:
        name = name.replace('&amp;', '&').replace('&quot;', '"').replace('&#39;', '\'')
        add_dir(name, 'http://www.empflix.com/categories/' + url, 2, 'http:' + thumb, fanart)


def emplix_sorting(url):
    home()
    content = make_request(url)
    match = re.compile('href="([^"]*)"  >(Being Watched|Most Recent|Most Viewed|Top Rated)').findall(content)
    for url, name in match:
        add_dir(name, empflix + url, 2, logos + 'empflix.png', fanart)


def txxx_categories(url):
    home()
    content = make_request(url)
    match = re.compile(
        '<a class="thumbnail" href="([^"]*)" title="([^"]*)">.+?="([^"]*)".+?<strong>(.+?)</strong> videos',
        re.DOTALL).findall(content)
    for url, name, thumb, duration in match:
        add_dir(name + ' [COLOR lime](' + duration + ')[/COLOR]', txxx + url, 2, thumb, fanart)


def upornia_categories(url):
    home()
    content = make_request(url)
    match = re.compile('<a class="thumbnail" href="(.+?)" title="(.+?)">.+?<img src="(.+?)" alt=".+?">',
                       re.DOTALL).findall(content)
    for url, name, thumb in match:
        add_dir(name, url, 2, thumb, fanart)


def upornia_models(url):
    home()
    content = make_request(url)
    match = re.compile('<a class="thumbnail" href="([^"]+)" title="(.+?)">.+?<img src="(.+?)"', re.DOTALL).findall(
        content)
    for url, name, thumb in match:
        add_dir(name, url, 2, thumb, fanart)
    try:
        match = re.compile('<li class="next">.+?<a href="(.+?)"', re.DOTALL).findall(content)
        add_dir('[COLOR blue]Next  Page  >>>>[/COLOR]', upornia + match[0], 51, logos + 'upornia.png', fanart)
    except:
        pass


def yespornplease_categories(url):
    home()
    content = make_request(url)
    match = re.compile('<a title=".+?" alt=".+?" href="(.+?)">.+?title="(.+?)".+?<span class="badge">(.+?)</span>',
                       re.DOTALL).findall(content)
    for url, name, duration in match:
        add_dir(name + ' [COLOR lime](' + duration + ')[/COLOR]', yespornplease + url, 2, logos + 'yespp.png', fanart)


def resolve_url(url):
    content = make_request(url)
    if 'xvideos' in url:
        media_url = urllib.unquote(re.compile("flv_url=(.+?)&amp").findall(content)[-1])
    elif 'tube8' in url:
        media_url = re.compile('videoUrlJS = "(.+?)"').findall(content)[0]
    elif 'redtube' in url:
        try:
            video_url = re.compile('<source src="(.+?)" type="video/mp4">').findall(content)[0]  # 720p+480p
        except:
            video_url = re.compile('value="quality_.+?=(.+?)=').findall(content)[0]  # 240p
        media_url = urllib.unquote_plus(video_url)
    elif '.porn.com' in url:
        try:
            media_url = re.compile('id:"720p",url:"(.+?)",definition:"HD"').findall(content)[0]
        except:
            media_url = re.compile('id:"240p",url:"(.+?)"},').findall(content)[0]
    elif 'vikiporn' in url:
        media_url = re.compile("video_url: '(.+?)'").findall(content)[0]
    elif 'xhamster' in url:
        media_url = re.compile("file: '(.+?)',").findall(content)[0]
    elif 'lubetube' in url:
        media_url = re.compile('id="video-.+?" href="(.+?)"').findall(content)[0]
    elif 'yes.xxx' in url:
        media_url = re.compile("video_url: '(.+?)',video_url_text:").findall(content)[0]
    elif 'pornxs' in url:
        media_url = re.compile('config-final-url="(.+?)"').findall(content)[0]
    elif 'zbporn' in url:
        media_url = re.compile('file: "(.+?)",').findall(content)[0]
    elif 'pornhd' in url:
        try:
            media_url = re.compile("'720p'  : '(.+?)'").findall(content)[0]
        except:
            media_url = re.compile("'480p'  : '(.+?)'").findall(content)[0]
    elif 'motherless' in url:
        media_url = re.compile('__fileurl = \'(.+?)\';').findall(content)[0]
    elif 'eporner' in url:
        media_url = re.compile('file: "(.+?)"').findall(content)[0]
    elif 'tubepornclassic' in url:
        media_url = re.compile("video_url: '(.+?)',").findall(content)[0]
    elif 'efukt' in url:
        media_url = re.compile('file: "(.+?)",').findall(content)[0]
    elif 'pornhub' in url:
        media_url = re.compile("var player_quality_.+? = '(.+?)'").findall(content)[0]
    elif 'pornsocket' in url:
        media_url = pornsocket + re.compile('<source src="(.+?)" type="video/mp4"/>').findall(content)[0]
    elif 'youjizz' in url:
        media_url = re.compile('<a href="(.+?)" class=".+?" >Download This Video</a>').findall(content)[0]
    elif 'hentaigasm' in url:
        media_url = re.compile('file: "(.+?)",').findall(content)[0]
    elif 'ashemaletube' in url:
        try:
            rstr = r'{file: "(.+?)", label: "High Quality"}'
            media_url = re.compile(rstr).findall(content)[0]
        except:
            media_url = 'https://' + re.compile('"https://(.+?).mp4"').findall(content)[0] + '.mp4'
    elif 'youporn' in url:
        try:
            media_url = re.compile("720: '([^']+)").findall(content)[0]
        except:
            media_url = re.compile("480: '([^']+)").findall(content)[0]
    elif 'heavy-r' in url:
        media_url = re.compile("file: '([^']+)',").findall(content)[0]
    elif 'jav720p' in url:
        media_url = re.compile('file: "([^"]+)"').findall(content)[0]
    elif 'gotporn' in url:
        media_url = re.compile('<source src="([^"]+)"').findall(content)[0]
    elif 'empflix' in url:
        try:
            video_url = re.compile('<videoLink>([^<]+.mp4[^<]+)').findall(content)[-1]
        except:
            video_url = re.compile('<videoLink>([^<]+.mp4[^<]+)').findall(content)[-1]
        media_url = urllib.unquote_plus(video_url)
    elif 'txxx' in url:
        media_url = re.compile('video_url: \'(.+?)\',').findall(content)[0]
    elif 'drtuber' in url:
        media_url = re.compile('<source src="(.+?)"').findall(content)[0]
    elif 'upornia' in url:
        media_url = re.compile('video_url: \'(.+?)\',').findall(content)[0]
    elif 'yespornplease' in url:
        media_url = re.compile('.*?video_url=(.+?)&.*?').findall(content)[0]
    elif 'fantasti' in url:
        url = re.compile('<div class="video-wrap" data-origin-source="([^"]+)">').findall(content)[0]
        return resolve_url(url)

    else:
        media_url = url
    item = xbmcgui.ListItem(name, path=media_url)
    xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)
    return


def get_params():
    param = []
    paramstring = sys.argv[2]
    if len(paramstring) >= 2:
        params = sys.argv[2]
        cleanedparams = params.replace('?', '')
        if (params[len(params) - 1] == '/'):
            params = params[0:len(params) - 2]
        pairsofparams = cleanedparams.split('&')
        param = {}
        for i in range(len(pairsofparams)):
            splitparams = {}
            splitparams = pairsofparams[i].split('=')
            if (len(splitparams)) == 2:
                param[splitparams[0]] = splitparams[1]
    return param


def add_dir(name, url, mode, iconimage, fanart):
    u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.quote_plus(
        name) + "&iconimage=" + urllib.quote_plus(iconimage)
    ok = True
    liz = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    # liz.setProperty('fanart_image', fanart)
    ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=True)
    return ok


def add_link(name, url, mode, iconimage, fanart):
    u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.quote_plus(
        name) + "&iconimage=" + urllib.quote_plus(iconimage)
    liz = xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
    # liz.setProperty('fanart_image', fanart)
    liz.setProperty('IsPlayable', 'true')
    ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz)


params = get_params()
url = None
name = None
mode = None
iconimage = None

try:
    url = urllib.unquote_plus(params["url"])
except:
    pass
try:
    name = urllib.unquote_plus(params["name"])
except:
    pass
try:
    mode = int(params["mode"])
except:
    pass
try:
    iconimage = urllib.unquote_plus(params["iconimage"])
except:
    pass

print "Mode: " + str(mode)
print "URL: " + str(url)
print "Name: " + str(name)
print "iconimage: " + str(iconimage)

if mode == None or url == None or len(url) < 1:
    main()

elif mode == 1:
    search()
elif mode == 2:
    start(url)
elif mode == 3:
    start(url)
    # media_list(url)
elif mode == 4:
    resolve_url(url)

elif mode == 10:
    redtube_channels_cat(url)

elif mode == 11:
    redtube_channels_list(url)

elif mode == 12:
    lubtetube_pornstars(url)

elif mode == 13:
    start(url)
    # flv_channels_list(url)

elif mode == 14:
    porncom_channels_list(url)

elif mode == 15:
    lubetube_categories(url)

elif mode == 16:
    vikiporn_categories(url)

elif mode == 17:
    xhamster_categories(url)

elif mode == 19:
    pornhd_categories(url)

elif mode == 20:
    pornhd_pornstars(url)

elif mode == 21:
    eporner_categories(url)

elif mode == 22:
    tube8_categories(url)

elif mode == 23:
    zbporn_categories(url)

elif mode == 24:
    xhamster_content(url)

elif mode == 25:
    pornhub_categories(url)

elif mode == 26:
    pornsocket_categories(url)

elif mode == 27:
    xvideos_categories(url)

elif mode == 28:
    youjizz_categories(url)

elif mode == 29:
    hentaigasm_categories(url)

elif mode == 30:
    ashemaletube_categories(url)

elif mode == 31:
    youporn_categories(url)

elif mode == 32:
    xvideos_pornstars(url)

elif mode == 33:
    heavyr_categories(url)

elif mode == 34:
    jav720p_categories(url)

elif mode == 35:
    jav720p_models(url)

elif mode == 36:
    jav720p_makers(url)

elif mode == 37:
    yesxxx_categories(url)

elif mode == 38:
    tubepornclassic_categories(url)

elif mode == 39:
    pornxs_categories(url)

elif mode == 40:
    gotporn_categories(url)

elif mode == 41:
    gotporn_content(url)

elif mode == 42:
    xhamster_rankigs(url)

elif mode == 43:
    youporn_sorting(url)

elif mode == 44:
    motherless_sorting(url)

elif mode == 45:
    emplix_categories(url)

elif mode == 46:
    emplix_sorting(url)

elif mode == 47:
    txxx_categories(url)

elif mode == 480:
    fantasti_tubesidx(url)

elif mode == 48:
    fantasti_collections(url)

elif mode == 49:
    fatasti_sorting(url)

elif mode == 50:
    upornia_categories(url)

elif mode == 51:
    upornia_models(url)

elif mode == 52:
    yespornplease_categories(url)

elif mode == 60:
    motherless_galeries_cat(url)

elif mode == 61:
    motherless_being_watched_now(url)

elif mode == 62:
    motherless_groups_cat(url)

xbmcplugin.endOfDirectory(int(sys.argv[1]))
