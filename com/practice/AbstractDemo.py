from abc import ABCMeta,abstractmethod
#2.7
import abc
#print dir(abc)
class AbcLogProcess(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def process(self):
        pass

    def makeDir(self,path):
        print "Create HDFS directory " + path

    def makeDir(self, path, mode):
        print('def makeDir(self,path):')



class WindowsLogs(AbcLogProcess):
    def myFunc(self):
        print "this is my func"

    def process(self):
        print 'Windows log prccess'



wl = WindowsLogs()
wl.myFunc()
wl.process()
wl.makeDir("abc")