# -*- coding: utf-8 -*-
import datetime
import logging.handlers
import os
import re
import sys
import time
import six
import requests



# Log configuration --------------------------------------
LOG_FILENAME = '/tmp/CacheDns.out'

LEVELS = {'debug': logging.DEBUG,
          'info': logging.INFO,
          'warning': logging.WARNING,
          'error': logging.ERROR,
          'critical': logging.CRITICAL}

level = logging.NOTSET  # Default, no log

if len(sys.argv) > 1:
    level_name = sys.argv[1]
    level = LEVELS.get(level_name, logging.NOTSET)

my_logger = logging.getLogger(__name__)
my_logger.setLevel(level)

# Add the handler
handler = logging.handlers.RotatingFileHandler(
    LOG_FILENAME, maxBytes=1048576, backupCount=5)
# Formatter creation
formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
# Add formatter to handler
handler.setFormatter(formatter)
my_logger.addHandler(handler)

handler = logging.StreamHandler()
# Formatter creation
formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(filename)s %(lineno)d %(message)s")
# Add formatter to handler
handler.setFormatter(formatter)
my_logger.addHandler(handler)


# End log configuration --------------------------------------


# sudo cat /etc/pihole/setupVars.conf | grep PASSWORD
PiHoleAPI='5586e2461abcfd028d55f6fc1315dcd39adf5a1c9b1c74cb94e0502cde4a82d5'

PiIP='192.168.1.107:8080/'

TotalURL='http://{0}/admin/api.php?{1}&auth={2}'


class PiHole():

    def getallqueries(IP:str,API:str):
        """
        Get destinations in %
        - IP: the PiHole mashine URL
        - API: PiHole API key
        """
        try:
            ur = TotalURL.format(IP, 'getallqueries', API)
            resp = requests.get(url=ur)
            my_logger.debug(ur)
            my_logger.info('Getting data from PiHole address '+IP)
            data=resp.json()
            return data
        except:
            my_logger.info('Error connecting to PiHole')

    def GetCacheInfo(IP: str, API: str):
        """
        Get cache info
        - IP: the PiHole mashine URL
        - API: PiHole API key
        """
        try:
            ur = TotalURL.format(IP, 'getCacheInfo', API)
            my_logger.debug(ur)
            resp = requests.get(url=ur)
            my_logger.info('Getting data from PiHole address ' + IP)
            data = resp.json()
            return data['cacheinfo']
        except:
            my_logger.debug("Error connecting to PiHole")

if __name__ == "__main__":
    # Test

    # print(PiHole.GetCacheInfo(PiIP,PiHoleAPI))
    print(PiHole.getallqueries(PiIP,PiHoleAPI))


