
## BLACKPHENIX - MALWARE ANALYSIS + AUTOMATION FRAMEWORK

BLACKPHENIX is an open-source malware analysis automation framework composed of services, scripts, plug-ins, and tools based on a Command-and-Control (C&C) architecture. It relies on virtual machine software to operate and scripts to remotely control (GUI and console) tools and scripts running on a guest (analysis) virtual machine. It reports back results to a controller machine to perform further deep data analysis and execution decisions.

This framework was released and presented at <a href="https://www.blackhat.com/us-19/arsenal/schedule/#blackphenix-malware-analysis--automation-framework-16941" target="_blank">BlackHat Arsenal 2019</a> 

## How this framework can be used?
Analysts can use the framework to perform automated, virtual machine-based malware analysis activities by automating the execution of well-known analysis tools, custom tools, and scripts that run in a remote virtual machine. They can do this through the execution of python scripts called “BPH Scripts” and “BPH Analysis Modules” to perform parsing and further data analysis.

A malware analyst can use the framework to fulfill a specific requirement that needs to be performed within a tight schedule, such as writing a quick prototype to collect specific data when a malware sample behaves in certain way.

For more information, please refer to the framework's documentation.

## Documentation
* Presentation slides  [[download]](docs/BH19_BLACKPHENIX_CHRISNAVARRETE.pdf)
* Implementation manual [[download]](docs/BPH_IMPLEMENTATION_MANUAL.pdf).
* BPH Scripting guide [[download]](docs/BPH_SCRIPT_DEVELOPMENT_GUIDE.pdf).

### Authors
- **Chris Navarrete**

### Contact
- Email: <a href="mailto:bph_framework@fortinet.com" target="_blank">bph_framework@fortinet.com</a>
- IRC(Freenode): #bph-framework

### License
This project is licensed under the Apache 2.0 License - see the LICENSE.md file for details
