
class Solution:
    def commonElements (self,A, B, C, n1, n2, n3):
        return sorted(list(set(A).intersection(set(B)).intersection(set(C))))