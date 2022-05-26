try:

    x = 10 / 0

except (ZeroDivisionError, TypeError) as err:

    print('QQ!: {0}'.format(err))