def example_function():
    result = 2 * 2
    return result

output = example_function()

def format_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"

formatted_name = format_name("PAUL", "Vatterott")
print(formatted_name)