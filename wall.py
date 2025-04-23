import umath
from pybricks.tools import wait
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port, Direction, Color

from hub import beepHigh, beepLow

# Aus dem Winkel in Grad muss die Strecke berechnet werden.
# Der Radius des Rades ist 7.5 mm.
_UP_DOWN_RADIUS = 7.95
_UP_DOWN_ANGLE2DISTANCE = 2.0*umath.pi*_UP_DOWN_RADIUS/360    # mm/deg 
_UP_DOWN_SPEED = 1 / _UP_DOWN_ANGLE2DISTANCE # deg/mm

_LEFT_RIGHT_RADIUS:float = 10.0
_LEFT_RIGHT_ANGLE2DISTANCE = 2.0*umath.pi*_LEFT_RIGHT_RADIUS/360    # mm/deg 
_LEFT_RIGHT_SPEED = 1/_LEFT_RIGHT_ANGLE2DISTANCE # deg/mm

_WALL_HORIZONTAL_BRIGHTNESS_BOUNDARY_ORANGE_WHITE = 70
_WALL_HORIZONTAL_BRIGHTNESS_BOUNDARY_BLACK_ORANGE = 15

class Wall:

    def __init__(self):
        self.motor_horizontal = Motor(Port.C, Direction.COUNTERCLOCKWISE)
        self.motor_vertical = Motor(Port.D, Direction.COUNTERCLOCKWISE)
        self.left_right_speed_default = 50         # 50 mm/s
        self.up_down_speed_default = 40               # 40 mm/s

        self.color_sensor = ColorSensor(Port.E)

        self.reset_pos()

    def get_left_right_angle_Speed_or_default(self, speed: float)->float:
        return _LEFT_RIGHT_SPEED*(speed if speed is not None else self.left_right_speed_default)
    
    def get_up_down_angle_speed_or_default(self, speed: float)->float:
        return _UP_DOWN_SPEED*(speed if speed is not None else self.up_down_speed_default)

    def reset_pos(self)->None:
        self.motor_vertical.reset_angle(0)
        self.motor_horizontal.reset_angle(0)

    def up(self, distance:float, speed: float=None, wait:bool=True):
        """Move wall up a given distance.

        Args:
            distance (float): distance to move up in mm
            speed (float, optional): Speed of the wall in mm/s. Defaults to default speed.
            wait (bool, optional): Wait for the maneuver to complete before continuing with the rest of the program. Defaults to True.
        """
        return self.motor_vertical.run_angle(self.get_up_down_angle_speed_or_default(speed), distance/_UP_DOWN_ANGLE2DISTANCE, wait=wait)

    def upTo(self, offset:float, speed: float=None, wait:bool=True):
        """Move wall up to a given offset.

        Args:
            offset (float): Offset in mm to move up to.
            speed (float, optional): Speed of the wall in mm/s. Defaults to None.
            wait (bool, optional): Wait for the maneuver to complete before continuing with the rest of the program. Defaults to True.
        """
        return self.motor_vertical.run_target(self.get_up_down_angle_speed_or_default(speed), offset/_UP_DOWN_ANGLE2DISTANCE, wait=wait)

    def down(self, distance: float, speed:float=None, wait:bool=True):
        """Move wall down a given distance.

        Args:
            distance (float): distance to move down in mm
            speed (float, optional): Speed of the wall in mm/s. Defaults to None.
            wait (bool, optional): Wait for the maneuver to complete before continuing with the rest of the program. Defaults to True.
        """
        return self.motor_vertical.run_angle(-self.get_up_down_angle_speed_or_default(speed), distance/_UP_DOWN_ANGLE2DISTANCE, wait=wait)

    def left(self, distance:float=None, speed: float=None, wait:bool=True):
        """Move wall a given distance to the left.

        Args:
            distance (float, optional): Distance in mm. Defaults to endless move.
            speed (float, optional): Speed of the wall in mm/s. Defaults to default speed.
            wait (bool, optional): Wait for the maneuver to complete before continuing with the rest of the program. Defaults to True.
        """
        if distance is not None:
            return self.motor_horizontal.run_angle(self.get_left_right_angle_Speed_or_default(speed), distance/_LEFT_RIGHT_ANGLE2DISTANCE, wait=wait)
        else:
            return self.motor_horizontal.run(self.get_left_right_angle_Speed_or_default(speed))

    def leftTo(self, offset:float, speed: float=None, wait:bool=True):
        """Move wall left to a given offset.

        Args:
            offset (float): Offset in mm to move left to.
            speed (float, optional): Speed of the wall in mm/s. Defaults to None.
            wait (bool, optional): Wait for the maneuver to complete before continuing with the rest of the program. Defaults to True.
        """
        return self.motor_horizontal.run_target(self.get_left_right_angle_Speed_or_default(speed), offset/_LEFT_RIGHT_ANGLE2DISTANCE, wait=wait)

    def right(self, distance:float=None, speed: float=None, wait:bool=True):
        if distance is not None:
            return self.motor_horizontal.run_angle(-self.get_left_right_angle_Speed_or_default(speed), distance/_LEFT_RIGHT_ANGLE2DISTANCE, wait=wait)
        else:
            return self.motor_horizontal.run(-self.get_left_right_angle_Speed_or_default(speed))

    def rightTo(self, distance:float, speed: float=None, wait:bool=True):
        return self.leftTo(-distance, speed=speed, wait=wait)

    def stop(self)->None:
        self.motor_vertical.stop()
        self.motor_horizontal.stop()

    def downToStop(self, speed:float=None)->None:
        self.motor_vertical.run(-self.get_up_down_angle_speed_or_default(speed))
        
        while not self.motor_vertical.stalled():
            wait(10)
        self.stop()

    def center_reflection(self):
        return self.color_sensor.reflection()

    def center_color(self):
        reflection = self.center_reflection()
        if reflection>_WALL_HORIZONTAL_BRIGHTNESS_BOUNDARY_ORANGE_WHITE:
            return Color.WHITE
        elif reflection>_WALL_HORIZONTAL_BRIGHTNESS_BOUNDARY_BLACK_ORANGE:
            return Color.ORANGE
        else:
            return Color.BLACK

    def center_color_coding(self, reflection: int):
        if reflection==Color.WHITE:
            return "WHITE"
        elif reflection==Color.ORANGE:
            return "ORANGE"
        else:
            return "BLACK"


    def center(self, speed:float = None)->None:
        beepHigh()
        DEBUG=True

        if DEBUG:
            print("Start: wand_horizontal_ausrichten_neu")
            print(self.color_sensor.reflection())

        # Ausrichtung über den Reflexionssensor bestimmen
        initial_color = self.center_color()
        if DEBUG:
            print("Startfarbe: ", self.center_color_coding(initial_color))
        
        if initial_color == Color.ORANGE:
            self.right(speed=speed)
        elif initial_color == Color.BLACK:
            self.left(speed=speed)
        else:
            # Ist die Wand ein wenig verschoben, so dass die Hälfte weiss, die andere Hälfte Orange ist, wird trotzdem schon ein Reflexionswert von 99 zurückgegeben.
            # Deshalb die Wand zuerst verschieben.
            self.right(speed)
            self.left(speed)
            initial_color = Color.BLACK
                
        color = initial_color
        while color != Color.WHITE:
            color = self.center_color()
            wait(5)
            if DEBUG:
                print("Reflection:", self.center_color_coding(color))
        if initial_color == Color.ORANGE:
            # Auf der orangen Seite liefert die Reflexion bereits eine Reflexionswerte für Weiss, wenn die Hälfte Orange, die andere Hälfte Weiss ist. 
            # Deshalb einfach ein wenig weiterlaufen lassen.
            wait(50)
        elif initial_color == Color.BLACK:
            wait(35)
        self.stop()
        beepLow()
        if DEBUG:
            print("Ende: wand_horizontal_ausrichten_neu")

wall = Wall()
