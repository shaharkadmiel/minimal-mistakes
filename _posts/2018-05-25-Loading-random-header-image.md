---
title: Randomizing header image
header:
  overlay_image: random
  overlay_filter: rgba(255, 255, 255, 0.3)
  caption: "Image subject to Copyright: [**© Shahar Shani-Kadmiel**](https://shaharkadmiel.github.io)"
tags: [Random stuff, Images, Jekyll, Liquid, JavaScript, jQuery, Hacking]
toc: true
toc_label: "Contents"
author_profile: true
published: true
---

Having a random header on reload is a neat feature. I managed to get it to work. *Try it... hit reload!*. I have included my initial attempt which didn't work but parts of it made it into the [solution](#solution).

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

which outputs:

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

The problem is that because Jekyll is a static site generator, this happens when the static page is *built* and not on reload. So we need to encapsulate this in a JavaScript that is executed every time a page is *served*.

## <a id="solution"></a>The solution

I found this very helpfull [post](https://thornelabs.net/2014/01/19/display-random-jekyll-posts-during-each-page-load-or-refresh-using-javascript.html) by *James W Thorne* that mixes Liquid code and JavaScript code. This may not be the most elegant solution but id works.

### default.html layout

I added the following JavaScript/Liquid mix to the ``<head>`` section of the ``default.html`` layout:

{% raw %}
```html
<!-- Load jQuery -->
<script src="/assets/js/vendor/jquery/jquery-3.3.1.min.js" type="text/javascript"></script>

{% if page.header.image == 'random' or page.header.overlay_image == 'random' %}
  <!-- Make a list of header images -->
  <!-- init the list -->
  {% assign header_images = "" | split: ',' %}

  <!-- loop and add -->
  {% for image in site.static_files %}
    {% if image.path contains '/assets/images/headers/' %}
      <!-- add image -->
      {% assign header_images = header_images | push: image.path %}
    {% endif %}
  {% endfor %}

  <!--
    Javascript and Liquid code to gather a list of all header images
    in /assets/images/headers/
  -->
  <script type="text/javascript">
    // get images from ``header_images`` array to js var
    var header_images = [
      {% for image in header_images %}
        "{{ site.baseurl }}{{ image }}",
      {% endfor %}
    ];

    var randomIndex = Math.floor(Math.random() * header_images.length);

    // and the winning ``header_image`` is...
    var header_image = header_images[randomIndex]

    // image without overlay
    {% if page.header.image == 'random' %}
      $(document).ready(function() {
        $(".page__hero-image").attr('src', header_image);
      });

    // image with overlay
    {% elsif page.header.overlay_image == 'random' %}
      // make sure overlay filter is handled correctly
      {% if page.header.overlay_filter contains "rgba" %}
        {% capture overlay_filter %}{{ page.header.overlay_filter }}{% endcapture %}
      {% elsif page.header.overlay_filter %}
        {% capture overlay_filter %}rgba(0, 0, 0, {{ page.header.overlay_filter }}){% endcapture %}
      {% endif %}

      $(document).ready(function() {
        $(".page__hero--overlay").attr('style',
          '{% if page.header.overlay_color %}
            background-color: {{ page.header.overlay_color | default:
                "transparent" }};
          {% endif %}
          background-image: {% if overlay_filter %}
            linear-gradient({{ overlay_filter }}, {{ overlay_filter }}),
          {% endif %}url(' + header_image + ')');
      });

    {% endif %}
  </script>
{% endif %}
```
{% endraw %}

Line 2 loads the [jQuery](http://jquery.com/) library that allows setting the ``src`` attribute of the ``.page__hero-image`` class in the case of ``image:`` or the ``style`` attribute of the ``.page__hero--overlay`` class in the case of ``overlay_image:``.

On build, line 4 makes sure nothing happens unless randomization is needed. If not, lines 5 through 62 will completely vanish from the page source.

Lines 7 through 15 compile a list of images in ``/assets/images/headers/`` and assigns that list to a ``header_images`` array variable. This is outside the JavaScrip code so it is run only when the page is built, not every time it is served.

The contents of the square brackets between lines 23 and 27 **must** be one line. Similarly, Lines 50 through 57 **must** be one line. *Lines here are broken for readability.

###  YAML front matter

Every other layout is initially dependent on the ``default`` layout so header ``image`` or ``overlay_image`` can be randomized in all layouts. Simply set ``image: random`` or ``overlay_image: random`` in the front matter and you are set.

Here is an example of a [page with a random header ``image``](/random_header_image/) (unlike this post which has a random header ``overlay_image``). If you were wondering what the front matter for this post looks like, here it is:

```yaml
---
title: Randomizing header image
header:
  overlay_image: random
  overlay_filter: rgba(255, 255, 255, 0.3)
  caption: "Image subject to Copyright: [**© Shahar Shani-Kadmiel**](https://shaharkadmiel.github.io)"
tags: [Random stuff, Images, Jekyll, Liquid, JavaScript, jQuery, Hacking]
toc: true
toc_label: "Contents"
author_profile: true
published: true
---
```