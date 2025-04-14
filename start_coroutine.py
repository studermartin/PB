from pybricks.tools import wait
from pybricks.tools import multitask, run_task
from wall import wall


print("Move wall up/down and right/left at the same time", None)
wall.downToStop()
wall.center()
wall.reset_pos()

wall.upTo(100, wait=False)
wall.leftTo(50, wait=False)

wait(2000)

wall.upTo(0, wait=False)
wall.leftTo(0, wait=False)

wait(3000)

print("Move wall while driving.")
