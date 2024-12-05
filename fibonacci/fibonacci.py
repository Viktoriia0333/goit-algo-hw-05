def caching_fibonacci():
    cash = {}
    def fibonacci(n :int):
        if n<=1:
            return n
        if n in cash:
            return cash[n]
        else:
            cash[n] = fibonacci(n - 2) + fibonacci(n - 1)
            return cash[n]
    return fibonacci

