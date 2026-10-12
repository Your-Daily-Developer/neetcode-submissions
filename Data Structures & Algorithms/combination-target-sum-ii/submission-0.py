class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        res = []

        def dfs(idx, path, cur):
            if cur == target:
                res.append(path[:])
                return

            for i in range(idx, len(candidates)):
                # Skip duplicates at the same recursion level
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                # Prune: sorted array, so all further elements are also too big
                if cur + candidates[i] > target:
                    break

                path.append(candidates[i])
                dfs(i + 1, path, cur + candidates[i])
                path.pop()

        dfs(0, [], 0)
        return res   