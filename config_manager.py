test_settings = {
    'theme': 'dark', 
    'notifications': 'enabled', 
    'volume': 'high'
}


def add_setting(test_settings, tuple_sett):
    key, value = tuple_sett
    key = key.lower()
    value = value.lower()

    if key in test_settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        test_settings[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"


def update_setting(test_settings, tuple_sett):
    key, value = tuple_sett
    key = key.lower()
    value = value.lower()

    if key in test_settings:
        test_settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(test_settings, key):
    key = key.lower()

    if key in test_settings:
        del test_settings[key]
        return f"Setting '{key}' deleted successfully!"
    return f"Setting not found!"

def view_settings(test_settings):
    if test_settings == {}:
        return "No settings available."

    result = "Current User Settings:\n"
    for key, value in test_settings.items():
        result += f"{key.capitalize()}: {value}\n"
    return result

print( add_setting({'theme': 'light'}, ('THEME', 'dark')) )

print ( add_setting({'theme': 'light'}, ('volume', 'high')) )
print(view_settings({
    'theme': 'dark', 
    'notifications': 'enabled', 
    'volume': 'high'
}))

print( update_setting({'theme': 'light'}, ('theme', 'dark')) )