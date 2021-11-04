
def prompt_question(question: str, example_answer: str, type: str = "string", accepted_anwers: list = []):
    format_question = f"{question}. ({example_answer}): "
    accepted = False

    if type == "string":
        while(not accepted):
            ans = input(format_question)
            if ans in accepted_anwers:
                accepted = True
                return ans
            else:
                print("Jawaban tidak sesuai pilihan, ulangi lagi")
    elif type == "float":
        while (not accepted):
            try:
                ans = float(input(format_question))
                accepted = True
                return ans
            except ValueError:
                print("Jawaban tidak sesuai pilihan, ulangi lagi")
    elif type == "int":
        while (not accepted):
            try:
                ans = int(input(format_question))
                accepted = True
                return ans
            except ValueError:
                print("Jawaban tidak sesuai pilihan, ulangi lagi")


def assert_raw_boolean(key: str, raw_data: list, data: list, answer: str):
    if key in raw_data:
        data[key] = True if raw_data[key] == answer else False
    else:
        data[key] = False


def assert_raw_float(key: str, raw_data: list, data: list):
    if key in raw_data:
        data[key] = float(raw_data[key])
    else:
        data[key] = float(0)


def assert_raw_int(key: str, raw_data: list, data: list):
    if key in raw_data:
        data[key] = int(raw_data[key])
    else:
        data[key] = int(0)


def sanitize_data(raw_data: dict) -> dict:
    data = {}
    # prerequisite data
    assert_raw_boolean('has_ktp', raw_data, data, 'y')
    assert_raw_boolean('is_wni', raw_data, data, 'y')
    assert_raw_boolean('is_domisili_indo', raw_data, data, 'y')
    assert_raw_boolean('is_age_over_21', raw_data, data, 'y')
    # job related data
    assert_raw_boolean('has_steady_job', raw_data, data, 'y')
    assert_raw_boolean('has_steady_income', raw_data, data, 'y')
    assert_raw_boolean('has_monthly_income', raw_data, data, 'y')
    assert_raw_boolean('has_personal_bank_account', raw_data, data, 'y')
    # income related data
    assert_raw_float('monthly_income', raw_data, data)
    assert_raw_float('monthly_spending', raw_data, data)
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
