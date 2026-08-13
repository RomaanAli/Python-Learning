import logging

logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.debug("This is debug.")
logging.info("This is info.")
logging.warning("This is warning.")
logging.error("This is error.")
logging.critical("This is critical.")

logger = logging.getLogger(__name__)

handler = logging.StreamHandler()

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)

handler.setFormatter(formatter)

logger.addHandler(handler)

logger.setLevel(logging.DEBUG)

logger.info("Application started")
logger.error("Something went wrong")