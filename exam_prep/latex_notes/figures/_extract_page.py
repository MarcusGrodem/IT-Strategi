#!/usr/bin/env python3
"""Usage: _extract_page.py <pdf_path> <page_1based> <output_png>"""
import sys
import fitz

pdf_path, page_num, output_png = sys.argv[1], int(sys.argv[2]), sys.argv[3]
doc = fitz.open(pdf_path)
page = doc[page_num - 1]
mat = fitz.Matrix(200 / 72, 200 / 72)
pix = page.get_pixmap(matrix=mat)
pix.save(output_png)
doc.close()
print(f"Saved {output_png}")
