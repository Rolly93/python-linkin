import logging

logging.basicConfig(level=logging.DEBUG,filename="emejmplo_logs.log",filemode="w")

logging.debug("Log de debugging")
logging.info("Log de informativo")
logging.warning("Log de advertencia")
logging.error("Log de Error")
logging.critical("Log de Error Critico")