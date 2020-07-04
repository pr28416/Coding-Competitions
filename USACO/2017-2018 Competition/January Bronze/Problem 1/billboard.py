class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.dl = (x1, y1)
        self.dr = (x2, y1)
        self.ul = (x1, y2)
        self.ur = (x2, y2)
    
    # def __str__(self):
    #     return "{} {} {} {}".format(self.dl, self.dr, self.ul, self.ur)

undesired, placebo = None, None
with open("billboard.in", "r") as f:
    temp = [int(i) for i in f.readline().split(" ")]
    undesired = Rectangle(*temp)
    temp = [int(i) for i in f.readline().split(" ")]
    placebo = Rectangle(*temp)
    # print("Undesired", undesired)
    # print("Placebo", placebo)

area = (undesired.dr[0] - undesired.dl[0]) * (undesired.ul[1] - undesired.dl[1])

# Remove hidden points
# dl
if undesired.dl[0] >= placebo.dl[0] and undesired.dl[1] >= placebo.dl[1]:
    undesired.dl = None
# dr
if undesired.dr[0] <= placebo.dr[0] and undesired.dr[1] >= placebo.dr[1]:
    undesired.dr = None
# ul
if undesired.ul[0] >= placebo.ul[0] and undesired.ul[1] <= placebo.ul[1]:
    undesired.ul = None
# ur
if undesired.ur[0] <= placebo.ur[0] and undesired.ur[1] <= placebo.ur[1]:
    undesired.ur = None

# print(undesired)
# Count # of Nones
noneCount = (1 if undesired.dl is None else 0) + (1 if undesired.dr is None else 0) + (1 if undesired.ul is None else 0) + (1 if undesired.ur is None else 0)

if noneCount == 1:
    pass # area stays the same
elif noneCount == 4:
    area = 0

# The following can be simplified without if statements:
# Find intersection of points using max() and min()
else: # noneCount = 2
    # Get axis
    if undesired.dl is None:
        if undesired.dr is None:
            area = (undesired.ur[0] - undesired.ul[0]) * (undesired.ul[1] - placebo.ul[1])
        else: # ul
            area = (undesired.ur[0] - placebo.ur[0]) * (undesired.ur[1] - undesired.dr[1])
    elif undesired.ur is None:
        if undesired.dr is None:
            area = (placebo.ul[0] - undesired.ul[0]) * (undesired.ul[1] - undesired.dl[1])
        else: # ul
            area = (undesired.dr[0] - undesired.dl[0]) * (placebo.dr[1] - undesired.dr[1])
    
with open("billboard.out", "w") as f:
    f.write("%s\n" % area)