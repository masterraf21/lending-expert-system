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


def store_answer(answer: str):
    pass
