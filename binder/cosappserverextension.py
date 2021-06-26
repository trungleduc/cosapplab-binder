from subprocess import Popen


def load_jupyter_server_extension(nbapp):
    """Start CoSApp Lab server"""
    Popen(["cosapp", "load", "-a"])
