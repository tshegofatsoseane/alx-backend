#!/usr/bin/env python3

'''Basic dictionary
'''


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''A `BasicCache` class which inherits from `BaseCaching`
       and is a caching system
    '''

    def put(self, key, item):
        '''assign the
           `item` value for the key `key` to the `self.cache_data` dictionary
        '''
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        '''return the `self.cache_data` value linked to `key`
        '''

        return self.cache_data.get(key, None)
