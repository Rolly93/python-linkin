import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s-%(levelname)s - %(message)s",
    datefmt="%H:%M:%S"
)

nombre= "Paco"
logging.error(f"{nombre} creo el error")
logging.warning("Log de advertencia")
logging.error("Log de Error")
logging.critical("Log de error critico")

try:
    devision = 2/0
except:
    logging.error("devision por cero")