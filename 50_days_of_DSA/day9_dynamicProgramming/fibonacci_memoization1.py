def fib_hash(n, ht={0:0, 1:1}):
    if n in ht:
        return ht[n]
    else:
        ht[n] = fib_hash(n-1, ht) + fib_hash(n-2, ht)
        return ht[n]
    
print(fib_hash(5))

print(fib_hash(8))