---
layout: page
permalink: /tags/
title: Tags
---

<div id="archives">

  {% assign sortedTags = site.tags | sort %}
  {% for tag in sortedTags %}
  <div class="archive-group">
    {% capture tag_name %}{{ tag | first }}{% endcapture %}
    <div id="#{{ tag_name | slugize }}"></div>
    <p></p>

    <h3 class="tag-head">{{ tag_name }}</h3>
    <a name="{{ tag_name | slugize }}"></a>
    {% for post in site.tags[tag_name] %}
    <article class="archive-item">
      <h4><a href="{{ site.baseurl }}{{ post.url }}">{{post.title}}</a></h4>
    </article>
    {% endfor %}
  </div>
{% endfor %}
</div>

<script type="text/javascript">

  let tags = '['
  {% for tag in site.tags %}
  tags += "'" + {{ tag }} + "' ,"
  {% endfor %}
  tags += ']'

  console.log(tags);
</script>

<script type="text/javascript">
  var jekyllTags = {{ site.tags | jsonify }};

  console.log(jekyllTags);
</script>