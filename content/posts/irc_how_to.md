title: IRC Primer
date: December 2012
tags: tools, tutorials
summary: IRC can be intimidating for the beginner, especially since there’s a lack of good (and up-to-date) material online. For those of us who grew up in the age of the GUI, there's something about the antiquated 'look and feel' of IRC that is also difficult to get a mental handle on. Don't worry--follow these instructions and you'll be savvy in no time. 


IRC can be intimidating for the beginner, especially since there’s a lack of good (and up-to-date) material online. Here’s everything you need to know to get started:
<br />

##What is IRC?

IRC stands for Internet Relay Chat, a technology that allows anyone with an Internet connection to chat in real time. 
 
The IRC environment consists of various networks, and each has its own flavor and following.  The FreeNode network caters to the Free and Open Source Software (FOSS) and non-profit communities, and is the network we'll be using to connect with local tech communities.
  
Within each network, communities organize conversations by creating different channels.  Channels are basically chatrooms, and are usually prepended by a hash (#) in the network.  (As you may have guessed, #pyladies is the channel for our group.)
<br />

##Joining a Network

In order to join FreeNode (or any IRC network), you need to either sign up to use the online version (which is platform agnostic), or you need to install a client app on your computer (there are options for Mac and Windows/Linux).  

We’ll get to the client options in a minute, but first let’s go over how to log in online, the best option for those who aren't ready or don’t want to commit to another app.
<br />
<br />

###Accessing FreeNode Online:

**signing up**:

The FreeNode online portal can be found at [http://webchat.freenode.net/](http://webchat.freenode.net/).
You’ll see three input areas: Nickname, Channels, and a reCaptcha box. In the first, pick a nickname that you would like to be identified by on IRC. 

_For privacy’s sake it’s generally advisable not to use your whole (first and last) name, but since it’s also nice to have some idea of who one is talking to,“1234” probably isn’t great either. Try to find a balance that you are comfortable with._

If you like the name you’ve chosen and want to continue to use IRC, we suggest that you register your nickname with NickServ (see Fundamentals section below).

Second, input “#channel_you_want_to_join” (the hash is important) into the “Channels” box, and enter the reCaptcha phrase. Hit “Connect”. 

That’s it--you’re in! 

**getting around**:

You should see a new page loading a bunch of code--ignore it and wait until a new, clean page appears. This is the FreeNode online console; it’s different from the loading page in that it is divided into two columns.  

The first, larger one should have a message near the top somewhere announcing that  at “[time] == (your nickname) .....has joined #channel_name.” This is the messaging console, and if you look really, really hard at the bottom of the window, you’ll see that the fine folks at FreeNode have placed a barely-visible text input bar there. 

Navigate to that bar and type in, “Hello!” Hit enter to see how posting works--your message should appear at the bottom of the discussion thread in the lefthand box. 

_FYI, any message you type in this way will be visible to everyone logged in to that channel (don’t worry, we’ll go over how to send private messages below)._  

The second column, the skinnier one on the right, shows the nicknames of other channel members who are currently logged on.

Finally, the very top bar is where you will see displayed all the channels that you have joined. 

**changing channels**:

We’ll go over this again in Fundamentals, but if you want to add more channels, type (sans quotes) “join #channelname”, hit return, and then click the link that comes up in the main console (left-column. Hovering over #channelname will show underline indicating that it’s a link); you’ll see that channel’s tab appear at the top of the page. 

To switch back and forth between channels, just click back and forth among these tabs, or hit the “X” to leave that channel. That's all there is to it!
<br />
<br />

###Accessing and Using FreeNode Through a Client	
There are a range of client options (applications for accessing IRC) that will work with FreeNode. Listed below are some popular choices for Mac and Windows machines. We can’t explain the use and layout of each different app, but they all basically work like [webchat.freenode.net](http://webchat.freenode.net/), only with more bells and whistles. 

_It is recommended that you download one of these options if you intend to use IRC regularly._

**For Mac:**

* _LimeChat_: LimeChat provides a simple, clean interface for basic IRC chatting. Free and available either through the app stores (there are Mac (free), iPad ($4.99), and iPhone ($4.99) versions) or at [http://limechat.net/mac](http://limechat.net/mac). There isn’t much to setting up--just pick freenode from the server list and click the “+” icon below the channel list to add #channel_name to your channels. You will need to choose a nickname as well; again, for privacy’s sake, don’t use your full legal name.  Don’t worry about all of the other input boxes--you’re done!

**For Windows/Linux**:

* _XChat_: XChat ver.2 can be downloaded at [http://silverex.org/download](http://silverex.org/download), or you can search [http://xchat.org/download](http://xchat.org/download) for the appropriate linux version. Both of these sites contain info on the particulars of XChat, and you may also want to visit [this thread](http://bit.ly/TnruwN) on Stack Exchange that gives a step-by-step on getting set up. There will be lots of boxes that you don’t need to worry about, but what you will need to do is choose a nickname (don’t use full legal name); select “FreeNode” from the “Networks” box (the server will be automatically chosen for you, so don’t worry about that); click “Connect” and wait for a success dialog, where you will select the radio button “Join this channel”. Type #channel_of_your_choice into this dialog and click “OK”. You should now find yourself in that channel.
<br />
<br />

##IRC Fundamentals 

###Registering Your Nick

If you think you might be interested in using IRC regularly, it is strongly recommended that you register your name with NickServ (the FreeNode nickname server). Much like Twitter, this will ensure that you and you alone will be represented by your username. You will also need to select a password along with your registration, and will be asked to provide an email address to aid in password recovery (should you lost it some time in the future).

To register your IRC nick, enter the following, subbing in your info, into the chat input bar on any channel (no one will see your entry---promise!):

```/msg NickServ REGISTER password youremail@example.com```

Press return. You should see a message somewhere in the console window verifying that FreeNode has received your registration and has sent a confirmation link to the email you provided. 

Open your email, copy the link, and then return to your client or to webchat.freenode.net and paste into the chat bar. Hit enter. You should see another confirmation, this time saying that your nickname has been registered and verified. Done!
<br />

###Using IRC Commands
In addition to being able to type basic plaintext messages into the chat bar, you may also use a number of shorthand commands to do things in IRC. Below is a list of the most common. You may find more complete lists [here](http://bit.ly/SMUOu7) and [here](http://bit.ly/TNmP3q) (just remember that the authors do not intend for you to use the <> when you use these commands).

For each of these, the “/” is intentional--ie, use it! Caps aren’t necessary, but are fine to use.

* /AWAY yourmessage  (let’s others know you’ve stepped away from your machine)
* /HELP  (requests help file)
* /INVITE nickname #channel  (invites user to channel)
* /ISON nickname  (is nickname somewhere on the network?)
* /JOIN #channel  (join a new channel; see list below for suggestions)
* /MSG nickname yourmessage  (send a private message to another user--other user doesn’t have to be on the channel at the time to receive)
* /NICK newnickname  (allows a client--you/your app--to change their IRC nickname)
* /WHOIS nickname/yournickname  (shows you info about another user/the info others can see about you)

##Fin.
** Don't forget to pop in and say hi at #pyladies! **