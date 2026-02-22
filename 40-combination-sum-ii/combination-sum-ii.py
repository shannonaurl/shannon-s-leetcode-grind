class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        candidates.sort(reverse=False)
        
        def dfs(i, curr_list, curr_sum):
            if curr_sum == target:
                output.append(curr_list[:])
                return
            if curr_sum > target or i >= len(candidates):
                return

            # include candidates[i]
            curr_list.append(candidates[i])
            dfs(i + 1, curr_list, curr_sum + candidates[i])
            curr_list.pop()

            # exclude candidates[i] - but skip duplicates
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i + 1, curr_list, curr_sum)

        dfs(0, [], 0)
        return output 
        