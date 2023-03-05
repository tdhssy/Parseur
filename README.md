# Parseur
Projet étudiant d'un
parseur d'articles scientifiques pdf vers un format texte ou XML.
## Fonctionnalités

- Conversions d'un article pdf vers un format TXT
- Conversions d'un article pdf vers un format XML


## Installation

Pour lancer le parseur les bibliothèques PyPDF2 et re sont nécessaire

```bash
  pip install pypdf2
  pip install re
```
    
## Lancement local

Clonez le parseur

```bash
  git clone https://github.com/LuffyVanquish/Parseur
```

Allez au repertoire du parseur

```bash
  cd .../parseur-main
```

Lancez le parseur

```bash
  python3 parseur.py <Option> <Article1.pdf> [<Article2.pdf> ...]
```


## Exemple

Pour lancement d'une conversion vers un format TXT

```bash
  python3 parseur.py -t ./pdf_apprentissage/Boudin-Torres-2006.pdf
```

Pour lancement d'une conversion vers un format XML

```bash
  python3 parseur.py -x ./pdf_apprentissage/Boudin-Torres-2006.pdf
```

## Auteurs

- [@LuffyVanquish](https://github.com/LuffyVanquish)

- [@vErifet](https://github.com/vErifet)

- [@TheoGJ](https://github.com/TheoGJ)

- [@Chloe-Dfs](https://github.com/Chloe-Dfs)

- [@Chaihtan](https://github.com/Chaihtan)


## En relation

D'autres projets réalisés :

[ProjectTama](https://github.com/LuffyVanquish/ProjectTama)

