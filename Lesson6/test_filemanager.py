import os
from f_account import account_change
from f_console_manager import file_copy
def test_account_change():
    assert account_change(100, 50) == 150
    assert account_change(200, -100) == 100

def test_file_copy():
    file_copy('1', '1_copy')
    assert os.path.exists('1_copy') == True
