## `Work - in - progress`
# PySome

`PySome` brings the `expect(...).to_be(...)` syntax to python to give developers more
flexible Options for testing for the testing of nested objects.

## Installation

    $ pip install pysome

## Usage:
### Example
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
        ],
        "randomInt": 4562,
        "auth_token": "1lm7QOvTDj",
        "labels": {
            "en": {
                "name": "name",
                "delete": "remove",
                "add": "insert"
            },
            "de": {
                "name": "Name", 
                "delete": "löschen", 
                "add": "hinzufügen"
            }
        }
    }
}

# test only important stuff
expect(api_response).to_be({
    "menu": {
        "tags": SomeList(
            SomeDict(id=Some(int))
        ),
        "randomInt": Some(int),
        "labels": Some(dict),
    }
})
```
### Why use `expect(...).to_be(...)` syntax

For most of the basic stuff it would not be necessary to use the `expect(...).to_be(...)` syntax.
You could for example safely do something like:
```python
from pysome import Some

assert {"a": 12, "b": "x", "c": {}} == {"a": Some(int), "b": Some(str), "c": Some(dict)}
```

It is still advised to use the `expect(...).to_be(...)` to avoid errors.
 todo: more in depth explanation why ...
...


## Some API

### <a name="Some"></a>Some
`Some` equals all objects under the given conditions defined by its args. It 
equals if any of the conditions is true. A condition can either be `type`, 
`Callable` or another `Some`.
```python
from pysome import Some, expect

expect(...).to_be(Some()) # equals always
expect(12).to_be(Some(int)) # equals any int
expect("abc").to_be(Some(int, str)) # equals all str and all int
```
`Some` can equal arbitrary objects by given functions:
```python
from pysome import Some, expect

def sums_to_10(x):
    return sum(x) == 10

expect([2, 3, 5]).to_be(Some(sums_to_10)) # 2 + 3 + 5 == 10
expect([5, 5]).to_be(Some(sums_to_10)) # 5 + 5 = =10
expect([1, 2, 3]).not_to_be(Some(sums_to_10)) # 1 + 2 + 3 != 10
expect({
    "a": 12,
    "b": [4, 3, 3] 
}).to_be({
    "a": Some(int), # 12 is an int
    "b": Some(sums_to_10)  # 4 + 3 + 3 == 10
})
```

but there are some useful pre-implemented subclasses of `Some`:

| name  | alias  | arguments <br> `*args = Union[type, Callable, Some]` | short description  |
|---    |---     |---        |---           |
| [Some()](#Some) |   |  `*args`  | equals all objects with any given type or function
| [AllOf()](#AllOf) |   | `*args`  | equals only an object if all given arguments are fulfilled
| [SomeOrNone()](#SomeOrNone) |   | `*args`  | same as `Some` but also equals None
| [SomeIterable()](#SomeIterable)   |   | `*args`, `length = None`, `is_type = None`  | equals all Iterables under given conditions
| [SomeList()](#SomeList)           |   | `*args`, `length = None`, `is_type = None`   | equals all Lists under given conditions
| [SomeDict()](#SomeDict)           |   | `partial_dict: dict = None`, `**kwargs`  | equals all dicts that have given subset
| [SomeIn()](#SomeIn)               | `is_in`  | container  | equals all objects that are in the given container
| [SomeWithLen()](#SomeWithLen)     | `has_len` |  `length = None`, `min_length = None`, `max_length = None` | equals al objects that fulfill given length conditions
| [NotSome()](#NotSome)             | `is_not` | *args  | equals all objects that do not fulfill any of the given conditions
| [SomeStr()](#SomeStr)             |  | `regex=None`, `pattern=None`, `endswith=None`, `startswith=None` | equals all strings under given conditions  

### <a name="AllOf"></a>AllOf
`AllOf()` equals all objects that fulfill <u>all</u> given conditions. So for example an object `AllOf(str, int)` could only match an 
object that inherits from `int` and `str`
```python
from pysome import AllOf


```
### <a name="SomeOrNone"></a>SomeOrNone
todo:
### <a name="SomeIterable"></a>SomeIterable
todo:
### <a name="SomeList"></a>SomeList
todo:
### <a name="SomeDict"></a>SomeDict
todo:
### <a name="SomeIn"></a>SomeIn
todo:
### <a name="SomeWithLen"></a>SomeWithLen
todo:
### <a name="NotSome"></a>NotSome
todo:
### <a name="SomeStr"></a>SomeStr
todo:

## Same API
> :warning: **Same** should only be used with the `expect(...).to_be(...)` syntax!


## Exceptions:
| name  | description |
|--- |--- |
| | |