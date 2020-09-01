#!/usr/bin/gdb -x
# This script is a sniffer for the IOU's internal MD5 "body" function.
#
# Based on https://github.com/crossbowerbt/GDB-Python-Utils
#
# Tested on GDB 7.7 running on Ubuntu 14.04 LTS

import gdb
import binascii


def usage():
    print("Usage:")
    print("\tsudo ./md5-sniffer -p <pid>")
    gdb.execute('quit')


class SnifferBreakpoint(gdb.Breakpoint):

    # Initialize the breakpoint
    def __init__(self):
        super(SnifferBreakpoint, self).__init__('*0x099a54b2')

    # Called when the breakpoint is hit
    def stop(self):
        # get the string address, from the second arguments of the function
        address = gdb.parse_and_eval('$ecx')

        # get the string
        data = binascii.hexlify(gdb.inferiors()[0].read_memory(address, 64))
        # data = bytearray(gdb.inferiors()[0].read_memory(address, 64))
        print(data)

        # return False to continue the execution of the program
        return False


# GDB setup
gdb.execute("set print repeats unlimited")
gdb.execute("set print elements unlimited")
gdb.execute("set pagination off")

# generate sniffer breakpoint
SnifferBreakpoint()

# run and sniff...
gdb.execute('continue')

# gdb.execute('detach')
# gdb.execute('quit')
