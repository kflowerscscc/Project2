# Author: Kristi Loesch
# Date: 2/21/2024
# Description: Project 2


from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
import SpaceJamClasses as spaceJamClasses
import DefensePaths as defensePaths
import math, random

class SpaceJam(ShowBase):
    
    def __init__(self):
  
        ShowBase.__init__(self)

        self.Universe = spaceJamClasses.GameObject(self.loader, "./Assets/Universe/Universe.x", self.render, 'Universe', "./Assets/Universe/starfield-in-blue.jpg", (0,0,0), 15000 )
        self.Planet1 = spaceJamClasses.GameObject(self.loader, "./Assets/Planets/protoPlanet.x", self.render, 'Planet1', "./Assets/Planets/jupiter.jpg", Vec3(-6000,-3000,-800), 250 )
        self.Planet2 = spaceJamClasses.GameObject(self.loader, "./Assets/Planets/protoPlanet.x", self.render, 'Planet2', "./Assets/Planets/earth_daymap.jpg", Vec3(0,6000,0), 300 )
        self.Planet3 = spaceJamClasses.GameObject(self.loader, "./Assets/Planets/protoPlanet.x", self.render, 'Planet3', "./Assets/Planets/saturn.jpg", Vec3(300,600,500), 150)
        self.Planet4 = spaceJamClasses.GameObject(self.loader, "./Assets/Planets/protoPlanet.x", self.render, 'Planet4', "./Assets/Planets/cracked_earth.jpg", Vec3(300,3000,500), 150 )
        self.Planet5 = spaceJamClasses.GameObject(self.loader, "./Assets/Planets/protoPlanet.x", self.render, 'Planet5', "./Assets/Planets/venus.jpg", Vec3(700,-2000,100), 500 )
        self.Planet6 = spaceJamClasses.GameObject(self.loader, "./Assets/Planets/protoPlanet.x", self.render, 'Planet6', "./Assets/Planets/pluto.jpg", Vec3(0,-9000,-1400), 700 )
        self.SpaceStation1 = spaceJamClasses.GameObject(self.loader, "./Assets/Space Station/spaceStation.egg", self.render, 'Space Station', "./Assets/Space Station/SpaceStation1_Dif2.png", (1500,1000,-100), 40 )
        self.Player1 = spaceJamClasses.GameObject(self.loader, "./Assets/Spaceships/theBorg.x", self.render, 'Player', "./Assets/Spaceships/theBorg.jpg", (0,0,0), 5 )
        

        # Place drone cloud around an object
        fullCycle = 60
        for j in range(fullCycle):
            spaceJamClasses.Drone.droneCount += 1
            nickName = "Drone" + str(spaceJamClasses.Drone.droneCount) 
            self.DrawCloudDefense(self.Planet3, nickName, 300 ) # Call function to draw cloud,  indicate scale

        
        # Place baseball seams around an object
        steps = 150
        for step in range(steps):
            spaceJamClasses.Drone.droneCount += 1
            droneName = "Seam" + str(spaceJamClasses.Drone.droneCount)
            self.DrawBaseballSeams(self.Planet4, droneName, step, 50, 300) # Call function to draw baseball seams, indicate scale

        
        # Draw circle on each plane around an object
        x=0
        for i in range(100):
            theta = x
            spaceJamClasses.Drone.droneCount += 1
            droneName = "Circle" + str(spaceJamClasses.Drone.droneCount)
            self.DrawCircleXY(self.Planet2, droneName, theta, 450) # Call function to draw XY circle, indicate scale
            self.DrawCircleXZ(self.Planet2, droneName, theta, 450) # Call function to draw XZ circle, indicate scale
            self.DrawCircleYZ(self.Planet2, droneName, theta, 450)# Call function to draw YZ circle, indicate scale
            x = x + .0628
        

    def DrawCloudDefense(self, centralObject, nickname, scale):
        unitVec = defensePaths.Cloud()
        unitVec.normalize()
        position = unitVec * scale + centralObject.modelNode.getPos()
        spaceJamClasses.Drone(self.loader, "./Assets/DroneDefender/DroneDefender.obj", self.render, nickname, "./Assets/DroneDefender/octotoad1_auv.png", position, 10)
    
    def DrawBaseballSeams(self, centralObject, droneName, step, numSeams, scale, radius=1):
        unitVec = defensePaths.BaseballSeams(step, numSeams, B = 0.4)
        unitVec.normalize()
        position = unitVec * scale + centralObject.modelNode.getPos()
        spaceJamClasses.Drone(self.loader, "./Assets/DroneDefender/DroneDefender.obj", self.render, droneName, "./Assets/DroneDefender/octotoad1_auv.png", position, 5)

    def DrawCircleXY(self, centralObject, droneName, theta, scale):
        unitVec = defensePaths.CircleXY(theta)
        unitVec.normalize()
        position = unitVec * scale + centralObject.modelNode.getPos()
        spaceJamClasses.Drone(self.loader, "./Assets/DroneDefender/DroneDefender.obj", self.render, droneName, "./Assets/DroneDefender/color_red.jpg", position, 5)
    
    def DrawCircleXZ(self, centralObject, droneName, theta, scale):
        unitVec = defensePaths.CircleXZ(theta)
        unitVec.normalize()
        position = unitVec * scale + centralObject.modelNode.getPos()
        spaceJamClasses.Drone(self.loader, "./Assets/DroneDefender/DroneDefender.obj", self.render, droneName, "./Assets/DroneDefender/color_green.jpg", position, 5)
    
    def DrawCircleYZ(self, centralObject, droneName, theta, scale):
        unitVec = defensePaths.CircleYZ(theta)
        unitVec.normalize()
        position = unitVec * scale + centralObject.modelNode.getPos()
        spaceJamClasses.Drone(self.loader, "./Assets/DroneDefender/DroneDefender.obj", self.render, droneName, "./Assets/DroneDefender/color_blue.jpg", position, 5)
        


app = SpaceJam()
app.run()