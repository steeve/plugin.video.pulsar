import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'resources', 'site-packages'))
from pulsar import navigation


navigation.run()
