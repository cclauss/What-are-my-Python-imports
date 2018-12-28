#!/usr/bin/env python3

# TODO: This is NOT an exhaustive list but works for one particular project
STD_LIB = """ConfigParser Cookie HTMLParser Queue StringIO __future__
argparse array atexit
base64 bz2
cPickle cStringIO calendar cgi codecs collections compress cookielib copy csv
datetime doctest
email
fcntl ftplib functools
gc getopt glob gzip
hashlib hmac html htmlentitydefs httplib
itertools
json
logging
math md5 mimetypes
numbers
optparse os
pdb pydoc random
re
sched sendmail shelve shlex shutil site socket stat string subcommand
    subprocess sys
tempfile threading time traceback types
unicodedata unittest urllib urllib2 uuid
warnings
xml
zlib""".split()

with open('files.txt') as in_file:
    lines = (line.strip().partition('.py:') for line
             in in_file.read().splitlines())
lines = (c.strip().replace(',', ' ').replace('.', ' ') for a, b, c in lines
         if b and c.startswith(('from ', 'import '))
         and not a.startswith('scripts/20'))
lines = sorted(set(line.split()[1] for line in lines
                   if line.split()[1] not in STD_LIB
                   and not line.split()[1].startswith(('infogami',
                                                       'openlibrary'))))
print('\n'.join(lines))
