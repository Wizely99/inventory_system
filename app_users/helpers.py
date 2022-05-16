from datetime import date
import math

def calc_age(birthdate):
    today=date.today()
    days_between=today-birthdate
    years_old=(days_between.days)/365.25
    months_old=((days_between.days)%365.25)/30
    return f'{math.floor(years_old)} years, {math.floor(months_old)} months'
