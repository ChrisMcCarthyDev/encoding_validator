from typing import Dict
from typing import Final
from typing import List


class EncodingConfig:
    """
    The EncodingConfig class holds the char encoding_pairs and valid_formats
    for use in the EncodingValidator class.
    """
    def __init__(self, encoding_pairs: List[Dict], valid_formats: List[str]):
        """
        The EncodingConfig constructor.

        :param encoding_pairs: A list of encoding key/value pairs, where the
            key is the encoded string, and the value is what is matched with
            the target. The value can be a single character or a list of
            characters.
        :param valid_formats: A list of valid encoded string formats.
        """
        self._encoding_pairs: Final[List[dict]] = encoding_pairs
        self._valid_formats: Final[List[str]] = valid_formats

    @property
    def encoding_pairs(self) -> List[dict]:
        """
        The list of encoding key/value pairs, where the key is the
        encoded string, and the value is what is matched with the target. The
        value can be a single value or a list of values.

        :return: A list of dicts.
        """
        return self._encoding_pairs

    @property
    def valid_formats(self) -> List[str]:
        """
        The list of valid encoded string formats.

        :return: A list of strings.
        """
        return self._valid_formats

    def __repr__(self):
        return (f"{self.__class__.__name__}("
                f"encoding_pairs={self.encoding_pairs}, "
                f"valid_formats={self.valid_formats})")

    def __hash__(self):
        return hash((self.encoding_pairs, self.valid_formats))

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (
                    (self.encoding_pairs, self.valid_formats) ==
                    (other.encoding_pairs, other.valid_formats)
            )
        return False
