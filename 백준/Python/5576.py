w = [int(input()) for _ in range(10)] 
k = [int(input()) for _ in range(10)]  

w_top = sorted(w, reverse=True)[:3]   
k_top = sorted(k, reverse=True)[:3]   

print(sum(w_top), sum(k_top))
