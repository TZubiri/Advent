
def consecutive_sum(digits):
    sum = 0
    last_digit = digits[-1:]
    for digit in digits:
        if digit == last_digit:
            sum += int(digit)
        last_digit = digit
    return sum

assert(consecutive_sum('1122')==3)
assert(consecutive_sum('1111')==4)
assert(consecutive_sum('1234')==0)
assert(consecutive_sum('11234')==1)
assert(consecutive_sum('11231')==2)
assert(consecutive_sum('91212129')==9)