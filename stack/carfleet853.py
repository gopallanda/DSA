def carFleet(target: int, position:list[int], speed:list[int])->int:
    n=len(position)
    cars=[(position[i],(target-position[i])/speed[i]) for i in range(n)]
    print(cars)
    cars.sort(reverse=True)
    print(type(cars))
    fleet=0
    current_time=-1.0
    for pos, t in cars:
        if t>current_time:
            fleet+=1
            current_time=t
    return fleet
if __name__=="__main__":
    target=int(input("enter the target:"))
    position=list(map(int,input("enter the positions of the cars:").split()))
    speed=list(map(int,input("enter the speeds of the cars:").split()))
    result=carFleet(target,position,speed)
    print("number of car fleets that will arrive at the destination:",result)