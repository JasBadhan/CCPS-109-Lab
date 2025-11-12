from itertools import combinations
import datetime
import heapq
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
     sec_pos_r = row.index("r", fir_pos_r + 1)#row.rindex("r")
     pos_king = row.index("K")
     fir_pos_b = row.index("b")
     sec_pos_b = row.index("b", fir_pos_b + 1)#row.rindex("b")
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


def josephus(n, k):
    totl_ppl = list(range(1, n + 1))
    exec_ordr = []
    crnt_indx = 0

    while len(totl_ppl) > 0:
        num_remng = len(totl_ppl)
        rmv_indx = (crnt_indx + k - 1 ) % num_remng
        crnt_indx = rmv_indx

        rmv_prsn = totl_ppl.pop(rmv_indx)
        exec_ordr.append(rmv_prsn)

    return exec_ordr


def lychrel(n, giveup):
    def reverse_integer(k):
        n_reverse = 0
        while k > 0:
            digit = k % 10
            n_reverse = (n_reverse * 10) + digit
            k //= 10
        return n_reverse

    if n == reverse_integer(n):
        return 0

    count = 0
    add_rev_n = n

    while count < giveup:
        rev = reverse_integer(add_rev_n)
        add_rev_n = add_rev_n + rev

        count += 1

        if add_rev_n == reverse_integer(add_rev_n):
            return count


    return None


def powertrain(n):
    steps = 0
    while n >= 10:
        digits = list(map(int, str(n)))
        result = 1

        for i in range(0, len(digits), 2):
            base = digits[i]
            exponent = digits[i + 1] if i + 1 < len(digits) else 0

            result *= base ** exponent

        n = result
        steps += 1
    return steps


def first_fit_bin_packing(items, capacity):
    
    resulting_bins = []
    
    for item in items:
        placed_in_bin = False

        for i in range(len(resulting_bins)):
            if resulting_bins[i] + item <= capacity:
                resulting_bins[i] += item
                placed_in_bin = True
                break
    
        if not placed_in_bin:
                resulting_bins.append(item)
    
    return resulting_bins


def count_triangles(sides):
    
    count = 0

    for x, y, z in combinations(sides, 3):
        if x + y > z:
            count += 1
    return count


def multiply_and_sort(n, multiplier):
    
    current_n = int(n)
    seen = set()
    same_seq = current_n

    while current_n not in seen:
        seen.add(current_n)
        product = current_n * multiplier
        current_n = int(''.join(sorted(str(product))))
        

        if current_n > same_seq:
            same_seq = current_n

    return same_seq

def approval_voting(ballots):

    n_candidates = len(ballots[0])

    approvals = [0] * n_candidates

    for ballot in ballots:
        for i, vote in enumerate(ballot):
            if vote == 'Y':
                approvals[i] += 1

    winning_candidate = approvals.index(max(approvals))

    return winning_candidate


def vigenere(text, key, direction):
    
    key = (key * ((len(text)) // len(key) + 1))[:len(text)]

    result = []

    for t_char, k_char in zip(text, key):
        t_index = ord(t_char) - ord('a')
        k_index = ord(k_char) - ord('a')

        new_index = (t_index + direction*k_index)%26

        result.append(chr(new_index + ord('a')))

    return ''.join(result)


def count_friday_13s(start, end):

    count_friday_13th = 0
    start_year = start.year 
    end_year = end.year

    for year in range(start_year, end_year + 1):
        for month in range(1,13):
            
            current_date = datetime.date(year,month, 13)

            if start <= current_date <= end and current_date.weekday() == 4:
                count_friday_13th += 1 

    return count_friday_13th

def bug_in_a_line(board):
    
    lights = list(board)
    len_board = len(board)
    pos = 0
    steps = 0

    while 0 <= pos < len_board:
        if lights[pos] == 'G':
            lights[pos] = 'Y'
            pos += 1

        elif lights[pos] == 'Y':
            lights[pos] = 'R'
            pos += 1

        else:
            lights[pos] = 'G'
            pos -= 1

        steps += 1

    return steps


def albuquerque_stretch(text):

    result = ""

    for c in range(len(text)):

        if text[c] in text[:c]:
            
            find_str = text[c-1::-1]
            find_str = find_str.find(text[c])
            result += text[c-find_str-1:c+1]

        else:
            result += text[c]

    return result

def double_ended_pop(items, k):
    n = len(items)

    prefix = [0] * (k + 1)
    for i in range(1, k+1):
        prefix[i] = prefix[i - 1] + items[i - 1]

    suffix = [0] * (k + 1)
    for i in range(1, k+1):
        suffix[i] = suffix[i - 1] + items[-i]

    max_sum = 0

    for i in range(0, k+1):
        if i <= n and (k-1) <= n:
            total = prefix[i] + suffix[k - i]
            max_sum = max(max_sum, total)

    return max_sum


def first_singleton(text):

    char_count = {}

    for char in text:
        char_count[char] = char_count.get(char, 0) + 1

    for char in text:
        if char_count[char] == 1:
            return char
    
    return None


def maximum_repeated_suffix(items):

    n = len(items)
    max_len = 0

    for m in range(1, n//2 + 1):
        if items[n - m : n] == items[n - 2*m : n - m]:
            max_len = m

    return max_len

def loopless_walk(steps):
    
    repeated_char = set()
    result = []

    for char in steps:
        
        if char in repeated_char:
            
            while result and result[-1] != char:
                repeated_char.remove(result.pop())
            result.pop()

        result.append(char)
        repeated_char.add(char)
    
    return ''.join(result)
 

def max_blocks(permutation):

    n = len(permutation)
    on = [True] * n
    blocks = 1
    max_blocks = 1

    for p in permutation:
        on[p] = False
        left_on = (p > 0 and on[p - 1])
        right_on = (p < n -1 and on[p+1])

        if left_on and right_on:
            blocks -= 1
        elif not left_on and not right_on:
            pass
        else:
            blocks -= 1

        max_blocks = max(max_blocks, blocks)

    return max_blocks


def split_at_none(items):
    result = []
    current = []

    for item in items:
        if item is None:
            result.append(current)
            current = []
        else:
            current.append(item)
    result.append(current)
    return result

def merge_biggest(items):
    heap = [-x for x in items]
    heapq.heapify(heap)

    while len(heap) > 1:
        a = -heapq.heappop(heap)
        b = -heapq.heappop(heap)
        if a != b:
            heapq.heappush(heap, -(abs(a - b)))

    return -heap[0] if heap else 0




