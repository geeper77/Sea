from .. import baseclasses

class SubsystemShear(baseclasses.Subsystem):
    """
    Adapter class for shear wave subsystems.
    """
    def __init__(self, obj, component):
        baseclasses.Subsystem.__init__(self, obj, component)
        component.Proxy.model.subsystem_shear = obj.Proxy.model
        
        
    
    def execute(self, obj):
        baseclasses.Subsystem.execute(self, obj)
        