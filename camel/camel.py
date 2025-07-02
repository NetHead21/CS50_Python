import re


def camel(variable_name: str) -> None:
    name_list = re.findall(".[^A-Z]*", variable_name)
    final_variable_name = "_".join(name_list).lower()
    print(final_variable_name)


variable_name = input("Enter a variable name: ")
camel(variable_name)
