def format_name(f_name, l_name):
    """Takes a first and last name and formats it to return the title case version of the name

    Args:
        f_name (string): first name as a string
        l_name (string): last name as a string

    Returns:
        string: first and last name in title case
    """
    if f_name == "" or l_name == "":
        return "Either a first or last name was not given"
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"

formatted_name = format_name("PAUL", "Vatterott")
print(formatted_name)