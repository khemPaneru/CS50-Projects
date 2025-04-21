
import inflect
grammar_formatter = inflect.engine()

names = []

while True:
    try:
        user_input = input("Input: ")
        names.append(user_input)
    except EOFError:
        break

adieu_line = grammar_formatter.join(names)

print(f"Adieu, adieu, to {adieu_line}")
