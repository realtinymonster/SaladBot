Cheapo-Bot
==========
A very basic IRC bot made in Python.

All commands are preceded with !
Administrative Commands
-----------------------

These commands change the operation of the bot.

* join <channel> – Joins <channel>

* part <channel> – Parts <channel>

* chanset [<channel>] – Sets the channel for main operations (say !chanset in a channel to set that channel)

* nick <newnick> – Set the bot’s nickname

* flush – Clears relay and conditional variables

* reset – Full reset of the bot

* log – enable/disable logging

* add <user> <command> – Allow <user> to use <command>

* del <user> <command> – Disallow <user> to use <command>

* auth <password> – Adds you to the admins if password matches adminpass

* pubadd <command> – Makes <command> public, everyone can use it

* pubdel <command> – removes <command> from public

* addmod <nick> – Adds <nick> to the admins

* delmod <nick> – Removes <nick> from the admins

* quit – Exits IRC and terminates script

Channel Admin Commands
----------------------

These commands only work if the bot is an OP in the channel. These commands apply on the channel specified by chanset, multi-channel administration is not possible.

* op [<nick>] – Ops <nick>. Ops you if no argument

* deop [<nick>] – Deops <nick> . Deops you if no argument

* voice <nick> – Gives voice to <nick>

* devoice <nick> – Takes voice from <nick>

* ban <nick> – Bans <nick>

* unban <nick> – Unbans <nick>

Misc Commands
-------------

These commands are mostly just for fun.

* ping – Bot replies with ‘PONG!’. Useful for latency testing

* relay <chan1> <chan2> – Relays messages from <chan1> to <chan2>. Specify the bot’s nick for <chan1> to relay messages sent to the bot to <chan2>.

* cond <word1> <word2> – Replies with <word2> if <word1> is said. Meant for PING-PONG but can be used for Hi replies.
