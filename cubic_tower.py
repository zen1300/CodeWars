BLOCKS = 5
VOL = 0

while BLOCKS > 0:
    VOL += BLOCKS**3
    print(VOL)
    BLOCKS -= 1

print(VOL)

while VOL > 0:
    BLOCKS += 1
    VOL -= BLOCKS**3
    print(VOL)

print(BLOCKS)