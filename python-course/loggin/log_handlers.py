import logging


logger = logging.getLogger(__name__)
#definicion de su nivel
logger.setLevel(logging.DEBUG)


#este es para crear un handler
handler_consola = logging.StreamHandler()

#este es para crear el formato del handler
format_logs = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

#agregar el formato
handler_consola.setFormatter(format_logs)

#definicion a donde pertenece el logger

logger.addHandler(handler_consola)

#nombre del archivo en el que se almacena los logs
handle_archivo = logging.FileHandler("arvhivo.log")

handle_archivo.setLevel(logging.ERROR)
handle_archivo.setFormatter(format_logs)
logger.addHandler(handle_archivo)

logger.info("Registro informativo")
