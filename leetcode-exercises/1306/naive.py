class Solution:
    def canReach(self, arr: list[int], start: int) -> bool:
        state = [start]
        non_visited = [True for el in arr]
        while any(non_visited[el] for el in state):
            new_state = []
            for el in state:
                if arr[el] == 0:
                    return True
                non_visited[el] = False
                l = el - arr[el]
                if l >= 0 and non_visited[l]:
                    if arr[l] == 0:
                        return True
                    new_state.append(l)

                r = el + arr[el]
                if r < len(arr) and non_visited[r]:
                    if arr[r] == 0:
                        return True
                    new_state.append(r)

            state = new_state

        return False
