---
revision_description: Initial Release
abstract: |
    Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod
    tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At
    vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren,
    no sea takimata sanctus est Lorem ipsum dolor sit amet.

    Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod
    tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At
    vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren,
    no sea takimata sanctus est Lorem ipsum dolor sit amet.
watermark: Draft
---

<!--PANDOC MANUAL: http://pandoc.org/MANUAL.html-->

\newpage


Document Revisions
==================

The following revisions have been issued:

<!--BEGIN REVISIONS-->
<!--END REVISIONS-->

<!-- end of header -->


Introduction
============

The syntax of source file is markdown. Markdown has several flavors. The one used here is the [pandoc markdown syntax](https://pandoc.org/MANUAL.html#pandocs-markdown).

Here are a few topics of interest:

* [paragraphs](https://pandoc.org/MANUAL.html#paragraphs)
* [headings](https://pandoc.org/MANUAL.html#headings)
* [lists & bullet lists](https://pandoc.org/MANUAL.html#lists)
* [tables](https://pandoc.org/MANUAL.html#tables) *cf* also [CSV tables](#csv_tables)


Details
=======

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod
tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At
vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren,
no sea[^hello] takimata sanctus est Lorem ipsum dolor sit amet.

[^hello]: Hello World!

Admonitions
-----------

cf [pandoc-latex-admonition](https://pandoc-latex-admonition.readthedocs.io/en/latest/) for documentation

Some admonitions can be made using:

### Notes

Warnings can also be released using the ``{.admonition .note}`` class:

::: {.admonition .note} :::
amet. Donec sit amet leo malesuada, euismod augue ac, fermentum sapien. Donec
vel nulla euismod, malesuada leo id, efficitur magna. Praesent sed faucibus
ipsum. Fusce vestibulum, odio in porta interdum, nisi urna mollis nisl, id
hendrerit velit metus eu libero.


:::::::::::::::::::::::::::::

### Warnings

Warnings can also be released using the ``{.admonition .warning}`` class:

::: {.admonition .warning} :::
**WARNING**

amet. Donec sit amet leo malesuada, euismod augue ac, fermentum sapien. Donec
vel nulla euismod, malesuada leo id, efficitur magna. Praesent sed faucibus
ipsum. Fusce vestibulum, odio in porta interdum, nisi urna mollis nisl, id
hendrerit velit metus eu libero.

:::::::::::::::::::::::::::::

### Tips

Tips can also be released using the ``{.admonition .tip}`` class:

::: {.admonition .tip} :::

This is a multi-paragraphs tip.

And it's very use full!

:::::::::::::::::::::::::::::

Equations and equations numbering
---------------------------------

The famous Engineer equation is often
written as $\sigma = \frac{M_f \cdot \nu}{I_{Gz}}$. But massaging the
variables can lead to equation @eq:id1.

$$M_f = \frac{\sigma \cdot I_{Gz}}{\nu}$${#eq:id1}


Page break
----------

For PDF output, a page break can be inserted by entering the raw latex command ``\newpage``.

\newpage


Dynamically linking CSV tables  {#csv_tables}
------------------------------

Given you have a ``mytable.csv`` file next to your ".md", you can dynamically this way:

[Example and documentation](https://github.com/ickc/pantable#example)


~~~~~
```table
---
include: static/mytable.csv
caption: 'Myasaki cartoons ranking'
markdown: True
table-width: 2/3
---
```
~~~~~

Which will be rendered as:

```table
---
include: static/mytable.csv
caption: 'Myasaki cartoons ranking'
markdown: True
table-width: 2/3
---
```

Showing figures
---------------

![Vought F4U Corsair[^1]](fig/Vought_F4U_Corsair_(USMC).jpg){#id .class width=100mm}

Refer to [Introduction chapter](#introduction) for more details.

[^1]: Par Gerry Metzler — https://www.flickr.com/photos/flyguy71/7427977930/sizes/l/in/photostream/, CC BY-SA 2.0, https://commons.wikimedia.org/w/index.php?curid=20571543 

<!-- dummy anchor to navigate to bottom of page -->

<a id="@"></a>
<a id="@bottom"></a>
