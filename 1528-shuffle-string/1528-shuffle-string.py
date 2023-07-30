class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = []
        
        # The list of tuples containing (i, j) pairs
        original_list = [(i, j) for (i, j) in zip(s, indices)]

        # Sort the list based on the second element (j)
        sorted_list = sorted(original_list, key=lambda x: x[1])
        tmp = [i[0] for i in sorted_list]
        result = ''.join(tmp)

        return result