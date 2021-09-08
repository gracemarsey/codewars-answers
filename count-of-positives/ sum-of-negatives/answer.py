def count_positives_sum_negatives(arr):
    if len(arr) == 0:
        return []
    
    sum=[0,0]     
    for x in arr:
        if x < 0:
            sum[1]= sum[1] + x
        elif x > 0:
            sum[0]= sum[0] + 1
    return sum 