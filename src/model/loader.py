
import os


def load_clp() -> list:
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    rules_file = os.path.join(THIS_FOLDER, 'rules.clp')
    templates_file = os.path.join(THIS_FOLDER, 'templates.clp')

    output = []

    with open(templates_file, 'r') as file:
        string = file.read().replace('\n', '')
        templates = string.split(';')
        for template in templates:
            output.append(template)

    with open(rules_file, 'r') as file:
        string = file.read().replace('\n', '')
        rules = string.split(';')
        for rule in rules:
            output.append(rule)
    return output
