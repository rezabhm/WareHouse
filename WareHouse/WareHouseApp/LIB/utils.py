import jdatetime


def ad2solar(year, month, day, week_day):

    """
    convert AD datetime to solar time
    """

    month2int = {

        'Jan': 1,
        'Feb': 2,
        'Mar': 3,
        'Apr': 4,
        'May': 5,
        'Jun': 6,
        'Jul': 7,
        'Aug': 8,
        'Sep': 9,
        'Oct': 10,
        'Nov': 11,
        'Dec': 12,

    }

    week = {

        'Sat': 'شنبه',
        'Sun': 'یکشنبه',
        'Mon': 'دوشنبه',
        'Tue': 'سه شنبه',
        'Wed': 'چهارشنبه',
        'Thu': 'پنج شنبه',
        'Fri': 'جمعه',

    }

    time = jdatetime.date.fromgregorian(year=year, month=month2int[month], day=day)
    return time.year, time.month, time.day, week[week_day]


def solar2ad(year, month, day):

    """
    convert solar datetime to ad datetime
    """

    time = jdatetime.date(year, month, day).togregorian()
    return time.year, time.month, time.day
