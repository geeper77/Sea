"""
Adapter classes for :class:`Sea.model.components.Component2DPlate`
"""

import Sea
from .. import baseclasses


class SubsystemLong(baseclasses.SubsystemLong):
    model = Sea.model.components.structural_2D_plate.SubsystemLong()

class SubsystemBend(baseclasses.SubsystemBend):
    model = Sea.model.components.structural_2D_plate.SubsystemBend()

class SubsystemShear(baseclasses.SubsystemShear):
    model = Sea.model.components.structural_2D_plate.SubsystemShear()

    
class Component2DPlate(baseclasses.ComponentStructural):
    """
    Plate structural component.
    
    This adapter describes a :class:`Sea.model.components.Component2DPlate`
    """

    name = 'Plate'
    description = 'A structural component with wave propagation along two dimensions.'
    
    model = Sea.model.components.Component2DPlate()
    
    def __init__(self, obj, system, material, part):
        
        obj.addProperty("App::PropertyFloat", "Length", self.name, "Length of the plate.")
        obj.addProperty("App::PropertyFloat", "Width", self.name, "Width of the plate.")
        
        baseclasses.ComponentStructural.__init__(self, obj, system, material, part)
        
        
        obj.addProperty("App::PropertyFloat", "Area", self.name, "Area of the plate.")
        obj.addProperty("App::PropertyFloat", "Thickness", self.name, "Thickness of the plate.")
        obj.addProperty("App::PropertyFloat", "MassPerArea", self.name, "Mass per unit area.")
        self.calc_area_and_thickness(obj)
        
        
        obj.SubsystemLong = obj.makeSubsystem(SubsystemLong)
        obj.SubsystemBend = obj.makeSubsystem(SubsystemBend) 
        obj.SubsystemShear = obj.makeSubsystem(SubsystemShear) 

        
    def onChanged(self, obj, prop):
        baseclasses.ComponentStructural.onChanged(self, obj, prop)
        
        if prop == 'Area':
            obj.Proxy.model.area = obj.Area
        
        elif prop == 'Thickness':
            obj.Proxy.model.thickness = obj.Thickness
        
        elif prop == 'Length':
            obj.Proxy.model.length = obj.Length
        
        elif prop == 'Width':
            obj.Proxy.model.width = obj.Width
        
        if prop == 'Shape':
            box = obj.Shape.BoundBox
            dim = [box.XLength, box.YLength, box.ZLength]
            smallest = min(dim)
            largest = max(dim)
            
            obj.Length = largest
            dim.remove(smallest)
            dim.remove(largest)
            obj.Width = dim[0]
        
    def execute(self, obj):
        baseclasses.ComponentStructural.execute(self, obj)
        self.calc_area_and_thickness(obj)
        
        obj.MassPerArea = obj.Proxy.model.mass_per_area
        
    def calc_area_and_thickness(self, obj):
        """
        Determine the area and thickness of the plate.
        """
        box = obj.Shape.BoundBox
        
        dim = [ box.XLength, box.YLength, box.ZLength ]
        obj.Thickness = min(dim)
        dim.remove(obj.Thickness)
        obj.Area = dim[0] * dim[1]
   
    