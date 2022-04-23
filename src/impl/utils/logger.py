from datetime import datetime as dt


class Logger:
    m_prefix: str

    def __init__(self, prefix: str = __name__):
        self.m_prefix = prefix

    def info(self, *args):
        print(f"[{self.m_prefix}] {dt.now()} INFO\t", *args)
