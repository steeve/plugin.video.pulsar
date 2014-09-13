# encoding: UTF-8

"""

    Variables Syncronized over json-rpc at both ends.
    
    This package has several datatypes to ease variable-sharing across peers.
    
    Proposed Utils:
    
    * FIFOBuffer: streams lists of bytes/numbers/etc over network.
    
    
    Proposed Types:
    
    * FloatSync: floating point number synced over network
        - sync_mode:  fixed master-slave, dynamic master-slave, 
            queued master-master
        - get, set(value)
        - apply(operator, value) -- sum 3, mult 1.5, set 6 ...
        - addcallback(fn), removecallback(fn)
        
    * TupleSync: Tuple synced over network
        - sync_mode:  fixed master-slave, dynamic master-slave, 
            queued master-master
        - get, set(value)
        - addcallback(fn), removecallback(fn)
        
    * StringSync: (small) String synced over network
        - sync_mode:  fixed master-slave, dynamic master-slave, 
            queued master-master
        - get, set(value)
        - addcallback(fn), removecallback(fn)
        
    * DictSync: dict of elements synced over network
        - sync_mode:  fixed master-slave, dynamic master-slave, 
            queued master-master
        - get(x), set(x,value)
        - apply(x, operator, value)        
        - addcallback(fn), removecallback(fn)

    * ListSync: list of elements synced over network.
        - sync_mode:  fixed master-slave, dynamic master-slave, 
            queued master-master
        - primary_key: index, full-item, dict-column, list-index
        - item_style: single-object, list, dict
        - clear
        - append(x),push(x)
        - remove(x),pop(x)
        - update(x,value)
        - addcallback(fn), removecallback(fn)
        

"""