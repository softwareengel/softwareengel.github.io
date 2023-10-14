---
layout: page
permalink: /tags/
title: Tags
---
{% comment %}
Allows you to leave un-rendered code inside a Liquid template. Any text within the opening and closing comment blocks will not be printed, and any Liquid code within will not be executed.
{% assign verb = "converted" %}
{% endcomment %}

<div id="archives">
  
  {% comment %}
  {% assign sortedTags = site.tags | sort %}
  {% for tag in sortedTags %}
  {% endcomment %}
  
{% for tag in site.tags %}
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

{% comment %}
<script type="text/javascript">
<!-- 
  let tags = '['
  {% for tag in site.tags %}
  tags += "'" + {{ tag }} + "' ,"
  {% endfor %}
  tags += ']'

  console.log(tags);
-->
</script>

<script type="text/javascript">
  <!-- 
  var jekyllTags = {{ site.tags | jsonify }};

  console.log(jekyllTags);
  -->

</script>
{% endcomment %}