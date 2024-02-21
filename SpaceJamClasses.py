# Author: Kristi Loesch
# Date: 2/14/2024
# Description: Project 1


from direct.showbase.ShowBase import ShowBase
from panda3d.core import *


class GameObject(ShowBase):
    
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, textPath:str, posVec: Vec3, scaleVec:float):
        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)
        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(textPath)
        self.modelNode.setTexture(tex, 1)

class Drone(GameObject):
    
    droneCount = 0

    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, textPath:str, posVec: Vec3, scaleVec:float):
        super().__init__(loader, modelPath, parentNode, nodeName, textPath, posVec, scaleVec)


#  Code below was refactored using class inheritance.
'''
class Drone(ShowBase):

    # How many drones have been spawned
    droneCount = 0

    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, textPath:str, posVec: Vec3, scaleVec:float):
        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)
        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(textPath)
        self.modelNode.setTexture(tex, 1)

class Planet(ShowBase):
    
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, textPath:str, posVec: Vec3, scaleVec:float):
        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)
        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(textPath)
        self.modelNode.setTexture(tex, 1)

class SpaceStation(ShowBase):
    
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, textPath:str, posVec: Vec3, scaleVec:float):
        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)
        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(textPath)
        self.modelNode.setTexture(tex, 1)

class Player(ShowBase):
    
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, textPath:str, posVec: Vec3, scaleVec:float):
        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)
        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(textPath)
        self.modelNode.setTexture(tex, 1)

class Universe(ShowBase):
    
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, textPath:str, posVec: Vec3, scaleVec:float):
        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)
        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(textPath)
        self.modelNode.setTexture(tex, 1)
'''