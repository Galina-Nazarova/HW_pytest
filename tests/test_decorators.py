from src.widget import mask_account_card


def test_log(capsys):
    """Тесты для проверки декоратора"""
    mask_account_card("Счет 35383033474447895560")
    captured = capsys.readouterr()
    assert captured.out == "mask_account_card: Счет **5560. Inputs:('Счет 35383033474447895560',), {}\n"
