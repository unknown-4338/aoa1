def fractional_knapsack(values, weights, W):
    n = len(values)
    
    
    ratios = [(values[i] / weights[i], values[i], weights[i]) for i in range(n)]
    
    ratios.sort(reverse=True)
    
    total_value = 0  
    current_weight = 0  
    
    
    for ratio, value, weight in ratios:
        if current_weight + weight <= W:
            
            total_value += value
            current_weight += weight
        else:
            
            fraction = (W - current_weight) / weight
            total_value += value * fraction
            break
    
    return total_value



values1 = [60, 100, 120]
weights1 = [10, 20, 30]
W1 = 50
print("Maximum value in knapsack =", fractional_knapsack(values1, weights1, W1))  

values2 = [40, 100, 50, 60]
weights2 = [20, 10, 40, 30]
W2 = 50
print("Maximum value in knapsack =", fractional_knapsack(values2, weights2, W2))  
