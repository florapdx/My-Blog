title: CLI for Beginners
date: January 2013
tags: tutorials
summary: With the command line comes great power--and great responsibility. Learn the basics of Unix and bash--and how to stay out of trouble-- and I promise that once you get a taste you'll just want to keep learning more. 

#CLI Basics for the Uninitiated

This is one of those things that as a beginner I felt really embarrassed about, but I was downright scared of the Command Line Interface (CLI) for at least the first few weeks I tried using it--add having to muck about in my dotfiles to the mix, and I was liable to have a panic attack on cue.

I still remember the hassle I went through trying to get Ruby, RVM, and Rails up and working on my MB Pro, during the course of which I had to rehab my cluttered PATH and install/deinstall some things. While it was only a pseudo-disaster (instead of the dreaded "sudo" disaster--not: beginners, beware of the "sudo"!), I probably shouldn't have been mucking about without a sense of a) what my dotfiles were for; b) that the command line is essentially just a window into the processes that are happening in GUI environments on the desktop (plus some added power).

Now, I'm one of those people who tends to suffer a lot of anxiety if I don't understand the basics of the context within which I am working, so my own fears may be an inflated version of yours...I sincerely hope for your sake that is the case. But regardless of your threshold for risk, having a basic understanding of the CLI is crucial to getting off the ground as a young developer.

##Unix basics:

Unix was invented in the 1960s and has been developed into a number of different ‘flavors,’ the most popular of which are GNU/Linux, Mac OSX’s Darwin, and Sun Solaris.
Though GUIs and advanced features will vary some between these popular flavors, most Unix features and commands work across these platforms.
Unix is an OS---a suite of programs that make a computer work—and is made up of three parts:
Kernel: the hub of the OS, the kernel allocates memory and time to programs and handles filestore and system call responses
Shell: the shell is a command line interpreter—that is, it acts as the interface between user and kernel—and is started automatically when you log in to your computer as a user. Popular Unix shells include csh, tcsh, ksh, zsh, and bash, which is likely the default shell on your system.
Programs: Remember, commands are just little programs. Programs can thus be anything from Unix commands, to shell commands, to programs you write. Unix programs come in both non-interactive and interactive varieties.
Everything in Unix is either a file or a process. A file is a collection of data; a process is an executing program. A directory is simply a special type of file that contains listing information for other files.
Basic Commands:

Default prompt is: username $

[Note: If your prompt ends with a “#” you are logged in as a super user (su; as in the first two letters of “sudo”), which is a mode you don’t generally want to be operating in. Super user privileges allow you access to system files that can be damaged if you don’t know what you’re doing.]

Tab completion works on most Unix shells.
Unix programs/commands are case sensitive and must be typed in lower case. Parts of a Unix phrase must be separated by spaces.
The default structure is: command option(s) file_or_directory_name(s--comma-separated list if multiple files or directories are being passed)
Options are usually one-letter add-ons that modify the way that a command works, prefixed by a dash (ex: -a). These may be used alone or combined (ex: -ab).
You can write two or more commands on the same line separated by “;”. These will be executed in order.
File names that include spaces must be surrounded by quotes.
Pressing “Return” runs the command you’ve typed.
o   pwd: Shows the present working directory. $ pwd

o   ls: View the contents of a directory. This command will list all the files and directories within the current directory.  $ ls

o   cd: Used on its own, in OSX, will take you to your home directory. $ cd

To change directories, use with name of directory (filenames won’t work). $ cd directory_name (you can also use absolute path if going levels deeper)

To return to the previous directory, use cd, space, and then two periods: $ cd ..

o   mkdir: Create a new directory. $ mkdir my_new_folder

o   open: open a file. $ open myfile.html

o   mv: Move a file into a directory. $ mv filename directoryname

You can also use move to rename a file—just specify a new filename instead of a new
directory name.

o   cp: Makes a copy of a file (helpful for backups or for versioning). $ cp file_to_be_copied destination

o   rm: Remove files or directories (warning: unlike using Trash, there is no going back!) $ rm directory_name

o   less: Display the contents of a file one screenful at a time. $ filename

o   kill: Terminates running of program. $ kill my_stuck_program

o   exit: Exit the command prompt program and close the terminal window. $ exit

 

<<<<<<<<<<<<<<<<<<<<<<<<< more to come >>>>>>>>>>>>>>>>>>>>>>>>>

 