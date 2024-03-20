import os
from console_manager import mk_dir, file_copy, save_listdir

def test_mk_dir():
    mk_dir('Dir1')
    assert os.path.isdir('Dir1') == True
def test_file_copy():
    file_copy('1.txt', '1_copy.txt')
    assert os.path.exists('1_copy.txt') == True

def test_save_listdir():
    save_listdir()
    assert os.path.exists('listdir.txt') == True
