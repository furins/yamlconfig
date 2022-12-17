"""libreria per la gestione di file di configurazione YAML"""
from pathlib import Path

import yaml

class ImproperConfiguration(Exception):
    """Eccezione sollevata quando si riscontra un file non valido e non recuperabile
    """

def loadconfig() -> dict:
    """
    Carica il file di configurazione.

    In caso di problemi termina il programma.

    """
    configpath = Path("./config.yaml")
    if configpath.is_file():
        with open(configpath, "r", encoding="utf-8") as configfile:
            try:
                return yaml.safe_load(configfile)
            except yaml.YAMLError as exc:
                raise ImproperConfiguration("file di configurazione non valido") from exc
    else:
        raise FileNotFoundError(f"file di configurazione non trovato: {configpath.resolve()}")
