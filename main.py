# Un file di entry point è il punto di ingresso principale di 
# un programma Python. È lo script che viene eseguito 
# per avviare l’applicazione o eseguire una funzionalità specifica

from src.model import train_model
from src import utils, models


if __name__ == "__main__":
    print ("Avvio progetto...")
    utils.function()
    models.function_1()
    train_model()