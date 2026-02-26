T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    v = list(map(int, input().split()))
    
    days = []
    
    for rating in v:
        placed = False
        
        for i in range(len(days)):
            if abs(rating - days[i]) >= K:
                days[i] = rating
                placed = True
                break
        
        if not placed:
            days.append(rating)
    
    print(len(days))