

def open_file(filepath, mode):
    try:
        f = open(filepath, mode)
        yield f
    finally:
        f.close()


# open_file is a function
print(type(open_file))
# Returns a generator object
gen_obj = open_file('output.txt', 'r')
# Now it yields the file object
f = next(gen_obj)
# We can now read the file
print(f.read())

# Now it closes but raises stop iteration
next(gen_obj, None)
print(f.closed)