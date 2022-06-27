
def in_range(n):
    if n>= 0 and n <= 255:
        return True
    return False

def has_zer_before(n):
    if len(n)>1:
        if n[0] == "0":
            return True
        return False
        
def isValid(s):
    s = s.split(".")
    if len(s) != 4:  
        return 0
    for n in s:
         
        if has_zer_before(n):
            return 0
        if len(n) == 0:
            return 0
        try:  
            n = int(n)
 
            if not in_range(n):
                return 0
        except:
            return 0
    return 1