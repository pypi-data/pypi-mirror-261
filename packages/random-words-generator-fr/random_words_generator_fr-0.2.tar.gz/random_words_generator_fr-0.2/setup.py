from setuptools import setup, find_packages

setup(
    name="random_words_generator_fr",
    version="0.2",
    packages=find_packages(),
    install_requires=[
        # Aucune dépendance externe nécessaire
    ],
    extras_require={
        "dev": [
            # Ajoutez ici les dépendances de développement, si nécessaire
            # Par exemple : "pytest>=6.2.2", "black>=20.8b1"
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
   python_requires=">=3.6",
   description="Génère un nombre spécifié de mots français au hasard, entre 0 et 20 mots. Par défaut, génère 8 mots. utile pour divers projets nécessitant des mots français aléatoires. Permet de générer des mots pour des jeux, des tests de vocabulaire, des noms de fichiers uniques, et bien plus encore.",
   long_description=open("README.md" , encoding="utf-8").read(),
   long_description_content_type="text/markdown",
   author="killymeed",
   author_email="gowleytizie@proton.me",
   keywords="mots français aléatoires générateur de mots",
)
