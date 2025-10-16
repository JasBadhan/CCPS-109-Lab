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


def multiplicative_persistence(n, ignore_zeros=False):
    iters = 0
    while n >= 10:
        product = 1
        for digit in str(n):
            if digit == "0" and ignore_zeros:
                continue
            product *= int(digit)
        n = product
        iters += 1
    return iters



def discrete_rounding(n):
    for k in range(n -1, 1, -1):
        remainder = n % k
        if remainder != 0:
           n = n + k - remainder
    return n



def extract_increasing(digits):
    result = []
    current = ""
    previous = -1
    for digit in digits:
        current = current + digit
        num = int(current)
        if num > previous:
            result.append(num)
            previous = num
            current = ""
    return result


def taxi_zum_zum(moves):
    x, y = 0, 0
    directions = [(0,1), (1,0), (0, -1), (-1,0)]
    dir_index = 0
    for move in moves:
        if move == 'L':
            dir_index = (dir_index - 1) % 4
        if move == 'R':
            dir_index = (dir_index + 1) % 4
        if move == 'F':
            dx, dy = directions[dir_index]
            x = x + dx
            y = y + dy
    return (x, y)


def colour_trio(colours):
    
    col_rule = {'rr':'r', 'yy':'y', 'bb': 'b',
            'ry': 'b', 'yr': 'b', 
            'yb': 'r', 'by': 'r',
            'rb': 'y', 'br': 'y'
            }

    while len(colours) > 1:
        colours = ''.join(col_rule[colours[i:i+2]] for i in range(len(colours) - 1))
    return colours
