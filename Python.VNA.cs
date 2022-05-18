using Keysight.Plugins.Python;

[assembly: System.Reflection.AssemblyVersion("1.0.0.0")]
[assembly: System.Reflection.AssemblyFileVersion("1.0.0.0")]
[assembly: System.Reflection.AssemblyInformationalVersion("1.0.0.0")]
[assembly: System.Runtime.InteropServices.GuidAttribute("9e571862-856e-473a-8c16-28bb7cfb2bb7")]
namespace Python.VNA
{
 [PythonWrapper.PythonName("VNA.VNA.VNA")]
 [OpenTap.DisplayAttribute("VNA", "Add VNA Network Analyzer", "VNA")]
 public class VNA : Keysight.OpenTap.Plugins.Python.PythonInstrumentWrapper
 {
  public override void load_instance()
  {
   load("VNA", "VNA");
  }

  [OpenTap.DisplayAttribute("VISA Address", "VISA address of the instrument to connect", "VISA", 1)]
  public System.String visa_address
  {
   get
   {
    return (System.String)this.getValue("visa_address", typeof(System.String));
   }

   set
   {
    this.setValue("visa_address", value);
   }
  }

  [OpenTap.DisplayAttribute("IO Timeout", "Timeout of the connection", "VISA", 2)]
  [OpenTap.UnitAttribute("sec", PreScaling: 1000)]
  public System.Int32 io_timeout
  {
   get
   {
    return (System.Int32)this.getValue("io_timeout", typeof(System.Int32));
   }

   set
   {
    this.setValue("io_timeout", value);
   }
  }
 }

 [PythonWrapper.PythonName("VNA.IDN.IDN")]
 [OpenTap.DisplayAttribute("IDN", "Check the instrument connection", "VNA")]
 public class IDN : Keysight.OpenTap.Plugins.Python.PythonStepWrapper
 {
  public override void load_instance()
  {
   load("IDN", "VNA");
  }

  [OpenTap.DisplayAttribute("Instrument", "The instrument to connect", "Resources")]
  public VNA vna
  {
   get
   {
    return (VNA)this.getValue("vna", typeof(VNA));
   }

   set
   {
    this.setValue("vna", value);
   }
  }
 }

 [PythonWrapper.PythonName("VNA.SParameterTest.SParameterTest")]
 [OpenTap.DisplayAttribute("S-ParameterTest", "Sparameter Test", "VNA")]
 public class SParameterTest : Keysight.OpenTap.Plugins.Python.PythonStepWrapper
 {
  public override void load_instance()
  {
   load("SParameterTest", "VNA");
  }

  [OpenTap.DisplayAttribute("Instrument", "The instrument to connect", "Resources", 1)]
  public VNA vna
  {
   get
   {
    return (VNA)this.getValue("vna", typeof(VNA));
   }

   set
   {
    this.setValue("vna", value);
   }
  }

  [OpenTap.DisplayAttribute("Calibrate VNA", "if enabled the VNA will be setup and ask the user to perform a calibration of the instrument", "Resources", 2)]
  public System.Boolean CalibrateVNA
  {
   get
   {
    return (System.Boolean)this.getValue("CalibrateVNA", typeof(System.Boolean));
   }

   set
   {
    this.setValue("CalibrateVNA", value);
   }
  }

  [OpenTap.DisplayAttribute("Channel", "Channel", "VNA Setup", 3)]
  public System.Int32 VnaChannel
  {
   get
   {
    return (System.Int32)this.getValue("VnaChannel", typeof(System.Int32));
   }

   set
   {
    this.setValue("VnaChannel", value);
   }
  }

  [OpenTap.DisplayAttribute("Window", "Window", "VNA Setup", 4)]
  public System.Int32 VnaWindow
  {
   get
   {
    return (System.Int32)this.getValue("VnaWindow", typeof(System.Int32));
   }

   set
   {
    this.setValue("VnaWindow", value);
   }
  }

  [OpenTap.DisplayAttribute("Start Frequency", "Start Frequency of the sweep", "VNA Setup", 5)]
  [OpenTap.UnitAttribute("Hz")]
  public System.Double StartFrequency
  {
   get
   {
    return (System.Double)this.getValue("StartFrequency", typeof(System.Double));
   }

   set
   {
    this.setValue("StartFrequency", value);
   }
  }

  [OpenTap.DisplayAttribute("Stop Frequency", "Stop Frequency of the sweep", "VNA Setup", 6)]
  [OpenTap.UnitAttribute("Hz")]
  public System.Double StopFrequency
  {
   get
   {
    return (System.Double)this.getValue("StopFrequency", typeof(System.Double));
   }

   set
   {
    this.setValue("StopFrequency", value);
   }
  }

  [OpenTap.DisplayAttribute("AutoScale", "Autoscale", "VNA Setup", 6.1)]
  public System.Boolean Autoscale
  {
   get
   {
    return (System.Boolean)this.getValue("Autoscale", typeof(System.Boolean));
   }

   set
   {
    this.setValue("Autoscale", value);
   }
  }

  [OpenTap.DisplayAttribute("Measurement", "put S21, S11, S22, S12", "Measurement", 7)]
  public System.String Measurement
  {
   get
   {
    return (System.String)this.getValue("Measurement", typeof(System.String));
   }

   set
   {
    this.setValue("Measurement", value);
   }
  }
 }
}