
def is_envelop(weight, width,length,thickness):
    """


    :param width:
    :param length:
    :param thickness:
    :return: True or False
    """

    #code ....
    print "ar detta ett brev"
    summa = width+length+thickness
    print summa,width,length
    if weight <= 2 and summa <= 90 and width >= 9 and 60 >= length >= 14:
        return True

    return False


def rulle(weight, length, diameter):

    print "Ar detta en rulle"
    summa = weight+diameter
    print summa
    if (length <=90 and length >=10) + 2*diameter and 17<= and <= 104:


