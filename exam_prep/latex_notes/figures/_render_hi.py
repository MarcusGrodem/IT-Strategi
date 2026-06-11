#!/usr/bin/env python3
"""Render specific page at HIGH DPI for inspection only."""
import sys
import os
import fitz

SLIDES = {
    'lec1': '260203_Lektion 1_Introduktion_IT-strategi-1.pdf',
    'lec2': '170226_Lektion 2_Strategisk analyse (del I) og typiske strategiske virkemidler_IT-strategi-1.pdf',
    'lec3': '260224_Lektion 3_Digitale forretningsmodeller-1.pdf',
    'lec4': '260305_Lektion 4_Digital transformation_IT-strategi (1).pdf',
    'lec5': '10032026_Lektion 5_Digital innovation disruption og strategier (1).pdf',
    'lec6': '170326_Lektion 6_Digitale økosystemer (1).pdf',
    'lec7': '260324_Lektion 7_Implementering (1).pdf',
    'lec9': '260421_Lektion 9_Opsummering mv.pdf',
}
SLIDES_DIR = '/Users/marcusgrude-grodem/Documents/GitHub/IT-Strategi/slides'

key = sys.argv[1]
page_num = int(sys.argv[2])
out_dir = '/tmp/slide_previews_hi'
os.makedirs(out_dir, exist_ok=True)
pdf_path = os.path.join(SLIDES_DIR, SLIDES[key])
doc = fitz.open(pdf_path)
page = doc[page_num - 1]
mat = fitz.Matrix(180 / 72, 180 / 72)
pix = page.get_pixmap(matrix=mat)
out_path = os.path.join(out_dir, f'{key}_p{page_num:02d}.png')
pix.save(out_path)
doc.close()
print(out_path)
