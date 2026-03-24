#! /usr/bin/python
# ~/bible.py

#format and write the Bible verse of the day from BibleGateway to a file
#output file:  .verse
#add the following to ~/.bashrc
#
#   if [ "$SHLVL" = "1" ]; then
#       if [ -f ".verse" ]; then cat .verse; fi
#       (./bible.py &)
#   fi
#
#note:  to save time; this cats the existing text in .verse and runs bible.py in the background
#on the first boot of the day, it will show yesterday's verse and then today's after that

from json import loads
from html import unescape
from requests import get
from time import sleep
import datetime

internet = False

while (not internet):
    try: 
        r = get("http://www.google.com")
        if r.status_code == 200:
            internet = True
    except: 
        sleep(1)

response = loads(get('https://www.biblegateway.com/votd/get/?format=json&version=esv'
                ).content)

text = unescape(response['votd']['text'])
today = datetime.datetime.now()

tarr = text.split(" ")
acc = "   "
ct = 0
for i in tarr:
    acc += i + ' '
    ct += 1
    if ct % 7 == 0:
        acc += "\n   "

with open(".verse", "w") as f:
    f.write(today.strftime("\033[1;33m\n   %a, %b %d\n\n")+ acc + "\n\t\t\t -- " + response['votd']['display_ref'] + "\n\n\033[0m")

