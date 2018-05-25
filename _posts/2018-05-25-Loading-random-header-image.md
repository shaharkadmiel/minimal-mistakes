---
title: Randomizing header image
tags: [Random stuff, Images, Jekyll]
# excerpt: Hillshading code.
classes: wide
author_profile: true
published: true
---

Having a random header on reload is a neat feature. Here is my attempt to accomplish that:

### First, list all header images

{% raw %}
```liquid
{% for image in site.static_files %}
    {% if image.path contains '/assets/images/headers/' %}
        <img src="{{ site.baseurl }}{{ image.path }}" alt="header" />
    {% endif %}
{% endfor %}
```
{% endraw %}

{% for image in site.static_files %}
    {% if image.path contains '/assets/images/headers/' %}
        <img src="{{ site.baseurl }}{{ image.path }}" alt="header" />
    {% endif %}
{% endfor %}