from theladders.name import Name, FullName

def test_full_name():
    first_name_str = "First"
    last_name_str = "Last"
    full_name_str = "First Last"

    first_name = Name(first_name_str)
    last_name = Name(last_name_str)

    full_name = FullName(first_name, last_name)

    assert("%s" % full_name == full_name_str)
