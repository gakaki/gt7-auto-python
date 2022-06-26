from util import l

races_elemnts = [
    {
       "name" : "reward117",
       "per_time_cr_range_w": [1.5,100], #1,5w ~ 100w
       "per_usage_second": 121,
    },
    {
       "name" : "clubman_tokyo",
       "per_time_cr_range_w": [7.5,10.5],
       "per_usage_second": 7*60 + 8,
    },
    {
       "name" : "pan_america_1st_round",
       "per_time_cr_range_w": [5.5,7.5],
       "per_usage_second": 5*60+20,
    },
    {
       "name" : "dyna",
       "per_time_cr_range_w": [1.5,3],
       "per_usage_second": 2*60 + 25,
    },
    {
        "name": "x",
        "per_time_cr_range_w": [1.5, 2.2],
        "per_usage_second": 4 * 60 + 48,
    }
]

for x in races_elemnts:
    hour_second = 60 * 60
    per_second = x["per_usage_second"]
    per_cr_range = x["per_time_cr_range_w"]

    hour_cr_range = [ round(hour_second / per_second * cr) for cr in per_cr_range]
    day_cr_range =  [ round(hour_cr *24) for hour_cr in hour_cr_range]
    month_cr_range =  [ round(day_cr *30) for day_cr in day_cr_range]

    l(f"""{x['name']}
    every 1hour cr {hour_cr_range}
    every day   cr {day_cr_range}
    every month cr {month_cr_range}
    """ )