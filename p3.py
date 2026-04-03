Practical 3
 Implementation of Infrastructure as a Service using Windows HyperV
(Windows Server 2012 R2)



1.	In the VM ware Workstation Create a new Virtual Machine
2.	Click Custom next
3.	Hardware Compatibility - Workstation 14.x
4.	Next
5.	Install from - select I will install Operating Sytem later
6.	Select a Guest OS - select Microsoft Windows & version - Windows Server 2012
7.	Name the Virtual Machine and save it in a new folder 
8.	Firmware type - BIOS
9.	Processor Configuration - 2 & 1
10.	Memory for the VM - 4GB (4096)
11.	Network Type - NAT
12.	Select I/O controller types - LSI Logic SAS (Recommended)
13.	Select a Disk Type - SCSI
14.	Select a Disk - Create a new Virtual disk
15.	Specify Disk Capacity - 60 & Store Virtual disk as a single file
16.	Specify Disk File - Browse and save in the same earlier VM folder
17.	Then Finish


18.	Go to Edit Virtual Machine Settings
19.	Hardware > CD/DVD (SATA) - tick connect at power on
20.	and tick Use ISO image file - 9600.16384.130821...
21.	Then Power on the VM
22.	Then in Language keep  as it is
23.	Click Install Now
24.	Enter the Product Key -  Windows Server 2012 R2 Standard is D2N9P-3P6X9-2R39C-7RTCD-MDVJX (U can find this in the Local server )
25.	Next
26.	Select the  Windows Server 2012 R2 Standard (Server with GUI) > Next
27.	Tick I accept the license terms > Next
28.	Type of Installation - Custom: Install Windows only (advanced)
29.	Next
30.	Create the password then login
31.	From the side panel of this Server manager > Local Server > Properties below you will find Computer Name
32.	Now change the computer name by click and change and then enter the name inside the textbox and click on OK.
33.	Click on OK when it prompts restart the computer and then click on restart now and the step up will be completed.


34.	Now Adding Hyper-V feature in windows server 2012 and create a virtual machine.
35.	Click on manage (Its on right top corner tabs) then click on Add Roles and features.
36.	Select the server and click next.
37.	In Server Roles select Hyper-V then click on Add
38.	features and click on next. (Will not work)


39.	Then Power off the Virtual Machine then go to edit virtual machine settings in that options tab in version select hyper-V (not supported)
40.	Then Now Power on the VM Again try to add the Hyper-V Feature
41.	Tick the Hyper -V > Next
42.	Click Add Feature
43.	Now in Features Tick .NET Framework 3.5 features
44.	Next
45.	Tick the Ethernet0 in Virtual Switches > Next
46.	In Migration tick the checkbox to allow this server to send and receive live migartions of virtual machines > Next
47.	Next
48.	In Confirmation Click on Install
49.	Now Restart the Server
50.	After Power On , Now Login  and Click on tools tab (Its at the right top corner tabs) and select the Hyper-V Manager
51.	Now Right click on the server > New > Virtual Machine
52.	Name the VM > Next
53.	Tick Generation 1 > Next
54.	Change the assign memory to 2048MB > Next
55.	Select The Configure Networking as Intel(R) 82574 Gigabit Network Connection - Virtual Switch
56.	Select the Virtual Hard Disk - Hyper-V (Virtual HArd Disk) and Size - 40GB   > Next
57.	Now In Installation Options Select Install an operating system later    > Next
58.	Finish
59.	Go to the Internet Explorer > Open the Local Server (192.168.2.2)
60.	And Download the en_Windows_7_Ultimate OR the Windows7_all in one (whichever u find)

61.	Assign the ISO File as below -
1.Open Hyper-V Manager.
2.Select the created Virtual Machine from the list.
3.Right-click on the virtual machine and click Settings.
4.In the left panel, select DVD Drive.
5.Choose the option Image file (.iso).
6.Click on Browse and select the ISO file from the drive where u downloaded it.

