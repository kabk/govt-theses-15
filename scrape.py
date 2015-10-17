#!/usr/bin/env python
# -*- coding: utf-8 -*-

import opengraph
from django.template.defaultfilters import slugify

from repos import final_theses

for thesis in final_theses:
    url = 'http://kabk.github.io/%s/' % thesis
    g = opengraph.OpenGraph(url=url, scrape=True)
    print g.to_json()

