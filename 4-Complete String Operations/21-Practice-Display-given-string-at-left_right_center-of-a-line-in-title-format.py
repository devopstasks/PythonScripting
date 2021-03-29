'''
=============
center
ljust
rjust
Terminal size in windows: "mode"
Terminal size in linux: "tput"
=============
'''
import os
terminal_width=os.get_terminal_size().columns
print(terminal_width)
display_str="python scripting"
print(display_str.center(terminal_width))
print(display_str.ljust(terminal_width))
print(display_str.rjust(terminal_width))
