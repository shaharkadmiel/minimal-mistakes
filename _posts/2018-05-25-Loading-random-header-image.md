---
title: Randomizing header image
# header:
#   image: random
tags: [Random stuff, Images, Jekyll, Liquid, JavaScript]
# excerpt: Hillshading code.
# classes: wide
toc: true
toc_label: "Contents"
author_profile: true
published: true
---

Having a random header on reload is a neat feature. Here is my first attempt to accomplish that:

## The initial idea

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

The problem is that because Jekyll is a static site generator, this happens when the static page is built and not on reload. So we need to encapsulate this in a JavaScript that is executed every time a page is reloaded.

## The solution

I found this very helpfull [post](https://thornelabs.net/2014/01/19/display-random-jekyll-posts-during-each-page-load-or-refresh-using-javascript.html) by *James W Thorne* that mixes Liquid code and JavaScript code. This may not be the most elegant solution but id works. Several files need to be modified for this to work.

### default.html layout

I added the following JavaScript/Liquid mix to the ``<head>`` section of the ``default.html`` layout:

{% raw %}
```html
<script src="/assets/js/vendor/jquery/jquery-3.3.1.min.js" type="text/javascript"></script>

<script type="text/javascript">
    var headers = [
    {% for image in site.static_files %}
        {% if image.path contains '/assets/images/headers/' %}
            "{{ site.baseurl }}{{ image.path }}"
                {% unless forloop.last %},{% endunless %}
        {% endif %}
    {% endfor %}];
</script>
```
{% endraw %}
\* *everything in the square brackets must be one line. Lines here are broken for readability*

And place the following code in the ``body`` section:

{% raw %}
```html
{% if page.header.image == 'random' %}
    <script type="text/javascript">
        var randomIndex;
        var headers;

        randomIndex = Math.floor(Math.random() * headers.length);

        $(document).ready(function() {
            $("#headerIMG").attr('src', headers[randomIndex]);
        });
    </script>
{% endif %}
```
{% endraw %}


Every other layout is initially dependent on the default layout so the ``headers`` variable set within the above script is available in the current page.

On every page that you want to randomize the header image place the following JavaScript code:

{{ page.header.image | inspect }}
