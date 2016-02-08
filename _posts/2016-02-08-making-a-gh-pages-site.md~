---
layout: post
title:  "Making a gh-apges site"
date:   2016-02-08 15:49:31 -0600
categories: 
---


Getting the repo

		$ git clone git@github.com:dnedveck/Beer.git

Going into the dir

		$ cd Beer/

Making the `gh-pages` branch

		$ git checkout --orphan gh-pages
		Switched to a new branch 'gh-pages'

Cleared the directory

		git rm -rf ./*

... I already had Jekyll installed, see:

		$ jekyll -v
		jekyll 3.0.2

Initialize jekyll in the directory

		$ jekyll new .
		New jekyll site installed in /home/derek/projects_git/Beer.

Let's see what it made:

		$ tree
		.
		├── about.md
		├── _config.yml
		├── css
		│   └── main.scss
		├── feed.xml
		├── _includes
		│   ├── footer.html
		│   ├── header.html
		│   ├── head.html
		│   ├── icon-github.html
		│   ├── icon-github.svg
		│   ├── icon-twitter.html
		│   └── icon-twitter.svg
		├── index.html
		├── _layouts
		│   ├── default.html
		│   ├── page.html
		│   └── post.html
		├── _posts
		│   └── 2016-02-08-welcome-to-jekyll.markdown
		└── _sass
				├── _base.scss
				├── _layout.scss
				└── _syntax-highlighting.scss

		5 directories, 19 files


Just to get things rolling, I'm going to edit the _config.yml, save this as a post, and then push to GitHub

pushing to github

		$ git push --set-upstream origin gh-pages



