from HW_9_Dovbysh_1 import make_3sg_form
from HW_9_Dovbysh_2 import make_ing_form

def test1_HW_9_1_make_3sg_form():
    assert make_3sg_form('run'), 'Should be - runs'

def test2_HW_9_1_make_3sg_form():
    assert make_3sg_form('gos'), 'Should be - goes'

def test1_HW_9_2_make_ing_form():
    assert make_ing_form('go'), 'Should be - going'

def test2_HW_9_2_make_ing_form():
    assert make_ing_form('huging'), 'Should be - hugging'
