from maya import cmds

for job in cmds.scriptJob(listJobs = True):
    print job

job_num = cmds.scriptJob(ct=["SomethingSelected", "cmds.delete()"])


#cmds.scriptJob(k=127)per eliminare un evento k sta per kill e poi il numero dell' evento

def changeColor():
    color = cmds.getAttr("blinn2.color")[0]
    if(color[0] == 1):cmds.setAttr("blinn2.color", 0, 1, 0)   
    elif(color[1] == 1):cmds.setAttr("blinn2.color", 0, 0, 1)
    elif(color[2] == 1):cmds.setAttr("blinn2.color", 1, 0, 0)
    
jobNum = cmds.scriptJob(attributeChange=["pCube1.ty", changeColor], runOnce = True)