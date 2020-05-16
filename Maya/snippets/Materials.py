import maya.cmds as mc

def applyMaterial(node):
    if mc.objExists(node):
        shd = mc.shadingNode('lambert', name="%s_lambert" % node, asShader=True)
        shdSG = mc.sets(name='%sSG' % shd, empty=True, renderable=True, noSurfaceShader=True)
        mc.connectAttr('%s.outColor' % shd, '%s.surfaceShader' % shdSG)
        mc.sets(node, e=True, forceElement=shdSG)

applyMaterial("pSphere1")
