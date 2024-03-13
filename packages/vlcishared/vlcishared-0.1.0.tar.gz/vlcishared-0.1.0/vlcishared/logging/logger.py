import logging
from datetime import date


# FIXME Corregir el número de linea que enseña el log, ahora siempre muestra
# la línea 34 de este mismo módulo
# TO-DO Modificar esto para que no sea una clase que devuelva un objeto, si no que
# haga un set up del logger.
class Logger:

    def __init__(self,
                 file_path: str,
                 etl_name: str,
                 loging_level: str) -> None:
        '''Encapsulates logging and add a pre defined format'''

        self.log_file_path = f"{file_path}/{etl_name}_{date.today()}"

        format_str = (
            f"time=%(asctime)s | lvl=%(levelname)s | comp={etl_name} "
            f"| op=%(name)s: %(filename)s[%(lineno)d]: %(funcName)s "
            f"| msg=%(message)s"
        )

        logging.basicConfig(
            level=logging.getLevelName(loging_level),
            format=format_str,
            handlers=[
                logging.FileHandler(self.log_file_path),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger()

    def get_log_file(self) -> str:
        return self.log_file_path

    def info(self, message: str) -> None:
        self.logger.info(message)

    def warning(self, message: str) -> None:
        self.logger.warning(message)

    def error(self, message: str) -> None:
        self.logger.error(message)

    def critical(self, message: str) -> None:
        self.logger.critical(message)
