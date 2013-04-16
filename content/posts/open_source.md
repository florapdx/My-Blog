title: Get Started in Open Source
date: April 2013
tags: tutorials
summary: This post represents (a slightly more coherent version of) my notes from Jessica McKellar's PyCon tutorial, "Contribute with Me"....turned into a roadmap, of sorts. It's one that I'm going to follow, so I will reiterate Jessica's plea--"contribute with me!"


This post represents (a slightly more coherent version of) my notes from Jessica McKellar's PyCon tutorial, "Contribute with Me"....turned into a roadmap, of sorts. It's one that I'm going to follow, so I will reiterate Jessica's plea--"contribute with me!"


Why contribute? How can I contribute if I'm a beginner?

There are many reasons to get involved with open source software, not the least of which is that employers are increasingly looking to hire people with OSS-heavy resumes. But there are many other reasons to contribute to the open source movement that are less, well, self-serving. For example, the opportunity to give back to the community--we have all benefitted tremendously from open-sourced software, and you can be part of making someone else's life, workflow, whatever, smoother (and more fun!). Getting involved in the open source community also necessarily means learning from other developers, and in all likelihood will prompt you to write better code--ie, there's an educational and training dimension to the process that can be tremendously beneficial. Then there's the people--the open source community tends to attract people who are passionate and appreciate other people who are similarly driven. These are good people to know. And finally, it's fun! You get the chance to play a part in a larger project that you care about, and get to (hopefully) make friends in the process.

I'll admit that I'm not confident enough at this point to start contributing complicated code to OSS projects--I need a 'softer' entry point. If you are like me, the following are great ways for a beginner to get involved:

Bugs: fix broken stuff--this includes docs!
Documentation: many OSS projects have either incomplete, inadequate, and/or English-only documentation
Website and/or infrastructure: help improve, beautify, or otherwise debug a project's website; if you are a hardware or server wiz, many projects could use help in these areas as well
Licensing: I have to be honest--I don't really know what this entails. But apparently it's a way for people (assumably with some legal knowledge) to contribute
Translation: help non-English speakers use a project by putting your extra-English language skills to work; or, translate projects from other languages into English
 

Let's play pest control!

In "Contribute with Me!" we concentrated on working on bugs, and that's what I will concentrate on here. The workflow for this type of contribution is pretty straight-forward, and you can come in (and exit) at any point in this cycle.

The Lifecycle of a Bug:

Report
Triage
Patch
Test
Review
Resolve
We'll go through each of these phases in detail shortly, but, before we get started, let's go over something basic to all---the need for good communication.

There are two sets of considerations when communicating with others in the context of contributing to open source projects: the first has to do with the social dimensions (content) of communication; the second concerns the tools you might use to communicate.

Content considerations:

Be nice. I would hope this one is self-evident; just be aware that written language can't benefit from the subtleties of inflection that voice, tone, and gesture can provide, so pay a little more attention than you normally might to what you're saying.
Be respectful. This was a great tip from Jessica: ask a question once and then wait for a reply--don't keep asking if you don't get a quick response. Obviously, if days go by and no one is responding to you then you should probably ask again. Another suggestion: be respectful of the work that has been done on the project so far, and strive for constructive conversations--don't be critical or dismissive if something looks confusing or less-than-optimal. I've totally broke this rule in moments of frustration, and very much regretted it later.
Don't assume that other people working on the project share your language or time zone. Communication is especially important and tricky when those with whom you are communicating are spread throughout the country...if not the whole world. Try to be clear and concise in your communication, and patient in your responses. Don't assume that you share the same cultural values either--ie, be sure your public discussions tasteful and appropriate to the task at hand.
Tools:

