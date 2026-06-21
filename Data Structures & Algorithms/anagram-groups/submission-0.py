class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_items = {}
        for item in strs:
            sorted_str = "".join(sorted(item))
            if sorted_items.get(sorted_str):
                sorted_items[sorted_str].append(item)
            else:
                sorted_items[sorted_str] = [item]
        return [v for v in sorted_items.values()]
