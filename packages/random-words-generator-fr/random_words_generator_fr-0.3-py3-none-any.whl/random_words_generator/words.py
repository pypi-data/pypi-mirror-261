import random
from typing import List

def generate_random_words(num_words: int = 8) -> List[str]:
   """
   Génère un nombre spécifié de mots français au hasard.

   Args:
      num_words (int, optional): Le nombre de mots à générer. Defaults to 8.

   Returns:
      List[str]: Une liste de mots français.

   Raises:
      ValueError: Si num_words est supérieur à 20 ou inférieur à 0.
   """
   
   if num_words > 20 or num_words < 0:
      raise ValueError("Le nombre de mots doit être entre 0 et 20.")
   
   french_words = [
         "dixième", "canari", "carotte", "escalier", "Mécanique", "havre", "nostalgie", "robe", "bombe", "visite", "faire",
         "united", "autour", "symbole", "astrologie", "pirate", "funiculaire", "balcon", "cyclope", "alpiniste",
         "terrasse", "sensible", "coupable", "somnambule", "bermudes", "soutien", "etriers", "jeune", "marié", "radical",
         "bienveillant", "puzzle", "troupes", "infini", "lance", "papillon", "gala", "croix", "guerre", "portable",
         "moyenne", "couture", "tire-bouchon", "galactique", "lourdaud", "avaler", "minuscule", "picorer", "immersion", "poker",
         "bandeau", "court", "assistant", "dinosaure", "africain", "naphte", "fiasco", "routes", "grenouille", "humain", "cidre",
         "lit", "chaussette", "presque", "attitude", "été", "projet", "stéréo", "tourbillon", "cartographie", "jumelles", "bronze",
         "nuque", "ballon", "manille", "harpon", "pompiers", "les", "caissier", "mannequin", "raccommoder", "hypnotiser", "mer",
         "fibre", "octobre", "limace", "paysage", "invisible", "moto", "tornade", "peste", "timbre", "hypnotise", "bronzer",
         "lagon", "coq", "surmonter", "caillot", "lame", "champion", "stylo", "myrtille", "afrique", "sénat", "senteur",
         "abri", "absurde", "accent", "accord", "accrocher", "accumuler", "aciduler", "acoustique", "acteur", "adhérer", "adjectif",
         "admirer", "adopter", "adulte", "aérodrome", "afficher", "agacer", "agglomérer", "agiter", "agréable", "aigle", "aigre",
         "aiguille", "aimanter", "air", "aisance", "alcool", "alerte", "algèbre", "alliance", "alligator", "allumer", "alphabet",
         "ambiance", "ambition", "améliorer", "amnésie", "amoureux", "amphithéâtre", "analyser", "anarchie", "anatomie", "ancêtre",
         "ancien", "angoisse", "animal", "anniversaire", "annonce", "annuler", "antenne", "antidote", "antique", "antisémite",
         "aperçu", "apologiser", "appareil", "appeler", "apporter", "apprendre", "appuyer", "aquarium", "arbitre", "arbre", "arcade",
         "arche", "archevêque", "archer", "architecte", "arctic", "aréna", "argent", "argenterie", "arme", "armure", "aromatique",
         "arracher", "arriver", "arroser", "artiste", "article", "aspect", "asperger", "aspirateur", "assaut", "assurer", "astuce",
         "atlas", "atome", "atout", "attacher", "attelage", "attendre", "attirer", "attraper", "auberge", "aubaine", "audace",
         "audible", "auditeur", "augmenter", "auteur", "autoriser", "autruche", "avalanche", "avancer", "avare", "avatar", "aventure",
         "avion", "avis", "avocat", "avouer", "axe", "axiomatique", "azimut", "azur", "babysitter", "bac", "baccarat",
         "bactérie", "badge", "baguette", "baiser", "baisser", "balade", "balcon", "balise", "ballet", "bambou", "banane",
         "banc", "bande", "banlieue", "banque", "banquier", "barbier", "barde", "baril", "barman", "barrage", "barre",
         "barrière", "baryton", "bascule", "bataille", "bateau", "batterie", "baver", "bavette", "beau", "beauté", "bébé",
         "bêche", "bêler", "bêta", "bible", "bicyclette", "bidon", "bifteck", "bifurquer", "bille", "billard", "binaire",
         "biologie", "biopsie", "biotope", "biscuit", "bison", "bistouri", "bivouac", "blague", "blanc", "blessé", "blinder",
   ]
   chosen_words = set()
   while len(chosen_words) < num_words:
      word = random.choice(french_words)
      chosen_words.add(word)
   return list(chosen_words)
 