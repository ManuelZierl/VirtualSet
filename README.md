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
| name  | alias  | description  |
|---            |---|---|
| [Some](#Some) |   |   |
| AllOf         |   |   |
| SomeOrNone    |   |   |
| SomeIterable  |   |   |
| SomeList      |   |   |
| SomeTuple     |   |   |
| SomeDict      |   |   |
| SomeSet       |   |   |
| SomeStrict    |   |   |
| SomeCallable  |   |   |
| SomeIn        |   |   |
| SomeWithLen   |   |   |
| NotSome       |   |   |
| SomeStr       |   |   |
| SomeNumber    |   |   |

#### <a name="Some"></a>Some
todo:


