# setup.py è un file di configurazione principale per 
# la creazione, distribuzione e installazione di pacchetti Python. 
# Viene utilizzato per trasformare il codice Python in 
# un pacchetto installabile tramite pip, rendendolo 
# riutilizzabile e distribuibile su PyPI (Python Package Index) 
# o in ambienti aziendali.

from setuptools import setup, find_packages



versione_progetto = "0.0.1" # versione del pacchetto
requisiti_pacchetti = [
    "numpy>=1.21", 
    "pandas>=1.3.0", 
    "scikit-learn>=1.0.0",
    "matplotlib>=3.4.3",
    ] # pacchetti richiesti
url_github = "" # URL del repository GitHub
autore = "" # autore del pacchetto
email_autore = "" # email dell'autore
nome_progetto = "" # nome del pacchetto
descrizione = "breve_descrizione_package"


setup(
    name=nome_progetto,
    version=versione_progetto,
    description=descrizione,
    long_description=open("README.md").read(), # file README.md per la descrizione estesa
    long_description_content_type="text/markdown",
    url=url_github,
    author=autore,
    author_email=email_autore,
    packages=find_packages(),
    install_requires=requisiti_pacchetti,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    license="MIT"
)