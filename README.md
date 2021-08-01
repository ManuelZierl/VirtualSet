### Work - in - progress
# PySome

`PySome` brings the `expect(...).to_be(...)` syntax to python for
easier and clearer testing of nested objects

### Installation

`pip install pysome`

### Example:
```python
from pysome import Some, SomeList, SomeDict, expect
# some large nested api response you want to test
api_response = {
    "menu": {
        "tags": [
            {"id": 1, "z-index": 12},
            {"id": 2, "name": "ax7"},
            {"id": 5, "name": "ax7", "z-index": 12},
            {"id": 2, "alias": "iivz"},
        ]
    }
}

# test only important stuff
expect(api_response).to_be({
    "menu": {
        "tags": SomeList(
            SomeDict(id=Some(int))
        )
    }
})
```

### Some API
| name  | alias  | arguments <br> `*args = Union[type, Callable, Some]` | description  |
|---    |---     |---        |---           |
| [Some()](#Some) |   |  `*args`  |
| [AllOf()](#AllOf) |   | `*args`  |
| [SomeOrNone()](#SomeOrNone) |   | `*args`  |
| [SomeIterable()](#SomeIterable)   |   | `*args`, `length = None`, `is_type = None`  |
| [SomeList()](#SomeList)           |   | `*args`, `length = None`, `is_type = None`   |
| [SomeTuple()](#SomeTuple)         |   | `*args`, `length = None`, `is_type = None`   |
| [SomeDict()](#SomeDict)           |   | `partial_dict: dict = None`, `**kwargs`  |
| [SomeSet()](#SomeSet)             |   |   |
| [SomeStrict()](#SomeStrict)       |   |   |
| [SomeCallable()](#SomeCallable)   |   |   |
| [SomeIn()](#SomeIn)               |   |   |
| [SomeWithLen()](#SomeWithLen)     | `has_len` |  `length = None`, `min_length = None`, `max_length = None` |
| [NotSome()](#NotSome)             |   |   |
| [SomeStr()](#SomeStr)             |   |   |
| [SomeNumber()](#SomeNumber)       |   |   |

### <a name="Some"></a>Some
todo:
### <a name="AllOf"></a>AllOf
todo:
### <a name="SomeOrNone"></a>SomeOrNone
todo:
### <a name="SomeIterable"></a>SomeIterable
todo:
### <a name="SomeList"></a>SomeList
todo:
### <a name="SomeTuple"></a>SomeTuple
todo:
### <a name="SomeDict"></a>SomeDict
todo:
### <a name="SomeSet"></a>SomeSet
todo:
### <a name="SomeStrict"></a>SomeStrict
todo:
### <a name="SomeCallable"></a>SomeCallable
todo:
### <a name="SomeIn"></a>SomeIn
todo:
### <a name="SomeWithLen"></a>SomeWithLen
todo:
### <a name="NotSome"></a>NotSome
todo:
### <a name="SomeStr"></a>SomeStr
todo:
### <a name="SomeNumber"></a>SomeNumber
todo:

