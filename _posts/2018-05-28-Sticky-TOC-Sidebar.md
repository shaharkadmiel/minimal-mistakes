---
title: Sticky table of contents sidebar
tags: [Random stuff, Jekyll, Liquid, CSS, Hacking]
toc: true
toc_label: "Contents"
author_profile: true
published: true
---

It is convenient to have the table of contents (TOC) sidebar scroll down with the page. This is assuming it is not longer than the window because then parts of the sidebar may be unaccessible.

Turns out this is rather easily accomplished with the CSS ``position: stiky;`` attribute. I modified the ``/_sass/minimal-mistakes/_sidebar.scss`` file so that the ``.sidebar__right`` class looks like this:

```css
.sidebar__right {
  margin-bottom: 1em;

  @include breakpoint($large) {
    position: sticky !important; /* added to make toc scroll with page */
    float: right !important; /* added to make toc scroll with page */
    top: 0;
    right: 0;
    width: $right-sidebar-width-narrow;
    margin-right: -1 * $right-sidebar-width-narrow;
    padding-left: 1em;
    padding-top: 1em !important; /* added to make toc scroll with page */
    z-index: 10;
  }
```

Here are some TOC entries to generate a TOC sidebar. Scroll to see the effect.

## Item 1

### Subitem 1.1

### Subitem 1.2

## Item 2

### Subitem 2.1

### Subitem 2.2

### Subitem 2.3

## The end
