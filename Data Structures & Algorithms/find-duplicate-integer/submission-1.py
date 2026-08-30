class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # assume array as linked list where each value at index tells us which index to go next
        # nums[0] can never be an ans as numbers are prsent btwn 1 to n so no value will ever suggest to go to 0 index
        slow, fast = nums[0], nums[0]
        # where slow and fast will meet for fist time that is point of intersection which confirms cycle exist it will not tell from where cycle is started. slow and fast can move n number of cycles before intersecting.
        # to detect point of intersection
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        # at this point of time slow and fast will be at there point of intersection
        # now again initialize a pointer at nums[0] eg: slow2
        # move slow and slow2 by one step each where they will meet it will be the starting point of cycle 
        # mathametically distand from start point to start of cycle is equal to distance between point of intersection to start of cycle. Hence we need to move slow and slow to by once step everytime to reach to ans
        slow2 = nums[0]
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        return slow 