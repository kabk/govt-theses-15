#!/usr/bin/env python
# -*- coding: utf-8 -*-

from codecs import open

template = open('_template.html', 'r', 'utf-8').read()

class_a = [(u"Aynetchi, Alyar", u"AlyarAynetchi_Site"),
(u"Chan, Melissa", u"MelissaChan"),
(u"Costa, Inês da", u"Thesis_Ines"),
(u"Couvert, Nina", u"Nina_Thesis"),
(u"Gragt, Reni van der", u"renivandergragt"),
(u"Hendriksma, Lennart", u"Lennart_Thisis"),
(u"Kokken, Mike", u"ScriptieReaderMikeKokken"),
(u"Laar, Tomas", u"Tomas_Laar_Thesis"),
(u"Leliveld, Danicha", u"danicha-scriptie"),
(u"Louter, René", u"ReneLouter-Thesis"),
(u"Mickuté, Monika", u"MonikaM"),
(u"Modder, Ilse", u"ilsemodder"),
(u"Monen, Wilco", u"wilcomonen"),
(u"Noordmans, Sep", u"SepNoordmans-thesis"),
(u"Pöll, Regina", u"ReginaPoell"),
(u"Puhl, Sander", u"sanderpuhl"),
(u"Risvåg, Sara", u"Sara_Therese_Thesis"),
(u"Rullerova, Tereza", u"Tereza_Thesis"),
(u"Salo, Irene", u"Irene_Thesis"),
(u"Schepen, Marcel", u"Marcel_Schepen_Thesis"),
(u"Stoop, Machteld", u"MachteldStoop")]

class_b = [(u"Annelot Bossink", u"AnnelotBossink"),
(u"Menno de Bruijn", u"mennodebruijn"),
(u"Ditmar van Dam", u"DitmarVanDam_Scriptie"),
(u"Rosa Douma", u"Rozel"),
(u"Marius Gottlieb", u"Marius-Thesis"),
(u"Sanne Groenendaal", u"SanneGroenendaal"),
(u"Tomas Komen", u"tomaskomen"),
(u"Mirte van Kooten", u"MirtevanKooten_Thesis"),
(u"Max Lennarts", u"MaxLennarts"),
(u"Viktorija Liaudanskaitė", u"Viktorija"),
(u"Julian van Lith", u"julian_thesis"),
(u"Alice Mulder", u"alicemulderthesis"),
(u"Sophie Neppelenbroek", u"SophieNeppelenbroek"),
(u"Eline van der Ploeg", u"Eline"),
(u"Tim van Remundt", u"tim_costimiseble"),
(u"Jordie Rovers", u"Jordie_Thesis"),
(u"Edgar Savisaar", u"edgar"),
(u"Orphé Tan-A-Kiam", u"OrpheTana"),
(u"Sandra Timmerman", u"AmbachtvsDigitaal_SandraTimmerman"),
(u"Ieva Valule", u"ieva"),
(u"Fedor Velyaminov", u"fedor.velyaminov"),
(u"Donna van West", u"donnathesis"),
(u"Terlouw, Janine", u"JanineThesis")]

class_a_links = u'\n'.join( u'<li><a href="http://kabk.github.io/%s/">%s</a></li>' % (thesis[1], thesis[0]) for thesis in class_a )
class_b_links = u'\n'.join( u'<li><a href="http://kabk.github.io/%s/">%s</a></li>' % (thesis[1], thesis[0]) for thesis in class_b )
result = template.format(class_a_links=class_a_links, class_b_links=class_b_links)

generated_file = open('index.html', 'w', 'utf-8')
generated_file.write(result)
generated_file.close()

