# Write your code here
def format_time(h, m, s):
    hstr = f'{h}'.rjust(2, "0")
    mstr = f'{m}'.rjust(2, "0")
    sstr = f'{s}'.rjust(2, "0")
    return f'{hstr}:{mstr}:{sstr}'