class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        def reachable(pos1,pos2,speed1,speed2,target):
            if speed1 == speed2 and pos1 != pos2: return False
            if speed1 == speed2 and pos1 == pos2: return True
            if speed2 < speed1: return False
            timeUntilMeet = abs(pos1-pos2)/abs(speed2-speed1)
            return pos1 + timeUntilMeet*speed1 <= target and pos1 + timeUntilMeet*speed1 >= 0

        order = sorted(range(len(position)), key=lambda i: -position[i])
        fleets = [order[0]]

        for i in range(1,len(order)):
            i = order[i]
            for car in fleets:
                if reachable(position[car],position[i],speed[car],speed[i],target):
                    
                    break
            else: fleets.append(i)
        
        return len(fleets)
            