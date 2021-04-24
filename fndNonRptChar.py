def fndNonRptChar(in_array):
    in_array = in_array.lower()
    for ch in in_array:
        init_char = ch
        count = 0
        for ch2 in in_array:
            if (ch2 == init_char):
                count += 1

        if (count == 1):
            print("the first non repeatable character is:", init_char)
            break



fndNonRptChar("saara zamana haseenon ka deewana")