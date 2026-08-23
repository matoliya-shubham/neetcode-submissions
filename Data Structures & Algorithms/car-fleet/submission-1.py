class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # first we have to sort combination of position nd speed in reverse order
        # after sorting calculate time for each combination and start pushing that time in stack
        # after pushing one item(time) in stack next item can only be pushed if it is lesser than that in top of stack
        # as lesser time taking car(which has more speed) has to slow down and move with speed of prev car and that will form a carFleet
        # finally length of stack will give all car fleets possible 
        pair = [(position[i], speed[i]) for i in range(len(position))]
        cars = sorted(pair, reverse=True)
        # or sorted(zip(position, speed), reverse=True)
        stack = []
        for pos, speed in cars:
            time = (target - pos) / speed
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)
