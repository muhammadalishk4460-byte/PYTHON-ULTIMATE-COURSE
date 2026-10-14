def count(n):
    if n == 6:      # Stop when n becomes 6
        return

    print(n)
    count(n + 1)    # Call the same function again

count(1)