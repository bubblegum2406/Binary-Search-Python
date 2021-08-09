arr = [1,6,8,20,30,69,50,38]
reqNum = 50

def myFunc(arr,reqNum):
    arr.sort()
    top = len(arr)
    bottom =0
    while top > bottom:
        mid = (top+bottom)//2
        if arr[mid] == reqNum:
            print(arr[mid])
            break
        elif arr[mid] > bottom:
            bottom = bottom+1
        elif arr[mid] > top:
            top = top + 1

myFunc(arr, reqNum)

