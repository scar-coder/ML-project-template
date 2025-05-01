# src

La cartella _src/_ (abbreviazione di source) viene utilizzata per contenere il **codice sorgente** di un progetto Python. È una best practice nei progetti ben strutturati per mantenere il codice organizzato e **separato** da **altri file** come _documentazione, dati e test_.

---

# Sottocartelle

Se vogliamo creare dei pacchetti dobbiamo per le sottocartelle inserire il file __init__.py_
- generalmente è vuoto ma possiamo definire degli input automatici
- si possono importare delle funzioni dei file appena creati in questo modo:
```python
from .nome_file import nome_funzione
```

Lista sottocartelle:
1. models/ - 
2. utils/ - 

---