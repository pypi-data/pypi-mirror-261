## PyRandPassword

---

### example

```python
from PyRandPassword import STP

print(STP().password)
```

```python
from PyRandPassword import RandomPassword
from PyRandPassword.constants import __chars__

rp = RandomPassword(words=__chars__)
rp.random(size=6)
rp.random(size=12)
print(rp.password)
```