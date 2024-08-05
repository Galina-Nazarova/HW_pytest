from src.mask import get_mask_card_number

def test_get_mask_card_number_fixture(card_numbers):
        assert get_mask_card_number(7000792289606361) == card_numbers


@pytest.mark.parametrize('value, expected', [
    ("123", "321"),
    ("hello", "olleh"),
    ("world", "dlrow"),
]
                         )
def test_get_mask_card_number_parametrize(value, expected):
    assert get_mask_card_number(value) == expected
