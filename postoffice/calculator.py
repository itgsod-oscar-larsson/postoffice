
def is_envelop(width,length,thickness):
    """

    :param width:
    :param length:
    :param thickness:
    :return: True or False
    """

    #code ....
    print "ar detta ett brev"
    summa = width+length+thickness
    if summa <= 90 and width >= 9 and 60 >= length >= 14:
        return True

    return False
