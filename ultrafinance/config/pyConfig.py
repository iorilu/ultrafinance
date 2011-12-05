'''
Created on Nov 30, 2010

@author: ppa
'''
import ConfigParser
from os import path
from ultrafinance.lib.errors import UfException, Errors

import logging
LOG = logging.getLogger(__name__)

class PyConfig(object):
    ''' class that handles configuration '''
    def __init__(self):
        ''' Constructor '''
        self.__dir = None
        self.__parser = None
        self.setDir(path.join(path.dirname(path.dirname(path.dirname(path.abspath(__file__))) ), 'conf') )

    def setDir(self, dirPath):
        ''' set dir of configuration '''
        self.__dir = dirPath

    def setSource(self, fileName):
        ''' set source file name'''
        fullPath = path.join(self.__dir, fileName)

        if not path.exists(fullPath):
            msg = "config file doesn't exist: %s" % fullPath
            LOG.error(msg)
            raise UfException(Errors.FILE_NOT_EXIST, msg)
        else:
            self.__parser = ConfigParser.SafeConfigParser()
            self.__parser.read(fullPath)

    def getSection(self, section):
        ''' load all configuration '''
        configs = {}
        if self.__parser and self.__parser.has_section(section):
            for name, value in self.__parser.items(section):
                configs[name] = value
            return configs

        return configs

    def getOption(self, section, option):
        ''' whether a option exists in the section '''
        if self.__parser and self.__parser.has_option(section, option):
            return self.__parser.get(section, option)
        else:
            return None

if __name__ == '__main__':
    print PyConfig().getOption('app_main', 'feeder')