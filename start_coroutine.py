from pybricks.tools import wait
from pybricks.tools import multitask, run_task
from wall import wall
from drive import drive

async def wait_and_up_to():
    await wait(100)
    await wall.upTo(50)

async def do():
    await multitask(drive.turn_to_and_drive(50, 100), wait_and_up_to())

run_task(do()) 

# async def drive():
#     await wait(100)
#     await c



wait(3000)

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
