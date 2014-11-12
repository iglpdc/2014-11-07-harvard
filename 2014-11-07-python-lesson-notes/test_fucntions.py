
# coding: utf-8

# In[3]:

def const():
    return 273.15

def fahr_to_kelvin(fahr_num_to_convert):
    converted = (fahr_num_to_convert - 32) * (5 / 9.0) + const()
    return converted


# In[4]:

def test_fahr_to_kelvin():
    assert fahr_to_kelvin(32) == 273.15
    assert fahr_to_kelvin(212) == 373.15

