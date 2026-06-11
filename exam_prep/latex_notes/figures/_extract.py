#!/usr/bin/env python3
"""Extract one page from a PDF at high DPI.

Usage: _extract.py <pdf_key> <page_1based> <output_filename>
where pdf_key is one of: lec1, lec2, lec3, lec4, lec5, lec6, lec7, lec9
"""
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
OUT_DIR = '/Users/marcusgrude-grodem/Documents/GitHub/IT-Strategi/exam_prep/latex_notes/figures'


def main():
    key = sys.argv[1]
    page_num = int(sys.argv[2])
    out_name = sys.argv[3]
    pdf_path = os.path.join(SLIDES_DIR, SLIDES[key])
    out_path = os.path.join(OUT_DIR, out_name)
    doc = fitz.open(pdf_path)
    page = doc[page_num - 1]
    mat = fitz.Matrix(200 / 72, 200 / 72)
    pix = page.get_pixmap(matrix=mat)
    pix.save(out_path)
    doc.close()
    print(f'Saved {out_path}')


if __name__ == '__main__':
    main()
