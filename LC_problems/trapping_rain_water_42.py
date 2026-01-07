def trapping_rain_water(heights):
    if not heights:
        return 0 
    left=0
    right=len(heights)-1
    left_max=0 
    right_max=0
    water=0
    while left<right:
        if heights[left]<heights[right]:
            if heights[left]>=left_max:
                left_max=heights[left]
            else:
                water+=left_max-heights[left]
            left+=1 
        else:
            if heights[right]>=right_max:
                right_max=heights[right]
            else:
                water+=right_max-heights[right]
            right-=1
    return water
if __name__=="__main__":
    n=int(input("enter length of heights array:"))
    heights=list(map(int,input("enter heights:").split()))
    result=trapping_rain_water(heights)
    print("Total trapped rain water:",result)
    