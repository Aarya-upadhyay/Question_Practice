def find_room_range(n, k, coins):
    current_sum = 0
    start = 0
    
    for end in range(n):
        # Add the current room's coins to the running sum
        current_sum += coins[end]
        
        # If the running sum exceeds K, shrink the window from the left
        while current_sum!=k and start <= end:
            current_sum -= coins[start]
            start += 1
            
        # Check if the current window's sum exactly equals K
        if current_sum == k:
            # Output 1-based indices
            return f"{start + 1} {end + 1}"
            
    return "No sequence found"

# Example usage with your provided test case
n = 10
k = 15
coins = [5, 3, 7, 14, 18, 1, 18, 4, 8, 3]

print(find_room_range(n, k, coins))

"""def golden_house(arr,n,k):
    l=0
    curr=0
    for i in range(0,n):
        curr+=arr[i]
        while curr!=k and l<=i:
            curr-=arr[l]
            l+=1
        if curr==k:
            res=[l+1,i+1]
    if res:
        return res
arr=[5,3,7,18,1,18,4,8,3]
n=10
k=15
a=golden_house(arr,n,k)
print(a)"""