# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) <= 1:
            return pairs
        m = len(pairs) // 2 
        left = self.mergeSort(pairs[:m])
        right = self.mergeSort(pairs[m:])

        return self.merge(left, right)
    
    def merge(self, left, right):
        i = 0
        j = 0
        combined = []
        while i < len(left) and j < len(right):
            
            if left[i].key <= right[j].key:
                combined.append(left[i])
                i += 1 
            # elif left[i].key == right[j].key:
            #     if left[i].value <= right[j].value:
            #         combined.append(left[i])
            #         i += 1
                # else:
                #     combined.append(right[j])
                #     j += 1
            else:
                combined.append(right[j])
                j += 1 
            # k += 1 
        while i < len(left):
            # combined += left 
            combined.append(left[i])
            i += 1
        while j < len(right):
            # combined += right 
            combined.append(right[j])
            j += 1 
        return combined