from ctypes import CDLL, c_int, c_void_p, c_longlong, c_bool, POINTER, byref
import enum
import time

class Dimension(enum.IntEnum):
    X = 0
    Y = 1
    Z = 2
    W = 3
    # future
    Y1 = X
    Y2 = Y
    Y3 = Z
    # future
    Y4 = W
    MAX = Z
    COUNT = MAX + 1

class Key(enum.Structure):
    _fields_ = [("key", c_int), ("apply", c_int)]

class MoveCursor(enum.Structure):
    _fields_ = [("position", c_longlong * Dimension.COUNT.value), ("justify_flag", c_bool)]

libmacro = CDLL("./libmacro.so")
libmacro.mcr_allocate.restype = c_void_p
libmacro.mcr_deallocate.argtypes = [c_void_p]
libmacro.mcr_MoveCursor_send_member.argtypes = [POINTER(MoveCursor), c_void_p]

context = libmacro.mcr_allocate()
try:
    if context:
        print("Initializing...")
        time.sleep(1)
        print("Init complete")
        mc = MoveCursor()
        mc.justify_flag = True
        mc.position[Dimension.X] = 1000
        print("Move X returns: ", libmacro.mcr_MoveCursor_send_member(byref(mc), context))
    else:
        print("\nError: Libmacro context is not available.")
except KeyboardInterrupt:
    print("\nExiting by KeyboardInterrupt.")
    exit()

except Exception as e:
    print("Error:", e)

finally:
    print("End program safe cleanup.")
    if context:
        libmacro.mcr_deallocate(context)
