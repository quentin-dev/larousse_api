## Larousse API

### Installation
* `pip install larousse-api-sunbro`

### Usage
`from larousse_api import larousse
print(larousse.get_definitions("Fromage")`

### Why ?
Because the Larousse website doesn't supply an api to look up definitions :(

### How ?
* python3
* requests
* re
* BeautifulSoup

### Possible improvements
* Suggest words if the word is misspelled
