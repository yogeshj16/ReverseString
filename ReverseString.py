# abc#def,gh$@
# hgf#edc,ba$@
# @$hg,fed#cba

#======================= FUNCTIONS ======================#

# Returns a list from a string
def str2list(istr):
    lst = []
    for c in istr:
        lst.append(c)
    return lst

# Returns a string from a list
def list2str(lst):
    ostr = ""
    for c in lst:
        ostr += c
    return ostr

# Interchange two elements in a list
def change(lst, begin, end):
    if (begin > end) or (end > (len(lst) - 1)):
        return
    tmp = lst[begin]
    lst[begin] = lst[end]
    lst[end] = tmp

# ================ BEGIN OF THE PROGRAM ================== #

print(".::REVERSE A STRING WITHOUT CHANGING THE SPECIAL CHARACTERS::.")

istr = input("Type the string you want to reverse: ")   # Original string
if len(istr) <= 0:
    print("The string is empty");
    exit();
special_chars = "!\"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~"    # Stores the special characters
lst = str2list(istr)                                    # Stores a list representation of the string

begin = 0               # Stores the position at the biginnig of the list
end = len(lst) - 1      # Stores the position at the end of the list
ltrs = 0                # Stores the number of letters that are'nt special characters
ltrcnt = 0              # Stores the number of letters that were changed
itr = True              # Loop control variable

# Counts the number of letters or non special characters in the list
for x in istr:
    if x not in special_chars:
        ltrs += 1

while itr:
    # Stop the loop when both positions in the list are the same
    if begin == end:
        itr = False
        continue
    
    if (lst[begin] in special_chars) and (lst[end] in special_chars):
        # Both characters are special
        begin += 1
        end -= 1
        continue
    else:
        # One of the characters are special
        if lst[begin] in special_chars:
            begin += 1
            continue
        elif lst[end] in special_chars:
            end -= 1
            continue
        else:
            # Both characters are NOT special
            ltrcnt += 2
            change(lst, begin, end)
            begin += 1
            end -= 1
    
    # Stop the loop when there's no more changes (Both number of letters and letters changed are the same)
    if ltrcnt == ltrs:
        itr = False

ostr = list2str(lst)    # Stores the string representation of the list
print(istr)             # Prints the original string
print("String reversed: ")
print(ostr)             # Prints the string reversed without changing the special characters' position