import Sea
from .. import baseclasses

class Coupling1DStructural(baseclasses.Coupling):
    """
    A coupling describing a connection of a single point.
    """
    name = 'Point'
    description = 'A coupling describing a connection of a single point.'
    
    model = Sea.model.couplings.Coupling1DStructural()
 
    def __init__(self, obj, connection, component_from, subsystem_from, component_to, subsystem_to):
        baseclasses.Coupling.__init__(self, obj, connection, component_from, subsystem_from, component_to, subsystem_to)
    
    
    def onChanged(self, obj, prop):
        baseclasses.Coupling.onChanged(self, obj, prop)
    
    def execute(self, obj):
        baseclasses.Coupling.execute(self, obj)
    
    @staticmethod
    def size(obj):
        """
        Return the size of the coupling.
        
        :param obj: an instance of :class:`Sea.adapter.couplings.CouplingPoint`
        
        """
        return
    
        
#class CouplingArea(baseclasses.Coupling):
    #"""
    #A coupling describing a connection along a surface.
    #"""
    #name = 'Surface'
    #description = 'A coupling describing a connection along a surface.'
    
    #model = Sea.model.couplings.CouplingLine()

    #def __init__(self, obj, system, subsystem_from, subsystem_to, **properties):
        #baseclasses.Coupling.__init__(self, obj, system, subsystem_from, subsystem_to, **properties)
        
        
        
