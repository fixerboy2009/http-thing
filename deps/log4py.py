count = 0
class log4py:
    def __init__(self):
        pass
    def log(self, msg: str):
        global count
        count += 1
        print(f"[ LOG4PY LOGID: {str(count)} ]: {str(msg)}")
