g = 100

def ryerson_letter_grade(n):
    if n < 50:
        return 'F'
    elif n > 89:
        return 'A+'
    elif n > 84:
        return 'A'
    elif n > 79:
        return 'A-'
    tens = n // 10
    ones = n % 10
    if ones < 3:
        adjust = "-"
    elif ones > 6:
        adjust = "+"
    else:
        adjust = ""
    return "DCB"[tens - 5] + adjust

def is_ascending(items):
    pre_item = items[0] - 1
    for item in items:
        if item <= pre_item:
            return False
        pre_item = item
    return True
    
def only_odd_digits(n):
    total_length = len(str(n))
    len_n = 0
    for digit in str(n):
        if int(digit) % 2 != 0:
            len_n += 1
    if len_n == total_length:
        return True
    else:
        return False

def riffle(items, out = True):
    items_left = items[:len(items)//2]
    items_right = items[len(items)//2:]
    items_riffle = []
    if out:
        for i in range(len(items_left)):
            items_riffle.append(items_left[i])
            items_riffle.append(items_right[i])
    else:
        for i in range(len(items_right)):
            items_riffle.append(items_right[i])
            items_riffle.append(items_left[i])
    return items_riffle

def is_cyclops(n):
    if n == 0:
        return True
    digits = []
    temp = n
    while temp > 0:
        digits.append(temp%10)
        temp //= 10
    len_n = len(digits)
    if len_n % 2 == 0:
        return False

    middle = len_n // 2

    if digits[middle] == 0 and digits.count(0) == 1 and n >= 0:
        return True
    else:
        return False
"""
def colour_trio(colours):
    
    if len(colours) == 1:
        return colours
    
    col =[]
    
    n_col = str(colours)
    len_col = len(str(colours))
    
    while len_col > 0:
        col.append()

"""
def is_chess_960(row):
     fir_pos_r = row.index("r")
     sec_pos_r = row.index("r", fir_pos_r + 1)
     pos_king = row.index("K")
     fir_pos_b = row.index("b")
     sec_pos_b = row.index("b", fir_pos_b + 1)
     if (fir_pos_r < pos_king < sec_pos_r and (fir_pos_b % 2) != (sec_pos_b % 2)):
         return True
     else:
         return False
