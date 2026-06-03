def maxRectangleArea(heights):
    stack=[]
    max_area=0
    for i,h in enumerate(heights):
        while stack and heights[stack[-1]]>h:
            height=heights[stack.pop()]
            width=i if not stack else i-stack[-1]-1
            max_area=max(max_area,height*width)
        stack.append(i)
    return max_area
if __name__=="__main__":
    heights=list(map(int,input("Enter the heights of the histogram bars: ").split()))
    result=maxRectangleArea(heights)
    print("The area of the largest rectangle in the histogram is:", result)