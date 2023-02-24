def test_pytest_is_work():
    assert 2 + 2 == 4


def test_pytest_fixture(two_plus_two_data):
    result = 0
    for item in two_plus_two_data:
        result += item
    assert result == 4


class TestPytestWork:
    def test_two_plus_two(self):
        assert 2 + 2 == 4

    def test_two_plus_fixture(self, two_plus_two_data):
        result = 0
        for item in two_plus_two_data:
            result += item
        assert result == 4
