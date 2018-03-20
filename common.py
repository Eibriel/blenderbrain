import re
import datetime


def check_regexs(text, regexs, return_re=False):
    check_status = False
    for regex in regexs:
        re_test = re.search(regex, text, re.IGNORECASE)
        if re_test:
            if return_re:
                return re_test
            check_status = True
            break
    return check_status


def calculate_age(born):
    if type(born) == list:
        return None
    today = datetime.date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
