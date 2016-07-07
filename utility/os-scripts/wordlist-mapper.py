#!/usr/bin/env python
#
#
#  wordlist-mapper.py
#  
#  Copyright 2016 Cashiuus <cashiuus@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
from __future__ import print_function
import os
# -(Compatibility Fix)- Use input() for both python 3.x and 2.x
try:
    input = raw_input
except NameError:
    pass
# -------------------------------


def main():
	MSF = '/usr/share/metasploit-framework/data/wordlists'

    # Build a list of dictionaries, each dict being a wordlist definition
    wordlists = []
    wordlist_map = {}

    dirlist = os.listdir(dir).sort()
    for f in dirlist:
        t = subprocess.check(['wc', '-l', os.path.join(MSF, f)])
        wordlist_map['path'] = t[1]
        wordlist_map['wordcount'] = t[0]
        # Get file size in Bytes
        wordlist_map['filesize'] = os.path.getsize(os.path.join(MSF, f))
	return 0

if __name__ == '__main__':
	main()
