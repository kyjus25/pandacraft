"""
awsd - movement
space - jump
mouse - look around
"""

import direct.directbase.DirectStart
from pandac.PandaModules import *
from direct.gui.OnscreenText import OnscreenText
import sys

from player import *


class FPS(object):
    """
        This is a very simple FPS like -
         a building block of any game i guess
    """
    def __init__(self):
        self.initCollision()
        self.loadLevel()
        self.initPlayer()
        base.accept( "escape" , sys.exit)
        base.disableMouse()

        props = WindowProperties()
        props.setCursorHidden(True)
        base.win.requestProperties(props)

        # OnscreenText(text="Simple FPS Movement", style=1, fg=(1,1,1,1),
        #             pos=(1.3,-0.95), align=TextNode.ARight, scale = .07)
        # OnscreenText(text=__doc__, style=1, fg=(1,1,1,1),
        #     pos=(-1.3, 0.95), align=TextNode.ALeft, scale = .05)
        
    def initCollision(self):
        """ create the collision system """
        base.cTrav = CollisionTraverser()
        base.pusher = CollisionHandlerPusher()
        
    def loadLevel(self):
        """ load the self.level 
            must have
            <Group> *something* { 
              <Collide> { Polyset keep descend } 
            in the egg file
        """
        self.level = loader.loadModel('level.egg')
        self.level.reparentTo(render)
        self.level.setTwoSided(True)
                
    def initPlayer(self):
        """ loads the player and creates all the controls for him"""
        self.node = Player()
        

       
FPS()
run() 