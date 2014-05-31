#!/bin/python
import socket, string, time, random, sys, subprocess
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("insomnia247.nl", 5015))
nickname = "SaladBot"
password = "" # Bot's NickServ password goes here
adminpass = "authpl0x" # Bot's auth password
channels = ["#moontest","#mtcm","##pingpong","#main"]
public = ["!auth","!ninja","#hashtag","!time","!say","PING","PONG",nickname + "!","XD",nickname + ": you suck"]
log = 1
grant = []
chan1 = ""
chan2 = ""
word1 = ""
word2 = ""
chanset = channels[0]
admins = ["zsoltisawesome","zsoltisawesome_","zsoltisawesome__"]
readbuffer = ""
s.send("USER %s %s %s %s \n" % (nickname, nickname, nickname, nickname))
s.send("NICK %s \n" % nickname)
s.send("PRIVMSG NickServ :IDENTIFY %s \n" % password)
for i in channels:
    s.send("JOIN %s \n" % i)
#########################
class irc(object):
    def join(self, channel):
        s.send("JOIN %s\n" % channel)
    def part(self, channel):
        s.send("PART %s :OMG, Who turned out the lights!\n" % channel)
    def say(self, target, message):
        s.send("PRIVMSG %s :%s\n" % (target, message))
        irc.logger(message)
    def saynick(self, target, message):
        s.send("PRIVMSG %s :" % (target) + nick + ": %s\n" % (message))
        irc.logger(nick + ": %s\n" % (message))
    def notice(self, target, message):
        s.send("NOTICE %s :%s\n" % (target, message))
    def kick(self, nickname, reason=nickname):
        s.send("KICK %s :%s\n" % (nickname, reason))
    def op(self, target, nickname):
        s.send("MODE %s +o %s\n" % (target, nickname))
    def deop(self, target, nickname):
        s.send("MODE %s -o %s\n" % (target, nickname))
    def voice(self, target, nickname):
        s.send("MODE %s +v %s\n" % (target, nickname))
    def devoice(self, target, nickname):
        s.send("MODE %s -v %s\n" % (target, nickname))
    def ban(self, target, nickname):
        s.send("MODE %s +b %s\n" % (target, nickname))
    def unban(self, target, nickname):
        s.send("MODE %s -b %s\n" % (target, nickname))
    def nick(self, newnick):
        s.send("NICK %s\n" % newnick)
    def quit(self):
        s.send("QUIT :OMG, Who turned out the lights!\n")
    def logger(self, loggable):
        print("["+nickname+"]: "+loggable+"\n")
        f = open("log", "a")
        f.write("["+nickname+"]: "+loggable+"\n")
        f.close()
