from threading import Semaphore

class H2O:
    def __init__(self):
        self.h_sem = Semaphore(2)      # allow 2 hydrogens at a time
        self.o_sem = Semaphore(1)      # allow 1 oxygen at a time
        self.reset_sem = Semaphore(0)  # oxygen waits for both H's here

    def hydrogen(self, releaseHydrogen):
        self.h_sem.acquire()           # wait if 2 hydrogens already in
        releaseHydrogen()
        self.reset_sem.release()       # signal oxygen that one H is done

    def oxygen(self, releaseOxygen):
        self.o_sem.acquire()           # wait if another oxygen is in
        releaseOxygen()
        self.reset_sem.acquire()       # wait for H1
        self.reset_sem.acquire()       # wait for H2
        self.h_sem.release()           # unblock next 2 hydrogens
        self.h_sem.release()
        self.o_sem.release()           # unblock next oxygen