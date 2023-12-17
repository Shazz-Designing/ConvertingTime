from modules.app import convert_to_24_hour

def test_conversion_am():
    result = convert_to_24_hour(8, 30, "am")
    assert result == "0830"

def test_conversion_pm():
    result = convert_to_24_hour(8, 30, "pm")
    assert result == "2030"