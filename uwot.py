###################################
# File name: uwot                #
# Author: Cole Woods             #                 
#################################


import socks
import socket
import urllib
import urllib2
 
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, '127.0.0.1', 9050)
socks.wrapmodule(urllib2)
socket.socket = socks.socksocket

 
Username = raw_input('Username: ')
AccountAmount = raw_input('Amount: ')
AdditiveValue = 0
 
while AdditiveValue != int(AccountAmount):
    AdditiveValue += 1
 
    Data = {'usercol': '000000000',
            'userpass': 'colewasherelol',
            'username': Username + str(AdditiveValue),
            'action': 'create'}
 
    PostRequest = urllib2.urlopen(urllib2.Request('http://67.19.72.26/stickarena/stick_arena.php', urllib.urlencode(Data)))
    PostResponse = PostRequest.read()


    
 
    if PostResponse == 'result=success':
        print('Succesfully created ' + Username + str(AdditiveValue))
    elif PostResponse == 'result=error':
        print('Couldn\'t create ' + Username + str(AdditiveValue))
    else:
        print(PostResponse)
