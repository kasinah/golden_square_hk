from datetime import datetime
# from dateutil import relativedelta


def age_checker(dob):
    age = datetime.strptime(dob, "%Y-%m-%d")
    now = datetime.now()
    res = (now.year - age.year)
    if res < 16:
        print(f"Their current age is {res} and the required age is (16)")
        return "Access denied"
    else:
        return "Access granted"
