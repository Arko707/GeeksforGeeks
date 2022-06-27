class Solution:
    def duplicates(self, arr, n):
        l = {}
        r = {}
        ll = []
        for i in arr:
            try:
                l[i] += 1
                try:
                    r[i] += 1
                except:
                    r[i] = 1
                    ll.append(i)
            except:
                l[i] = 1

        if len(ll) == 0:
            return [-1]
        ll.sort()
        return ll
