def common_fun():
    print("common_fun dentro de libutils")

    return True

def hello():
    print("hello!")

def compute_first_n_primes(n: int) -> list:
    """
    Compute the first n prime numbers.

    Parameters:
    n (int): The number of prime numbers to compute. Must be 100 or less.

    Returns:
    list: A list containing the first n prime numbers.

    Raises:
    ValueError: If n is greater than 100.
    """
    if n > 100:
        raise ValueError("n should not be greater than 100")
    
    primes = []  # List to store prime numbers
    candidate = 2  # Starting candidate for prime number
    
    while len(primes) < n:
        # Check if candidate is a prime number
        is_prime = all(candidate % p != 0 for p in primes)
        if is_prime:
            primes.append(candidate)  # Add prime number to the list
        candidate += 1  # Move to the next candidate
    
    return primes