## Useful information about IPython's asynchronous access
https://ipython.readthedocs.io/en/stable/interactive/autoawait.html
<br></br>
"As running asynchronous code is not supported in interactive REPL (as of Python 3.7) we have to rely to a number of complex workaround and heuristic to allow this to happen. It is interesting to understand how this works in order to comprehend potential bugs, or provide a custom runner.
<br></br>
Among the many approaches that are at our disposition, we find only one that suited out need. Under the hood we use the code object from a async-def function and run it in global namespace after modifying it to not create a new locals() scope:"
```python
async def inner_async():
    locals().update(**global_namespace)
    #
    # here is user code
    #
    return last_user_statement
codeobj = modify(inner_async.__code__)
coroutine = eval(codeobj, user_ns)
display(loop_runner(coroutine))
```
