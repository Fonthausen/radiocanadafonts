baseFont = OpenFont("../src/Radio-Canada-Regular.ufo", showUI=False)

font = CurrentFont()

for baseGlyph in baseFont:
    glyph = font[baseGlyph.name]
    if glyph.unicodes != baseGlyph.unicodes:
        print glyph
            