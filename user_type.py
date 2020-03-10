def button_available(type):
    if type == "社員" or type == "契約社員":
        return True
    elif type == "派遣社員":
        return False
        