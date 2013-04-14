title: Customize Your Bash Prompt
date: February 2013
tags: tools, tutorials
summary: Like IRC, the bash shell is intimidating for the beginner and is something that you kind of just have to get used to. Unlike IRC clients, however, there are all sorts of fun ways to customize your prompt and shell environment to better suit your workflow (and your style). While we're going to leave more complex scripting assignments for later, expect to exit this tutorial with a more useful, and fun, prompt.

Your bash prompt comes with a standard command prompt with a default setting something like ````$ PS1="\u@\h \w>```` in your .bash_profile or .profile (if you are using OSX) that translates to something like this:

````UserName YourComputerName DirectoryName $````

While useful, this is kind of boring and doesn’t give us very much information about the environment we’re working in. So let’s customize our prompts!
<br />

##Steps:
####1.
Open your Terminal and type in ~/.bash_profile. 
**(see link at end of this doc for discussion of .bash_profile v. .bashrc). 

This should open your bash_profile file in TextEdit if you are on a Mac. Alternatively, you can open with another editor by typing in ````$ vi ~/.bash_profile````, substituting “vi” for your chosen editor (unless your chosen editor is vi!). 

If you can’t find these files or would like to search for them visually, you can reveal your hidden dot files using:

````
$ defaults write com.apple.Finder AppleShowAllFiles YES
````

After pressing enter, navigate to your finder icon on your launch bar. Press the Alt (Option) key and Ctrl-click on the Finder icon. Choose “Relaunch” from the menu, then release keys. This will relaunch the finder with your hidden files revealed.

When you are finished accessing your hidden files, be sure to hide them again for safety by repeating the process, only this time typing into the CLI:

````
$ defaults write com.apple.Finder AppleShowAllFiles NO
````

[*Note: if using pre-Lion OSX, use TRUE and FALSE instead of YES and NO.]
<br />

You can also check your current PS1 settings in the CLI by typing in: ````$ echo $PS1````

And change your PS1 variable in the CLI by typing in: ````PS1=’…’```` (though you won’t be able to add Chris’s ‘parse_git_branch’ function this way).
<br />
<br />

####2.
Add this template (below, between lines) to the bottom of your bash_profile:

