# https://www.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        meetings = sorted([(end[i], start[i]) for i in range(n)])
        
        count = 1
        prev_end = meetings[0][0]
        
        for i in range(1,n):
            if meetings[i][0] > prev_end:
                count = count + 1
                prev_end = meetings[i][0]
        
        return count