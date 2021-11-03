
import os


def load_clp_files() -> list[str]:
    o = []
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    rules_file = os.path.join(THIS_FOLDER, 'rules.clp')
    templates_file = os.path.join(THIS_FOLDER, 'templates.clp')
    o.append(templates_file)
    o.append(rules_file)

    return o
