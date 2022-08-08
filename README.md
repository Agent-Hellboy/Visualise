# Visualise
An attempt to make a library which helps in visualisation of program execution


```bash
from visualise import call_stack
def subsets(nums):
    res = []
    sub = []
    def dfs(i):
        if i >= len(nums):
            res.append(sub.copy())
            return
        sub.append(nums[i])
        dfs(i+1)
        sub.pop()
        dfs(i+1)
        call_stack()
    dfs(0)
    return res

subsets([1,2,3])


```
OUTPUT:
 
whole summary of call_stack whenever program execution hits the point of function call
```
********************************************************************************
{'current_frame': <frame at 0x7f5c74c7fdd0, file '/home/proshan/stackoverflow/Visualise/visualise/v_call_stack.py', line 9, code call_stack>}
None
{'dfs': <function subsets.<locals>.dfs at 0x7f5c74b815e0>,
 'i': 2,
 'nums': [1, 2, 3],
 'res': [[1, 2, 3], [1, 2]],
 'sub': [1, 2]}
None
{'dfs': <function subsets.<locals>.dfs at 0x7f5c74b815e0>,
 'i': 1,
 'nums': [1, 2, 3],
 'res': [[1, 2, 3], [1, 2]],
 'sub': [1, 2]}
None
{'dfs': <function subsets.<locals>.dfs at 0x7f5c74b815e0>,
 'i': 0,
 'nums': [1, 2, 3],
 'res': [[1, 2, 3], [1, 2]],
 'sub': [1, 2]}
None
{'dfs': <function subsets.<locals>.dfs at 0x7f5c74b815e0>,
 'nums': [1, 2, 3],
 'res': [[1, 2, 3], [1, 2]],
 'sub': [1, 2]}
None
********************************************************************************
{'current_frame': <frame at 0xe87dd0, file '/home/proshan/stackoverflow/Visualise/visualise/v_call_stack.py', line 9, code call_stack>}
None
{'dfs': <function subsets.<locals>.dfs at 0x7f5c74b815e0>,
 'i': 2,
 'nums': [1, 2, 3],
 'res': [[1, 2, 3], [1, 2], [1, 3], [1]],
 'sub': [1]}
None
{'dfs': <function subsets.<locals>.dfs at 0x7f5c74b815e0>,
 'i': 1,
 'nums': [1, 2, 3],
 'res': [[1, 2, 3], [1, 2], [1, 3], [1]],
 'sub': [1]}
None
{'dfs': <function subsets.<locals>.dfs at 0x7f5c74b815e0>,
 'i': 0,
 'nums': [1, 2, 3],
 'res': [[1, 2, 3], [1, 2], [1, 3], [1]],
 'sub': [1]}
None
{'dfs': <function subsets.<locals>.dfs at 0x7f5c74b815e0>,
 'nums': [1, 2, 3],
 'res': [[1, 2, 3], [1, 2], [1, 3], [1]],
 'sub': [1]}
None
********************************************************************************
{'current_frame': <frame at 0xe87b30, file '/home/proshan/stackoverflow/Visualise/visualise/v_call_stack.py', line 9, code call_stack>}
None
{'dfs': <function subsets.<locals>.dfs at 0x7f5c74b815e0>,
 'i': 1,
 'nums': [1, 2, 3],
 'res': [[1, 2, 3], [1, 2], [1, 3], [1]],
 'sub': [1]}
None
{'dfs': <function subsets.<locals>.dfs at 0x7f5c74b815e0>,
 'i': 0,
 'nums': [1, 2, 3],
 'res': [[1, 2, 3], [1, 2], [1, 3], [1]],
 'sub': [1]}
None
{'dfs': <function subsets.<locals>.dfs at 0x7f5c74b815e0>,
 'nums': [1, 2, 3],
 'res': [[1, 2, 3], [1, 2], [1, 3], [1]],
 'sub': [1]}
None
********************************************************************************
{'current_frame': <frame at 0xe88af0, file '/home/proshan/stackoverflow/Visualise/visualise/v_call_stack.py', line 9, code call_stack>}
None
{'dfs': <function subsets.<locals>.dfs at 0x7f5c74b815e0>,
 'i': 2,
 'nums': [1, 2, 3],
 'res': [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2]],
 'sub': [2]}
None
{'dfs': <function subsets.<locals>.dfs at 0x7f5c74b815e0>,
 'i': 1,
 'nums': [1, 2, 3],
 'res': [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2]],
 'sub': [2]}
None
{'dfs': <function subsets.<locals>.dfs at 0x7f5c74b815e0>,
 'i': 0,
 'nums': [1, 2, 3],
 'res': [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2]],
 'sub': [2]}
None
{'dfs': <function subsets.<locals>.dfs at 0x7f5c74b815e0>,
 'nums': [1, 2, 3],
 'res': [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2]],
 'sub': [2]}
None
********************************************************************************
{'current_frame': <frame at 0xe89030, file '/home/proshan/stackoverflow/Visualise/visualise/v_call_stack.py', line 9, code call_stack>}
None
{'dfs': <function subsets.<locals>.dfs at 0x7f5c74b815e0>,
 'i': 2,
 'nums': [1, 2, 3],
 'res': [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []],
 'sub': []}
None
{'dfs': <function subsets.<locals>.dfs at 0x7f5c74b815e0>,
 'i': 1,
 'nums': [1, 2, 3],
 'res': [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []],
 'sub': []}
None
{'dfs': <function subsets.<locals>.dfs at 0x7f5c74b815e0>,
 'i': 0,
 'nums': [1, 2, 3],
 'res': [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []],
 'sub': []}
None
{'dfs': <function subsets.<locals>.dfs at 0x7f5c74b815e0>,
 'nums': [1, 2, 3],
 'res': [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []],
 'sub': []}
None
********************************************************************************
{'current_frame': <frame at 0xe87640, file '/home/proshan/stackoverflow/Visualise/visualise/v_call_stack.py', line 9, code call_stack>}
None
{'dfs': <function subsets.<locals>.dfs at 0x7f5c74b815e0>,
 'i': 1,
 'nums': [1, 2, 3],
 'res': [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []],
 'sub': []}
None
{'dfs': <function subsets.<locals>.dfs at 0x7f5c74b815e0>,
 'i': 0,
 'nums': [1, 2, 3],
 'res': [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []],
 'sub': []}
None
{'dfs': <function subsets.<locals>.dfs at 0x7f5c74b815e0>,
 'nums': [1, 2, 3],
 'res': [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []],
 'sub': []}
None
********************************************************************************
{'current_frame': <frame at 0xe892d0, file '/home/proshan/stackoverflow/Visualise/visualise/v_call_stack.py', line 9, code call_stack>}
None
{'dfs': <function subsets.<locals>.dfs at 0x7f5c74b815e0>,
 'i': 0,
 'nums': [1, 2, 3],
 'res': [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []],
 'sub': []}
None
{'dfs': <function subsets.<locals>.dfs at 0x7f5c74b815e0>,
 'nums': [1, 2, 3],
 'res': [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []],
 'sub': []}
None
```
