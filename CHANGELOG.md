# Directions

- h3 heading
- X.X.X - YYYY-MM-DD

### 1.7.0.alpha1 - 2020-08-17

- Added `UJSONRenderer.translate_func` attribute for translating data into a `ujson`
serializable object.

### 1.6.0 - 2020-03-10

- Add `ujson>=2` compatibility

### 1.5.1 - 2020-03-09

- Pin `ujson<2`

### 1.5.0 - 2020-02-13

- Dropped support for `python<3.6`
- Type hinting
- `Django3` testing
- Added `drf_ujson.__version__`

### 1.4.1 - 2019-11-05

- Fixed repo url in `setup.py`

### 1.4.0 - 2019-11-05

- Drop `py27` support

### 1.3.1 - 2019-11-05

- Don't include `tests` module in build

### 1.3.0 - 2019-11-05

- Fix DRF4 import path
- Add attributes to `UJSONParser` to pass values to `ujson.loads`
- Add attributes to `UJSONRenderer` to pass values to `ujson.dumps`

### 1.2.1 - 2019-11-04

- Pinned `djangorestframework<3.10`
- Added `MANIFEST.in`
    - included `README.md`
    - included `LICENSE`
