import logging
logging.basicConfig(
    filename="error.log",      # File ka naam
    level=logging.ERROR,       # ERROR aur usse upar wale logs save honge
    format="%(asctime)s - %(levelname)s - %(message)s"
)
try:
    a = 10 / 0
except Exception:
    logging.exception("Exception occurred")