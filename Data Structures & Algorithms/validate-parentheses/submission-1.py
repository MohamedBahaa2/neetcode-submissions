class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {")": "(", "}": "{", "]": "["}

        for c in s:
            if c in pairs:
                if not stack or stack.pop() != pairs[c]: 
                    return False
            else:
                stack.append(c)

        return not stack

        """    
        for i in range(int(x/2)):
            case = list()
            opp = s[x - (i + 1)] 
            
            case.append(s[i])
            case.append(opp)
            
            #print("".join(case))

            if "".join(case) not in pairs:
                return False
            else:
                return True
        """
