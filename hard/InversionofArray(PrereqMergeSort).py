# https://www.naukri.com/code360/problems/count-inversions_615?leftPanelTabValue=PROBLEM

def getInversions(arr, n) :
    cnt = 0
    n = len(arr)
    
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                cnt += 1
                
    return cnt