input_names = []


def adieu() -> None:
    final_str = "Adieu, adieu, to "

    if len(input_names) == 1:
        final_str += f"{input_names[0]}"
    elif len(input_names) == 2:
        final_str += f"{input_names[0]} and {input_names[1]}"
    else:
        for idx, name in enumerate(input_names):
            if len(input_names) > 2:
                last_element = input_names[-1]
                if name == last_element:
                    final_str += f"and {name}"
                else:
                    final_str += f"{name}, "

    print(final_str)


eoferror = False

while not eoferror:
    try:
        name = input().capitalize()
        input_names.append(name)
    except EOFError:
        eoferror = True

adieu()
