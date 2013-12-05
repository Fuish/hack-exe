#!/usr/bin/python
import random
import socket
import sys
import time

clear = '\033[0m'
red = '\033[31m'
yellow = '\033[33m'

such_demon = "{0}\
          .                                                      .\n\
        .n                   .                 .                  n.\n\
  .   .dP                  dP                   9b                 9b.    .\n\
 4    qXb         .       dX                     Xb       .        dXp     t\n\
dX.    9Xb      .dXb    __                         __    dXb.     dXP     .Xb\n\
9XXb._       _.dXXXXb dXXXXbo.                 .odXXXXb dXXXXb._       _.dXXP\n\
 9XXXXXXXXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXXXXXP\n\
  `9XXXXXXXXXXXXXXXXXXXXX'~   ~`OOO8b   d8OOO'~   ~`XXXXXXXXXXXXXXXXXXXXXP'\n\
    `9XXXXXXXXXXXP' `9XX'   {2}DIE{0}    `98v8P'  {2}HUMAN{0}   `XXP' `9XXXXXXXXXXXP'\n\
        ~~~~~~~       9X.          .db|db.          .XP       ~~~~~~~\n\
                        )b.  .dbo.dP'`v'`9b.odb.  .dX(\n\
                      ,dXXXXXXXXXXXb     dXXXXXXXXXXXb.\n\
                     dXXXXXXXXXXXP'   .   `9XXXXXXXXXXXb\n\
                    dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb\n\
                    9XXb'   `XXXXXb.dX|Xb.dXXXXX'   `dXXP\n\
                     `'      9XXXXXX(   )XXXXXXP      `'\n\
                              XXXX X.`v'.X XXXX\n\
                              XP^X'`b   d'`X^XX\n\
                              X. 9  `   '  P )X\n\
                              `b  `       '  d'\n\
                               `             '\n\
{1}".format(red, clear, yellow)

def get_ip(url):
    try:
        ip = socket.gethostbyname_ex(url)[2][0]
    except:
        sr = lambda: str(random.randrange(0,255))
        ip = sr()+'.'+sr()+'.'+sr()+'.'+sr()
    return ip

def dot(i):
    for i in xrange(i):
      sys.stdout.write('.')
      sys.stdout.flush()
      time.sleep(0.04)
    sys.stdout.write('[{0}COMPLETE{1}]\n'.format('\033[92m', '\033[0m'))
    time.sleep(0.6)

def main(url):
    print such_demon

    print "Enumerating Target",
    dot(40)
    print " [+] Host: {0}\n [+] IPv4: {1}".format(url, get_ip(url)) #fixme
    print "Opening SOCK5 ports on infected hosts",
    dot(21)
    print " [+] SSL entry point on 127.0.0.1:1337"
    print "Chaining proxies",
    dot(42)
    print ' [+] 7/7 proxies chained {BEL>AUS>JAP>CHI>NOR>FIN>UKR}'
    print "Launching port knocking sequence",
    dot(26)
    print " [+] Knock on TCP<143,993,587,456,25,587,993,80>"
    print "Sending PCAP datagrams for fragmentation overlap",
    dot(10)
    print " [+] Stack override ***** w00t w00t g0t r00t!"

    sys.stdout.write('\n[')
    for i in xrange(65):
      sys.stdout.write('=')
      sys.stdout.flush()
      time.sleep(0.01)
    sys.stdout.write(']\n')
    time.sleep(0.5)

    print "root@{0}:~# ".format(url),
    sys.stdout.flush()
    time.sleep(5)

