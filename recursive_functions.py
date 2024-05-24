def add_one(num):

    if num >= 9:
        return num+1

    total = num+1
    print("Total", total)

    # Recursive and calls the function from within the function itself
    return add_one(total)


new_total = add_one(0)
print("New Total : ", new_total)
