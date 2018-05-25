---
title: Randomizing header image
tags: [Random stuff, Images, Jekyll]
# excerpt: Hillshading code.
classes: wide
author_profile: true
published: true
---

Having a random header on reload is a neat feature. Here is my attempt to accomplish that:

### Loop through header images and construct a list

I have placed all the header images that I would like to randomize in ``/assets/images/headers/``. So I want to loop over all ``site.static_files`` and add only the images within that specific folder to my list.

{% raw %}
```liquid
<!-- init the list -->
{% assign headers = "" | split: ',' %}

<!-- loop and add -->
{% for image in site.static_files %}
    {% if image.path contains '/assets/images/headers/' %}
        <!-- add image -->
        {% assign headers = headers | push: {{ site.baseurl }}{{ image.path }} %}
    {% endif %}
{% endfor %}

{{ headers }}
```
{% endraw %}

{% assign headers = "" | split: ',' %}

{% for image in site.static_files %}
    {% if image.path contains '/assets/images/headers/' %}
        {% assign headers = headers | push: {{ site.baseurl }}{{ image.path }} %}
    {% endif %}
{% endfor %}

{{ headers | inspect}}
{{ headers | jsonify}}