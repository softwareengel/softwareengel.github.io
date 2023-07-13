---
layout: post
title: Serenity - Einfügen von 2. Spalte mit CSS 
categories: [3D]
tags: [ Serenity ]
--- 

- [Serenity Einfügen von 2. Spalte mit CSS](#serenity-einfügen-von-2-spalte-mit-css)
  - [JS und HTML Files](#js-und-html-files)

# Serenity Einfügen von 2. Spalte mit CSS 

- <https://github.com/serenity-is/Serenity/blob/master/INSTALL.md>

- <http://thucydides.info/docs/serenity-staging/#_writing_serenity_page_objects >
- <https://volkanceylan.gitbooks.io/serenity-guide/content/>

## JS und HTML Files 

split.js 
```js
.split {
    -webkit-box-sizing: border-box;
    -moz-box-sizing: border-box;
    box-sizing: border-box;
    overflow-y: auto;
    overflow-x: hidden;
    width:100%;
    height: 100%;

    

}

.split-content {
    border: 1px solid #C0C0C0;
    box-shadow: inset 0 1px 2px #e4e4e4;
    background-color: #fff;
    height: 100%;
    display: flex;
    flex-direction: row;
}
.gutter {
    background-color: transparent;
    background-repeat: no-repeat;
    background-position: 50%;
    height: 100%;
}

.split.split-horizontal,
.gutter.gutter-horizontal {
    height: 100%;
    float: left;
}

.gutter.gutter-horizontal {
    cursor: col-resize;
}

.gutter.gutter-vertical {
    cursor: row-resize;
}

```

html 
```html 
<div id="b" class="split">
    <p> bb bb </p>
</div>
```
