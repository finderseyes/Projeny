
from prj.util.Assert import *

class ProjectConfig:
    def __init__(self):
        self.pluginsFolder = []
        self.assetsFolder = []
        self.solutionProjects = []
        self.solutionFolders = {}
        self.prebuilt = []

