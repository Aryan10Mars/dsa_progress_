# https://www.naukri.com/code360/problems/rotate-array_1230543?interviewBundleRedirection=true&leftPanelTabValue=PROBLEM

def rotateArray(arr: list, k: int) -> list:
    n = len(arr)
    k = k % n
    return arr[k:] + arr[:k]