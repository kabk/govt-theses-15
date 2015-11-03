#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from codecs import open
import json

import opengraph
from repos import final_theses as thesis_slugs

template = open('_template.html', 'r', 'utf-8').read()

theses = []
for thesis_slug in thesis_slugs:
    url = 'http://kabk.github.io/%s/' % thesis_slug
    print "parsing %s:" % url
    g = opengraph.OpenGraph(url=url, scrape=True)
    d = json.loads(g.to_json())
    d['slug'] = thesis_slug
    theses.append(d)

template = open('_template.html', 'r', 'utf-8').read()

thesis_template = """
<div class="preview">
    <figure>
        <a href="{url}"><img src="{image}"/></a>
    </figure>
    <h2><a href="{url}">{title}</a></h2>
    <h3>{creator}</h3>
    <p>{description} <a href="{url}">Continue reading…</a></p>
</div>

"""

thesis_links = ""
for thesis in theses:
    thesis_links += thesis_template.format(image=thesis['image'],
                                  title=thesis['title'],
                                  creator=thesis['creator'],
                                  description=thesis['description'],
                                  url=thesis['url'],
                                  slug=thesis['slug'])

result = template.format(body=thesis_links)

generated_file = open('index.html', 'w', 'utf-8')
generated_file.write(result)
generated_file.close()

