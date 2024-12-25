# Info:

Image created by create-and-display-img.py

```c
Filename: '/Users/tdiprima/Documents/MATLAB/2021/images/my.png'
FileModDate: '01-Feb-2022 09:58:27'

FileSize: 74
  Format: 'png'
   Width: 1
  Height: 100

BitDepth: 24

                 ColorType: 'truecolor'
           FormatSignature: [137 80 78 71 13 10 26 10]
             InterlaceType: 'none'
              Transparency: 'none'
```

# Size:

```c
SIZE:
rows: 100
columns: 1
num channels: 3

dimensions
100     1     3
```

# At what index is the non-zero value?

```c
NONZERO ELEMENT:
row: 83
pixel index: 3
value: 240
```

# Five by Five ;)

five-by-five.png

According to Matlab:

```c
SIZE:
rows: 5
columns: 5
num channels: 3

NONZERO ELEMENT:
row: 3
column: 13
value: 174
```

==**matlab array index starts at 1**==

A single blue pixel, in the center.

```
val(:,:,3) =

     0     0     0     0     0
     0     0     0     0     0
     0     0   174     0     0
     0     0     0     0     0
     0     0     0     0     0
```

Dead center: row 3, column 13

```
 1  2  3  4  5
10  9  8  7  6
11 12 13 14 15
20 19 18 17 16
21 22 23 24 25
```
