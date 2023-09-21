# JSONAPI

A Python package for custom JSON encoding and decoding.

## Installation

```bash
pip install jsonapi
```

## Usage

### Custom JSON Encoding and Decoding

```python
import json
from jsonapi.jsonapi import dumps, loads

# Sample data
my_data = {
    "hey": complex(1, 2),
    "there": list(range(1, 10, 3)), 73: False,
}

# JSON serialization with custom encoder
json_data = dumps(my_data)

# JSON deserialization with custom decoder
decoded_data = loads(json_data)

print("Serialized data:\n", json_data)
print("Deserialized data:\n", decoded_data)

```
