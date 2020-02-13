from typing import Union, Optional, Mapping, Any

from rest_framework.renderers import JSONRenderer
import ujson


__all__ = ["UJSONRenderer"]


class UJSONRenderer(JSONRenderer):
    """
    Renderer which serializes to JSON.
    Applies JSON's backslash-u character escaping for non-ascii characters.
    Uses the blazing-fast ujson library for serialization.
    """

    # Controls how many decimals to encode for double or decimal values.
    double_precision: int = 9
    # Controls whether forward slashes (/) are escaped.
    escape_forward_slashes: bool = False
    # Used to enable special encoding of "unsafe" HTML characters into safer
    # Unicode sequences.
    encode_html_chars: bool = False

    def render(
        self,
        data: Union[dict, None],
        accepted_media_type: Optional[str] = None,
        renderer_context: Mapping[str, Any] = None,
    ) -> bytes:

        if data is None:
            return bytes()

        accepted_media_type = accepted_media_type or ""
        renderer_context = renderer_context or {}
        indent = self.get_indent(accepted_media_type, renderer_context)

        ret = ujson.dumps(
            data,
            ensure_ascii=self.ensure_ascii,
            escape_forward_slashes=self.escape_forward_slashes,
            encode_html_chars=self.encode_html_chars,
            double_precision=self.double_precision,
            indent=indent or 0,
        )

        # force return value to unicode
        if isinstance(ret, str):
            # We always fully escape \u2028 and \u2029 to ensure we output JSON
            # that is a strict javascript subset. If bytes were returned
            # by json.dumps() then we don't have these characters in any case.
            # See: http://timelessrepo.com/json-isnt-a-javascript-subset
            ret = ret.replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")
            return bytes(ret.encode("utf-8"))
        return ret
