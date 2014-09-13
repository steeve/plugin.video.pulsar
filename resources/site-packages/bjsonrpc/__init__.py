
# Copyright (c) 2010 David Martinez Marti
# All rights reserved.
#
# Licensed under 3-clause BSD License. 
# See LICENSE.txt for the full license text.


__version__ = '0.2'
"""Version number of the library as a string with the format X.Y"""

__release__ = '0.2.1'
"""Release number of the library as a string with the format X.Y.Z"""


__all__ = [
    "createserver",
    "connect",
    "server",
    "connection",
    "request",
    "handlers",
    "proxies",
    "jsonlib",
    "exceptions"
]

bjsonrpc_options = {
    'threaded' : False
}
"""
Dictionary with global options for the library. 

**threaded**
    (Default: False) When is set to True, threads will be created for handling 
    each incoming item.

"""

from bjsonrpc.main import createserver, connect

import bjsonrpc.server
import bjsonrpc.connection
import bjsonrpc.request
import bjsonrpc.handlers
import bjsonrpc.proxies
import bjsonrpc.jsonlib
import bjsonrpc.exceptions

