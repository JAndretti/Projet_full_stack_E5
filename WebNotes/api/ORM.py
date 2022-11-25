from typing import Optional
from pydantic import BaseModel


class Resto(BaseModel):

    nom: Optional[str] = '-1'
    quartier: str
    adresse: str
    ville: str
    coord: str
    type: str

