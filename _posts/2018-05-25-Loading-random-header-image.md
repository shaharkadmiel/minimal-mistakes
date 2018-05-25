---
title: Randomizing header image
tags: [Random stuff, Images, Jekyll]
# excerpt: Hillshading code.
classes: wide
author_profile: true
published: true
---

<script type="text/javascript">
    var randomIndex;
    var headersJS;

    randomIndex = Math.floor(Math.random() * headersJS.length);

    document.write('<p>' + headersJS[randomIndex] + '</p>');
</script>

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
        {% assign headers = headers | push: image.path %}
    {% endif %}
{% endfor %}
```
{% endraw %}

{% assign headers = "" | split: ',' %}

{% for image in site.static_files %}
    {% if image.path contains '/assets/images/headers/' %}
        {% assign headers = headers | push: image.path %}
    {% endif %}
{% endfor %}

We can now have a look at what is stored in the ``headers`` array with:

{% raw %}
```liquid
{{ headers | inspect }}
```
{% endraw %}

{{ headers | inspect }}

### Pick a random header

Using the ``sample`` filter we get a random item from the ``headers`` array.

{% raw %}
```liquid
{% assign random-header = headers | sample %}
{{ random-header | inspect }}
```
{% endraw %}

{% assign random-header = headers | sample %}
{{ random-header | inspect }}

The problem is that because Jekyll is a static site generator, this happens when the static page is built and not on reload. So we need to encapsulate this in a Javascript.
