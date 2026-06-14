#!/usr/bin/env python3
"""Batch-extract high-resolution PNGs of selected slides."""
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

# Each entry: (lecture_key, page_number_1based, output_filename)
EXTRACTIONS = [
    # Lecture 1: Introduction
    ('lec1', 15, 'lec01-makro-meso-mikro-matrix.png'),
    ('lec1', 17, 'lec01-mintzberg-5ps-strategy.png'),
    ('lec1', 19, 'lec01-chen-narrow-vs-broad-digital-strategy.png'),
    ('lec1', 20, 'lec01-it-strategy-in-context.png'),

    # Lecture 2: Strategic analysis I
    ('lec2', 8, 'lec02-pestel-and-forecasting.png'),
    ('lec2', 16, 'lec02-forecasting-under-uncertainty.png'),
    ('lec2', 20, 'lec02-porter-five-forces.png'),
    ('lec2', 28, 'lec02-industry-life-cycle.png'),
    ('lec2', 36, 'lec02-vrio-decision-matrix.png'),
    ('lec2', 37, 'lec02-porter-value-chain.png'),
    ('lec2', 39, 'lec02-swot.png'),
    ('lec2', 41, 'lec02-five-building-blocks-digital-transformation.png'),

    # Lecture 3: Digital business models
    ('lec3', 10, 'lec03-johnson-four-building-blocks.png'),
    ('lec3', 17, 'lec03-adjustment-vs-reinvention-curve.png'),
    ('lec3', 24, 'lec03-weill-woerner-digital-business-model-framework.png'),
    ('lec3', 30, 'lec03-business-model-canvas.png'),
    ('lec3', 31, 'lec03-business-model-canvas-airbnb.png'),

    # Lecture 4: Digital transformation
    ('lec4', 11, 'lec04-digital-transformation-vs-it-enabled.png'),
    ('lec4', 20, 'lec04-wessel-transformation-full-model.png'),
    ('lec4', 25, 'lec04-kemp-situating-ai-grounding-bounding-recasting.png'),
    ('lec4', 26, 'lec04-kemp-situated-ai-table.png'),

    # Lecture 5: Digital innovation & disruption
    ('lec5', 12, 'lec05-digital-innovation-strategy-framework.png'),
    ('lec5', 14, 'lec05-innovation-typologies.png'),
    ('lec5', 18, 'lec05-disruption-eye-model.png'),
    ('lec5', 19, 'lec05-digital-innovation-vs-disruption-venn.png'),

    # Lecture 6: Digital ecosystems & platforms
    ('lec6', 17, 'lec06-uber-network-effects-napkin.png'),
    ('lec6', 22, 'lec06-axes-of-network-effects.png'),
    ('lec6', 28, 'lec06-three-dimensional-chess-platform-competition.png'),
    ('lec6', 39, 'lec06-platform-business-model-canvas-compact.png'),
    ('lec6', 41, 'lec06-platform-business-model-canvas-details.png'),

    # Lecture 7: Implementation
    ('lec7', 10, 'lec07-miller-four-success-factors.png'),
    ('lec7', 13, 'lec07-tawse-tabesh-implementation-framework.png'),
    ('lec7', 18, 'lec07-kotter-eight-step-leading-change.png'),
    ('lec7', 23, 'lec07-schein-culture-model.png'),
    ('lec7', 32, 'lec07-miller-five-implementation-factors.png'),
]


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    mat = fitz.Matrix(200 / 72, 200 / 72)
    for key, page_num, out_name in EXTRACTIONS:
        pdf_path = os.path.join(SLIDES_DIR, SLIDES[key])
        out_path = os.path.join(OUT_DIR, out_name)
        doc = fitz.open(pdf_path)
        page = doc[page_num - 1]
        pix = page.get_pixmap(matrix=mat)
        pix.save(out_path)
        doc.close()
        print(f'OK  {out_name}')
    print(f'\nExtracted {len(EXTRACTIONS)} figures.')


if __name__ == '__main__':
    main()
