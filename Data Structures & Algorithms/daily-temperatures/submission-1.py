class Solution:
    # def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # i = 0
        # j = i + 1
        # ans = []

        # while i < len(temperatures):

        #     if j == len(temperatures):
        #         ans.append(0)
        #         i += 1
        #         j = i + 1

        #     elif temperatures[j] > temperatures[i]:
        #         ans.append(j - i)
        #         i += 1
        #         j = i + 1

        #     else:
        #         j += 1

        # return ans

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        ans = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):

            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev = stack.pop()
                ans[prev] = i - prev

            stack.append(i)

        return ans