irc = irc()
#########################
while 1:
 try:    
    readbuffer=readbuffer+s.recv(1024)
    temp=string.split(readbuffer, "\n")
    readbuffer=temp.pop()
    rndm = float("0." + str(random.randint(1,99999999999999999)))

    for msg in temp:
        msg=string.rstrip(msg)

    if msg.find('PING') != -1:
        s.send('PONG ' + msg.split() [1] + '\r\n')

    if msg.split(' ')[1] == "PRIVMSG" or msg.split(' ')[1] == "NOTICE":
        message = ' '.join(msg.split(' ')[3:])[1:]
        nick = msg.split('!')[0][1:]
        target = msg.split(' ')[2]
        #print message, nick, target
        if target == nickname:
            target = nick
        split = message.split()
        if len(split) > 0:
            cmd = split[0]
        if log == 1:
            print("[Message from "+target+"]: "+nick+": "+message+"\n")
            f = open("log", "a")
            f.write("[Message from "+target+"]: "+nick+": "+message+"\n")
            f.close()

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
    #    hmm = str(sys.stdin.readlines())
    #    s.send("PRIVMSG "+target+" :"+hmm)
    #########################
        if cmd == "!file" and len(split) > 1 and auth():
             irc.saynick(target, "Appending to User File!")
             f = open(nick + ".txt",'a')
             f.write(" ".join(split[1:]) + '\n')
             f.close()
             irc.saynick(target, "Done!")
             irc.logger(nick+" used the '"+cmd+"' command!")
        elif cmd == "!file" and gen(1):
             irc.saynick(target, "Argument pl0x!")

        if cmd == "!fortune" and gen(1):
             outputs = """""".join(subprocess.check_output("fortune"))
             irc.say(target, outputs)
             irc.logger(nick+" used the '"+cmd+"' command!")

        if cmd == "!testcmd" and gen(1):
             if rndm > 0.5:
                  rndmTxt = "Leave me alone!"
             else:
                  rndmTxt = "Did I miss something?"
             #irc.say(target, rndm)
             irc.saynick(target, "What? " + rndmTxt)
             irc.logger(nick+" used the '"+cmd+"' command!")

        if cmd == "!ninja" and gen(2):
             irc.say(target, split[1] + ": You have been cut by " + nick + "!")
             irc.logger(nick+" used the '"+cmd+"' command!")

        elif cmd == "!ninja" and gen(1):
             irc.saynick(target, "Give me someone to cut!")

        if cmd == "!salad" and gen(1):
             irc.saynick(target, "where my name comes from: https://www.youtube.com/watch?v=-KRnCnuE3xU")
             irc.logger(nick+" used the '"+cmd+"' command!")


        if cmd == "!join" and gen(2):
             irc.join(split[1])
             irc.logger(nick+" used the '"+cmd+"' command!")
        if cmd == "!part" and gen(2):
             irc.part(split[1])
             irc.logger(nick+" used the '"+cmd+"' command!")
        if cmd == "!cmd" and len(split) > 1 and auth():
             s.send(" ".join(split[1:])+"\n")
             irc.logger(nick+" used the '"+cmd+"' command!")
        if cmd == "!say" and len(split) > 1 and auth():
             irc.saynick(chanset, " ".join(split[1:]))
             irc.logger(nick+" used the '"+cmd+"' command!")
        if cmd == "!rev" and len(split) > 1 and auth():
             string = " ".join(split[1:])
             irc.saynick(chanset, string[::-1])
             irc.logger(nick+" used the '"+cmd+"' command!")
        if cmd == "!notice" and len(split) > 1 and auth():
             irc.notice(chanset, " ".join(split[1:]))
             irc.logger(nick+" used the '"+cmd+"' command!")

        if cmd == "!chanset" and gen(2):
             chanset = split[1]
             irc.saynick(target, "chanset = %s" % chanset)
             irc.logger(nick+" used the '"+cmd+"' command!")
        elif cmd == "!chanset" and gen(1):
             chanset = target
             irc.saynick(target, "chanset = %s" % chanset)
             irc.logger(nick+" used the '"+cmd+"' command!")

        if cmd == "!kick" and gen(2):
             irc.kick(chanset, split[1])
             irc.logger(nick+" used the '"+cmd+"' command!")

        if cmd == "!op" and gen(2):
             irc.op(chanset, split[1])
             irc.logger(nick+" used the '"+cmd+"' command!")

        elif cmd == "!op" and gen(1):
             irc.op(chanset, nick)
             irc.logger(nick+" used the '"+cmd+"' command!")

        if cmd == "!deop" and gen(2):
             irc.deop(chanset, split[1])
             irc.logger(nick+" used the '"+cmd+"' command!")

        elif cmd == "!deop" and gen(1):
             irc.deop(chanset, nick)
             irc.logger(nick+" used the '"+cmd+"' command!")


        if cmd == "!voice" and gen(2):
            irc.voice(chanset, split[1])
            irc.logger(nick+" used the '"+cmd+"' command!")

        if cmd == "!devoice" and gen(2):
            irc.devoice(chanset, split[1])
            irc.logger(nick+" used the '"+cmd+"' command!")

        if cmd == "!ban" and gen(2):
            irc.ban(chanset, split[1])
            irc.logger(nick+" used the '"+cmd+"' command!")
        if cmd == "!unban" and gen(2):
            irc.unban(chanset, split[1])
            irc.logger(nick+" used the '"+cmd+"' command!")

        if cmd == "!nick" and gen(2):
            irc.nick(split[1])
            irc.logger(nick+" used the '"+cmd+"' command!")
        if cmd == "!ping" and gen(1):
            irc.saynick(target, "PONG!")
            irc.logger(nick+" used the '"+cmd+"' command!")
        if cmd == "!relay" and gen(3):
            chan1 = split[1]
            chan2 = split[2]
            irc.saynick(target, "Messages from %s will be relayed to %s" % (chan1, chan2))
            irc.logger(nick+" used the '"+cmd+"' command!")
        if chan1 != "" and chan2 != "" and target == chan1:
            irc.saynick(chan2, message)

        if cmd == "!cond" and gen(3):
            word1 = split[1]
            word2 = split[2]
            irc.saynick(target, "Messages matching %s will be followed with %s" % (word1, word2))
            irc.logger(nick+" used the '"+cmd+"' command!")
        if word1 != None and word2 != None and cmd == word1:
            irc.saynick(target, word2)

        if cmd == "!flush" and gen(1):
            chan1 = ""
            chan2 = ""
            word1 = ""
            word2 = ""
            irc.saynick(target, "Variables flushed")
            irc.logger(nick+" used the '"+cmd+"' command!")
        elif cmd == "!reset" and gen(1):
            public = []
            log = 1
            grant = []
            chan1 = ""
            chan2 = ""
            word1 = ""
            word2 = ""
            chanset = channels[0]
            admins = ["zsoltisawesome"]
            irc.saynick(target, "Bot has been reset")
            irc.logger(nick+" used the '"+cmd+"' command!")
        if cmd == "!log" and gen(1) and log == 0:
            log = 1
            irc.saynick(target, "log = 1")
            irc.logger(nick+" used the '"+cmd+"' command!")
        elif cmd == "!log" and gen(1) and log == 1:
            log = 0
            irc.saynick(target, "log = 0")
            irc.logger(nick+" used the '"+cmd+"' command!")
        if cmd == "!add" and gen(3):
            grant.append(split[1]+":"+split[2])
            irc.saynick(target, "%s can use %s" % (split[1], split[2]))
            irc.logger(nick+" used the '"+cmd+"' command!")
        elif cmd == "!del" and gen(3):
            grant.remove(split[1]+":"+split[2])
            irc.saynick(target, "%s can no longer use %s" % (split[1], split[2]))
            irc.logger(nick+" used the '"+cmd+"' command!")
        if cmd == "!addmod" and gen(2):
            admins.append(split[1])
            irc.saynick(target, "%s added to admins" % split[1])
            irc.logger(nick+" used the '"+cmd+"' command!")
        elif cmd == "!delmod" and gen(2) and split[1] in admins:
            admins.remove(split[1])
            irc.saynick(target, "%s removed from admins" % split[1])
            irc.logger(nick+" used the '"+cmd+"' command!")
        if cmd == "!auth" and wordc(2) and split[1] == adminpass:
            admins.append(nick)
            irc.saynick(target, "Congrats! You are now a tempadmin!")
            irc.logger(nick+" used the '"+cmd+"' command!")
        if cmd == "!pubadd" and gen(2):
            public.append(split[1])
            irc.saynick(target, "%s added as a public command" % split[1])
            irc.logger(nick+" used the '"+cmd+"' command!")
        elif cmd == "!pubdel" and gen(2) and split[1] in public:
            public.remove(split[1])
            irc.saynick(target, "%s is no longer a public command" % split[1])
            irc.logger(nick+" used the '"+cmd+"' command!")
        if cmd == "!quit" and gen(1):
            irc.logger(nick+" used the '"+cmd+"' command!")            
            irc.quit()
            time.sleep(5)
            exit()

        if cmd == (nickname + ": die") and gen(2):
            irc.logger(nick+" used the '"+cmd+"' command!")
            irc.quit()
            time.sleep(5)
            exit()

        if cmd == "PING" and gen(1):
             irc.saynick(target, "PONG")
             irc.logger(nick+" used the '"+cmd+"' command!")
        if cmd == "PONG" and gen(1):
             irc.saynick(target, "PING")
             irc.logger(nick+" used the '"+cmd+"' command!")
        if cmd == "#hashtag" and gen(1):
             irc.saynick(target, "Shut up...")
             irc.logger(nick+" used the '"+cmd+"' command!")
        if cmd == (nickname + "!") and gen(1):
             irc.say(target, "Hi " + nick + "!")
             irc.logger(nick+" used the '"+cmd+"' command!")
        if cmd == (nickname + ": you suck") and gen(3):
            irc.say(target, ":(")
            irc.kick(chanset, nick, "No, you suck!")
            irc.logger(nick+" used the '"+cmd+"' command!")
        if cmd == "!dumb" and gen(1):
             irc.saynick(target, "DUN DUN DUN!")
             irc.logger(nick+" used the '"+cmd+"' command!")
        if cmd == ("!time") and gen(1):
            localtime = time.asctime(time.localtime(time.time()))
            irc.saynick(target, "It is currently " + localtime + " in my timezone")
            irc.logger(nick+" used the '"+cmd+"' command!")
        if cmd == "!help" and gen(1):
             irc.saynick(target, "Help: http://harpnet.comuv.com/ndrku/")
             irc.logger(nick+" used the '"+cmd+"' command!")
        if cmd == "!dump" and gen(1):
             print("message dump: " + msg)
             irc.logger(nick+" used the '"+cmd+"' command!")
        if cmd == "!allow" and gen(1):
             irc.say(target, "Am I allowed in here?")
             irc.logger(nick+" used the '"+cmd+"' command!")
        if cmd == "!sum" and gen(3):
            try:
             dasum = float(split[1]) + float(split[2])
            except ValueError:
             continue
            irc.saynick(target, "Sum is: " + str(dasum))
            irc.logger(nick+" used the '"+cmd+"' command!")
        if cmd == "!dif" and gen(3):
            try:
             dadif = float(split[1]) - float(split[2])
            except ValueError:
             continue
            irc.saynick(target, "Difference is: " + str(dadif))
            irc.logger(nick+" used the '"+cmd+"' command!")
        if cmd == "!rem" and gen(3):
            if split[2] == "0":
             irc.saynick(target, "You think I'm an idiot? I'm not gonna divide by zero!")
             continue
            try:
             darem = float(split[1]) / float(split[2])
            except ValueError:
             continue
            irc.saynick(target, "Remainder is: " + str(darem))
            irc.logger(nick+" used the '"+cmd+"' command!")
        if cmd == "!pro" and gen(3):
            try:
             dapro = float(split[1]) * float(split[2])
            except ValueError:
             continue
            irc.saynick(target, "Product is: " + str(dapro))
            irc.logger(nick+" used the '"+cmd+"' command!")
 except KeyboardInterrupt:
    irc.quit()
    sys.exit()
