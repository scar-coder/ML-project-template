# Specifica il nome dell’ambiente virtuale
VENV = venv

# Installa le dipendenze
install:
	python3 -m venv $(VENV)
	$(VENV)/bin/pip install -r requirements.txt

# Prepara i dati
prepare_data:
	python scripts/preprocess.py

# Addestra il modello
train:
	python src/train.py --epochs 10 --batch_size 32

# Esegue i test
test:
	pytest tests/

# Pulisce i file temporanei e cache
clean:
	rm -rf __pycache__ *.pyc $(VENV)

# Aiuto: mostra i comandi disponibili
help:
	@echo "Comandi disponibili:"
	@echo "  make install       - Installa le dipendenze"
	@echo "  make prepare_data  - Prepara il dataset"
	@echo "  make train         - Addestra il modello"
	@echo "  make test          - Esegue i test"
	@echo "  make clean         - Pulisce i file temporanei"
