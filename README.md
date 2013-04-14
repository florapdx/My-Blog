## Overview ##

This repository contains the source for my personal blog, built with Python microframework Flask and using Frozen-Flask and Flask-FlatPages to generate a static site. I've added my own customizations to the scaffolding offered by other projects, listed below.

## Using ##
You are welcome, within the limits of each requirement's license, to take and use as you please my implementation here (minus the content & personal info, of course). To do so:

1. create a new directory for your blog in your projects folder (or wherever you want to keep your blog's source files) ```$ mkdir my_blog```
2. change into your new blog's directory ```$ cd my_blog```
3. create a new virtualenv for your blog:
* if you create your virtualenvs in each of your projects' folders: ```$ mkdir my_blogs_env``` and then ```$ virtualenv my_blogs_env```
* if you create your virtualenvs in their own directory, separate from your project files (but also in your home directory): ```$ mkdir -p ~/Virtualenvs_directory/my_blog_env``` and then ```$ virtualenv ~/Virtualenvs_directory/my_blog_env```
4. activate your virtualenv:
* ```$ source my_blogs_env/bin/activate``` 
* or ```$ ~/Virtualenvs_directory/my_blogs_env/bin/activate```
5. Install the foundation requirements:
```$ pip install Flask Frozen-Flask Flask-FlatPages```
6. clone this repo ```$ git clone https://github.com/florapdx/My-Blog.git``` 
Note: until such time as I set up a separate repo to house only the scaffolding, you will have to strip out all of my personal blog stuff, twitter widget, meetup.com widget, etc.
…or, see the "Attributions" list and follow their lead to make your own implementation :)
7. Do it up! Add filters for different post tags; customize the templates; add some cool JS; make it pretty with your own CSS…you get the idea.
8. Run locally with the command ```$ python sitebuilder.py``` and "freeze" for publishing with ```$ python sitebuilder.py build```

## Attribution ##
There's not a whole lot to pull from when using these tools, so I relied heavily on the following projects to get going (and recommend that you do too):
* Nicolas Perriault's [blog post](https://nicolas.perriault.net/code/2012/dead-easy-yet-powerful-static-website-generator-with-flask/)
* Jeremy Axmacher's [blog post](http://obsoleter.com/2012/12/12/creating-plume-a-static-site-generator-with-flask-part-1/)
* Alexander Jung's [Blogen project](https://github.com/alexex/blogen)
* Jacob Peck's [Ptah project](https://github.com/gatesphere/ptah)

## Licensing ##
All content is Creative Commons (Attribution). All my code in this repo is [MIT Public License](http://opensource.org/licenses/mit-license.php) (i.e., do what you want with the code, but consider it as-is). 
All projects used herein subject to their own licensing (see "Attributions" as well as software documentation for specific terms).

## Next Steps ##
There is still much work to do on my blog before it goes live, but the real next step would be to abstract out all of my personal customizations and to offer this as a resource that can be easily localized.

