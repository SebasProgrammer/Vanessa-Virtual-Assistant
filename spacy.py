import spacy
# from spacy.matcher import Matcher
# from spacy.tokens import Span
# from spacy import displacy

pattern1 = [{"LEMMA": {"IN": ["like", "love"]}},
            {"POS": "NOUN"}]

nlp = spacy.load("es_core_news_md")

texto = """España incumple la regla del déficit del euro y queda como único país bajo el control de Bruselas. 
España no aprobará finalmente la regla europa del déficit y se quedará como único país de la Eurozona que 
suspende y sigue bajo vigilancia. El Gobierno se salta finalmente el requisito de saneamiento presupuestario 
del Tratado de Maastricht y obtiene así más margen de gasto en 2018."""

# y procesamos el texto
doc = nlp(texto)