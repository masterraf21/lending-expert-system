def parse_single_facts(fact_lists: list[str]) -> dict:
    d = {}
    for fact in fact_lists:
        clean_fact = fact.strip('(').strip(')').split()
        if (len(clean_fact) == 2):
            d[clean_fact[0]] = clean_fact[1]
    return d