Note: This will produce a command prompt that looks like this (using mine as an example:
````My-MacBook-Air Wed Feb 20 19:51 TwitterAPI (master)  ♡ $````

….and if I press <enter> and command returns false, then:
````My-MacBook-Air Wed Feb 20 19:31 TwitterAPI (master)  ♥ $````

____________________________________________________________________

````# Prompt customizations:````
<br />


	# This function lets us know which branch we are on when working in a local repo:
	function parse_git_branch() {
    	x=`git branch --no-color 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/(\1)/'`
    	if [[ "$x" == "" ]]; then
      	echo ""
    	else
      	echo "$x "
    	fi
	}


<br />


	# Checks status to see whether last command returned a true or false:
	export PROMPT_COMMAND='export OLD_STATUS=$?'

<br />


	# Build your new command prompt:
	export PS1='\[\033[1;35m\]\h \[\033[0;30m\]\d \[\033[0;30m\]\A \[\033[1;30m\]\W \[\033[0;30m\]`parse_git_branch` \[\033[0;30m\]`if [ $OLD_STATUS = 0 ]; then echo \♡; else echo \♥; fi` \[\033[1;33m\]\$ \[\033[0m\]'

_________________________________________________________________________

**So let’s break that down.** 

*  “````export PS1=````”: means export the PS1 variable to primary prompt on bash load

*  “````[\033[1;35m\]\h ````“: everything in between the brackets is setting the color of the following variable, in this case the “\h “ for hostname. 

*  The ````\033```` doesn’t change--it just tells bash that it can expect 33-octal ASCI color codes to follow.

*  The ````1;35m\```` is the actual color code. For a list of these codes refer to chart below.

*  The ````\h````, as we said before, is the variable name for the piece of data that you want your command to display. Be sure to add a space after the variable and before the next term in your PS1 ‘sentence’ (beginning with a “\”) or your prompt will look like this ````MyComputerFeb4Desktop$````, etc.

<br />
[**This template is a modified version of the one provided by Christopher Swenson, whose original you can find at:
https://github.com/swenson/dotfiles/blob/master/bash_prompt.sh]
<br />

####3.

Use the following variables, color codes, and symbols to customize the given template (substituting your choices in for the ones given). 
<br />[Note that you can use the “````\n ````” newline variable to break your prompt into multiple lines.]

***Bash variables*:**
<br />\a : an ASCII bell character (07)
<br />\d : the date in "Weekday Month Date" format (e.g., "Tue May 26")
<br />\D{format} :	the format is passed to strftime(3) and the result is inserted into the prompt string; an empty format results in a locale-specific time representation. The braces are required
<br />\e : an ASCII escape character (033)
<br />\h : the hostname up to the first '.'
<br />\H : the hostname
<br />\j : the number of jobs currently managed by the shell
<br />\l : the basename of the shell’s terminal device name
<br />\n : newline
<br />\r : carriage return
<br />\s : the name of the shell, the basename of $0 (the portion following the final slash)
<br />\t : the current time in 24-hour HH:MM:SS format
<br />\T : the current time in 12-hour HH:MM:SS format
<br />\@ : the current time in 12-hour am/pm format
<br />\A : the current time in 24-hour HH:MM format
<br />\u : the username of the current user
<br />\v : the version of bash (e.g., 2.00)
<br />\V : the release of bash, version + patch level (e.g., 2.00.0)
<br />\w : the current working directory, with $HOME abbreviated with a tilde
<br />\W : the basename of the current working directory, with $HOME abbreviated with a tilde
<br />\! : the history number of this command
<br />\# : the command number of this command
<br />\$ : if the effective UID is 0, a #, otherwise a $
<br />\nnn : the character corresponding to the octal number nnn
<br />\\ : a backslash
<br />\[ : begin a sequence of non-printing characters, which could be used to embed a terminal control sequence into the prompt
<br />\] : end a sequence of non-printing characters

 <br />
 ***Bash Color Codes:***

Black 0;30m
<br />Dark Gray 1;30m
<br />Blue 0;34m
<br />Light Blue 1;34m
<br />Green 0;32m
<br />Light Green 1;32m
<br />Cyan 0;36m
<br />Light Cyan 1;36m
<br />Red 0;31m
<br />Light Red 1;31m
<br />Purple 0;35m
<br />Light Purple 1;35m
<br />Brown 0;33m
<br />Yellow 1;33m
<br />Light Gray 0;37m
<br />White 1;37m

<br />
***Symbols (just copy/paste symbol itself rather than inserting UTF encoding)***:

☀	Sun
<br />☼	Sun w/Rays
<br />☁	Cloud
<br />☽	Moon
<br />☆	White Star
<br />★	Black Star
<br />☠	Skull and Crossbones
<br />⚑	Black Flag
<br />⚐	White Flag
<br />☭	Hammer and Sickle
<br />☺	Smiley Face
<br />☹	Frowny Face
<br />♡	White Heart
<br />♥	Black Heart
<br />♨	Hot Springs (or Hot Soup, as I like to think of it)
<br />💔	Broken Heart (copy/paste square--will show up in bash)
<br />😱	Screaming Face (copy/paste square--will show up in bash)
<br />🎂	Birthday Cake (copy/paste square--will show up in bash)
<br />⛤	Pentagram (copy/paste square--will show up in bash)

<br />
...for more see http://en.wikipedia.org/wiki/Miscellaneous_Symbols (copy/paste symbol)
<br />

####4.
If you want, you can also customize the secodary (PS2), tertiary (PS3), and quaternary (PS4) prompts, which may be issued when programming in your shell:
<br />

* ***PS2***: Is the continuation interactive prompt, and is issued when bash needs more information to complete your command/script (ie, when you are issuing a multi-line command). The default value is “>”, but you might want it to say “more ->” or “continue ->”, etc. for clarity.

* ***PS3***: The tertiary prompt string is called when you issue the select command inside of a shell script (ie, when user is given a list of selections from which to pick). By default your prompt will ask you for “#?”, but you might want it to ask you for an option more explicitly. See http://www.serverwatch.com/tutorials/article.php/3821966/The-Various-bash-Prompts.htm for explaination and easy-to-follow example. 

* ***PS4***: The quaternary string is used to prefix tracing output (to STDOUT) when invoking “set -x” for debugging (ie, your program will print out each line of the script as it is running commands). By default, your prompt will give you a “++” for every line, but you might want to set it to give you line numbers instead using: export PS$=’$LINENO+ ‘.

* ***PROMPT_COMMAND***: Bash executes the PROMPT_COMMAND just before displaying the PS1 variable. You can use this to:
 set window title: (http://blog.friedland.id.au/2010/03/automatically-update-terminal-window.html),
make substitutions in your PS1 (though setting PS1 directly is recommended): (http://www.tldp.org/HOWTO/Bash-Prompt-HOWTO/x264.html), 
or control history across multiple Terminal sessions: (http://www.numerati.com/2011/08/03/bash-goodies-turbocharging-your-history)
<br />

####5.

**Read more**:

http://www.tldp.org/HOWTO/Bash-Prompt-HOWTO/c141.html

If you are confused about .bash_profile vs .bashrc (since many sites will tell you to use one or the other, which can be confusing if you don’t understand the difference. Additionally, OSX doesn’t come with a .bashrc file, which, although you can easily make your own, doesn’t make anything less confusing).....you might take a look at:

http://superuser.com/questions/409186/environment-variables-in-bash-profile-or-bashrc