Bug-trackers/Issue-trackers. 9 times out of 10, your contribution to a project will involve either sourcing bugs and/or posting patches to what's called an "issue (or bug) tracker"--essentially a database of problems and fixes maintained by a particular project. There are many flavors of issue/bug tracker-- including Bugzilla, Github's built-in "Issues" tracker, Google Code's tracker, Launchpad, Roundup, and Trac --and each one works slightly differently, but they (mostly) all share the same basic features: a search/sort feature that allows you to find bugs according to some criteria (date, keyword, category, etc.); and an interface for reporting on a bug you've found. [Note: reported bugs/issues are often referred to as "tickets", and occasionally these trackers are referred to as "ticketing systems."]
IRC. Internet Relay Chat (IRC) is an old school, but still widely used, system for conversing in real-time. Though it's essentially just a system of chat rooms, IRC can be confusing, and may be intimidating, to those who've never used it before. Stick with it till you've got it down--real-time chatting is super-fun, and you'll soon wonder how you ever lived without IRC in your life. Too long to go into here, I've got a primer to get you going here. Introduce yourself on IRC early in your contribution, and use it to ask questions and keep on top of new developments. Remember that IRC is for short messages --not for pasting big blocks of code.
 

1. Report

Just as in any other type of reporting, the keys to writing good bug reports are precision and completeness. Obviously, "Program stalled when I pressed 'Enter'" is too vague and doesn't communicate enough information for anyone to be able to track down and fix the bug you've discovered...a little due diligence at this point will save the person (who may be you, after all), a lot of time down the line.

Any bug report should include the following, at a minimum:

a short, self-contained example (ie, code that produced problem w/information about the environment you are working in--operating system, program/language/application version, virtual environment, if any)
explicit steps to reproduce the bug, including input, expected output, and actual output (error message or trackback, etc.)
You'll be submitting this information in the project's bug/issue tracker, which should either be linked to by the project's homepage or may be found by running a Google search (for example, "Django bug-tracker"). Remember that in addition to looking for the words "bug" and "issue" when you are looking for a project's tracker you should also look for any mention of "tickets" or "ticketing system" (essentially a synonym for issue tracker).

Once you find the issue tracker you are looking for, locate the link or button that will take you to the report page. This will, in all likelihood, mean having to create an account, either with the project itself or with the bug tracking software that the project is using (if Github, Bugzilla, etc). Once you've created an account and are through to the bug reporting page, you'll probably notice that you are being asked for more than just the essential info outlined previously. Below is a list of possible fields and what they mean:

Summary/Title: a concise one-line summary that adequately represents the bug

Description: this is where to put the "any bug report should include" info listed above

Product: in larger projects, what specific product are you using (ie, if you're at Mozilla's bug tracker site, indicate whether your bug relates to Firefox, Thunderbird, Persona, etc.)

Component: in larger projects, what library, module, subproduct, etc. contains the bug? (May or may not be within "product," above)

Version: the version number of the software/language that you are using

Type/Category: so others can use the search/sort mechanism to find your bug, choose a category that best fits; may also be used to distinguish a bug from a feature request (oh yeah, you can submit these too!), etc.

Keywords: any keywords that may serve to make your bug more findable in the database

Status: are you leaving the bug for someone else to fix? Consider it "Open." Fixing the bug yourself? "In-progress" is probably what you're looking for. Submitting a patch for the bug in the report? "Needs review" is the choice for you. There will be variations, so use your best judgement.

Severity/Urgency/Priority: how urgent or critical is the bug? does it relate to an essential function of the site? to security/information safety? If so, it's critical. Otherwise, use your best judgement.

Level/"Easy"/"bite-sized"/etc: is asking for an indication of the suitability of your ticket for beginners

Owner/Assigned To: If you are planning on fixing the bug, assign it to yourself. If you want to hand the problem off to someone specific, assign it to him/her. Otherwise, leave this blank.

Nosy/CC: If you want someone else to be clued in on your progress, or if you will be working with someone else to fix the bug, list her/him/them here.

While it's important to give all the info you can, don't expect to fill out every field on the form--and if in doubt, just leave the field blank. When you're finished, submit the report and...voila! You've just made your first contribution to open source!

 

2. Triage

To "triage" means to descend on and manage the treatment for a group of victims in times of war or disaster. In the less carnage-y case of software, to triage means to define the boundaries around and intervene in a section of code that isn't working as it should.

Triaging may or may not be separated from reporting. If you've reported a bug that is relatively straightforward (ie, a typo or minor CSS bug) and you are submitting a patch yourself, you probably don't need to worry about triaging at all. On the other hand, you may skip the reporting phase yourself by picking an "open" bug from the project's database to work on, and would thus likely start at the triage phase. This would entail reading someone else's bug report and then using the information they've provided to isolate the offending code so that you can create a plan to fix it. To do this may involve bringing other "doctors" into the fray; particularly if you require assistance, plan to reach out through IRC, the project's mailing list, or on Stack Overflow.

