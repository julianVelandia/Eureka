import pytest

from internal.platform.constant.scopes import Scope

s1 = Scope()
s2 = Scope()

@pytest.mark.parametrize(
    "input_a, input_b",
    [
        (id(s1), id(s2))
    ]
)
def test_singleton_scope(input_a, input_b):
    assert input_a == input_b

