#!/usr/bin/env python3
"""Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente o programa exibe a mensagem
correspondente.

Como usar:

Tenha a variável LANG devidamente configurada ex:

    export LANG=pt_BR

Execução:

    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.0.1"
__author__ = "João Ferreira"
__license__ = "Unlicense"

import os

# __Dunder__

# Uma boa pratica adicionar shebang no script
# Maneira mais recomendada e usar o ambiente virtual

# Este programa imprime Hello World

current_language = os.getenv("LANG", "en_US")[:5]
# snake case
# CurrentLanguage Pascal Case usado para outros tipos de objetos

msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_SP":
    msg = "Hola, Mundo!"
elif current_language == "fr_FR":
    msg = "Bonjour Monde"

print(msg) # built-in são recursos que já vem embutido na linguagem
