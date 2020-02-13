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

    # Set to enable usage of higher precision (strtod) function when decoding
    # string to double values. Default is to use fast but less precise builtin
    # functionality.
    precise_float: bool = False

    def parse(
        self,
        stream,
        media_type: str = None,
        parser_context: Optional[Mapping[str, Any]] = None,
    ) -> dict:
        """
        Parses the incoming bytestream as JSON and returns the resulting data.
        """
        parser_context = parser_context or {}
        encoding = parser_context.get("encoding", settings.DEFAULT_CHARSET)

        try:
            data = stream.read().decode(encoding)
            return ujson.loads(data, precise_float=self.precise_float)
        except ValueError as exc:
            raise ParseError("JSON parse error - %s" % str(exc))
