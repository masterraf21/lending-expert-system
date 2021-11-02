class Prompt():
    data = {}

    def __init__(self) -> None:
        pass


def prompt_question(question: str, example_answer: str, type: str = "string", accepted_anwers: list = []):
    accepted = False
    format_question = "%s. (%s): ".format(question, example_answer)

    if type == "str":
        ans = input(format_question)
        while(not accepted):
            if ans in accepted_anwers:
                accepted = True
                return ans
            else:
                print("Jawaban tidak sesuai pilihan, ulangi lagi")
    elif type == "float":
        ans = float(input(format_question))
        return ans

    elif type == "int":
        ans = int(format_question)
        return ans


def assert_raw_boolean(key: str, raw_data: list, data: list, answer: str):
    if key in raw_data:
        data[key] = True if raw_data[key] == answer else False
    else:
        data[key] = False


def assert_raw_float(key: str, raw_data: list, data: list):
    data[key] = float(raw_data[key]) if key in raw_data else data[key] = float(0)


def assert_raw_int(key: str, raw_data: list, data: list):
    data[key] = int(raw_data[key]) if key in raw_data else data[key] = int(0)


def sanitize_data(raw_data: dict) -> dict:
    data = {}
    # prerequisite data
    assert_raw_boolean('has_ktp', raw_data, data, 'y')
    assert_raw_boolean('has_ktp', raw_data, data, 'y')
    assert_raw_boolean('has_ktp', raw_data, data, 'y')
    assert_raw_boolean('has_ktp', raw_data, data, 'y')
    # job related data
    assert_raw_boolean('has_ktp', raw_data, data, 'y')
    assert_raw_boolean('has_ktp', raw_data, data, 'y')
    assert_raw_boolean('has_ktp', raw_data, data, 'y')
    assert_raw_boolean('has_ktp', raw_data, data, 'y')
    # income related data
    assert_raw_float('monthly_income', raw_data, data)
    assert_raw_float('monthly spending', raw_data, data)
    # loan related
    assert_raw_float('loan_amount', raw_data, data)
    assert_raw_int('suggested_duration', raw_data, data)
    # guarantee related data
    assert_raw_boolean('has_valuable_asset', raw_data, data, 'y')
    assert_raw_boolean('has_reachable_relative', raw_data, data, 'y')
    # compliance related data
    assert_raw_boolean('is_comply_with_payment_terms', raw_data, data, 'y')
    assert_raw_boolean('is_comply_with_service_terms', raw_data, data, 'y')

    return data


def store_answer(answer: str):
    pass