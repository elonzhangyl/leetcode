```python
r = float('inf')
for i in range(len(res)-1):  // 统计有序数组的最小差值
    r = min(abs(res[i]-res[i+1]),r)
```