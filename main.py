def square_root_bisection(number, tolerance=1e-6, max_iterations=100):
    if number < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")
    if number == 0:
        print("The square root of 0 is 0")
        return 0
    if number == 1:
        print("The square root of 1 is 1")
        return 1
    low = 0
    high = max(1, number)
    iteration = 0
    while iteration < max_iterations:
        mid = (low + high) / 2
        mid_squared = mid * mid
        if mid_squared == number:
            print(f"The square root of {number} is approximately {mid}")
            return mid
        elif mid_squared < number:
            low = mid
        else:
            high = mid
        if high - low <= tolerance:
            root = mid
            print(f"The square root of {number} is approximately {root}")
            return root
        iteration += 1
    print(f"Failed to converge within {max_iterations} iterations")
    return None
