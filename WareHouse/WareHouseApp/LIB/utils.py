import jdatetime


def ad2solar(year, month, day):

    """
    convert AD datetime to solar time
    """

    time = jdatetime.date.fromgregorian(year=year, month=month, day=day)
    return time.year, time.month, time.day


def solar2ad(year, month, day):

    """
    convert solar datetime to ad datetime
    """

    time = jdatetime.date(year, month, day).togregorian()
    return time.year, time.month, time.day
