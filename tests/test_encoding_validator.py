import string

import pytest

from encoding_validator.encoding_config import EncodingConfig
from encoding_validator.validator import EncodingValidator


@pytest.fixture
def encoding_validator() -> EncodingValidator:
    encoding_config = EncodingConfig(
        encoding_pairs=[
            {" ": " "},
            {"N": list(string.digits)},
            {"A": list(string.ascii_uppercase)}
        ],
        valid_formats=[
            "AN ",
            "NA ",
            " AN",
            "NNN",
            "AAA"
        ]
    )
    return EncodingValidator(encoding_config)


def test_encoding_validator_correct(encoding_validator):
    test_data_map = {
        "F1 ": True,
        "F11": False,
        "1F ": True,
        "11F": False,
        " F1": True,
        "  F": False,
        "123": True,
        "ABC": True,
        "   ": False,
        "£^(": False,
        "!23": False,
        None: False
    }
    for key, is_valid in test_data_map.items():

        assert encoding_validator.is_valid_str(key) == is_valid


