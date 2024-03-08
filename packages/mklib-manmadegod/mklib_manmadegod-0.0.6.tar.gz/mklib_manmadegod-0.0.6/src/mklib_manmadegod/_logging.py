from loguru import logger

import sys

import json

from ._reflection import ObjectReflector


def _levelFilter(b: bool = False):

    def is_level(record):

        return record["level"].name == "OBJECT"


    def is_not_level(record):

        return record["level"].name != "OBJECT"


    if b is False:

        return is_not_level


    return is_level



class Log:

    _initialized = False


    @staticmethod

    def Init():

        logger.remove()

        logger.level("SERIALIZED", no=99, color="<yellow>")

        logger.level("OBJECT", no= 100, color="<yellow>")
        logger.add(

            sys.stdout,

            format="<level>[{level}]</level> {message}",

            colorize=True,

            filter=_levelFilter(),
        )

        logger.add(

            sys.stdout,

            format="<green>{extra[object]}</green>:\n{extra[properties]}",

            colorize=True,

            filter=_levelFilter(True),
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

    def LogProperties(obj: object):

        properties = ObjectReflector.GetProperties(obj)


        if len(properties) == 0:
            return


        value = ""
        
        for prop in properties:

            value += f'   {prop[0]} <{type(prop[1]).__name__}>: {prop[1]}\n'


        with logger.contextualize(object = type(obj).__name__, properties = value[0:-1]):

            Log._log("OBJECT", "")


    @staticmethod

    def _serialize(obj: object) -> str:

        return json.dumps(obj, default=lambda o: o.__dict__, sort_keys=True, indent=4)


    @staticmethod

    def _log(level: str, message: str):

        if Log._initialized is False:

            Log.Init()


        logger.log(level, message)

