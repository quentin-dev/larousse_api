## Larousse API

### Installation
* `pip install larousse-api-sunbro`

### Usage
```python3
from larousse_api import larousse

# Print the array containing all defintions of "Fromage"
print(larousse.get_definitions("Fromage"))
```

### Why ?
Because the Larousse website doesn't supply an api to look up definitions :(

### How ?
By making a request to the larousse website and parsing the result using the following modules. 

* python3
* requests
* re
* BeautifulSoup

### Possible improvements
* Suggest words if the word is misspelled
