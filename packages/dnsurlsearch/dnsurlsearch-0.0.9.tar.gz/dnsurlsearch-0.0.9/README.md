# DNSurlSearch

[![PyPI - Version](https://img.shields.io/pypi/v/dnsurlsearch.svg)](https://pypi.org/project/dnsurlsearch)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/dnsurlsearch.svg)](https://pypi.org/project/dnsurlsearch)

-----

**Table of Contents**

- [Installation](#Installation)
- [Getting started](#Getting_started)
- [Whitelist](#Whitelist)
- [Blacklist](#Blacklist)
- [Pihole](#Pihole)
- [License](#License)

# Installation

```console
pip install dnsurlsearch
```

# Getting_started
This package allow you to build a whitelist like that :
```
rr1.sn-cv0tb0xn-uane.googlevideo.com.
rr2.sn-cv0tb0xn-uane.googlevideo.com.
rr3.sn-cv1tb1xn-uane.googlevideo.com.
```
or a blacklist like that :
```
0.0.0.0 rr1.sn-cv0tb0xn-uane.googlevideo.com.
0.0.0.0 rr2.sn-cv0tb0xn-uane.googlevideo.com.
0.0.0.0 rr3.sn-cv1tb1xn-uane.googlevideo.com.
```
that you can save in a file and use with PiHole, for example, to filter urls.

The selection of urls is based on DNS protocol via exploration of cache file of DNS server like bind9 software
if you have installed bind9 on your localhost or via a sniffer in command line like tcpdump.

Initially the aim of this package was to filter advertisements on youTube video based on urls like *.googlevideo.com. Unfortunatedly,
some of these urls are not advertisements, so that we also need whitelist. 

# Whitelist
Whitelist generation is supposed to be manually. The script is launched and severals youTube video are played without any advertisement
to get url like *.googlevideo.com. without advertisement.

Here is an example of script example1.py (need to configure sudo to get rid of password) :

```python

from dnsurlsearch import DNSurlSearch

# First create url filter
whitelist = DNSurlSearch.UrlFilter()

# Create the cache
cache = DNSurlSearch.CacheDns()

# Set the SnifferCacheHandler to snif DNS protocol
h = DNSurlSearch.SnifferCacheHandler(DNSurlSearch.MANUAL)
h.set_cache_file_name('/tmp/log')

# The sniffer used is tcpdump
# The executable file tcpdump_cache_dns.sh contains the following command :
# "/usr/bin/tcpdump -n -s 0 port 53 > $1 &"
# to sniff DNS protocol
h.set_start_cmd('sudo /home/<user>/tcpdump_cache_dns.sh')
# The executable file k_tcpdump_cache_dns.sh contains the following command :
# "pkill tcpdump"
# to kill process
h.set_kill_cmd('sudo /home/<user>/k_tcpdump_cache_dns.sh')
cache.set_handler(h)
    
# Set patterns to search in the cache
cache.set_filter('.googlevideo.com.')
cache.set_filter('.other1.com.')
cache.set_filter('.other2.com.')
    
# Launch the sniffer to get url and search urls
new_cache = cache.get_cache_dns()
        
# Add urls found in the whitelist
whitelist.add(new_cache)
# Save the whitelist in a file
whitelist.write_url('whitelist')

```
You can launch this script with debug option (debug, info, warning, error, critical)
```bash
$ python3 example.py level=debug
2024-02-26 10:02:30,531 dnsurlsearch.DNSurlSearch DEBUG DNSurlSearch.py 278 ----------------- CacheDns.set_handler()() -----------------
2024-02-26 10:02:30,531 dnsurlsearch.DNSurlSearch DEBUG DNSurlSearch.py 282 ----------------- CacheDns.set_filter()() ------------------
2024-02-26 10:02:30,531 dnsurlsearch.DNSurlSearch DEBUG DNSurlSearch.py 284 filters : ['.googlevideo.com.']
2024-02-26 10:02:30,531 dnsurlsearch.DNSurlSearch DEBUG DNSurlSearch.py 526 --------------------- init_dns_cache() ---------------------
2024-02-26 10:02:30,531 dnsurlsearch.DNSurlSearch DEBUG DNSurlSearch.py 528 sudo /home/<user>/tcpdump_cache_dns.sh /tmp/log
Type enter to stop tcpdump...
2024-02-26 10:02:32,922 dnsurlsearch.DNSurlSearch DEBUG DNSurlSearch.py 537 sudo /home/<user>/k_tcpdump_cache_dns.sh
2024-02-26 10:02:32,941 dnsurlsearch.DNSurlSearch DEBUG DNSurlSearch.py 313 ---------------- CacheHandler._search_url() ----------------
2024-02-26 10:02:32,941 dnsurlsearch.DNSurlSearch DEBUG DNSurlSearch.py 314  pattern : ['.* (.+\\.googlevideo\\.com\\.).*'] - filename : Found_url.txt
2024-02-26 10:02:32,941 dnsurlsearch.DNSurlSearch DEBUG DNSurlSearch.py 328 Le cache est vide
2024-02-26 10:02:32,941 dnsurlsearch.DNSurlSearch DEBUG DNSurlSearch.py 160 --------------------- UrlFilter.add() ----------------------
2024-02-26 10:02:32,941 dnsurlsearch.DNSurlSearch DEBUG DNSurlSearch.py 161  Number of url to add : 0
2024-02-26 10:02:32,941 dnsurlsearch.DNSurlSearch DEBUG DNSurlSearch.py 143 ------------------ UrlFilter.write_url() -------------------
2024-02-26 10:02:32,941 dnsurlsearch.DNSurlSearch DEBUG DNSurlSearch.py 144  Number of urls to write : 0 - file name : whitelist 
```

# Blacklist
Blacklist is supposed to be automatic. A script is launched by crontab every 10 minutes via crontab for example.

Here is an example of script that can be launched on a host 
where a DNS server like bind9 is installed:
```python
from dnsurlsearch import DNSurlSearch

# Read Whitelist if any
whitelist = DNSurlSearch.UrlFilter()
whitelist.read_url('whitelist')

# To get some measurements of urls found in the cache sent by mail
# See https://docs.python.org/2.6/library/logging.html?highlight=logger#smtp-handler for more information on parameters
# Mesure period                          : 2024-02-05 18:51:01.128016 - 2024-02-05 18:51:42.497950
#        Number of new url found on the period  : 4
#        Total number of url found              : 4
stats = DNSurlSearch.CacheDnsStat(<mailhost>, <fromaddrmail>, <toaddrsmail>, 'Filtered url stats')

# First create url filter
# '0.0.0.0' parameter is the IP address to add in the file for each url
blacklist = DNSurlSearch.UrlFilter('0.0.0.0', 'black_list')

# treatment  
#  - when reading blacklist file : remove ip_address to get url only
#  - when writting blacklist file : add ip_address 
blacklist.set_treatment(DNSurlSearch.BlackListFilterTreatment())

nb_url_start = blacklist.read_url('blacklist')

# Create the cache
cache = DNSurlSearch.CacheDns()

# Set the BindCacheHandler to snif cache of the DNS server bind9
h = DNSurlSearch.BindCacheHandler()

# Location of the file where rndc dump the cache of DNS server
h.set_cache_file_name('/var/cache/bind/named_dump.db')

# Set the command to dump the cache of DNS server
h.set_start_cmd('/usr/sbin/rndc dumpdb -cache')
cache.set_handler(h)

# Set patterns to search in the cache
cache.set_filter('.googlevideo.com.')

# Launch the update of cache and search urls
new_cache = cache.get_cache_dns()

# Add urls found in the blacklist
blacklist.add(new_cache)

# Check urls and remove url from blacklist if present in whitelist
blacklist.check(whitelist.get_url())

nb_url_end = blacklist.write_url('blacklist')

stats.save_stats(nb_url_start, nb_url_end, 144)
```

Here is an example of another script example3.py that can be launched on a host 
where DNS protocol can be sniffed with tcpdump. The handler is initialized in automatic mode during 600 seconds. 
After 600 seconds, the sniffer is automatically killed by the handler.
```python
from dnsurlsearch import DNSurlSearch

# Read Whitelist if any
whitelist = DNSurlSearch.UrlFilter()
whitelist.read_url('whitelist')

# To get some measurements of urls found in the cache sent by mail
# See https://docs.python.org/2.6/library/logging.html?highlight=logger#smtp-handler for more information on parameters
# Mesure period                          : 2024-02-05 18:51:01.128016 - 2024-02-05 18:51:42.497950
#        Number of new url found on the period  : 4
#        Total number of url found              : 4
stats = DNSurlSearch.CacheDnsStat(<mailhost>, <fromaddrmail>, <toaddrsmail>, 'Filtered url stats')

# First create url filter
# '0.0.0.0' parameter is the IP address to add in the file for each url
blacklist = DNSurlSearch.UrlFilter('0.0.0.0', 'black_list')

# treatment  
#  - when reading blacklist file : remove ip_address to get url only
#  - when writting blacklist file : add ip_address 
blacklist.set_treatment(DNSurlSearch.BlackListFilterTreatment())

nb_url_start = blacklist.read_url('blacklist')

# Create the cache
cache = DNSurlSearch.CacheDns()

# Set the SnifferCacheHandler to snif DNS protocol
h = DNSurlSearch.SnifferCacheHandler(AUTOMATIC, 600)
h.set_cache_file_name('/tmp/log')

# The sniffer used is tcpdump
# The executable file tcpdump_cache_dns.sh contains the following command :
# "/usr/bin/tcpdump -n -s 0 port 53 > $1 &"
# to sniff DNS protocol
h.set_start_cmd('sudo /home/<user>/tcpdump_cache_dns.sh')
# The executable file k_tcpdump_cache_dns.sh contains the following command :
# "pkill tcpdump"
# to kill process
h.set_kill_cmd('sudo /home/<user>/k_tcpdump_cache_dns.sh')
cache.set_handler(h)

# Set patterns to search in the cache
cache.set_filter('.googlevideo.com.')

# Launch the update of cache and search urls
new_cache = cache.get_cache_dns()

# Add urls found in the blacklist
blacklist.add(new_cache)

# Check urls and remove url from blacklist if present in whitelist
blacklist.check(whitelist.get_url())

nb_url_end = blacklist.write_url('blacklist')

stats.save_stats(nb_url_start, nb_url_end, 144)

```

```bash
$ python3 example3.py level=debug
2024-03-03 11:55:05,115 dnsurlsearch.DNSurlSearch DEBUG DNSurlSearch.py 140 ------------------- UrlFilter.read_url() -------------------
2024-03-03 11:55:05,115 dnsurlsearch.DNSurlSearch DEBUG DNSurlSearch.py 140 ------------------- UrlFilter.read_url() -------------------
2024-03-03 11:55:05,115 dnsurlsearch.DNSurlSearch DEBUG DNSurlSearch.py 313 ----------------- CacheDns.set_handler()() -----------------
2024-03-03 11:55:05,115 dnsurlsearch.DNSurlSearch DEBUG DNSurlSearch.py 317 ----------------- CacheDns.set_filter()() ------------------
2024-03-03 11:55:05,115 dnsurlsearch.DNSurlSearch DEBUG DNSurlSearch.py 319 filters : ['.googlevideo.com.']
2024-03-03 11:55:05,115 dnsurlsearch.DNSurlSearch DEBUG DNSurlSearch.py 561 --------------------- init_dns_cache() ---------------------
2024-03-03 11:55:05,115 dnsurlsearch.DNSurlSearch DEBUG DNSurlSearch.py 563 sudo /home/<user>/tcpdump_cache_dns.sh /tmp/log
2024-03-03 11:55:05,122 dnsurlsearch.DNSurlSearch DEBUG DNSurlSearch.py 569 Waiting for 20 seconds (0 minutes) before killing sniffer
2024-03-03 11:55:05,122 dnsurlsearch.DNSurlSearch DEBUG DNSurlSearch.py 570 2024-03-03 11:55:05
2024-03-03 11:55:25,133 dnsurlsearch.DNSurlSearch DEBUG DNSurlSearch.py 572 2024-03-03 11:55:25
2024-03-03 11:55:25,133 dnsurlsearch.DNSurlSearch DEBUG DNSurlSearch.py 575 sudo /home/<user>/k_tcpdump_cache_dns.sh
2024-03-03 11:55:25,173 dnsurlsearch.DNSurlSearch INFO DNSurlSearch.py 343 Cache DNS : /tmp/log 03-03-2024 11:55 0.9453125 Ko
2024-03-03 11:55:25,173 dnsurlsearch.DNSurlSearch DEBUG DNSurlSearch.py 360 ---------------- CacheHandler._search_url() ----------------
2024-03-03 11:55:25,173 dnsurlsearch.DNSurlSearch DEBUG DNSurlSearch.py 361  pattern : ['.* (.+\\.googlevideo\\.com\\.).*'] - filename : Found_url.txt
2024-03-03 11:55:25,173 dnsurlsearch.DNSurlSearch DEBUG DNSurlSearch.py 375 Le cache est vide
2024-03-03 11:55:25,173 dnsurlsearch.DNSurlSearch DEBUG DNSurlSearch.py 184 --------------------- UrlFilter.add() ----------------------
2024-03-03 11:55:25,173 dnsurlsearch.DNSurlSearch DEBUG DNSurlSearch.py 185  Number of url to add : 0
2024-03-03 11:55:25,173 dnsurlsearch.DNSurlSearch INFO DNSurlSearch.py 192 0 New urls inserted
2024-03-03 11:55:25,173 dnsurlsearch.DNSurlSearch DEBUG DNSurlSearch.py 158 ------------------- UrlFilter.get_url() --------------------
2024-03-03 11:55:25,173 dnsurlsearch.DNSurlSearch DEBUG DNSurlSearch.py 196 -------------------- UrlFilter.check() ---------------------
2024-03-03 11:55:25,173 dnsurlsearch.DNSurlSearch INFO DNSurlSearch.py 204 0 Urls deleted (whitelist)
2024-03-03 11:55:25,173 dnsurlsearch.DNSurlSearch DEBUG DNSurlSearch.py 167 ------------------ UrlFilter.write_url() -------------------
2024-03-03 11:55:25,174 dnsurlsearch.DNSurlSearch DEBUG DNSurlSearch.py 168  Number of urls to write : 0 - file name : blacklist 
2024-03-03 11:55:25,174 dnsurlsearch.DNSurlSearch DEBUG DNSurlSearch.py 267 ---------------- CacheDnsStat.save_stats() -----------------
2024-03-03 11:55:25,174 dnsurlsearch.DNSurlSearch DEBUG DNSurlSearch.py 282 Start date: 2024-03-03 11:50:00.388145
 nb url orig: 0 total nb url: 0
2024-03-03 11:55:25,174 dnsurlsearch.DNSurlSearch DEBUG DNSurlSearch.py 236 --------------- CacheDnsStat.send_message() ----------------
2024-03-03 11:55:25,174 dnsurlsearch.DNSurlSearch DEBUG DNSurlSearch.py 237 Start date : 2024-03-03 11:50:00.388145
 nb new url : 0 total nb url : 0
2024-03-03 11:55:25,212 dnsurlsearch.DNSurlSearch DEBUG DNSurlSearch.py 246 Message : 
Mesure period                          : 2024-03-03 11:50:00.388145 - 2024-03-03 11:55:25.174378
Number of new url found on the period  : 0
Total number of url found              : 0

```

# Pihole

Here is an example of another script example4.py that can be launched on a host 
where pihole server is installed (as root). In this example the log file of pihole is analyzed (have a look at /etc/dnsmasq.d/01-pihole.conf)

```python
from dnsurlsearch import DNSurlSearch

# Read Whitelist if any
whitelist = DNSurlSearch.UrlFilter()
whitelist.read_url('whitelist')

# To get some measurements of urls found in the cache sent by mail
# See https://docs.python.org/2.6/library/logging.html?highlight=logger#smtp-handler for more information on parameters
# Mesure period                          : 2024-02-05 18:51:01.128016 - 2024-02-05 18:51:42.497950
#        Number of new url found on the period  : 4
#        Total number of url found              : 4
stats = DNSurlSearch.CacheDnsStat(<mailhost>, <fromaddrmail>, <toaddrsmail>, 'Filtered url stats')

# First create url filter
# '0.0.0.0' parameter is the IP address to add in the file for each url
blacklist = DNSurlSearch.UrlFilter('0.0.0.0', 'black_list')

# treatment  
#  - when reading blacklist file : remove ip_address to get url only
#  - when writting blacklist file : add ip_address 
blacklist.set_treatment(DNSurlSearch.BlackListFilterTreatment())

nb_url_start = blacklist.read_url('blacklist')

# Create the cache
cache = DNSurlSearch.CacheDns()

# Set the SnifferCacheHandler to snif DNS protocol
h = DNSurlSearch.SnifferCacheHandler(DNSurlSearch.AUTOMATIC, 1)
h.set_cache_file_name('/var/log/pihole/pihole.log')

h.set_start_cmd('')
h.set_kill_cmd('')
cache.set_handler(h)

# Set patterns to search in the cache
cache.set_filter('.googlevideo.com')

# Launch the update of cache and search urls
new_cache = cache.get_cache_dns()

# Add urls found in the blacklist
blacklist.add(new_cache)

# Check urls and remove url from blacklist if present in whitelist
blacklist.check(whitelist.get_url())

nb_url_end = blacklist.write_url('blacklist')

stats.save_stats(nb_url_start, nb_url_end, 144)
```

# License

`dnsurlsearch` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
