+ 统计有序数组的最小差值
```python
r = float('inf')
for i in range(len(res)-1):  
    r = min(abs(res[i]-res[i+1]),r)
```

+ 字符串中有多少个0和1
```python
ones = strs[k].count('1')
zeros = strs[k].count('0')
```
