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


def safe_squares_rooks(n, rooks):
    attacked_rows = set()
    attacked_cols = set()

    for row, col in rooks:
        attacked_rows.add(row)
        attacked_cols.add(col)
    return (n - len(attacked_rows))*(n - len(attacked_cols))


def topswops(cards):
    cards = list(cards)
    n = len(cards)
    count = 0
    while cards[0] != 1:
        k = cards[0]
        cards[:k] = reversed(cards[:k])
        count+=1
    return count


def tr(text, ch_from, ch_to):
    transform = {ch_from[i]: ch_to[i] for i in range(len(ch_from))}
    
    result = []
    for char in text:
        if char in transform:
            result.append(transform[char])
        else:
            result.append(char)
    return ''.join(result)


def count_cigarettes(n, k):
    tot_cig_smk = n
    butts = n

    while butts >= k:
        new_cigs = butts // k
        tot_cig_smk = tot_cig_smk + new_cigs
        butts = butts % k + new_cigs

    return tot_cig_smk

def word_positions(sentence, word):
    return [i for i, w in enumerate(sentence.split()) if w == word]


def is_left_handed(pips):
    pips_list = [
                [1,2,3], [3,1,2], [2,3,1],
                [1,4,2], [2,1,4], [4,2,1],
                [1,3,5], [5,1,3], [3,5,1],
                [1,5,4], [5,4,1], [4,1,5],
                [6,3,2], [2,6,3], [3,2,6],
                [6,2,4], [2,4,6], [4,6,2],
                [6,5,3], [5,3,6], [3,6,5],
                [6,4,5], [5,6,4], [4,5,6]
                ]
    return pips in pips_list


def give_change(amount, coins):
    result = []
    for coin in coins:
        while amount >= coin:
            result.append(coin)
            amount = amount - coin
    return result


def power_prefix(prefix):
    
    len_prefix = len(prefix)
    k = 1
    power_two = 2

    while True:
        power_str = str(power_two)
        match_prefix = True

        if len(power_str) < len_prefix:
            match_prefix = False
        else:
            for p in range(len_prefix):
                prefix_char = prefix[p]
                power_char = power_str[p]

                if prefix_char == '*':
                    continue

                if prefix_char != power_char:
                    match_prefix = False
                    break

        if match_prefix:
            return k

        k = k + 1
        power_two = power_two * 2


def parking_lot_permutation(preferred_spot):
    pref_spot_len = len(preferred_spot)
    parking_spots = [None] * pref_spot_len

    for car in range(pref_spot_len):
        curnt_spot = preferred_spot[car]

        while parking_spots[curnt_spot] is not None:
            curnt_spot = (curnt_spot + 1) % pref_spot_len

        parking_spots[curnt_spot] = car
    
    return parking_spots


def winning_cards(cards, trump=None):
    
    ranks = {'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
         'nine': 9, 'ten': 10, 'jack': 11, 'queen': 12, 'king': 13, 'ace': 14}

    trump_cards = [card for card in cards if card[1] == trump]

    if trump_cards:
        return max(trump_cards, key=lambda card: ranks[card[0]])

    lead_suit = cards[0][1]
    lead_suit_cards = [card for card in cards if card[1] == lead_suit]
    return max(lead_suit_cards, key=lambda card: rank_order[card[0]])


def knight_jump(knight, start, end):
    
    if len(knight) != len(start) or len(start) != len(end):
        return False

    difference = []
    
    for k in range(len(start)):
        diff = abs(start[k] - end[k])
        difference.append(diff)

    difference.sort(reverse=True)

    return tuple(difference) == tuple(knight)

def can_balance(items):

    l_itm = len(items)
    for i in range(l_itm):
        l_torq = 0
        r_torq = 0

        for j in range(i):
            dis = i - j
            l_torq += items[j] * dis

        for j in range(i + 1, l_itm):
            dis = j - i
            r_torq += items[j] * dis

        if l_torq == r_torq:
            return i
    
    return -1

















