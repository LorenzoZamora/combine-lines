# Name: Lorenzo Zamora
# Problem: There are 2 lines, and people go in order of P, G, B to form a single one
# Input: 2 strings (of people waiting in line)
# Output: 1 string (of people formed from the two lines according to badge order)

def combine_lines(line1, line2):
    l, l1, l2 = [], [], []
    l1m, l2m = 0, 0 # marker of where we are comparing for each line
    l1[:0], l2[:0] = line1, line2 # turn string into list to iterate through more easily

    l1_len, l2_len = len(line1), len(line2)
    t_len = l1_len + l2_len
    i = 0

    while (i < t_len):
        if ((l1m != l1_len) and (l2m != l2_len)): # check if marker got to end of a line
            if (l1[l1m] >= l2[l2m]):              # if not, check which badge is greater,
                l.append(l1[l1m])                 #  add them to the single line and 
                l1m += 1                          #  increment that line's marker
            elif (l2[l2m] >= l1[l1m]):
                l.append(l2[l2m])
                l2m += 1
        else:                                    # if at end of a line, just add the 
            if (l1_len == l1m):                  #  rest of the other line into the 
                l += l2[l2m:l2_len]              #  single line, since only 1 line has 
                break                            #  people left. No more comparison
            elif (l2_len == l2m):
                l += l1[l1m:l1_len]
                break
        i += 1
        
    return("".join(l))                           # return single line of people as a string

if __name__ == "__main__":                       # solution takes the higher badge from
    line1 = "PG"                                 # the first line when comparing.
    line2 = "BG" 
    print(combine_lines(line1, line2))

    line1 = "PGBPG"
    line2 = "PBGGBPB"
    print(combine_lines(line1, line2))

    line1 = "PGGPBBGGBPBGPBBPG"
    line2 = "PGBPGBPPGBBGGP"                     # Thank you for taking the time to read
    print(combine_lines(line1, line2))           #  my solution! :)
