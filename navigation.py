import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'resources', 'site-packages'))
from pulsar import navigation


import xbmc
xbmc.log("%s" % [xbmc.ISO_639_1, xbmc.ISO_639_2, xbmc.ENGLISH_NAME])

navigation.run()
