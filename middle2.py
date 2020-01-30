def get_middle(s):
    lens = len(s)
    if lens % 2 == 0:
        i = lens // 2
        print(s[i-1:i+1])
        
    else:
        j = lens // 2
        print(s[j])
    return s


get_middle("testing")
