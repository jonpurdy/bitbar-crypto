#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

import sys
import requests
import json
import logging

# collect and create the cryptocurrencies to check
import collections
c_dict = collections.OrderedDict()

for item in sys.argv[1:]:
	c_dict[item] = ""

# get information on each cryptocurrency
for c in c_dict:
	r = requests.get('https://api.coinmarketcap.com/v1/ticker/%s/' % c)
	r_dict = json.loads(r.text)
	c_dict[c] = r_dict[0]

bitbar_format = "font=Menlo size=10"

# display the results
# in menu bar
print("$%s | %s" % (format(float(c_dict['bitcoin']["price_usd"]), '.2f'), bitbar_format))

# in submenu
print("---")
print("currency price 1h/24h delta | %s" % bitbar_format)
for c in c_dict:
	url = "href=https://coinmarketcap.com/currencies/%s/" % c
	price = format(float(c_dict[c]["price_usd"]), '.2f')
	# adds a + symbol to positive, adds nothing to negative (since "-" is there)
	if "-" in c_dict[c]["percent_change_1h"]:
		hour_delta = "%s%%" % round(float(c_dict[c]["percent_change_1h"]), 1)
	else:
		hour_delta = "+%s%%" % round(float(c_dict[c]["percent_change_1h"]), 1)
	if "-" in c_dict[c]["percent_change_24h"]:
		day_delta = "%s%%" % round(float(c_dict[c]["percent_change_24h"]), 1)
	else:
		day_delta = "+%s%%" % round(float(c_dict[c]["percent_change_24h"]), 1)
	print("%s $%s %s/%s | %s %s" % (c_dict[c]["symbol"], price, hour_delta, day_delta, url, bitbar_format))
	
