"""
    bjson/proxies.py
    
    Copyright (c) 2010 David Martinez Marti
    All rights reserved.

    Licensed under 3-clause BSD License. 
    See LICENSE.txt for the full license text.

"""
# import weakref

class Proxy(object):
    """
    Object that forwards calls to the remote.
    This class is intended to be instantiated from Connection class.
    
    Parameters:
    
    **conn**
        Connection object to forward calls.
        
    **sync_type**
        synchronization type. 0-synchronous. 1-asynchronous. 2-notification.
        
    **obj** = None
        optional. Object name to call their functions, (used to proxy 
        functions of *RemoteObject*)
        
    """
    def __init__(self, conn, sync_type, obj = None):
        self._conn = conn
        self._obj = obj
        self.sync_type = sync_type

    def __getattr__(self, name):
        if self._obj:
            name = "%s.%s" % (self._obj, name)
            
        def function(*args, **kwargs):
            """
                Decorator-like function that forwards all calls to proxy 
                method of connection.
            """
            return self._conn.proxy(self.sync_type, name, args, kwargs)
        #print name
        function.__name__ = str(name)
        function._conn = self._conn
        # function.sync_type = self.sync_type
        
        return function

