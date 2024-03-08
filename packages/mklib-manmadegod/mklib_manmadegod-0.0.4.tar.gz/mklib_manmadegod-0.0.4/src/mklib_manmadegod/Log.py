from loguru import logger
import sys
import json

class Log:
    _initialized = False

    @staticmethod
    def Init():
        logger.remove()
        logger.level("SERIALIZED", no=99, color="<yellow>")
        logger.add(
            sys.stdout, format="<level>[{level}]</level> {message}", colorize=True
        )
        Log._initialized = True
        return

    @staticmethod
    def Debug(message):
        Log._log("DEBUG", message)
        return

    @staticmethod
    def Error(message):
        Log._log("ERROR", message)
        return

    @staticmethod
    def Info(message):
        Log._log("INFO", message)
        return

    @staticmethod
    def Serialized(obj: object):
        Log._log("SERIALIZED", Log._serialize(obj))
        return

    @staticmethod
    def LogProperties():
        pass

    @staticmethod
    def _serialize(obj: object) -> str:
        return json.dumps(obj, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    @staticmethod
    def _log(level: str, message: str):
        if Log._initialized is False:
            raise Exception("Logger not initialized")

        logger.log(level, message)
