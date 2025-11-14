from ...attrs import LIKE_NUM

_num_words = [
    "cero",
    "uno",
    "dos",
    "tres",
    "cuatro",
    "cinco",
    "seis",
    "siete",
    "ocho",
    "nueve",
    "diez",
    "once",
    "doce",
    "trece",
    "catorce",
    "quince",
    "dieciséis",
    "diecisiete",
    "dieciocho",
    "diecinueve",
    "veinte",
    "veintiuno",
    "veintidós",
    "veintitrés",
    "veinticuatro",
    "veinticinco",
    "veintiséis",
    "veintisiete",
    "veintiocho",
    "veintinueve",
    "treinta",
    "cuarenta",
    "cincuenta",
    "sesenta",
    "setenta",
    "ochenta",
    "noventa",
    "cien",
    "mil",
    "millón",
    "billón",
    "trillón",
]


_ordinal_words = [
    "primer", # apocopated
    "tercer", # apocopated
    "primero",
    "segundo",
    "tercero",
    "cuarto",
    "quinto",
    "sexto",
    "séptimo",
    "octavo",
    "noveno",
    "décimo",
    "undécimo",
    "duodécimo",
    "decimotercero",
    "decimocuarto",
    "decimoquinto",
    "decimosexto",
    "decimoséptimo",
    "decimoctavo",
    "decimonoveno",
    "vigésimo",
    "trigésimo",
    "cuadragésimo",
    "quincuagésimo",
    "sexagésimo",
    "septuagésimo",
    "octogésimo",
    "nonagésimo",
    "centésimo",
    "milésimo",
    "millonésimo",
    "billonésimo",
]


_ordinal_fem = [ord[:-1] + 'a' for ord in _ordinal_words[2:]]


_ordinal_pl = [ord + 's' for ord in _ordinal_words[2:] + _ordinal_fem]


_ordinal_abbr = [
    "º",
    "ª",
    "o",
    "a",
]


def like_num(text):
    if text.startswith(("+", "-", "±", "~")):
        text = text[1:]
    text = text.replace(",", "").replace(".", "")
    if text.isdigit():
        return True
    if text.count("/") == 1:
        num, denom = text.split("/")
        if num.isdigit() and denom.isdigit():
            return True
    text_lower = text.lower()
    if text_lower in _num_words:
        return True
    # Check ordinal number (i.e., number, gender)
    if text_lower in _ordinal_words + _ordinal_fem + _ordinal_pl:
        return True
    # Check abbreviation or indicator of ordinal number
    if text_lower.endswith(tuple(_ordinal_abbr)):
        # Handles cases like "1.º", "2.o", or "3.a"
        if text[:-1].endswith("."):
            if text[:-2].isdigit():
                return True
        # Handles cases like "5o", 10º", "10a" 
        if text[:-1].isdigit():
            return True

    return False


LEX_ATTRS = {LIKE_NUM: like_num}
