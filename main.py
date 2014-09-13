import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'resources', 'site-packages'))

import json
import sys
import urllib
import urllib2
import xbmcgui
import xbmcplugin

HANDLE = int(sys.argv[1])
PULSARD_HOST = "http://localhost:10001"

import socket
socket.setdefaulttimeout(120)

class closing(object):
    def __init__(self, thing):
        self.thing = thing
    def __enter__(self):
        return self.thing
    def __exit__(self, *exc_info):
        self.thing.close()

class NoRedirectHandler(urllib2.HTTPRedirectHandler):
    def http_error_302(self, req, fp, code, msg, headers):
        infourl = urllib.addinfourl(fp, headers, headers["Location"])
        infourl.status = code
        infourl.code = code
        return infourl
    http_error_300 = http_error_302
    http_error_301 = http_error_302
    http_error_303 = http_error_302
    http_error_307 = http_error_302
opener = urllib2.build_opener(NoRedirectHandler())
urllib2.install_opener(opener)

def _json(url):
    with closing(urllib2.urlopen(url)) as response:
        if response.code >= 300 and response.code <= 307:
            xbmcplugin.setResolvedUrl(HANDLE, True, xbmcgui.ListItem(path=response.geturl()))
            return
        payload = response.read()
        if payload:
            return json.loads(payload)

url = sys.argv[0].replace("plugin://plugin.video.pulsar", PULSARD_HOST) + sys.argv[2]
xbmc.log(repr(url))
data = _json(url)
if data:
    if data["content_type"]:
        xbmcplugin.addSortMethod(HANDLE, xbmcplugin.SORT_METHOD_UNSORTED)
        xbmcplugin.addSortMethod(HANDLE, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
        xbmcplugin.addSortMethod(HANDLE, xbmcplugin.SORT_METHOD_DATE)
        xbmcplugin.addSortMethod(HANDLE, xbmcplugin.SORT_METHOD_GENRE)
        xbmcplugin.setContent(HANDLE, data["content_type"])

    listitems = []
    for item in data["items"]:
        listItem = xbmcgui.ListItem(label=item["label"], iconImage=item["icon"], thumbnailImage=item["thumbnail"])
        if item.get("info"):
            listItem.setInfo("video", item["info"])
        if item.get("stream_info"):
            for type_, values in item["stream_info"].items():
                listItem.addStreamInfo(type_, values)
        if item.get("art"):
            listItem.setArt(item["art"])
        if item.get("context_menu"):
            listItem.addContextMenuItems(item["context_menu"])
        listItem.setProperty("isPlayable", item["is_playable"] and "true" or "false")
        for k, v in (item.get("properties") or {}).items():
            listItem.setProperty(k, v)
        listitems.append([
            item["path"],
            listItem,
            not item["is_playable"],
        ])

    xbmcplugin.addDirectoryItems(HANDLE, listitems, totalItems=len(listitems))
    xbmcplugin.endOfDirectory(HANDLE, succeeded=True, updateListing=False, cacheToDisc=True)
