#!/bin/python
import socket, string
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("irc.freenode.net", 6667))
nickname = "mtmt"
adminpass = ""
password = ""
channels = ["#mtcm"]
public = []
log = 0
grant = []
chan1 = ""
chan2 = ""
word1 = ""
word2 = ""
chanset = channels[0]
admins = ["markveidemanis"]
readbuffer = ""
s.send("USER %s %s %s %s \n" % (nickname, nickname, nickname, nickname))
s.send("PRIVMSG NickServ :IDENTIFY %s \n" % password)
s.send("NICK %s \n" % nickname)
for i in channels:
    s.send("JOIN %s \n" % i)
#########################
class irc(object):
    def join(self, channel):
        s.send("JOIN %s\n" % channel)
    def part(self, channel):
        s.send("PART %s\n" % channel)
    def say(self, channel, message):
        s.send("PRIVMSG %s :%s\n" % (channel, message))
    def notice(self, target, message):
        s.send("NOTICE %s :%s\n" % (target, message))
    def kick(self, nickname, reason=nickname):
        s.send("KICK %s :%s\n" % (nickname, reason))
    def op(self, channel, nickname):
        s.send("MODE %s +o %s\n" % (channel, nickname))
    def deop(self, channel, nickname):
        s.send("MODE %s -o %s\n" % (channel, nickname))
    def voice(self, channel, nickname):
        s.send("MODE %s +v %s\n" % (channel, nickname))
    def devoice(self, channel, nickname):
        s.send("MODE %s -v %s\n" % (channel, nickname))
    def ban(self, channel, nickname):
        s.send("MODE %s +b %s\n" % (channel, nickname))
    def unban(self, channel, nickname):
        s.send("MODE %s -b %s\n" % (channel, nickname))
    def nick(self, newnick):
        s.send("NICK %s\n" % newnick)
    def quit(self):
        s.send("QUIT\n")
irc = irc()
#########################
while 1:
    readbuffer=readbuffer+s.recv(1024)
    temp=string.split(readbuffer, "\n")
    readbuffer=temp.pop()

    for msg in temp:
        print msg
        #print repr(msg)
        msg=string.rstrip(msg)
    
    suffix1 = nickname + ": "

    if msg.find('PING') != -1:
        s.send('PONG ' + msg.split() [1] + '\r\n')

    if msg.split(' ')[1] == "PRIVMSG":
        message = msg.split(' ')[3][1:]
        nick = msg[msg.find('!'):][1:]
        target = msg.split(' ')[2]
        if target == nickname:
            target = nick
        split = message.split()
        if len(split) > 0:
            cmd = split[0]
        if log == 1:
            f = open("log", "a")
            f.write(msg+"\n")
            f.close()
cmd = suffix1+""
#########################
    def gen(number):
        if auth() and wordc(number):
            return True

    def wordc(num):
        if len(split) == num:
            return True

    def auth():
        if nick in admins:
            return True
        if nick+":"+cmd in grant:
            return True
        if cmd in public:
            return True
#########################
    if cmd == "!join" and gen(2):
        irc.join(split[1])
    if cmd == "!part" and gen(2):
        irc.part(split[1])

    if cmd == "!cmd" and len(split) > 1 and auth():
        s.send(" ".join(split[1:])+"\n")

    if cmd == "!say" and len(split) > 1 and auth():
        irc.say(chanset, " ".join(split[1:]))
    if cmd == "!notice" and len(split) > 1 and auth():
        irc.notice(chanset, " ".join(split[1:]))

    if cmd == "!chanset" and gen(2):
        chanset = split[1]
        irc.say(target, "chanset = %s" % chanset)
    elif cmd == "!chanset" and gen(1):
        chanset = target
        irc.say(target, "chanset = %s" % chanset)

    if cmd == "!kick" and gen(2):
        irc.kick(chanset, split[1])

    if cmd == "op" and gen(2):
        irc.op(chanset, split[1])
    elif cmd == "op" and gen(1):
        irc.op(chanset, nick)
    if cmd == "deop" and gen(2):
        irc.deop(chanset, split[1])
    elif cmd == "deop" and gen(1):
        irc.deop(chanset, nick)

    if cmd == "voice" and gen(2):
        irc.voice(chanset, split[1])
    if cmd == "devoice" and gen(2):
        irc.devoice(chanset, split[1])

    if cmd == "ban" and gen(2):
        irc.ban(chanset, split[1])
    if cmd == "unban" and gen(2):
        irc.unban(chanset, split[1])

    if cmd == "nick" and gen(2):
        irc.nick(split[1])

    if cmd == "ping" and gen(1):
        irc.say(target, "PONG!")

    if cmd == "relay" and gen(3):
        chan1 = split[1]
        chan2 = split[2]
        irc.say(target, "Messages from %s will be relayed to %s" % (chan1, chan2))
    if chan1 != "" and chan2 != "" and target == chan1:
        irc.say(chan2, message)

    if cmd == "cond" and gen(3):
        word1 = split[1]
        word2 = split[2]
        irc.say(target, "Messages matching %s will be followed with %s" % (word1, word2))
    if word1 != None and word2 != None and cmd == word1:
        irc.say(target, word2)

    if cmd == "flush" and gen(1):
        chan1 = ""
        chan2 = ""
        word1 = ""
        word2 = ""
        irc.say(target, "Variables flushed")
    elif cmd == "reset" and gen(1):
        public = []
        log = 0
        grant = []
        chan1 = ""
        chan2 = ""
        word1 = ""
        word2 = ""
        chanset = channels[0]
        admins = ["markveidemanis"]
        irc.say(target, "Bot has been reset")
        
    if cmd == "log" and gen(1) and log == 0:
        log = 1
        irc.say(target, "log = 1")
    elif cmd == "log" and gen(1) and log == 1:
        log = 0
        irc.say(target, "log = 0")

    if cmd == "!add" and gen(3):
        grant.append(split[1]+":"+split[2])
        irc.say(target, "%s can use %s" % (split[1], split[2]))
    elif cmd == "del" and gen(3):
        grant.remove(split[1]+":"+split[2])
        irc.say(target, "%s can no longer use %s" % (split[1], split[2]))

    if cmd == "addmod" and gen(2):
        admins.append(split[1])
        irc.say(target, "%s added to admins" % split[1])
    elif cmd == "delmod" and gen(2) and split[1] in admins:
        admins.remove(split[1])
        irc.say(target, "%s removed from admins" % split[1])

    if cmd == "auth" and wordc(2) and split[1] == adminpass:
        admins.append(nick)
    if cmd == "pass" and gen(2):
        adminpass = split[1]

    if cmd == "pubadd" and gen(2):
        public.append(split[1])
        irc.say(target, "%s added as a public command" % split[1])
    elif cmd == "pubdel" and gen(2) and split[1] in public:
        public.remove(split[1])
        irc.say(target, "%s is no longer a public command" % split[1])

    if cmd == "quit" and gen(1):
        irc.quit()
        exit()