If you've already submitted a bug report at one time or another, then reading someone else's report shouldn't be too mysterious. First, you'll notice that there's probably some sort of table at the top of the report containing the data collected in the initial report-- program, version number, assignee, nosy list, etc. Then, you'll find a list of any files that have been uploaded, including patch files and/or diff files that give patches context. Last, you might find a list of messages (starting with the original bug description) that have been posted by different people working on the bug, followed by a table or graphical representation of the history of the intervention (the triage effort).
It's important to be aware that the relative importance of the triage phase is directly proportional to the complexity, or "slipperiness" of the bug in question. For example, you may run into a bug that only pops up in particular browser versions or that causes different problems for different users, and you don't yet know why. You can probably imagine that some bugs are caused by minor problems in foundational code that then only manifest "symptoms" after they've snowballed by traveling through one or another thread. These bugs need to be reproduced in different environments in order to discover their origin and reach.

Hopefully, you aren't jumping right into one of these more complex bugs as a newbie (though I've run into seemingly "innocent" CSS bugs that unearthed strange compatibility issues in Chrome v.24 on IE8 with Windows Vista. Sometimes you just find yourself down the rabbit hole.) My advice would be to leave triaging up to more experienced contributors for now--isolating complex bugs requires experience, knowledge of the code base, and probably some elaborate virtual machines/environments setup for testing....all things that you won't possess as a beginner. Just know that it happens, you'll get there soon, and that any info you can provide will be much appreciated.

 

3. Patch

Okay, so you've either discovered a bug yourself or have chosen one from your favorite project's database of bugs to work on. Now what? Squash the bug, of course!

We've already gone through how to write and read bug reports, but before we can go through the steps to submitting your first patch we need to go over a couple of essential tools.

Git: (Hopefully you already have git installed on your local machine and have a basic working knowledge. If not, check out this guide.)

No matter how your chosen project accepts bug fixes (ie, in ".patch" files or via pull request) you'll need to download a copy of the project (or some part of it) to your local machine so that you can modify its files. Depending on the project, you may already have it installed locally or may be able to install it via a package manager or tool, such as pip or Homebrew. Other projects, particularly those hosted on Github or Bitbucket, you'll likely need to "clone" to your machine. This is a relatively straightforward process:

1. open your Terminal application

2. in Unix/Linux systems type into prompt
$ mkdir project_name
# make a new project directory

3. make sure you are in this directory before you clone
$ cd project_name
# change directories into your new project directory

4. using the actual https address (or ssh address, if you've configured your ssh file already) for the project that is listed on its Github or Bitbucket page, clone the project repository locally by typing into your prompt
$ git clone https://host.com/project_name

5. wait for your prompt$ to reappear; this should be preceded by a bunch of loading code filling up your Terminal!

6. navigate to wherever you've created your directory, either in the command-line (using the "cd" command) or in your Finder. If the former, type "ls" from within its directory to view the contents of the project you've just cloned; if the latter, double-click to reveal the project's files. Now get to work!

 

"diff" and "patch":

in CLI, use "diff -u"

--if generate a diff, can use the patch tool to merge that diff into your version

Git:

--collaborative development

--managing changes/history

--like wikipedia

* git log to look at history

* git show commitID will show you more info on a specific commit

 

4. Test

Make sure that this actually fixes the problem and doesn't break anything else; this can be a big job

ex. twitter-python uses unittest module

ex. Twisted uses buildbot for testing, and automates tests across many different OSs

 

5. Review

Bugs happen in code--there is no such thing as completely bug-free code;

But we try….so someone else (not patch submitter) will read over the diff, see if readable, well-documented, tests added, etc.

Probably going to be a bit of back-and-forth during this process

 

6. Resolve

Means its out in source code, pushed out for everyone to use and enjoy

 

 

Other Projects in Need

Write the Docs, Already!

If you are interested in working on documentation, some resources to look into would be Sphinx--for Python projects, specifically--and/or Write the Docs for general information on the art and science of documentation.