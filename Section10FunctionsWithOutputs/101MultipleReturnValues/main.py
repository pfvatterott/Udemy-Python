def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "Either a first or last name was not given"
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"

formatted_name = format_name("PAUL", "Vatterott")
print(formatted_name)