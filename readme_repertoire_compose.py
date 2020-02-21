#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Fichier: readme_repertoire_compose.py
# Auteur: Marc COATANHAY

"""
    Module pour écrire un fichier d'aide du module.
"""

# Import des modules
import repertoire
import sys

# Définitions constantes et variables globales
repertoire.filerep()
file = open('readme.md', 'w')
sys.stdout = file
help(repertoire)
file.close()
sys.stdout = sys.__stdout__

# Définitions fonctions et classes

