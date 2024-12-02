# list as given
def split_input(text):
    return [list(map(int, ln.split(" "))) for ln in text.strip().split("\n")]

# day two, part one
def check_single_report(report):
    max_diff = 3
    is_inc = True
    is_dec = True

    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]

        if not (0 < diff <= max_diff):
            is_inc = False

        if not (0 > diff >= -max_diff):
            is_dec = False

        if not is_inc and not is_dec:
            break
    else:
        if is_inc:
            return True
        elif is_dec:
            return True
        else:
            return False

def check_reports(reports):
    res = 0
    for report in reports:
        valid = check_single_report(report)
        res += 1 if valid else res
    return res

# day two, part two
def check_reports_tolerate_level(reports):
    res = 0
    for report in reports:
        if check_single_report(report):
            res += 1
            continue

        for itm in range(len(report)):
            rep = report[:itm] + report[itm+1:]
            if check_single_report(rep):
                res += 1
                break

    return res


