# import logging
# logging.basicConfig(level=logging.DEBUG)
# logging.debug("Debug")
# logging.info("Info")
# logging.warning("Warning")
# logging.error("Error")
# logging.critical("Critical")




import logging
logging.basicConfig(level=logging.DEBUG,format="%(levelname)s : %(message)s")
logging.debug("Debug")
logging.info("Info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")