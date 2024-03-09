"""Top-level package for Big Planner.


Recommended design steps:

1. [ ] define the use cases (logic/*.py)
    1.1 [ ] write down main use cases (docs/use_cases.md)
    1.2 [ ] write down some test cases (tests/test__xxx.py), but not coding yet, to detect main concerns (TDD)
    1.3 [ ] use `beacons.py` as an example or reference

2. [ ] define the data models needed to support such logic (models/*.py) 
3. [ ] define the primary abstract ports to allow incoming interaction (ports/*.py)
4. [ ] implement primary ports: cli and/or rest api
    4.1 [ ] use make docker-run to have a instant feedback when code is broken from API perspective
    4.2 [ ] use make ptw to have a instant feedback when code is broken from CLI perspective

5. [ ] define the secondary abstract ports to allow external interaction (ports/*.py)
6. [ ] implement secondary ports (i.e. storage/*.py)
7. [ ] define test cases (tests/*.py) and get main
8. [ ] implement automatic test cases

"""

__author__ = """Asterio Gonzalez"""
__email__ = "asterio.gonzalez@gmail.com"
__version__ = "0.1.0"
