---
layout: page
permalink: /categories/
title: Categories
---

<div id="archives">
{% for category in (site.categories| upcase | sort )  %}
  <div class="archive-group">
    {% capture category_name %}{{ category | first }}{% endcapture %}
    <div id="#{{ category_name | slugize }}"></div>
    <p></p>
    <h3 class="category-head">{{ category_name }}</h3>
    <a name="{{ category_name | slugize }}"></a>
    {% for post in site.categories[category_name] %}
    <article class="archive-item">
      <h4><a href="{{ site.baseurl }}{{ post.url }}">{{post.title}}</a></h4>
    </article>
    {% endfor %}
  </div>
{% endfor %}
</div>

<div id="archives2">
{% assign sorted_categories = site.categories | sort %}
{% for category in sorted_categories %}
  {{ category[0] }} <!-- category name -->
  {% for post in category[1] %}
    {{ post.title }} <!-- post title within the category -->
  {% endfor %}
{% endfor %}
</div>