62.	Select the Virtual Machine and click on start from the right side panel 
63.	Complete the Installation Process 
64.	FINISH










For Viva-
# Practical 3 Viva Questions  
## Implementing IaaS using Windows Hyper-V (Windows Server 2012 R2)  

---

## 1. IaaS and Cloud Concepts  

**Q1. What is Infrastructure as a Service (IaaS)?**  
IaaS provides virtualized computing resources such as servers, storage, and networking over the internet.  

**Q2. What are the main components of IaaS?**  
Virtual machines, storage, networking, and hypervisors.  

**Q3. Give examples of IaaS providers.**  
AWS EC2, Microsoft Azure Virtual Machines, Google Compute Engine.  

---

## 2. Hyper-V Concepts  

**Q1. What is Hyper-V?**  
Hyper-V is a Type 1 hypervisor that enables virtualization on Windows systems.  

**Q2. What type of hypervisor is Hyper-V?**  
Type 1 (bare-metal) hypervisor.  

**Q3. What is the role of Hyper-V in this practical?**  
It is used to create and manage virtual machines on Windows Server.  

---

## 3. Virtualization Concepts  

**Q1. What is virtualization?**  
Virtualization is the creation of virtual versions of physical resources like servers, storage, and networks.  

**Q2. What are the advantages of virtualization?**  
Efficient resource utilization, cost reduction, scalability, and isolation.  

**Q3. What are the types of virtualization?**  
Server virtualization, storage virtualization, and network virtualization.  

---

## 4. Windows Server Concepts  

**Q1. What is Windows Server 2012 R2?**  
A server operating system used to manage network resources and services.  

**Q2. What is the purpose of Server Manager?**  
To manage server roles, features, and configurations.  

**Q3. What are server roles and features?**  
Roles provide core functions (like Hyper-V), while features add additional capabilities (.NET Framework, etc.).  

---

## 5. Virtual Machine Concepts  

**Q1. What is a virtual machine?**  
A software-based system that behaves like a physical computer.  

**Q2. What is Generation 1 and Generation 2 VM in Hyper-V?**  
Generation 1 uses BIOS-based boot  
Generation 2 uses UEFI-based boot  

**Q3. What is virtual hard disk (VHD)?**  
A file that stores the data of a virtual machine.  

---

## 6. Resource Management  

**Q1. What resources are allocated in Hyper-V?**  
CPU, memory, storage, and network.  

**Q2. What is dynamic memory in Hyper-V?**  
A feature that automatically adjusts RAM allocation based on VM needs.  

**Q3. What is virtual switch in Hyper-V?**  
A software-based network switch used to connect virtual machines.  

---

## 7. Networking Concepts  

**Q1. What is virtual networking in Hyper-V?**  
It allows communication between VMs and external networks.  

**Q2. Types of virtual switches in Hyper-V**  
External, Internal, and Private  

**Q3. Why is networking important in IaaS?**  
It enables communication between virtual machines and external systems.  

---

## 8. Comparison-Based Questions  

**Q1. Difference between Hyper-V and VMware ESXi**  
- Hyper-V → Developed by Microsoft  
- ESXi → Developed by VMware  

**Q2. Difference between Hyper-V and Xen Server**  
- Hyper-V → Microsoft-based  
- Xen Server → Citrix-based  

**Q3. Difference between physical and virtual machine**  
- Physical → Dedicated hardware  
- Virtual → Shared resources via hypervisor  

---

## 9. Advantages and Limitations  

**Q1. Advantages of Hyper-V**  
Cost-effective, integrated with Windows, scalable  

**Q2. Limitations of Hyper-V**  
Requires Windows environment, performance overhead in nested setup  

**Q3. Advantages of IaaS**  
Scalable, flexible, reduces hardware cost  

---

## 10. Final Conceptual Question  

**Q. Explain how Hyper-V supports IaaS.**  
Hyper-V virtualizes hardware resources and allows multiple virtual machines to run independently on a server. This enables users to access computing resources on demand, which is the core concept of IaaS.  

---
