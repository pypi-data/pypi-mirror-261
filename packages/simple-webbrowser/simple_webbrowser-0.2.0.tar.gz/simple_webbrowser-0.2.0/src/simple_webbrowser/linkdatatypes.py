from urllib import parse as parser
from typing import Iterable


class LinkString:
    def __init__(self, url: str, encoding: str | None = 'utf-8', **kwargs: str | None | Iterable[int]) -> None:
        self._link: str = url
        self._encoding: str | None = encoding
        self._errors: str | None = kwargs.get('errors', None)
        self._safe: str | Iterable[int] = kwargs.get('safe', '/')
    
    def __repr__(self) -> str:
        return self.link
    
    @property
    def encoded_link(self) -> str:
        return parser.quote(self._link, self._safe, self._encoding, self._errors)
    
    @property
    def link(self) -> str:
        return self._link

    @property
    def encoded_link_plus(self) -> str:
        return parser.quote_plus(self._link, self._safe, self._encoding, self._errors)
    

class LinkBytes:
    def __init__(self, url: bytes | bytearray, safe: str | Iterable[int] = '/') -> None:
        self._link: str = url
        self._safe: str | Iterable[int] = safe

    def __repr__(self) -> str:
        return self.link
    
    @property
    def encoded_link(self) -> str:
        return parser.quote_from_bytes(self._link, self._safe)
    
    @property
    def link(self) -> bytes | bytearray:
        return self._link  
