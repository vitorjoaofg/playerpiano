import sys
import os.path

outfile = None

def write(s):
    """write s to stdout"""
    s = s.replace('\n', '\r\n')
    outfile.write(s)
    outfile.flush()

def make_target(options):
    global outfile
    if os.path.exists(options.fifo):
        os.unlink(options.fifo)
    os.mkfifo(options.fifo)
    outfile = open(options.fifo, 'a', 0)
    write(chr(27)+"[2J") # clear the screen
    write(chr(27)+"[H")
    return write
    
def free_target():
    outfile.close()
    os.unlink(outfile.name)
