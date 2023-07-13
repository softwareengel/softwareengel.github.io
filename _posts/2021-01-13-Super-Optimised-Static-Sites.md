---
layout: post
title: Super Optimised Static Sites
categories: [Blog]
tags: [Jekyll, OSS, Markdown, Theme]
--- 

![](../pics/20230707130447_jamstack.png)

<!-- TOC -->
- [Super Optimised Static Sites](#super-optimised-static-sites)
  - [Docusaurus](#docusaurus)
  - [Static Site Generators List](#static-site-generators-list)

<!-- /TOC -->
# Super Optimised Static Sites

Super Optimised Static Sites

If you use GitHub pages, there's a high chance you're also using Jekyll. The biggest thing Jekyll brings is templating - which is great both for developer speed and for getting consistency in your site.

Today, Jekyll is over 12 years old, and it does show its age in places. I wanted to see what was possible with today's more modern tooling.

The toolchain makes heavy use react-dom/server and leverages a powerful custom component system that handles the site's assets. While I'm not the first to do a static site system based on React, the custom component system is what sets it apart, and gives way to,

React-based templating
Does not include React on the client (or any JS unless you want it)
Effortless compression/minification of images, CSS, and JS
Simple long term caching of assets
Granular control of how assets are used - including inlining critical CSS and JS
The best CSS optimisation available - I've not seen anything that comes close here

Putting this all together makes the total page weight for the page you're currently on less than 100kb - and that's including a 50kb font.

Firstly, React-based templating. This is basically the same as MDX. You can include HTML and JSX inside your markdown,

- <https://jacobdoescode.com/2020/12/30/super-optimised-static-sites>

## Docusaurus

- <https://docusaurus.io/docs/en/tutorial-publish-site>

## Static Site Generators List

- <https://jamstack.org/generators/>

![Static Side Generators 1](../pic/Screenshot_2021-02-10%20Static%20Site%20Generators%20-%20Top%20Open%20Source%20SSGs%20Jamstack.png)

- <https://staticsitegenerators.net/>

![Static Side Generators 2](../pic/Screenshot_2021-02-10%20Static%20Site%20Generators.png)
