#!/usr/bin/env python3
"""Render preview PNGs (low-DPI) for every page of every lecture PDF."""
import fitz
import os

slides_dir = '/Users/marcusgrude-grodem/Documents/GitHub/IT-Strategi/slides'
preview_dir = '/tmp/slide_previews'
os.makedirs(preview_dir, exist_ok=True)
files = {
    'lec1': '260203_Lektion 1_Introduktion_IT-strategi-1.pdf',
    'lec2': '170226_Lektion 2_Strategisk analyse (del I) og typiske strategiske virkemidler_IT-strategi-1.pdf',
    'lec3': '260224_Lektion 3_Digitale forretningsmodeller-1.pdf',
    'lec4': '260305_Lektion 4_Digital transformation_IT-strategi (1).pdf',
    'lec5': '10032026_Lektion 5_Digital innovation disruption og strategier (1).pdf',
    'lec6': '170326_Lektion 6_Digitale økosystemer (1).pdf',
    'lec7': '260324_Lektion 7_Implementering (1).pdf',
    'lec9': '260421_Lektion 9_Opsummering mv.pdf',
}
for key, fname in files.items():
    path = os.path.join(slides_dir, fname)
    doc = fitz.open(path)
    out_sub = os.path.join(preview_dir, key)
    os.makedirs(out_sub, exist_ok=True)
    mat = fitz.Matrix(110 / 72, 110 / 72)
    n = len(doc)
    for i in range(n):
        page = doc[i]
        pix = page.get_pixmap(matrix=mat)
        pix.save(os.path.join(out_sub, f'p{i+1:02d}.png'))
    doc.close()
    print(f'{key}: rendered {n} pages -> {out_sub}')
print('Done')
