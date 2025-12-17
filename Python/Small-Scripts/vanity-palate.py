def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    #“No periods, spaces, or punctuation marks are allowed.” 
    if s.isalnum():
        #vanity plates may contain a maximum of 6 characters and a minimum of 2
        if 2 <= len(s) <= 6:
            #“All vanity plates must start with at least two letters.”
            if s[0:2].isalpha():
                #“Numbers cannot be used in the middle of a plate; they must come at the end
                for c in s:
                    if c.isdigit():
                        #The first number used cannot be a ‘0’.”
                        if c != "0":
                            if s[s.index(c):].isdigit():
                                return True
                            else:
                                return False
                        else:
                            return False
                else:
                    return False
        

main()