
class SeaWorkbench(Workbench):
    """
    Statistical Energy Analysis workbench
    """

    Icon = """
            /* XPM */
            static char *dummy[]={
            "100 100 16 1",
            ". c #0000ff",
            "n c #3333cc",
            "g c #3333ff",
            "d c #660099",
            "a c #663399",
            "e c #6633cc",
            "# c #6666cc",
            "f c #6666ff",
            "l c #cc3366",
            "b c #cc3399",
            "h c #cc6699",
            "m c #cc66cc",
            "k c #cc99cc",
            "j c #ff0000",
            "i c #ff3333",
            "c c #ff6666",
            "....................................................................................................",
            "....................................................................................................",
            "....................................................................................................",
            "....................................................................................................",
            "....................................................................................................",
            "....................................................................................................",
            "....................................................................................................",
            "....................................................................................................",
            "....................................................................................................",
            "....................................................................................................",
            "....................................................................................................",
            "....................................................................................................",
            "....................................................................................................",
            "....................................................................................................",
            "....................................................................................................",
            "....................................................................................................",
            "....................................................................................................",
            "....................................................................................................",
            "....................................................................................................",
            "....................................................................................................",
            "....................................................................................................",
            "....................................................................................................",
            "....................................................................................................",
            "....................................................................................................",
            "....................................................................................................",
            "....................................................................................................",
            "....................................................................................................",
            "....................................................................................................",
            "....................................................................................................",
            "....................................................................................................",
            "....................................................................................................",
            "....................................................................................................",
            "..............#abcccccde#.............ffffffffffffffffffffff................ffffff..................",
            "...........ghijjjjjjjjjjjichf.........jjjjjjjjjjjjjjjjjjjjjc...............gijjjji..................",
            "..........kijjjjjjjjjjjjjjjjj.........jjjjjjjjjjjjjjjjjjjjjc...............ejjjjjj#.................",
            ".........hjjjjjjjjjjjjjjjjjjj.........jjjjjjjjjjjjjjjjjjjjjc...............cjjjjjjc.................",
            "........kjjjjjjche###eacijjjj.........jjjjjiiiiiiiiiiiiiiiic..............gjjjjjjjjg................",
            ".......gijjjji#..........#cjj.........jjjjc...............................hjjjjjjjje................",
            ".......ajjjjig.............gh.........jjjjc...............................ijjjccjjjc................",
            ".......cjjjj#.........................jjjjc..............................#jjjjeajjjjf...............",
            ".......ijjji..........................jjjjc..............................cjjjiggjjjjh...............",
            ".......jjjji..........................jjjjc.............................gijjjb..cjjjig..............",
            ".......jjjji..........................jjjjc.............................ejjjj#..ejjjje..............",
            ".......ijjjjg.........................jjjjc.............................cjjji...gijjjc..............",
            ".......cjjjjl.........................jjjjc............................fjjjjh....bjjjjg.............",
            ".......hjjjjjcf.......................jjjjc............................hjjjjf....#jjjjh.............",
            ".......gijjjjjjch#g...................jjjjiffffffffffffffff...........gijjjc......ijjji.............",
            "........kjjjjjjjjjjica#...............jjjjjjjjjjjjjjjjjjjji...........#jjjje......hjjjj#............",
            ".........mjjjjjjjjjjjjjic#............jjjjjjjjjjjjjjjjjjjji...........cjjjig......gjjjjb............",
            "..........#cjjjjjjjjjjjjjjcg..........jjjjjjjjjjjjjjjjjjjji..........gjjjjc........cjjjig...........",
            "............#bijjjjjjjjjjjjik.........jjjjjiiiiiiiiiiiiiiii..........hjjjj#........ejjjje...........",
            "...............falcijjjjjjjjj#........jjjjc..........................ijjji.........gijjjc...........",
            "....................#hijjjjjjig.......jjjjc.........................#jjjjh..........cjjjjf..........",
            ".......................kijjjjje.......jjjjc.........................bjjjjf..........#jjjjh..........",
            "........................gijjjjc.......jjjjc........................gijjjjccccccccccccjjjji..........",
            ".........................mjjjji.......jjjjc........................ejjjjjjjjjjjjjjjjjjjjjj#.........",
            ".........................gjjjjjg......jjjjc........................cjjjjjjjjjjjjjjjjjjjjjjc.........",
            "..........................ijjjjf......jjjjc.......................fjjjjjjjjjjjjjjjjjjjjjjjjg........",
            "..........................ijjjjg......jjjjc.......................hjjjjheeeeeeeeeeeeeehjjjja........",
            ".........................gjjjji.......jjjjc.......................ijjjig..............gjjjjc........",
            ".......f.................hjjjjc.......jjjjc......................#jjjjc................cjjjjf.......",
            ".......ic#..............nijjjjh.......jjjjc......................cjjjj#................ejjjjh.......",
            ".......ijjceg.........gmijjjjig.......jjjjc.....................gjjjji.................gijjjig......",
            ".......ijjjjjche#ff#ebijjjjjjm........jjjjjiiiiiiiiiiiiiiiii....ajjjjb..................bjjjje......",
            ".......ijjjjjjjjjjjjjjjjjjjjh.........jjjjjjjjjjjjjjjjjjjjjj....cjjjj#..................#jjjjc......",
            ".......cjjjjjjjjjjjjjjjjjjim..........jjjjjjjjjjjjjjjjjjjjjj...fjjjji....................ijjjjg.....",
            "........gecijjjjjjjjjjjjihg...........jjjjjjjjjjjjjjjjjjjjjj...hjjjjh....................hjjjjh.....",
            "............feaccccccdef............................................................................",
            "....................................................................................................",
            "....................................................................................................",
            "....................................................................................................",
            "....................................................................................................",
            "....................................................................................................",
            "....................................................................................................",
            "....................................................................................................",
            "....................................................................................................",
            "....................................................................................................",
            "....................................................................................................",
            "....................................................................................................",
            "....................................................................................................",
            "....................................................................................................",
            "....................................................................................................",
            "....................................................................................................",
            "....................................................................................................",
            "....................................................................................................",
            "....................................................................................................",
            "....................................................................................................",
            "....................................................................................................",
            "....................................................................................................",
            "....................................................................................................",
            "....................................................................................................",
            "....................................................................................................",
            "....................................................................................................",
            "....................................................................................................",
            "....................................................................................................",
            "....................................................................................................",
            "....................................................................................................",
            "....................................................................................................",
            "....................................................................................................",
            "...................................................................................................."};
            """
    
    
    
    
    MenuText = "SEA"
    ToolTip = "Statistical Energy Analysis workbench"
    
    def Initialize(self):
        from PyQt4 import QtCore, QtGui

        import Paths
        import gui
        import Sea
        
        Gui.addIconPath(Paths.iconsPath())
        Gui.addLanguagePath(Paths.translationsPath())


        items = ["Sea_AddSystem", "Sea_AddComponent", "Sea_AddExcitation", "Sea_AddMaterial"]
        self.appendToolbar(str(QtCore.QT_TRANSLATE_NOOP("Sea", "Add item")), items)
        self.appendMenu(str(QtCore.QT_TRANSLATE_NOOP("Sea", "Add item")), items)        
 
        
        items = ["Sea_RunAnalysis", "Sea_StopAnalysis", "Sea_ClearAnalysis"];
        self.appendToolbar(str(QtCore.QT_TRANSLATE_NOOP("Sea", "Analysis")), items)
        self.appendMenu(str(QtCore.QT_TRANSLATE_NOOP("Sea", "Analysis")), items)
        

        Log('Loading Sea module... done\n')
        
    def Activated(self):
        Msg("SeaWorkbench::Activated()\n")
        
    def Deactivated(self):
        Msg("SeaWorkbench::Deactivated()\n")

Gui.addWorkbench(SeaWorkbench)