class Solution():
    def counterZeroInFourLists(
        self, 
        lst1:list[int], 
        lst2:list[int], 
        lst3:list[int], 
        lst4:list[int]) -> int:

        def twoNextedLists(lst1, lst2):
            dct = {}
            for val1 in lst1:
                for val2 in lst2:
                    val = val1 + val2
                    if val in dct: 
                        dct[val] += 1
                    else:
                        dct[val] = 1
            return dct
        
        dct12 = twoNextedLists(lst1, lst2)
        dct34 = twoNextedLists(lst3, lst4)

        def switcher(a, b):
            if len(a) > len(b):
                temp = a
                a = b
                b = temp
            return a, b

        dct12, dct34 = switcher(dct12, dct34)

        counter = 0
        for key1 in dct12:
            if -key1 in dct34:
                counter += max(dct12[key1], dct34[-key1])
        
        return counter

A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

Solution().counterZeroInFourLists(A,B,C,D)
        
