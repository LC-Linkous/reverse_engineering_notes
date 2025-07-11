# reverse_engineering_notes
an educational sample for selecting tools and methods to get started with reverse engineering. Updated periodically. This is the public half of the documentation used in an undergraduate elective course. 

This repository provides some general methodology and a lot of references for how to get started with reverse engineering. It is for educational use only, so (code) examples included in this repository will be focused on tool usage only. 

The two main components of this repository, affectionally referred to as [`The Flow Chart`](#the-flow-chart) and [`The Table`](#the-table), are part of the [`Tool-Problem-Device Method`](#tool-problem-device-method) described below.  These are meant as informational references for how different parts of the reverse engineering process are related, and to show where some popular tools fit into the process. 

As a general disclaimer, do not attempt to access or interface any device or network that you do not own or have explicit permission to work with. Unauthorized access to a system, network, or device may have legal repercussions. Some methodology is destructive and will void any warranties. The tools and software demonstrated in this repository is not an endorsement of any particular tool. This is also not a shopping list; not all tools are needed for all problems. 

## Table of Contents
* [Requirements](#requirements)
* [Reverse Engineering](#reverse-engineering)
  * [What is Reverse Engineering?](#what-is-reverse-engineering)
  * [Getting Started with Reverse Engineering](#getting-started-with-reverse-engineering)
* [Tool-Problem-Device Method](#tool-problem-device-method)
* [The Flow Chart](#the-flow-chart)
* [The Table](#the-table)
* [Documentation Methods](#documentation-methods)
* [Bookshelf](#bookshelf)
* [Glossary](#glossary)
* [References](#references)

## Requirements

Most of this repository does not require code dependencies due to it being primarily resources. However, select examples will be added to demonstrate some basic tool usage. In cases where tools are being demonstrated via code, there will be a designated directory in the `src` directory with a local `README` and `requirements.txt`

## Reverse Engineering
### What is Reverse Engineering?

Reverse engineering is the process of analyzing a technology through a systematic process of research and physical analysis to understand the design, function, and operation. This can be applied to product, system, network, software, device, etc., and may involve physical disassembly to examine and interface with specific components. A primary goal of reverse engineering is extracting information from the technology itself in order to understand it, recreate it, identify vulnerabilities, and/or improve upon it. There are applications for interoperability, device development, security research, education, and technology improvement.

Techniques for reverse engineering can be applied across numerous fields. In software, this may mean analyzing (de)compiled code to understand algorithms or operation, locating vulnerabilities, or to create compatible software/APIs. Hardware (and firmware extraction) applications may require disassembly of a physical enclosure (if it exists), or even isolating (removing) integrated circuit chips from the main circuit to extract firmware or other information. 

This repository focuses on general techniques and tools rather than going into the details of software and hardware disassembly. Before physically disassembling a device, it is recommended to document all external markings and features, and to do cursory research to understand if any part of the process is destructive. Some steps in the disassembly, such as cutting open an enclosure, are destructive in nature but not harmful to the device operation. Other steps, such as opening a case too quickly seem benign but may break ribbon cables or rip contacts from circuity. Care should be taken at all steps of this process to document and prevent early or unintentional destruction of device functionality. 

### Getting Started with Reverse Engineering

The physical and digital tools needed for reverse engineering are highly dependent on the situation. Software-focused work may require no hardware aside from a computer running an IDE, or it may require both hardware and expensive measurement equipment. Hardware may need nothing more than a multimeter for basic circuit analysis, or it may need a specialized chip-removal tool in order to isolate and test components. 

The [`Tool-Problem-Device Method`](#tool-problem-device-method) section is designed to help narrow down tools and approaches based on the starting information. [`The Flow Chart`](#the-flow-chart) is a visualization of how some (not all) reverse engineering methods are related, while [`The Table`](#the-table) provides links to supporting tools, software, references, etc. mentioned in this repository. The chart and table have been altered from their original format to make them more markdown/README friendly, but the information is still there!

The tool information in this repository is not a replacement for a solid `documentation method`, building strong foundational knowledge, or getting hands-on experience. Reverse engineering is very domain-knowledge heavy in its implementation and many people will specialize in one (or several) areas due to the broad scope of the field. While there are many topics that fall under Reverse Engineering, there are key cross-domain skills needed to work across the full attack surface of a device:

* Operating System basics and navigation
* Understanding and manipulating file formats
* Familiarity with network protocols and understanding when they are used
* Functional knowledge of computer architecture, especially how data is moved and stored across different components
* Functional knowledge in at least one programming language, though languages such as C, Assembly, Java, and Python are common
* Scripting and automation for repeating tests and validating collected data
* Creating a proper virtual machine and/or environment setup for isolated, reproducible analysis environments
* Locating and reading commercial data sheets to identify circuit component information
* Literacy of circuit diagrams and components
* Basic soldering and electronics skills
* Knowledge and `implementation` of best safety practices when working with electricity

This is not an exhaustive list (if there ever could be one). The specific topic and attempted problem to be solved will also contribute heavily to prioritization of skills.

> [!CAUTION]
> Regarding circuity and power, an often repeated piece of advice is `If you DON'T KNOW, DON'T GUESS! Look it up!`. If you are working with, or around, hardware with ANY kind of power source (including capacitors!), look up the specs and make sure that you and your equipment are not at risk of electric shock. If you are still unsure after looking it up, find someone and ask!



## Tool-Problem-Device Method

The `Tool-Problem-Device Method` used here is a general technique for answering the following questions:
* Where am I starting?
* What am I working with? 
* What am I trying to accomplish?

With this method, you have three components to consider before answering the above questions: a tool, a problem, and a device. You choose one of those components, and that decision influences the other two. For instance, if you want to learn how to use a `JTAG enumerator` or `serial to RS232` reader, then you need to find a device with those interfaces. Knowing the tool and the device, your starting problem is then something similar to "how do I get data" or "how do I make the serial connection". If, instead, you start with a device such as a `Bluetooth wearable heartrate sensor`, then your problem may be "how do I get Bluetooth data" and your tool will need to be selected to collect and/or decode that data.

This is, of course, a simplification of the possible scope. In this method, a `device` could be represented by a piece of target software, a circuit component, or other device under test (DUT) being investigated. It is a system, network, program, or physical device that some action is being taken against. Knowing the three components of the Tool-Problem-Device Method makes it possible to then begin identifying the scope, limitations, and constraints of the reverse engineering task.

* Where am I starting?
  * The tools and resources available
  * The identified 'device' being investigated
  * Topic knowledge & depth of the researchers, including skills that might need to be learned and tested during investigation
* What am I working with? 
  * The limitations (can only look at software, can open the device, cannot remove chips, no live demo or data)
  * The constraints (time, money, device must be returned)
  * **Safety!** Check what kind of safety precautions need to be taken 
    * This includes electrical shock risk to people and equipment, fire risk (especially with internal batteries), and malware exposure to larger research systems
* What am I trying to accomplish?
  * Getting data, getting firmware, getting memory
  * Creating documentation for a project about to be adopted by a company
  * Creating an interface API to expand functionality

In the real world, you may be given the device or problem (and thus the constraints) in a work environment. Your job will then be how to select the tool or tools in order to address the problem and stay within the imposed limits and constraints. The `Tool-Problem-Device` method still holds up.

The following sections contain some notes for choosing tools, identifying and articulating problems, and choosing devices. The [Flow Chart](#the-flow-chart) and [Table](#the-table) sections do into more detail about specific tools and approaches. 


## The Flow Chart

`The Flow Chart` (All Caps) is the affectionate nickname given to the constantly referenced chart of how select topics in reverse engineering are related or use similar tools. This version is simplified a little so it can be formatted on this README, but the information is still there (just maybe linked to a table in the next section). 

The Flow Chart starts off with 4 core topics:
* Wireless Analysis
* Code Analysis
* Hardware Analysis 
* Network Analysis

Within each of those topics are a series of sub-topics, and then eventually some tools and examples. These are not exhaustive lists and are meant as a starting point. There are undoubtedly other good tools that exist for specific purposes that may not have been included in this list. 

Clicking on a sub-topic block will redirect either to a subsection with more information on the topic, or the respective table if clicking a block listing tools. 



mermaid markdown test

```mermaid
graph LR;
    A[Reverse Engineering] --> B[Hardware Analysis]
    A --> C[Code Analysis]
    A --> D[Wireless Analysis]
    A --> E[Network Analysis]

    B --> B1[Physical Device Access]
    B --> B2[Circuit Analysis]
    B --> B3[Component ID]    
    B --> B4[PCB Layout]
    B --> B5[Signal Analysis]
    B --> B6[Power Analysis]
    B --> B7[Side-channel Analysis]
    B --> B8[Fault Injection]
    
    C --> C1[Software]
    C --> C2[Firmware] 
    C --> C3[Embedded]
    C --> C4[Mobile]
    C --> C5[Web Applications]
    C --> C6[Malware Analysis]
        
    D --> D1[WiFi]
    D --> D2[Bluetooth]
    D --> D3[RFID/NFC]
    D --> D4[Sub-GHz/ISM]
    D --> D5[Cellular/Mobile]
    D --> D6[IoT Protocols]
    
    E --> E1[Protocol Analysis]
    E --> E2[Packet Capture]
    E --> E3[Network Security]
    E --> E4[Industrial/IoT Protocols]
    E --> E5[Network Infrastructure]
    E --> E6[Network Forensics]
        
    B1 --> B1a1["Task Examples:<br>• EXAMPLE<br>• EXAMPLE<br>• EXAMPLE"]
    B1 --> B1a2["Tool Examples:<br>• EXAMPLE<br>• EXAMPLE<br>• EXAMPLE"]
    B2 --> B2a1["Task Examples:<br>• EXAMPLE<br>• EXAMPLE<br>• EXAMPLE"]
    B2 --> B2a2["• Multimeter<br>• Oscilloscope<br>• Logic Analyzer"]
    B3 --> B3a1["Task Examples:<br>• EXAMPLE<br>• EXAMPLE<br>• EXAMPLE"]
    B3 --> B3a2["• Microscope<br>• Thermal Camera<br>• UV Light"]
    B4 --> B4a1["Task Examples:<br>• EXAMPLE<br>• EXAMPLE<br>• EXAMPLE"]
    B4 --> B4a2["• KiCad<br>• Altium Viewer<br>• PCB Photos"]
    B5 --> B5a1["Task Examples:<br>• EXAMPLE<br>• EXAMPLE<br>• EXAMPLE"]
    B5 --> B5a2["• Logic Analyzer<br>• Oscilloscope<br>• Function Generator"]
    B6 --> B6a1["Task Examples:<br>• EXAMPLE<br>• EXAMPLE<br>• EXAMPLE"]
    B6 --> B6a2["• Power Supply<br>• Current Meter<br>• EXAMPLE"]
    B7 --> B7a1["Task Examples:<br>• EXAMPLE<br>• EXAMPLE<br>• EXAMPLE"]
    B7 --> B7a2["• EXAMPLE<br>• EXAMPLE<br>• EXAMPLE"]
    B8 --> B8a1["Task Examples:<br>• EXAMPLE<br>• EXAMPLE<br>• EXAMPLE"]
    B8 --> B8a1["• EXAMPLE<br>• EXAMPLE<br>• EXAMPLE"]

    C1 --> C1a["• EXAMPLE<br>• EXAMPLE<br>• EXAMPLE"]
    C2 --> C2a["• EXAMPLE<br>• EXAMPLE<br>• EXAMPLE"]
    C3 --> C3a["• EXAMPLE<br>• EXAMPLE<br>• EXAMPLE"]
    C4 --> C4a["• EXAMPLE<br>• EXAMPLE<br>• EXAMPLE"]
    C5 --> C5a["• EXAMPLE<br>• EXAMPLE<br>• EXAMPLE"]
    C6 --> C6a["• EXAMPLE<br>• EXAMPLE<br>• EXAMPLE"]

    D1 --> D1a["• EXAMPLE<br>• EXAMPLE<br>• EXAMPLE"]
    D2 --> D2a["• EXAMPLE<br>• EXAMPLE<br>• EXAMPLE"]
    D3 --> D3a["• EXAMPLE<br>• EXAMPLE<br>• EXAMPLE"]
    D4 --> D4a["• EXAMPLE<br>• EXAMPLE<br>• EXAMPLE"]
    D5 --> D5a["• EXAMPLE<br>• EXAMPLE<br>• EXAMPLE"]
    D6 --> D6a["• EXAMPLE<br>• EXAMPLE<br>• EXAMPLE"]

    E1 --> E1a["• EXAMPLE<br>• EXAMPLE<br>• EXAMPLE"]
    E2 --> E2a["• EXAMPLE<br>• EXAMPLE<br>• EXAMPLE"]
    E3 --> E3a["• EXAMPLE<br>• EXAMPLE<br>• EXAMPLE"]
    E4 --> E4a["• EXAMPLE<br>• EXAMPLE<br>• EXAMPLE"]
    E5 --> E5a["• EXAMPLE<br>• EXAMPLE<br>• EXAMPLE"]
    E6 --> E6a["• EXAMPLE<br>• EXAMPLE<br>• EXAMPLE"]

      
    style A fill:#87ceeb,color:#000  
    style B fill:#dda0dd,color:#000  
    style C fill:#98fb98,color:#000  
    style D fill:#f0c674,color:#000  
    style E fill:#f08080,color:#000  


    click B "https://github.com/LC-Linkous/reverse_engineering_notes#hardware-analysis"
    click B1 "https://github.com/LC-Linkous/reverse_engineering_notes#physical-device-access"
    click B2 "https://github.com/LC-Linkous/reverse_engineering_notes#circuit-analysis"
    click B3 "https://github.com/LC-Linkous/reverse_engineering_notes#component-id"
    click B4 "https://github.com/LC-Linkous/reverse_engineering_notes#pcb-layout"
    click B5 "https://github.com/LC-Linkous/reverse_engineering_notes#signal-analysis"
    click B6 "https://github.com/LC-Linkous/reverse_engineering_notes#power-analysis"
    click B7 "https://github.com/LC-Linkous/reverse_engineering_notes#side-channel-analysis"
    click B8 "https://github.com/LC-Linkous/reverse_engineering_notes#fault-injection"

    click C "https://github.com/LC-Linkous/reverse_engineering_notes#code-analysis"
    click C1 "https://github.com/LC-Linkous/reverse_engineering_notes#software"
    click C2 "https://github.com/LC-Linkous/reverse_engineering_notes#firmware"
    click C3 "https://github.com/LC-Linkous/reverse_engineering_notes#embedded"
    click C4 "https://github.com/LC-Linkous/reverse_engineering_notes#mobile"
    click C5 "https://github.com/LC-Linkous/reverse_engineering_notes#web-applications"
    click C6 "https://github.com/LC-Linkous/reverse_engineering_notes#malware-analysis"

    click D "https://github.com/LC-Linkous/reverse_engineering_notes#wireless-analysis"
    click D1 "https://github.com/LC-Linkous/reverse_engineering_notes#wifi"
    click D2 "https://github.com/LC-Linkous/reverse_engineering_notes#bluetooth"
    click D3 "https://github.com/LC-Linkous/reverse_engineering_notes#rfidnfc"
    click D4 "https://github.com/LC-Linkous/reverse_engineering_notes#sub-ghzism"
    click D5 "https://github.com/LC-Linkous/reverse_engineering_notes#cellularmobile"
    click D6 "https://github.com/LC-Linkous/reverse_engineering_notes#iot-protocols"

    click E "https://github.com/LC-Linkous/reverse_engineering_notes#network-analysis"
    click E1 "https://github.com/LC-Linkous/reverse_engineering_notes#protocol-analysis"
    click E2 "https://github.com/LC-Linkous/reverse_engineering_notes#packet-capture"
    click E3 "https://github.com/LC-Linkous/reverse_engineering_notes#network-security"
    click E4 "https://github.com/LC-Linkous/reverse_engineering_notes#industrialiot-protocols"
    click E5 "https://github.com/LC-Linkous/reverse_engineering_notes#network-infrastructure"
    click E6 "https://github.com/LC-Linkous/reverse_engineering_notes#network-forensics"


```


### Hardware Analysis

#### Physical Device Access

#### Circuit Analysis

#### Component ID

#### PCB Layout

#### Signal Analysis

#### Power Analysis

#### Side-channel Analysis

#### Fault Injection





### Code Analysis

#### Software


#### Firmware


#### Embedded


#### Mobile


#### Web Applications


#### Malware Analysis

       

### Wireless Analysis


#### WiFi


#### Bluetooth


#### RFID/NFC


#### Sub-GHz/ISM


#### Cellular/Mobile


#### IoT Protocols


### Network Analysis


#### Protocol Analysis


#### Packet Capture

#### Network Security

#### Industrial/IoT Protocols

#### Network Infrastructure

#### Network Forensics


## The Table

## Documentation Methods


## Bookshelf

In this section are a collection of books and websites for further reading. No single reference is a catch-all for any topic, but some of these may prove useful.
(No PDFs are provided through this repository or from the authors of this repository)


**Reverse Engineering**
1. REFERENCE
  * short explanation
2. REFERENCE
  * short explanation
3. REFERENCE
  * short explanation
4. REFERENCE
  * short explanation




**Circuity Basics**
1. REFERENCE
  * short explanation
2. REFERENCE
  * short explanation
3. REFERENCE
  * short explanation
4. REFERENCE
  * short explanation




**Hardware Interfacing Basics**
1. REFERENCE
  * short explanation
2. REFERENCE
  * short explanation
3. REFERENCE
  * short explanation
4. REFERENCE
  * short explanation



**Wireless Basics**
1. REFERENCE
  * short explanation
2. REFERENCE
  * short explanation
3. REFERENCE
  * short explanation
4. REFERENCE
  * short explanation


**SDR Basics**
1. REFERENCE
  * short explanation
2. REFERENCE
  * short explanation
3. REFERENCE
  * short explanation
4. REFERENCE
  * short explanation


**Using Operating Systems**
1. REFERENCE
  * short explanation
2. REFERENCE
  * short explanation
3. REFERENCE
  * short explanation
4. REFERENCE
  * short explanation





## Glossary
This section provides s beginner-friendly launch point to more specific terminology, techniques, and best practices. To keep this accessible, some terms are a bit simplified and may link to other references. 


* WORD OR ABBREVIATION - full spelling if abbreviation. definition or usage. 




## References

**Making Charts and Tables**
1. github markdown tables
2. the mermaid cite
3.
4.


**Popular Tool Purchasing Sites Used for Tool Descriptions and Pricing**
NOTE: This is not an endorsement of any particular vendor, manufacturer, or tool. 



