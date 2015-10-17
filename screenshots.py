# -*- coding: utf-8 -*-

# Creates screenshots for the theses in the FB-friendly format of 1200x630

# Uses webkit2png and imagemagick
# If you have Homebrew installed, run the following command in your terminal:
# brew install webkit2png imagemagick

import os
import subprocess
from random import randint

from repos import final_theses as slugs

for slug in slugs:
    url = "http://kabk.github.io/%s/" % slug
    print slug, url
    # append a random query string to the uri so webkit doesn’t use a cached result
    url = "%s?id=%s" % (url, randint(222222,777777))
    outfile = "images/screenshots/%s" % slug
    # webkit2png automatically appends '-full.png' to the output (bad idea, imho)
    outfile_def = outfile + '-full.png' 
    pipe = subprocess.Popen(['webkit2png', '-o', outfile, '-W', '1200', '-H' '630', '-F', url])
    pipe.wait()
    # slug-full.png is full height (webkit2png doesnt honor the -H)
    # convert slug-full.png to 150 by 110 assets/as/screenshots/of/slug.png
    # use imagemagick, because webkit2png’s built in resize looks fuzzy
    pipe = subprocess.Popen("convert %s -crop 1200x630+0+0 %s.png" % (outfile_def, slug), shell=True)
    pipe.wait()
    # remove slug-full.png
    os.remove(outfile_def)
