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
from System import String, Int32, Double, Boolean # Import types to reference for generic methods.
from .VNA import VNA
import time



@Attribute(DisplayAttribute, "S-ParameterTest", "Sparameter Test", "VNA")
class SParameterTest(TestStep):
    def __init__(self):
        super(SParameterTest, self).__init__()
        
        # ToDo: Add property here for each parameter the end user should be able to change.
        # AddProperty("property_name", default property value, property data type)

        # String property example.
        prop = self.AddProperty("vna", None, VNA)
        prop.AddAttribute(DisplayAttribute, "Instrument", "The instrument to connect", "Resources", 1)
        
        prop = self.AddProperty("CalibrateVNA", False, Boolean)
        prop.AddAttribute(DisplayAttribute, "Calibrate VNA", "if enabled the VNA will be setup and ask the user to perform a calibration of the instrument", "Resources", 2)
        
        
        prop = self.AddProperty("VnaChannel", 1, Int32)
        prop.AddAttribute(DisplayAttribute, "Channel", "Channel", "VNA Setup", 3)

        prop = self.AddProperty("VnaWindow", 1, Int32)
        prop.AddAttribute(DisplayAttribute, "Window", "Window", "VNA Setup", 4)

        prop = self.AddProperty("StartFrequency", 1E+09, Double)
        prop.AddAttribute(DisplayAttribute, "Start Frequency", "Start Frequency of the sweep", "VNA Setup", 5)
        prop.AddAttribute(UnitAttribute, "Hz")

        prop = self.AddProperty("StopFrequency", 2E+09, Double)
        prop.AddAttribute(DisplayAttribute, "Stop Frequency", "Stop Frequency of the sweep", "VNA Setup", 6)
        prop.AddAttribute(UnitAttribute, "Hz")

        prop = self.AddProperty("Autoscale", True, Boolean)
        prop.AddAttribute(DisplayAttribute, "AutoScale", "Autoscale", "VNA Setup", 6.1)
        
        self.AddProperty("Measurement", "S21", String).AddAttribute(DisplayAttribute, "Measurement", "put S21, S11, S22, S12", "Measurement", 7)
    
          
        
    def Run(self):
        # ToDo: Add test case code.
        self.vna._io.ScpiCommand("SYSTem:FPReset")
        self.vna._io.ScpiCommand(f"DISPlay:WINDow{self.VnaWindow}:STATE ON")
        self.vna._io.ScpiCommand(f"CALCulate{self.VnaChannel}:PARameter:DEFine:EXT 'Meas', '{self.Measurement}'")
        self.vna._io.ScpiCommand(f"DISPlay:WINDow{self.VnaWindow}:TRACe1:FEED 'Meas'")
        self.vna._io.ScpiCommand(f"SENSe{self.VnaChannel}:FREQuency:STARt {self.StartFrequency}")
        self.vna._io.ScpiCommand(f"SENSe{self.VnaChannel}:FREQuency:STOP {self.StopFrequency}")
        if self.Autoscale:
            time.sleep(1)
            self.vna._io.ScpiCommand(f"DISP:WIND{self.VnaWindow}:Y:AUTO")
        # If the step supports child steps, run the child steps.
        for step in self.EnabledChildSteps:
            self.RunChildStep(step)
        
        # If no verdict is specified, the default verdict will be NotSet.
        # Please change the verdict using UpgradeVerdict() as shown below.
        self.UpgradeVerdict(Verdict.NotSet)
        
        pass

    def PrePlanRun(self):
        # ToDo: Add test case code when the plan starts.
        
        pass

    def PostPlanRun(self):
        # ToDo: Add test case code when the plan completes.
        
        pass
