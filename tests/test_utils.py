import re
from typing import Any, List

import pytest

from pycfmodel.constants import IMPLEMENTED_FUNCTIONS
from pycfmodel.resolver import FUNCTION_MAPPINGS
from pycfmodel.utils import convert_to_list, regex_from_cf_string


def test_implemented_functions():
    assert set(FUNCTION_MAPPINGS) == IMPLEMENTED_FUNCTIONS


@pytest.mark.parametrize("param, expected_output", [(1, [1]), ([1], [1]), ("a", ["a"]), (["a"], ["a"])])
def test_convert_to_list(param: Any, expected_output: List):
    assert convert_to_list(param) == expected_output


@pytest.mark.parametrize(
    "action, expected_pattern",
    [
        ("", re.compile("^$", re.IGNORECASE)),
        ("*", re.compile("^.*$", re.IGNORECASE)),
        ("?", re.compile("^.{1}$", re.IGNORECASE)),
        ("a", re.compile("^a$", re.IGNORECASE)),
        ("a*", re.compile("^a.*$", re.IGNORECASE)),
        ("a?", re.compile("^a.{1}$", re.IGNORECASE)),
        ("a*a?", re.compile("^a.*a.{1}$", re.IGNORECASE)),
    ],
)
def test_build_regex(action, expected_pattern):
    assert regex_from_cf_string(action) == expected_pattern
