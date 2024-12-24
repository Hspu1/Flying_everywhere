import logging
from logging.handlers import RotatingFileHandler


lg = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.DEBUG, datefmt="%Y-%m-%d %H:%M:%S", filename="log.log",
    format="[%(asctime)s] %(module)20s:%(lineno)3d %(levelname)10s "
           f"->{' '*4}%(message)s", encoding="utf-8", filemode="w"
)

handler = RotatingFileHandler(
    filename="log.log", maxBytes=10*1024, backupCount=10
)
lg.addHandler(handler)
