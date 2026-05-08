''' Container With Most Water

Question:
Given an integer array height where each element represents the height of a vertical line, find two lines that together form a container such that the container stores the maximum amount of water.

Return the maximum area.

📌 Example:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
'''

def maxArea(heights):
    left=0
    right=len(heights)-1
    max_area=0
    while left<right:
        current_width=right-left
        current_height=min(heights[left],heights[right])
        current_area=current_width*current_height
        max_area=max(max_area,current_area)
        if heights[left]<heights[right]:
            left+=1
        else:
            right-=1
    return max_area

if __name__=="__main__":
    heights=list(map(int,input().split()))
    result=maxArea(heights)
    print(result)
        