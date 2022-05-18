"""
 For more examples, please refer to the plugin example of OpenTAP Python plugin.
"""
import sys
import clr
import PythonTap
import OpenTap
import System
from PythonTap import *
from OpenTap import DisplayAttribute, UnitAttribute, Verdict
from System import String, Int32 # Import types to reference for generic methods.
from OpenTap.Plugins.BasicSteps import GenericScpiInstrument

@Attribute(DisplayAttribute, "VNA", "Add VNA Network Analyzer", "VNA")
class VNA(Instrument):
    def __init__(self):
        super(VNA, self).__init__()
        
        self._io = GenericScpiInstrument()
        self.Name = "VNA"
        # ToDo: Add property here for each parameter the end user should be able to change.
        # AddProperty("property_name", default property value, property data type)

        # String property example.
        prop = self.AddProperty("visa_address", "TCPIP0::127.0.0.1::hislip0::INSTR", String)
        prop.AddAttribute(DisplayAttribute, "VISA Address", "VISA address of the instrument to connect", "VISA", 1)

        # Integer property example.
        prop = self.AddProperty("io_timeout", 5000, Int32)
        prop.AddAttribute(DisplayAttribute, "IO Timeout", "Timeout of the connection", "VISA", 2)
        prop.AddAttribute(UnitAttribute, "sec", PreScaling=1000)

    def Open(self):
        """Called by OpenTAP when the test plan starts."""
        # ToDo: Open the connection to the instrument here
        self._io.VisaAddress = self.visa_address
        self._io.Open()
        
        #pass

    def Close(self):
        """Called by OpenTAP when the test plan ends."""
        # ToDo: Shut down the connection to the instrument here
        self._io.Close()
        #pass