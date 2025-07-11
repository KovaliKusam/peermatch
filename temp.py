import bisect

def maxValue(events, k):
    events.sort(key=lambda x: x[1])  # Sort by end time
    ends = [event[1] for event in events]
    n = len(events)
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        start, end, value = events[i - 1]
        # Find the latest event that ends before current event starts
        prev = bisect.bisect_left(ends, start)
        
        for j in range(1, k + 1):
            # Option 1: Don't take current event
            dp[i][j] = dp[i - 1][j]
            # Option 2: Take current event (if we have remaining capacity)
            dp[i][j] = max(dp[i][j], dp[prev][j - 1] + value)
    
    return dp[n][k]

n = int(input())
events = []
for _ in range(n):
    s, e, v = map(int, input().split())
    events.append([s, e, v])

k = int(input())
print(maxValue(events, k))