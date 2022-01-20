# Matrix Generator

## How to run:
Copy and run either _.py_ script in a Python IDE or download the _.zip_ and run the executable file.

Enter a value for height, width and opacity (how densely the pattern should generate).

Note: _For coloured outputs, run the "-coloured.py" script an IDE._

## Design
I am part of a team called Neo and I wanted to create a new console output logo for whenever we ran code builds, using this image as my inspiration related to our team name:

![wallpaper-mania com_High_resolution_wallpaper_background_ID_77701857800](https://user-images.githubusercontent.com/95386143/150292157-dceec17e-c6c3-4150-82ad-b53757b559c1.jpg)

By using relatively little syntax, a _random_ import and some string colour format codes, it creates something slightly similar:

<img width="1345" alt="Screenshot 2022-01-19 at 22 28 21" src="https://user-images.githubusercontent.com/95386143/150292516-8b01ded9-e200-498b-a903-b1930c67a235.png">

Using standard and high intensity blue and cyan colours, I tried to mimick the varying brightness of each streak:
```
"\033[0;94m" // High intensity blue
"\033[0;96m" // High intensity cyan
"\033[0;34m" // Blue
"\033[0;36m" // Cyan
```

Whereas the bold formatting tries to replicate the 3D effect of some streaks appearing closer than others:
```
"\033[1;94m" // Bold high intensity blue
"\033[1;96m" // Bold high intensity cyan
"\033[1;34m" // Bold blue
"\033[1;36m" // Bold cyan
```

I then added the option for a second set of colour options of green and cyan, to try to match the actual matrix colours:

<img width="1345" alt="Screenshot 2022-01-19 at 22 29 29" src="https://user-images.githubusercontent.com/95386143/150293151-232a3834-3f3f-4a12-9dc8-91b8740967bc.png">

It still looks very flat and isn't as impressive as the edited original, with fading colours, blur effects or even looking close to the real matrix patterns in the films, but it served it's purpose for me.

After adding my custom _banner.txt_ as a variable and using a little extra syntax:

```
if logoIncluded:
   if height>12 and width>40:
      start=round(width/2)-18
      end=round(width/2)+17
      index=0
      for line in neoLogo:
         row=toPrint.pop(index)
         toPrint.insert(index,row[0:start]+line+row[end:width])
         index+=1
```

It allowed me to auto generate this at the click of a button:

```
0001011100000000111001101011110101001 ___      _____________    ____    01110000111100011110100110100110011101
111000101 10001000111 111000101111000 `MM\     `M'`MMMMMMMMM   6MMMMb   00011 1111 111111 1 110011 1110000 100
100   111 01111 11010 0 10110000 0000  MMM\     M  MM      \  8P    Y8  01001 1100 1 0110 1 0110 1  1 10 0 000
01    011  0111 11001   100 0010 1011  M\MM\    M  MM        6M      Mb 001 0  000   1000 1 0001    1 00 0   1
11    010   110  0011   010 10 1 01 0  M \MM\   M  MM        MM      MM  01 1  10    00 0    100    0 00 0   0
0     00    101  000    11  00 0 0  0  M  \MM\  M  MMMMMMM   MM      MM  1  0  00    10 0    00     1 01 1   1
1      0     01   01     1  11   1  1  M   \MM\ M  MM        MM      MM  0  1  0     1  0    11        0 0   0
       1     10   1      1  1       0  M    \MM\M  MM        MM      MM  1     0     1  0     1        0 1   0
       1     10   0         0       0  M     \MMM  MM        YM      M9        0     0        1        0      
              1             0          M      \MM  MM      /  8b    d8               0        0               
              0                       _M_      \M _MMMMMMMMM   YMMMM9                1                        
```
