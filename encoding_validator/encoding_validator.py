from typing import Final
from typing import Optional

from encoding_config import EncodingConfig


class EncodingValidator:
    """
    The EncodingValidator class is used to encode chars and strings based
    on a set of char encoding key/value pairs. The validity of a string can be
    determined by checking is against of a list of valid formats.The
    encoding key-pairs and list of valid_formats are provided in an instance
    of EncodingConfig.
    """

    def __init__(self, encoding_config: EncodingConfig):
        """
        The EncodingValidator constructor.

        :param encoding_config: An instance of EncodingConfig.
        """
        self._encoding_config: Final[EncodingConfig] = encoding_config

    @property
    def encoding_config(self) -> EncodingConfig:
        """
        The EncodingConfig used in encoding and string validation.

        :return: The EncodingConfig.
        """
        return self._encoding_config

    def encode_char(self, target_char: str) -> Optional[str]:
        """
        Attempts to encode a char using the list of encoding key/value
        pairs in the encoding_config. The list of encoding key/value pairs
        is iterated over, firstly, if the encoding value equals the target,
        the encoding key is returned. If the encoding value is a list and
        the target is in said list, the encoding key is returned. If the
        target cannot be encoded, None is returned.

        :param target_char: A target char that is to be encoded.
        :return: The encoded char.
        """
        for item in self._encoding_config.encoding_pairs:
            (k, v), = item.items()
            if v == target_char:
                return k
            if isinstance(v, list):
                if target_char in v:
                    return k
        raise ValueError(f"Failed to encode the {target_char} character")

    def encode_str(self, target_str: str) -> Optional[str]:
        """
        Attempts to encode a string using the list of encoding key/value
        pairs in the encoding_config. The target_str is iterated over,
        with each char passed to the encode_char function. If the char can
        be encoded, it is added to a list of encoded chars. nce all chars
        have been encoded, the list of encoded chars is joined to form a
        string and is returned.

        :param target_str: A target string that is to be encoded.
        :return: The encoded string.
        """
        chars = []
        for char in target_str:
            try:
                x = self.encode_char(char)
                chars.append(x)
            except ValueError:
                msg = (f"Failed to encode the {target_str} string at the "
                       f"{char} character")
                raise ValueError(msg)
        return "".join(chars)

    def is_valid_encoding(self, encoded_str: str) -> bool:
        """
        Checks the validity of an encoded string by performing a lookup of the
        list of valid_formats in encoding_config.valid_formats.

        :param encoded_str: A string that is to be checked.
        :return: A boolean determined by whether the encoded_str is in the
            encoding_config.valid_formats list.
        """
        return encoded_str in self._encoding_config.valid_formats

    def is_valid_str(self, target_str: str) -> bool:
        """
        Checks whether a target str could be encoded and validated. this is
        done by passing the target_str to the encode_str function. If a
        ValueError is raised, the string cannot be encoded and False is
        returned. If an encoded string is returned, it is passed to the
        is_valid_encoding function and the returned value is returned.

        :param target_str: A target string that is to be encoded and validated.
        :return: A boolean determined by whether the target_str can be
            encoded, and is in the encoding_config.valid_formats list.
        """
        try:
            return self.is_valid_encoding(self.encode_str(target_str))
        except (ValueError, TypeError):
            return False

    def __repr__(self):
        return (f"{self.__class__.__name__}("
                f"encoding_config={self.encoding_config})")

    def __hash__(self):
        return hash(self.encoding_config)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.encoding_config == other.encoding_config
        return False
