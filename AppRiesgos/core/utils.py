import string
import random
from datetime import datetime, timedelta, date


def id_generator(size=18, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def comprobeConvertedFloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def daterange(start_date, end_date):
    for n in range(int (((end_date + timedelta(days=1)) - start_date).days)):
        yield start_date + timedelta(n)