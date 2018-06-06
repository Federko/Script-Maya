#gameindrustry.byz
#aswift.com
from maya import cmds

BSM_TEXT_SCROLL_LIST = "BSM_TEXT_SCROLL_LIST"
BSM_FLOAT_SLIDER_GRP = "BSM_FLOAT_SLIDER_GRP"

def blend_shape_manager_UI():
    win_name = "blend_shape_manager_UI"
    
    if cmds.window(win_name, q=True, ex=True):
        cmds.deleteUI(win_name)
        
    
    cmds.window(win_name, t="Blend Shape Manager")
    cmds.columnLayout()
    cmds.textScrollList(BSM_TEXT_SCROLL_LIST, ams=True)
    cmds.floatSliderGrp(BSM_FLOAT_SLIDER_GRP, field=True, minValue=0, maxValue=1)
    cmds.button(l="Refresh", c=refresh_blend_shape_manager_UI)
    cmds.button(l="Reset", c=reset_blend_shape_manager_UI)
    cmds.setParent("..")
    cmds.showWindow(win_name)


def refresh_blend_shape_manager_UI(*args):
    bsn = get_blend_shape_node()
    if not bsn:
        print("[Warning] Selected elements has no blend shapes")
    attrs = cmds.listAttr(blend_shape_node + ".weight", m=True)
    cmds.textScrollList(BSM_TEXT_SCROLL_LIST, e=True, ra=True)
    
    for attr in attrs:
        print(attr)
        cmds.textScrollList(BSM_TEXT_SCROLL_LIST, e=True, append=attr)
        
        
def get_blend_shape_node():
    selection = cmds.ls(sl=True)
    history = cmds.listHistory(selection[0])
    blend_shape_node = ""
    for node in history:
        print(node)
        if(cmds.nodeType(node) == "blendShape"):
            blend_shape_node = node
            break
    else:
        print("[Warning] Selected elements has no blend shapes")
        
    return blend_shape_node
    


def apply_blend_shape():
    bsn = get_blend_shape_node()
    attr = cmds.textScrollList(BSM_TEXT_SCROLL_LIST, q=True, si=True)[0] 
    reset_blend_shape_UI()
    cmds.setAttr(bsn + "." + attr, 1)
    
            
blend_shape_manager_UI()

refresh_blend_shape_manager_UI()














from maya import cmds

BSM_TEXT_SCROLL_LIST = "BSM_TEXT_SCROLL_LIST"
BSM_FLOAT_SLIDER_GRP = "BSM_FLOAT_SLIDER_GRP"

def blend_shape_manager_UI():
    win_name = "blend_shape_manager_UI"
    
    if cmds.window(win_name, q=True, ex=True):    
        cmds.deleteUI(win_name)
    
    cmds.window(win_name, t="Blend Shape Manager Cane")
    cmds.columnLayout()
    cmds.textScrollList(BSM_TEXT_SCROLL_LIST, ams=True, dcc=apply_blend_shape, sc=connect_slider)
    cmds.floatSliderGrp(BSM_FLOAT_SLIDER_GRP, field=True, minValue=0, maxValue=1, value=0)
    cmds.button(l="Refresh", c=refresh_blend_shape_manager_UI)
    cmds.button(l="Reset", c=reset_blend_shape_manager_UI)
    cmds.setParent("..")
    cmds.showWindow(win_name)
        

def refresh_blend_shape_manager_UI(*args):
    bsn = get_blend_shape_node()
    if not bsn:
        print("[Warning] Selected node has no blend shapes")
        return 
    attrs = cmds.listAttr(bsn + ".weight", m=True)
    cmds.textScrollList(BSM_TEXT_SCROLL_LIST, e=True, ra=True)

    for attr in attrs:
        cmds.textScrollList(BSM_TEXT_SCROLL_LIST, e=True, append=attr)

def reset_blend_shape_manager_UI(*args):
    bsn = get_blend_shape_node()
    attrs = cmds.listAttr(bsn + ".weight", m=True)
    for attr in attrs:
        cmds.setAttr(bsn + "." + attr, 0)
    
def get_blend_shape_node():
    selection = cmds.ls(sl=True)
    history = cmds.listHistory(selection[0])
    blend_shape_node = ""
    for node in history:
        if cmds.nodeType(node) == "blendShape":
            blend_shape_node = node
            break
    return blend_shape_node
    
def apply_blend_shape():
    bsn = get_blend_shape_node()
    attr = cmds.textScrollList(BSM_TEXT_SCROLL_LIST, q=True, si=True)[0]
    reset_blend_shape_manager_UI()
    cmds.setAttr(bsn + "." + attr, 1)

def connect_slider(*args):
    bsn = get_blend_shape_node()
    attrs = cmds.textScrollList(BSM_TEXT_SCROLL_LIST, q=True, si=True)
    attrs_lst = [bsn + "." + attr for attr in attrs]
    cmds.connectControl(BSM_FLOAT_SLIDER_GRP, *attrs_lst)

blend_shape_manager_UI()