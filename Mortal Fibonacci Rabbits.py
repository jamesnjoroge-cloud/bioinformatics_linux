def mortal_fibonacci_rabbits(n, m):
    # list representing the count of rabbit pairs at each age group:
    # index 0: 1 month old (newborns)
    # index 1: 2 months old
    # ...
    # index m-1: m months old
    ages = [0] * m
    
    # We start with 1 pair of newborns in the first month
    ages[0] = 1
    
    # Simulate for month 2 up to month n
    for month in range(1, n):
        # 1. Calculate newborns for this month. 
        # Only rabbits of age 2 or older (index 1 to m-1) can reproduce.
        newborns = sum(ages[1:])
        
        # 2. Shift all existing rabbits up by one month (aging them)
        # This naturally discards the rabbits at index m-1 (they die).
        next_ages = [0] * m
        for i in range(1, m):
            next_ages[i] = ages[i - 1]
            
        # 3. Place the newborns into age group 1 (index 0)
        next_ages[0] = newborns
        
        # Update our ages state
        ages = next_ages

    # The total surviving rabbit pairs is the sum of all age groups
    return sum(ages)

# Example Usage (Rosalind Sample Dataset: n = 6, m = 3)
n, m = 6, 3
print(f"Total surviving pairs after {n} months (lifespan {m}): {mortal_fibonacci_rabbits(n, m)}")