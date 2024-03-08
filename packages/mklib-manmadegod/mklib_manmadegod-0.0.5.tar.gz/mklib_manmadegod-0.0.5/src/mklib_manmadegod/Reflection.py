from typing import Literal, List


type _accessModifier = Literal["public", "private", "protected", "any"]

class ObjectReflector():

    @staticmethod
    def GetProperties(obj: object, accesMod: _accessModifier = "public") -> List[tuple[str, object]]:
        
        propertyNames = [x for x in dir(obj) if not x.startswith('_')]
        out: List[tuple[str, object]] = []

        for prop in propertyNames:
            attr = getattr(obj, prop)
            
            if callable(attr):
                continue

            out.append((prop, attr))
        
        return out