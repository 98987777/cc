Practical 2
Xen Server and Windows 7 Installation
1.	Go to the Workstation Pro
2.	Home Tab 
3.	Click Custom next
4.	Next
5.	Next
6.	Install from - select I will install Operating Sytem later
7.	Select linux and version ubuntu 64 bit
8.	Click on browse and create new folder name Cetrix and next
9.	Next
10.	Change the Memory for Virtual Machine to 6000 and next
11.	Next
12.	Next
13.	Next
14.	Next specify disk capacity 60 and select option store and next
15.	Specify Disk Capacity select option Split virtual disk into multiple files and Next
16.	Browse to the Folder created and save and Next
17.	Finish
18.	Go to the local server > soft > cloudcomputing > XenServerClient > Install both the files
19.	Then Go to edit virtual machine settings
20.	CD/DVD > Use ISO image file and browse to this XenServer-6.2.0-install-cd.iso
21.	Power On the Virtual Machine
22.	Tab to click ok
23.	Then again click on OK
24.	Accept EULA and then ok
25.	Ok
26.	Ok
27.	Ok
28.	Ok
29.	supplement yes
30.	Select Skip verification and then ok
31.	Give password 123456
32.	Nothing in network Then ok
33.	Tick Manually specify and and keep xenserver only else remove the text
34.	Ok
35.	Select Asia and Calcutta and ok
36.	Ok
37.	Ok
38.	Then Install XenServer
39.	Ok
40.	Go to network and management interface and see the IP address
41.	Check virtualize intel VT option 1 from processors<settings in both the Workstation machine and the Citrix Zen Server


Another Virtual Machine
42.	Now Again in the Workstation Create a new Virtual Machine
43.	Click Custom next
44.	Next
45.	Next
46.	Install from - select I will install Operating Sytem later
47.	Select a Guest OS - select Microsoft Windows & version - Windows 7 64x
48.	Name the Virtual Machine and save it in a new folder 
49.	Firmware type - BIOS
50.	Processor Configuration - 1 & 1
51.	Memory for the VM - 2048
52.	Network Type - NAT
53.	Select I/O controller types - LSI Logic SAS (Recommended)
54.	Select a Disk Type - SCSI
55.	Select a Disk - Create a new Virtual disk
56.	Specify Disk Capacity - 60 & Store Virtual disk as a single file
57.	Specify Disk File - Browse and save in the same earlier VM folder
58.	Then Finish
59.	Go to Edit Virtual Machine Settings
60.	Hardware > CD/DVD (SATA) - tick connect at power on
61.	and tick Use ISO image file - en_windows_7_ultimate...
62.	Then Power on the VM
63.	Then in Language keep  as it is
64.	Click Install Now
65.	Tick I accept the license terms
66.	In Which type of installlation do you want? Choose Custom
67.	Next
68.	Give the user name and Computer name and make sure to remember 
69.	Type a Password (eg - 1234567)
70.	Skip the Product Key
71.	Then Select Ask Me Later
72.	Select Time Zone - Chennai, Mumbai, New Delhi
73.	Select Home Network
74.	Then After the Starting the Windows go to File explorer
75.	Go to Local Disk (C:) and Create a new folder and name it ISO Library
76.	Right click on the ISO Library Folder > Properties > Go to sharing tab 
77.	Click on Share
78.	Click on the Dropdown and select Everyone and Add it and then Click share
79.	Click on windows and search and open Control Panel > System and Security > Windows Firewall > from the right side panel click Turn Windows Firewall on or off 
80.	Then Under Home or work (Private) network location settings > Turn off
81.	Public network location settings > keep as it is Turn On



Now in Citrix Xen Center
82.	Installing Xen Center Client 
83.	Open and Click on Add New Server
84.	Add the Server IP address, username, password and add it
85.	Then Go to the Storage tab in the Xenserver itself (Not on the Citrix Xen Center application storage tab)
86.	Click on the New SR
87.	Select - ISO Library > Windows File sharing (CIFS)
88.	Next
89.	Name it as CIFS ISO Library
90.	Next
91.	Then when Earlier in the another windows virtual machine we created earlier where we create a folder as ISO Library in that Sharing Properties 
92.	In that Network Path Put that path in this Location > Share Name > (eg. - \\ROOTS\ISO Library) (ROOTS is Computer Name)
93.	Tick the Use Different User name and put the User name of that Windows Virtual Machine and Password of that same
94.	then Finish
95.	DONE





