def printKMax(a, n, k): 
      
    # If k = 1, prall elements 
    if (k == 1): 
        for i in range(n): 
            print(a[i], end=" "); 
        return; 
          
    # Using p and q as variable pointers 
    # where p iterates through the subarray 
    # and q marks end of the subarray. 
    p = 0; 
    q = k - 1; 
    t = p; 
    max = a[k - 1]; 
  
    # Iterating through subarray. 
    while (q <= n - 1): 
  
        # Finding max 
        # from the subarray. 
        if (a[p] > max): 
            max = a[p]; 
        p += 1; 
  
        # Printing max of subarray 
        # and shifting pointers 
        # to next index. 
        if (q == p and p != n): 
            print(max, end=" "); 
            q += 1; 
            p = t + 1; 
  
            if (q < n): 
                max = a[q]; 
  
# Driver Code 
if __name__ == '__main__': 
    a = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]; 
    n = len(a); 
    K = 3; 
  
    printKMax(a, n, K); 
  