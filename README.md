# arithmanic
A tool for working on mental arithmetic


```bash
usage: arithmanic.py [-h] [--range INT INT] [--range2 INT INT]
                     [--op OPERATION] [--shuffle]

Run main.

optional arguments:
  -h, --help            show this help message and exit
  --range INT INT, -r INT INT
                        Lowest and highest operand values
  --range2 INT INT, -r2 INT INT
                        Lowest and highest other operand values
  --op OPERATION, -o OPERATION
                        Arithmetic op (+ - * /)
  --shuffle, -s
```
```
$ python arithmanic.py
 4 -  3 = 1
 5 - 12 = -7
10 /  7 = uhhhh
!!! NO NO NO NO NO !!!
10 /  7 = 1.3424
!!! NO NO NO NO NO !!!
    1.4285714285714286
 3 +  4 = 7
11 -  3 = 8
11 /  1 = 11
 6 *  6 = 36
 4 -  0 = 4
12 - 11 = 1
 6 -  9 = -3
 7 -  5 = 2
 8 *  3 = 24
 7 /  7 = 1
 5 -  8 = -3
 6 +  2 = ^D
$
```
