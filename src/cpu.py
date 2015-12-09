import multiprocessing
import subprocess


class CPU:
    def __init__(self):
        self.cores = multiprocessing.cpu_count()

        status, self.name = subprocess.getstatusoutput('grep "model name" /proc/cpuinfo -m 1')
        self.name = self.name[self.name.find(":") + 1:].strip() if status == 0 else "general"
        while self.name.find('  ') > -1:
            self.name = self.name.replace('  ', ' ')

        status, self.flags = subprocess.getstatusoutput('cpuinfo2cpuflags-x86')
        self.flags = self.flags[self.flags.find("\"") + 1: -1] if status == 0 else "mmx sse sse2 sse3 ssse3"

    def __str__(self):
        return "name : {}\n" \
               "cores: {}\n" \
               "flags: {}".format(self.name, self.cores, self.flags)

    def get_num_cores(self):
        return self.cores

    def get_flags(self):
        return self.flags