For Viva-
# Practical 2 Viva Questions  
## Implementing IaaS using Citrix Xen Server  

---

## 1. IaaS and Cloud Concepts  

**Q1. What is Infrastructure as a Service (IaaS)?**  
IaaS provides virtualized computing resources such as servers, storage, and networking over the internet.  

**Q2. What are the key features of IaaS?**  
On-demand resource allocation, scalability, pay-as-you-use model, and virtualization.  

**Q3. Give examples of IaaS platforms.**  
AWS EC2, Microsoft Azure Virtual Machines, Google Compute Engine.  

---

## 2. Xen Server Concepts  

**Q1. What is Citrix Xen Server?**  
Citrix Xen Server is a Type 1 (bare-metal) hypervisor used to create and manage virtual machines.  

**Q2. What type of hypervisor is Xen Server?**  
Type 1 hypervisor.  

**Q3. What is the Xen Hypervisor?**  
A virtualization layer that allows multiple operating systems to run on a single physical machine.  

---

## 3. Virtualization Concepts  

**Q1. What is virtualization?**  
Virtualization is the process of creating virtual versions of hardware resources like servers, storage, and networks.  

**Q2. What are the advantages of virtualization?**  
Efficient resource usage, cost reduction, scalability, and isolation.  

**Q3. What are the types of virtualization?**  
Server virtualization, storage virtualization, network virtualization.  

---

## 4. Resource Management  

**Q1. What resources are provided in IaaS?**  
CPU, memory, storage, and networking.  

**Q2. How does a hypervisor manage resources?**  
It allocates and controls hardware resources among multiple virtual machines.  

**Q3. What is resource allocation in virtualization?**  
Assigning CPU, RAM, and storage to virtual machines.  

---

## 5. Storage Concepts  

**Q1. What is a Storage Repository (SR)?**  
A storage location where virtual machine disks and ISO files are stored.  

**Q2. What is an ISO file?**  
A disk image file used to install an operating system.  

**Q3. What is shared storage in virtualization?**  
Storage accessible by multiple virtual machines or servers over a network.  

---

## 6. Networking Concepts  

**Q1. What is virtual networking?**  
A network created within a virtual environment to connect VMs.  

**Q2. What is NAT in virtualization?**  
A method that allows VMs to access external networks using the host system’s IP address.  

**Q3. Why is networking important in IaaS?**  
It enables communication between virtual machines and external systems.  

---

## 7. Management Tools  

**Q1. What is Xen Center?**  
A management tool used to monitor and control Xen Server and its virtual machines.  

**Q2. Why are management tools required in IaaS?**  
To manage, monitor, and control virtual resources efficiently.  

---

## 8. Comparison-Based Questions  

**Q1. Difference between Xen Server and VMware ESXi**  
- Xen Server → Open-source (Citrix)  
- ESXi → Proprietary (VMware)  

**Q2. Difference between Type 1 and Type 2 hypervisor**  
- Type 1 → Runs directly on hardware  
- Type 2 → Runs on host operating system  

---

## 9. Advantages and Limitations  

**Q1. Advantages of IaaS**  
Scalability, cost-effectiveness, flexibility, and remote access.  

**Q2. Limitations of IaaS**  
Security concerns, dependency on internet, and technical complexity.  

**Q3. Advantages of Xen Server**  
High performance, open-source, efficient virtualization.  

---

## 10. Final Conceptual Question  

**Q. Explain how Xen Server supports IaaS.**  
Xen Server acts as a hypervisor that virtualizes hardware resources and allows multiple virtual machines to run independently. This enables users to access infrastructure like servers and storage on demand, which is the core concept of IaaS.  

---
