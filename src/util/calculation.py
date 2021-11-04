def count_loan_duration(
        loan_amount: float,
        income: float,
        spending: float) -> int:
    try:
        surplus = income - spending

        if (loan_amount % surplus == 0):
            duration = loan_amount / surplus
        else:
            duration = (loan_amount//surplus)+1

        return int(duration)
    except ZeroDivisionError:
        return 0
