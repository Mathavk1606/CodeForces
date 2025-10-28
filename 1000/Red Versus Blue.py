for _ in range(int(input())):
    n, r, b = map(int, input().split(" "))
    
    if b > 0:
        spacing = (r + 1) // (b + 1)
        
        result = []
        r_remaining = r
        for i in range(b):
            if i < b:
                if r_remaining > 0: result.append("R" * spacing)
                result.append("B")
                r_remaining -= spacing
        
        result.append("R" * r_remaining)
        s = "".join(result)
    
    print(s)