# for x in range(6):
#     print(f'{x:4} {x**2:4} {x**3:4}')
picWidth = 27
hangmanPicListEnd = [
    f'{"      _____________ ".rjust(picWidth)}', #0
    f'{"     |  _________  |".rjust(picWidth)}', #1
    f'{"     [ ]         | |".rjust(picWidth)}', #2
    f'{"     [ ]         | |".rjust(picWidth)}', #3
    f'{"     [_]         | |".rjust(picWidth)}', #4
    f'{"    (X_X)        | |".rjust(picWidth)}', #5
    f'{" ____| |____     | |".rjust(picWidth)}', #6
    f'{"| _       _ |    | |".rjust(picWidth)}', #7
    f'{"|| |     | ||    | |".rjust(picWidth)}', #8
    f'{"|| |     | ||    | |".rjust(picWidth)}', #9
    f'{"|| |  _  | ||    | |".rjust(picWidth)}', #10
    f'{"   | | | |       | |".rjust(picWidth)}', #11
    f'{"   | | | |       | |".rjust(picWidth)}', #12
    f'{"   | | | |       | |".rjust(picWidth)}', #13
    f'{"   |_| |_|       | |".rjust(picWidth)}', #14
    f'{"                 | |".rjust(picWidth)}', #15
    f'{"_________________|_|".rjust(picWidth, "_")}' #16
]

hangmanPicList = [
    f'{"      _____________ ".rjust(picWidth)}', #0
    f'{"     |  _________  |".rjust(picWidth)}', #1
    f'{"     [ ]         | |".rjust(picWidth)}', #2
    f'{"     [ ]         | |".rjust(picWidth)}', #3
    f'{"     [_]         | |".rjust(picWidth)}', #4
    f'{"                 | |".rjust(picWidth)}', #5
    f'{"                 | |".rjust(picWidth)}', #6
    f'{"                 | |".rjust(picWidth)}', #7
    f'{"                 | |".rjust(picWidth)}', #8
    f'{"                 | |".rjust(picWidth)}', #9
    f'{"                 | |".rjust(picWidth)}', #10
    f'{"                 | |".rjust(picWidth)}', #11
    f'{"                 | |".rjust(picWidth)}', #12
    f'{"                 | |".rjust(picWidth)}', #13
    f'{"                 | |".rjust(picWidth)}', #14
    f'{"                 | |".rjust(picWidth)}', #15
    f'{"_________________|_|".rjust(picWidth, "_")}' #16
]

if lives == ""



for x in range(len(hangmanPicList)):
    print(hangmanPicList[x])