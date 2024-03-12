from setuptools import setup

LICENSE = '''MIT License

Copyright (c) 2024 MoYeRanQianZhi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

README = '''## PyRandPassword

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
'''

setup(
    name='PyRandPassword',
    version='0.1.0',
    packages=['PyRandPassword'],
    url='https://github.com/MoYeRanqianzhi/PyRandPassword',
    license=LICENSE,
    author='MoYeRanQianZhi',
    author_email='moyeranqianzhi@gmail.com',
    description='To Make Random Password',
    long_description=README,
    long_description_content_type="text/markdown",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    python_requires='>=3.6.0',
    requires=[
        'numpy'
    ],
)
