import sys

# sys.path.append('i:\Xite development\JARVIS 2.0\Brain')
from Brain.nuralnetwork import TasksExecutor

# sys.path.append('i:\Xite development\JARVIS 2.0\Automation')
from Automation.open import OpenExe

# sys.path.append('i:\Xite development\JARVIS 2.0\Features')
from Features.play import play
from Brain.task import time
from Brain.task import Date, Day


def taskexe(Query):
    if Query == "":
        pass
    else:
        task = str(Query).lower()
        tasknew = str(Query).lower()
        ReturnData = TasksExecutor(task)

    if ReturnData is not None:
        if "None" in ReturnData:
            pass
        elif "open" in ReturnData:
            Value = OpenExe(tasknew)
            return Value
        elif "music" in ReturnData:
            Value = play(tasknew)
            return Value
        elif "time" in ReturnData:
            Value = time()
            return Value
        elif "date" in ReturnData:
            Value = Date()
            return Value
        elif "day" in ReturnData:
            Value = Day()
            return Value
