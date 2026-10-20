class Solution:
    def trap(self, height: List[int]) -> int:

        def diff(l,r):
            diff = 0
            l += 1
            while l < r:
                diff += height[l]
                l += 1
            return diff

        l, r = 0, len(height) - 1
        if l == r: return 0
        res = 0
        while l < r:
            while l < r and height[r-1] > height[r]:
                r -= 1
            while l < r and height[l+1] > height[l]:
                l += 1
            
            if l >= r: break

            if height[l] <= height[r]:
                templ = l + 1
                while height[templ] < height[l]:
                    templ += 1
                area = (templ-l-1) * min(height[l],height[templ])
                area -= diff(l,templ)
                res += area
                l = templ
            else:
                tempr = r - 1
                while height[tempr] < height[r]:
                    tempr -= 1
                area = ((r-1)-tempr) * min(height[r],height[tempr])
                area -= diff(tempr,r)
                res += area
                r = tempr
        
        return res



