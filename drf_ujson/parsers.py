from typing import Any, Mapping, Optional, Type

from django.conf import settings
from rest_framework.exceptions import ParseError
from rest_framework.parsers import BaseParser
from rest_framework.renderers import JSONRenderer, BaseRenderer
import ujson

__all__ = ["UJSONParser"]


class UJSONParser(BaseParser):
    """
    Parses JSON-serialized data by ujson parser.
    """

    media_type: str = "application/json"
    renderer_class: Type[BaseRenderer] = JSONRenderer

    def parse(
        self,
        stream,
        media_type: Optional[str] = None,
        parser_context: Optional[Mapping[str, Any]] = None,
    ) -> dict:
        """
        Parses the incoming bytestream as JSON and returns the resulting data.
        """
        parser_context = parser_context or {}
        encoding = parser_context.get("encoding", settings.DEFAULT_CHARSET)

        try:
            data = stream.read().decode(encoding)
            return ujson.loads(data)
        except ValueError as exc:
            raise ParseError("JSON parse error - %s" % str(exc))
