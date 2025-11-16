

def rahme_ein(*texte):
    for text in texte:
        if isinstance(text,list):
            text = [str(x) for x in text]
            text = "\n".join(text)
        text = str(text)
        zeilen = text.splitlines()
        breite = max(len(zeile) for zeile in zeilen)
        rahmen_oben = "╔" + "═" * (breite + 2) + "╗"
        rahmen_unten = "╚" + "═" * (breite + 2) + "╝"

        print(rahmen_oben)
        for zeile in zeilen:
            print(f"║ {zeile.ljust(breite)} ║")
        print(rahmen_unten)