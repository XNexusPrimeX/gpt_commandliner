import os
import json
import utils.logger as logger

class CacheManager:
    CACHE_FILENAME = ".cache"

    @staticmethod
    def get(key=None, errMsg=None):
        if not os.path.exists(CacheManager.CACHE_FILENAME):
            return None

        with open(CacheManager.CACHE_FILENAME, 'r') as f:
            data = json.load(f)

        if key:
            data = data.get(key) 

            if data and len(data) > 0:
                return data
            else:
                if errMsg:
                    logger.error(errMsg)
                    exit()
                else:
                    return None 
        else:
            return data

    @staticmethod
    def set(key, value):
        data = {}
        if os.path.exists(CacheManager.CACHE_FILENAME):
            with open(CacheManager.CACHE_FILENAME, 'r') as f:
                data = json.load(f)

        data[key] = value

        with open(CacheManager.CACHE_FILENAME, 'w') as f:
            json.dump(data, f)
