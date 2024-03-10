#!/usr/bin/env python3

import datetime, time, traceback, multiprocessing

import sys

utils_pgdebug  = 0
utils_locktout = 7

locklevel = {}

def set_pgdebug(level):
    global utils_pgdebug
    utils_pgdebug = level

# Class for ensuring that all file operations are atomic, treat
# initialization like a standard call to 'open' that happens to be atomic.
# This file opener *must* be used in a "with" block.
class AtomicOpen:
    # Open the file with arguments provided by user. Then acquire
    # a lock on that file object (WARNING: Advisory locking).
    def __init__(self, path, *args, **kwargs):
        # Open the file and acquire a lock on the file before operating
        self.file = open(path,*args, **kwargs)
        # Lock the opened file
        lock_file(self.file)

    # Return the opened file object (knowing a lock has been obtained).
    def __enter__(self, *args, **kwargs): return self.file

    # Unlock the file and close the file object.
    def __exit__(self, exc_type=None, exc_value=None, traceback=None):
        # Flush to make sure all buffered contents are written to file.
        self.file.flush()
        os.fsync(self.file.fileno())
        # Release the lock on the file.
        unlock_file(self.file)
        self.file.close()
        # Handle exceptions that may have come up during execution, by
        # default any exceptions are raised to the user.
        if (exc_type != None): return False
        else:                  return True

try:
    # Posix based file locking (Linux, Ubuntu, MacOS, etc.)
    #   Only allows locking on writable files, might cause
    #   strange results for reading.
    import fcntl, os
    def lock_file(f):
        if f.writable(): fcntl.lockf(f, fcntl.LOCK_EX)
    def unlock_file(f):
        if f.writable(): fcntl.lockf(f, fcntl.LOCK_UN)
except ModuleNotFoundError:
    # Windows file locking
    import msvcrt, os
    def file_size(f):
        return os.path.getsize( os.path.realpath(f.name) )
    def lock_file(f):
        msvcrt.locking(f.fileno(), msvcrt.LK_RLCK, file_size(f))
    def unlock_file(f):
        msvcrt.locking(f.fileno(), msvcrt.LK_UNLCK, file_size(f))

fhand = 0

def xlockfile(fname):
    global fhand
    fhand = open(fname, 'w')
    lock_file(fhand)

def xunlockfile(fname):
    global fhand
    unlock_file(fhand)
    fhand.close()
    os.unlink(fname)

def put_exception(xstr):

    cumm = xstr + " "
    a,b,c = sys.exc_info()
    if a != None:
        cumm += str(a) + " " + str(b) + "\n"
        try:
            #cumm += str(traceback.format_tb(c, 10))
            ttt = traceback.extract_tb(c)
            for aa in ttt:
                cumm += "File: " + os.path.basename(aa[0]) + \
                        "  Line: " + str(aa[1]) + "\n" +  \
                        "    Context: " + aa[2] + " -> " + aa[3] + "\n"
        except:
            print( "Could not print trace stack. ", sys.exc_info())

    print(cumm)

# ------------------------------------------------------------------------
# Get date out of UUID

def uuid2date(uuu):

    UUID_EPOCH = 0x01b21dd213814000
    dd = datetime.datetime.fromtimestamp(\
                    (uuu.time - UUID_EPOCH)*100/1e9)
    #print(dd.timestamp())
    return dd

def uuid2timestamp(uuu):

    UUID_EPOCH = 0x01b21dd213814000
    dd = datetime.datetime.fromtimestamp(\
                    (uuu.time - UUID_EPOCH)*100/1e9)
    return dd.timestamp()

def pad(strx, lenx=8):
    ttt = len(strx)
    if ttt >= lenx:
        return strx
    padx = " " * (lenx-ttt)
    return strx + padx

def decode_data(self, encoded):

    try:
        bbb = self.packer.decode_data(encoded)
    except:
        print("Cannot decode", sys.exc_info())
        bbb = ""
    return bbb

# ------------------------------------------------------------------------
# Simple file handle system based locking system.
# Linux does not like file existance locks

gl_fpx = None

def dellock(lockname):

    ''' Lock removal;
        Test for stale lock;
    '''

    if utils_pgdebug > 1:
        print("Dellock", lockname)

    global gl_fpx
    if not gl_fpx:
        try:
            gl_fpx = open(lockname, "wb+", O_NONBLOCK)
        except:
            if utils_pgdebug > 1:
                #print("Del lock failed", sys.exc_info())
                put_exception("Del Lock")

    fcntl.lockf(gl_fpx, fcntl.LOCK_UN)


def waitlock(lockname):

    ''' Wait for lock file to become available. '''

    if utils_pgdebug > 1:
        print("Waitlock", lockname)

    global gl_fpx
    if not gl_fpx:
        try:
            gl_fpx = open(lockname, "wb+")
        except:
            if utils_pgdebug > 1:
                #print("Create lock failed", sys.exc_info())
                put_exception("Del Lock")

    cnt = 0
    while True:
        try:
            #print("flock", fcntl.lockf(gl_fpx, fcntl.F_GETLK))
            #print(os.lockf(gl_fpx, os.F_TEST, 0))
            #ttt = time.time()
            buff = gl_fpx.read()
            gl_fpx.seek(0, os.SEEK_SET)
            gl_fpx.write(buff)
            #print("process read/write %.3f" % ((time.time() - ttt) * 1000), buff )
            break;
        except:
            print("waiting", sys.exc_info())
            pass

        cnt += 1
        time.sleep(1)

        if cnt > utils_locktout :
            # Taking too long; break in
            if utils_pgdebug > 1:
                print("Lock held too long pid =", os.getpid(), cnt, lockname)
            dellock(lockname)
            break

    # Finally, create lock
    try:
        #gl_fpx.write(str(os.getpid()).encode())
        fcntl.lockf(gl_fpx, fcntl.LOCK_EX)
        #if lockname not in locklevel:
        #    locklevel[lockname] = 0
        #locklevel[lockname] += 1
    except:
        print("Cannot create lock", lockname, sys.exc_info())

# break in if not this process
#try:
#    fcntl.lockf(fpx, fcntl.LOCK_EX)
#    buff = fpx.read()
#    pid = int(buff)
#    fpx.close()
#
#    #print(os.getpid())
#    if os.getpid() != pid:
#        dellock(lockname)
#except:
#    print("Exception in lock test", put_exception("Del Lock"))

def truncs(strx, num = 8):

    ''' Truncate a string for printing nicely. Add '..' if truncated'''

    if len(strx) > num:
        strx = strx[:num] + b".."
    return strx

# EOF