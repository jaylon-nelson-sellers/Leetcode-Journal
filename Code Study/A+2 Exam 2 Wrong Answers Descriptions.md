# Q2
You need to run Disk Defragmenter, but several other applications are running. Why should you shut down all running applications first?

- **A) Disk Defragmenter requires exclusive access to drives.**
    
- **B) Running other applications may result in disk write operations forcing Disk Defragmenter to restart continually.**
    
- **C) If the other applications are running, Disk Defragmenter offers to run at the next bootup time.**
    
- **D) Running applications prevent Disk Defragmenter from being launched.**
    

### Explanation

Running other applications may result in disk write operations, forcing Disk Defragmenter to restart continually. Disk Defragmenter reorders file contents on the disk in an attempt to store each file in a contiguous sequence of disk storage blocks. Any application that is running and writing data to the disk may disrupt the ordering carried out by Disk Defragmenter and force the defragmentation process to be restarted.

You can open Disk Defragmenter by typing dfrgui.exe at the Run command prompt or by choosing Defragment and Optimize Drives from the Windows Administrative Tools app.

Disk monitoring and antivirus applications, both of which continuously monitor disks, frequently cause Disk Defragmenter to restart several times. The Terminate and Stay Resident (TSR) applications used with MS-DOS had a similar effect. TSR programs were designed to run in the background and disrupt the many maintenance programs, causing them to restart.

Disk Defragmenter does not require exclusive access to drives. Disk Defragmenter can run concurrently with other applications that are accessing the drives. The CHKDSK utility requires exclusive drive access while checking boot drives.

In a multitasking operating system, such as Windows, the launch of an application is not prevented by other running applications.

Disk Defragmenter does not offer to run at the next bootup time if other applications are running. This behavior is exhibited by the disk maintenance program named CHKDSK while checking boot drives. CHKDSK cannot run without exclusive access to drives. If CHKDSK encounters open files, it cannot proceed. In either situation, CHKDSK typically offers to reschedule its run to the next bootup to gain exclusive disk access without being hindered by open files.

A+ technicians are expected to understand and be able to implement preventative maintenance procedures that include the following:

- **Scheduled backups** – Backups can be scheduled using Task Scheduler (taskschd.msc), the Backup utility, or a third-party solution. Backups should be implemented on a regular basis. Backups should occur at a time when the computer demands are the lowest, usually when the user is not at the computer. Backups should periodically be tested to ensure that they can be restored. In addition, selected backups should be stored offsite to ensure that the data can be restored in the event of a natural disaster. In most cases, backups are performed on a daily or weekly basis, depending upon the value of the data.
    
- **Scheduled check disks** – The chkdsk utility is used to check the disk for errors. This utility is usually scheduled to run using Task Scheduler. In most cases, disks are checked for errors on a weekly or monthly basis.
    
- **Scheduled defragmentation** – The defrag utility (dfrgui.exe) is used to defragment the hard drive. This utility is usually scheduled to run using Task Scheduler. When the defragmenter is executed, it first performs a test to see if a defragmentation is necessary. In most cases, disks are defragmented on a weekly or monthly basis.
    
- **Windows Updates** – Windows Updates are vital to any Windows computer. Windows updates allow you to determine how often you want to check for updates and how the updates will be downloaded and/or installed. In most cases, Windows Updates are downloaded and installed automatically. In some corporate environments, a Windows Updates server will be deployed to ensure that Windows Updates are deployed in a more centralized manner.
    
- **Patch management** – All applications will need security updates and other patches. It is important to maintain all applications in a timely manner. You should be familiar with the proper procedure for downloading and installing the latest patches. Vendor Web sites should be monitored for application updates. Always test the latest patches before installing to production.
    
- **Driver/firmware updates** – Periodically hardware vendors will release new drivers and/or firmware. The latest driver or firmware should be installed when it is released. Always test the latest drivers and firmware before installation to production.
    
- **Antivirus updates** – All computers should be protected with antivirus software. Antivirus software requires that you periodically update the software with the latest virus definitions from the antivirus vendor. Most antivirus applications have a built-in feature that checks for updates automatically. Users should be educated on the important of the antivirus updates. The latest updates should be installed when they are released.
# Q4
An IT department plans to upgrade its endpoint protection software across all employee workstations. The deployment is scheduled two weeks from now, with testing to be completed in a lab environment to minimize disruption. However, a new vulnerability was just reported, and the security team has requested that a last-minute patch be deployed to live systems by the same department as soon as possible.

Which of the following change management terms most accurately describe these respective updates? (Choose two.)

- **A) Change freeze**
    
- **B) Standard change**
    
- **C) Maintenance window**
    
- **D) Normal change**
    
- **E) Emergency change**
    

### Explanation

The respective updates are best described as a standard change for the scheduled deployment and an emergency change for the vulnerability patch.

Standard changes are pre-approved, low-risk updates that follow established procedures and require minimal oversight. These are typically repeatable changes, such as antivirus updates or printer driver deployments, that have already gone through risk analysis and peer review. The endpoint protection upgrade, which was scheduled in advance and tested thoroughly, falls into this category.

Emergency changes, by contrast, are unplanned but critical. They are implemented quickly in response to pressing issues, such as a zero-day vulnerability or system outage. The last-minute patch requested by the security team is an emergency change. Emergency changes often bypass some steps in the formal approval process, but are still logged and reviewed after implementation.

A normal change is a planned, non-emergency update that goes through full documentation, approval, and testing before implementation. While the antivirus upgrade may seem to qualify, it has already been predefined and is repeatable, placing it in the standard category instead.

A change freeze is a designated period when no changes may be implemented—often during critical business cycles or end-of-year processing. There is no mention of such a restriction in this scenario.

A maintenance window refers to the predefined period during which changes are allowed to occur—typically during off-hours. While relevant to scheduling, it does not classify the nature of the change itself.

For the exam, you should also understand the role of peer review. A peer review is an essential step in change management, particularly for normal and standard changes. Before implementation, proposed changes are reviewed by colleagues or cross-functional team members to validate the scope, risk level, impact, and rollback plans. This collaborative scrutiny reduces the likelihood of unintended consequences and helps ensure that changes align with organizational policies and security standards.

# Q10
You suspect that a Windows 10 computer has been infected with a Trojan horse. You need to determine if any Trojan horses are loading at system startup and remove them. Which tool should you use to find out if any Trojan horses are being loaded at startup?

- **A) Windows Recovery Environment**
    
- **B) Anti-malware software**
    
- **C) Settings**
    
- **D) SYSTEM Restore**
    

### Explanation

If you need to determine if a Trojan horse is loading at system startup, you should use Settings. Then select Apps and Startup. Check each application shown in the list to ensure that it is a valid application you need. As shown in the following exhibit, you can prevent an application from loading at startup simply by turning off the application:

The Task Manager can also be used to Disable startup applications.

Keep in mind, however, that this does not remove the Trojan horse from the computer. It just keeps it from loading at startup.

Anti-malware software does not remove Trojan horses from startup, which is what was requested in the scenario. The anti-malware software may be able to remove the Trojan horse from the system itself, but you should make sure that the anti-malware software is updated to ensure that it is capable of detecting the newest threats that have emerged.

System Restore restores a computer to a previously saved state. It does not remove Trojan horses from computer startup, especially if the Trojan were included in the restore image.

The Windows Recovery Environment is a recovery environment that can repair common causes of unbootable operating systems. It does not remove Trojan horses from computer startup.

# Q13
Your company has decided it wants to implement multi-factor authentication. From the options given, what is the BEST implementation you should deploy?

- **A) smart cards, usernames, and strong passwords**
    
- **B) smart cards, usernames, and PIN**
    
- **C) usernames, strong passwords, and PIN**
    
- **D) biometrics, smart cards, and strong passwords**
    

### Explanation

You should deploy biometrics, smart cards, and strong passwords. This covers three different factors of authentication: something you are (biometrics), something you have (smart cards), and something you know (passwords.)

Biometrics devices help verify users' identities against unique physical characteristics. Biometric devices include retinal scanners, hand scanners, and fingerprint.

Smart cards, which are a type of identification badge, are used to give people access to buildings, doors and computers and parking lots. Smart cards are inserted into a computer or a smart card reader. Since they can be easily stolen or duplicated, modern smart cards typically require users to enter passwords or PINs to activate them.

Usernames, strong passwords, and a PIN are all things you know, so this solution would not be considered multifactor authentication.

Smart cards, usernames, and strong passwords only include two factor types: something you have and something you know.

Smart cards, usernames, and PINs only include two factor types: something you have and something you know.

# Q19
You open Device Manager and notice a red X next to your wireless network adapter. What does this indicate?

- **A) The adapter is disabled.**
    
- **B) The adapter is experiencing a resource conflict.**
    
- **C) The adapter was not installed properly.**
    
- **D) The adapter's drivers need to be reinstalled.**
    

### Explanation

A red X next to a device in Device Manager indicates that the device is disabled. You could also see a black down arrow in a circle, depending on the operating system version you have.

A yellow exclamation point indicates that the device has a problem. This problem is usually either a resource conflict or device driver issue. Error codes for the device can be viewed on the Properties page of the device.

A blue I indicates you need to view the device information. This notification is due to the operating system forcing the resource configuration.

A yellow exclamation point (!) indicates that a resource conflict is occurring. A problem code is given to explain the problem. The device may be operational. If the device is operational, many of its capabilities may not work until the resource conflict is resolved.

A green question mark (?) indicates that a compatible driver is not installed and some functionality may be disabled until the updated driver is installed.

The two most common wireless network issues occur when the wireless access point is turned off and when the computer's wireless network interface is disabled.

# Q21
A user reports that their web browser is opening tabs without input and redirecting them to suspicious websites. You observe additional behavior, including pop-ups and unauthorized extensions. Which of the following should you do first?

- **A) Identify and research the malware symptoms.**
    
- **B) Schedule a malware scan and run updates.**
    
- **C) Remediate the infected system.**
    
- **D) Enable System Restore, and create a restore point.**
    

### Explanation

The first step in any malware removal process is to identify and research the malware symptoms. Before taking any action, you would document what the user has experienced and observe any additional indicators such as suspicious processes, browser redirects, or unauthorized software. Gathering this information helps determine the type of malware involved and find the most effective response strategy.

In a later step, you would remediate the infected system. This step is taken only after isolation and backups have occurred and a plan established. Based on the findings, your next step might be to run an immediate anti-virus or anti-malware scan, disconnect the system from the Internet, examine and edit the registry, or other appropriate remediation steps.

You would enable System Restore and create a restore point as part of the preparation before making system changes, but it is not appropriate until the threat has been fully understood.

You would schedule scans and run updates in a follow-up step to ensure that all antivirus tools and definitions are current, often done before or after remediation.

For the exam, you are expected to understand CompTIA's sequence to follow when removing small office/home office (SOHO) malware and what happens in each step. The following is a sequential list of steps with explanations:

1. **Investigate and verify malware symptoms** – The first step in the malware removal process is to gather as much information as possible. This includes talking to the user, observing system behavior, and identifying any obvious signs of infection such as pop-ups, slow performance, or unauthorized programs. Researching the symptoms helps determine the type of malware and guides the next steps in the response.
    
2. **Quarantine the infected system** – Once an infection is suspected, isolating the affected system is critical to prevent the malware from spreading across the network or infecting other systems. Quarantine may involve disconnecting the device from Wi-Fi or Ethernet, disabling file sharing, or moving the device to a separate VLAN or network segment.
    
3. **Disable System Restore (in Windows Home)** – Before attempting to remove malware, it is important to disable System Restore. Some malware embeds itself in restore points, which could cause the infection to return if the system is rolled back. Disabling System Restore ensures that the malware cannot persist through restoration.
    
4. **Remediate the infected system** – This step involves removing the malware using appropriate tools. Remediation may include running antivirus or antimalware scans, using bootable rescue environments, or performing manual removal steps. In some cases, it may involve reimaging the system or reinstalling the OS if the infection is deeply embedded.
    
5. **Update anti-malware software** – After removing the malware, update the anti-malware software to ensure that the latest virus definitions and scanning engines are in place. This helps detect any lingering threats and improves protection against new ones. Updated tools increase the effectiveness of final scans and long-term system security.
    
6. **Scan and removal techniques (e.g., safe mode, preinstallation environment)** – Use specialized tools and environments to perform deep system scans and removal. Safe Mode loads minimal services, making it easier to detect and eliminate stubborn malware. For advanced infections, a bootable preinstallation environment may be required. These techniques improve accuracy and reduce interference from active threats.
    
7. **Reimage/reinstall** – If the malware cannot be fully removed or the system remains unstable, reimaging or reinstalling the operating system is the most reliable option. This process replaces the compromised system with a clean, known good version. It ensures complete removal of persistent threats such as rootkits or deeply embedded infections. Always restore from trusted sources and follow up with updates.
    
8. **Schedule scans and run updates** – After the system is clean and stable, schedule regular malware scans to maintain ongoing protection. Ensure the operating system and applications are fully updated with the latest patches. Automatic updates reduce exposure to known vulnerabilities. This step helps prevent reinfection and supports long-term system health.
    
9. **Enable System Restore, and create a restore point (in Windows Home)** – Once the system is verified clean, re-enable System Restore and create a fresh restore point. This provides a secure fallback in case future issues occur. Creating a restore point after cleanup ensures that no infected files are included. It is a key step before returning the system to regular use.
    
10. **Educate the end user** – Training the user on safe computing practices is a critical final step. This may include recognizing phishing emails, avoiding untrusted downloads, and updating software regularly. Educating users helps prevent future infections and promotes a culture of security awareness.

# Q24
A user working on a document in Pages on their iPad realizes it would be much easier if they changed over to their full-size Mac with an ergonomic keyboard. They do not want to manually transfer the file. They also appreciate being able to make and receive phone calls and text messages on their Mac using their iPhone's cellular connection. Which macOS feature enables this level of integration across Apple devices?

- **A) AirDrop**
    
- **B) Continuity**
    
- **C) iCloud Keychain**
    
- **D) Handoff**
    

### Explanation

Continuity is a suite of features in macOS and iOS/iPadOS that allows seamless transitions and integration between Apple devices signed in with the same Apple ID. Key Continuity capabilities include:

- **Handoff**, which lets users start a task on one device and pick it up instantly on another (e.g., editing a document or browsing a website).
    
- **Phone and SMS relay**, allowing users to make and receive cellular calls and texts from their Mac using their iPhone.
    
- **Universal Clipboard**, which enables copying on one Apple device and pasting on another.
    
- **Instant Hotspot**, for quickly sharing the iPhone's Internet connection.
    
- **Continuity Camera**, for taking photos or scanning documents with an iPhone and inserting them directly into macOS apps.
    

These features rely on Bluetooth, Wi-Fi, and iCloud to maintain a continuous experience across Apple's ecosystem.

AirDrop is used for nearby file sharing but does not allow task continuity or communication relay.

iCloud Keychain stores and syncs passwords and secure data across Apple devices but is not involved in device-to-device task continuity.

Handoff is part of Continuity but only represents one feature within the larger suite. It does not include call and message integration or clipboard sharing on its own.

# Q28
What is the correct order of steps for the basic boot process of a Linux machine? Choose the correct steps from the left and place them into the correct order on the right.

The correct order is:

1. BIOS
    
2. POST
    
3. MBR
    
4. GRUB
    
5. Primary Partition
    
6. Stage 2 Bootloader
    

The Basic Input/Output System (BIOS) is a fragment of code stored on a non-volatile memory, like ROM or EEPROM. This code is executed when the computer is booted. It does a Power-On Self-Test (POST), which checks system integrity including the BIOS itself, CPU registers, DMA, interrupt controllers, and system timer. Then it loads the first sector from the master boot record (MBR) on the boot drive.

The MBR contains a partition table and bootloader code. The purpose of a bootloader is to load the Linux kernel. The older Linux bootloader was Linux Loader (LILO), which has been replaced by Grand Unified Bootloader (GRUB) and now GRUB2. GRUB is a bootloader, its code is executed by the BIOS, and it is called the stage 1 bootloader. The GRUB is a bootloader program that allows a user to choose from different boot options. GRUB is installed into the MBR of a bootable hard drive or the partition boot record of a partition.

The MBR code then looks for a primary partition on the boot drive. Then the MBR loads the first sector of the primary partition. This has a piece of code that is executed and is called the partition boot record. The partition boot record loads a new set of code for execution called stage 2 bootloader, which loads the complete operating system. MBR only supports one active primary partition. This becomes a problem when you need several operating systems on your computer.

For the Linux+ exam, you need to know how to boot a Linux system from other boot sources, such as booting from a universal serial bus (USB) drive or booting from ISO.

To boot from an ISO image, you need to have Linux installed on a hard drive and the machine also needs to have the GRUB2 bootloader on it. The ISO file you use for booting needs to be a Linux CD release that is live. You can download the ISO files from the Ubuntu, RedHat, Debian, and LinuxMint sites. You then need to determine the partition path for the hard drive. In GRUB terminology, (hd0,1) refers to the first partition (1) of the first hard disk (hd0). You can use the fdisk –l to view a listing of Linux device paths. Next, you need to add a custom boot entry to GRUB by editing the /etc/grub.d/40_custom script. To do this, you can run the following command to edit the file as root:

`$ sudo gedit /etc/grub.d/40_custom`

In this file you will then make several entries that include the following for booting an Ubuntu distribution from an ISO file:

Finally, you need to update GRUB by running the update-grub command. After you do this, you will see an option to boot form the ISO when you boot up the system.

To boot from a USB drive, you need a bootable USB drive. For this you can use Etcher or use the command line.

You can first download the Linux ISO you want to use and then begin the process of creating a bootable USB drive.

One way to do this is using Etcher which is an open-source utility. You download and run Etcher and then connect the USB drive to the computer. In the Etcher window, you select the ISO image you want to use and then select the Flash image button. This creates a bootable USB drive.

You can also create a bootable USB drive for Linux using the dd tool. For this you first insert the USB drive into the computer and run the lsblk command which will indicate the name of the USB drive under the /dev/sdx entry. You then unmount the USB drive using the unmount command. You can then flash the Linux ISO to the USB drive using the following command:

`$ sudo dd bs=4M if=/path/to/ubuntu-22.04.1-desktop-amd64.iso of=/dev/sdx status=progress oflag=sync`

It is important to remember that hackers and crackers usually target the root account on a Linux system through SSH for unauthorized access. A root account with SSH enabled and Internet connectivity can pose a huge security risk to the system. So, to ensure the security of a server, an SSH root account needs to be _disabled_. To do this, first log in as root:


# Q34

A user contacts you stating that he believes that his computer is infected with malware. Which symptoms may indicate that he is correct? (Choose all that apply.)

- **A) pop-ups**
    
- **B) junk email**
    
- **C) security alerts**
    
- **D) browser redirection**
    
- **E) low disk space warning alert**
    
- **F) slower performance**
    

### Explanation

The following symptoms may indicate that a computer is infected with malware:

- pop-ups
    
- browser redirection
    
- security alerts
    
- slow or degraded browser performance
    

Another browser related symptom that you will need to be aware of for the A+ exam are certificate warnings. Certificate warnings are used to notify a user that the site they are attempting to access has a certificate that is either invalid or is not recognized. The purpose of these messages is to warn a user about a potentially malicious site that may be attempting to collect personal information or install malware. However, errors can occur where valid sites are not recognized and are flagged as dangerous. If this error occurs, the user can either set the site manually as a genuine safe site or download the impacted site’s security certificate themselves.

A low disk space warning alert is not generally a symptom of malware infection. The minimum amount of hard drive space for optimal performance is 200 MB.

Junk email is not usually a sign of malware infection.

# Q37
What should be your primary consideration when upgrading from Windows 10 to Windows 11?

- **A) Prerequisites/hardware compatibility**
    
- **B) Load alternate third-party drivers when necessary**
    
- **C) Time/date/region/language settings**
    
- **D) OS compatibility/upgrade path**
    

### Explanation

Your primary consideration when upgrading from Windows 10 to Windows 11 should be the OS compatibility/upgrade path. Microsoft no longer supports upgrades from versions prior to Windows 10 to Windows 11. Further, support for Windows 10 is scheduled (at the time of this writing) to end in October 2025.

There may be times when you need to load alternate third-party drivers. An example of when this might be necessary is if you used the factory recovery partition to rebuild the operating system but you have a newly released multifunction printer. However, third-party drivers are not the primary consideration when upgrading Windows.

Time/date/region/language settings allow you to provide the user with settings that are relevant to their location. Time settings adjust to the time zone, date formats vary with countries, and language settings allow for alternate spellings, special keyboard characters and currency symbols. These settings generally move over from one version of Windows to the next.

Prerequisites and hardware compatibility are also issues. It is best to use the Compatibility Troubleshooter on the system prior to running the upgrade. The Compatibility Troubleshooter will identify issues and potential issues with devices, among other things. But hardware compatibility should be a secondary concern after determining OS compatibility.

# Q38
Which of the following file systems was specifically developed by Microsoft to provide enhanced data integrity, automatic error correction, and support for very large volumes?

- **A) exFAT**
    
- **B) NTFS**
    
- **C) ReFS**
    
- **D) APFS**
    

### Explanation

Resilient File System (ReFS) is a proprietary file system developed by Microsoft to provide high availability and data integrity, especially in enterprise and server environments. ReFS was designed to overcome the limitations of older file systems by supporting extremely large volume sizes (up to 35 petabytes), integrating automatic error detection and correction using checksums, and enabling features like real-time data scrubbing. Unlike NTFS, ReFS can detect silent data corruption and correct it without user intervention when used with Storage Spaces. It also offers improved performance and scalability for data-intensive applications and is typically used in conjunction with Windows Server and advanced storage scenarios.

New Technology File System (NTFS) is the default file system for modern Windows installations and supports permissions, encryption, compression, and large volume sizes. However, it does not offer the same built-in resiliency and self-healing features that ReFS does. While robust enough for desktop use, NTFS is not as fault-tolerant under large-scale or enterprise workloads as ReFS.

Extended File Allocation Table (exFAT) was created by Microsoft for use with USB flash drives and external storage. It supports larger file sizes than FAT32 and cross-platform compatibility, particularly with macOS and Windows. However, it lacks support for features like journaling, permissions, and error correction, making it unsuitable for enterprise or mission-critical use.

Apple File System (APFS) is a proprietary file system developed by Apple and used on macOS, iOS, iPadOS, and other Apple devices. It is optimized for flash and SSD storage and supports features such as snapshots, cloning, and strong encryption. However, APFS is not compatible with Windows systems and is not designed for large-scale server environments like ReFS is.

# Q40
Alan of Northern Company is travelling to several conferences in various states to present his new product line to consumers. When he left the last site, he packed the SlimPort he uses to project from his Android, but forgot his other cables.. His next presentation is in four hours. What can he request from the hotel technical team to keep the show rolling for Alan? (Choose two.)

- **A) a Miracast or Chromecast**
    
- **B) a Micro HDMI cable**
    
- **C) an HDMI cable**
    
- **D) a mini USB cable**
    

### Explanation

Alan should request an HDMI cable, which will connect to his Slimport device or a Chromecast or Miracast.

The other two options do will not work his current configuration.

Users frequently complain that they cannot broadcast to an external monitor. There are many ways to troubleshoot the issue. If the mobile device is connecting to an external monitor via a cable connection, you should ensure that the resolution is configured to one that is compatible with the monitor and that the correct cable is used. If the mobile device is connecting to an external monitor via a wireless connection, you should ensure that the connection is properly established and that the resolution is configured to one that is compatible with the monitor. You also may have to figure out the key combination or gesture that will ensure that the display is sent to the external device.

Another common issue is lack of sound from the speakers. Mobile devices can be accidentally put into silent mode, which keeps sound from coming from the speakers and headphones or to other connected devices. The easiest way to troubleshoot this is to check whether silent mode has been enabled. If not, restarting the device will usually restore the sound.

# Q41
According to your organization's data backup policy, you must keep track of the number and location of backup versions of the organization's data. What is the main purpose of this activity?
A) to ensure proper disposal of information
B) to demonstrate due diligence
OC) to create an audit trail
XOD) to restrict access to the backup versions
### Explanation
The main purpose of keeping track of the number and location of backup versions is to ensure proper disposal of information.
To restrict access to the backup version, you should implement the appropriate access and physical controls.
To create an audit trail, you should enable event or audit logging.
To demonstrate due diligence, you need to retain event and audit logs.
For the A+ exam, you need to understand the following data destruction or disposal methods:
• Low-level format versus standard format - A standard format marks space that is occupied by data as being available, but it does not actually erase the existing data. A low-level format completely cleans the disk, ensuring that all existing data is removed. Low-level formats are performed by the disk manufacturer.
• Drive wipe - This sanitation method erases the contents of the hard drive. This method is not foolproof. If you truly must ensure that data cannot be retrieved, you should destroy the media.
• Physical destruction methods - There are several different physical hard drive destruction methods that are used, including the following:
• Shredder - This is an accepted method for destroying CDs and DVDs. However, to shred hard drives, you would need access to an expensive hard drive shredder.
• Drill/hammer - After disassembling the physical hard drive, you could use a drill, hammer, or sander to turn the shiny surface of the hard drive platters into dust. Make sure to wear both eye and nose protection. This process is very time-consuming.
• Electromagnetic - This method uses strong magnets to destroy the magnetic media. A degaussing tool is actually a type of electromagnetic destruction method. Degaussing tool - This tool is a type of electromagnetic destruction tool. They range from $500 for a wand degausser to $30,000 for a desktop degausser. • Incineration – This destroys the drive by burning it.
• Certificate of destruction - Many companies offer drive destruction services and will provide a certificate of destruction for any drives sent to them. This is preferred for drives that contain highly classified information.

# Q44
An IT technician reports that he ran the sfc utility on a user's computer. Why would this utility be used?

- **A) It repopulates the dllcache folder when contents are corrupted.**
    
- **B) It monitors changes to protected system files.**
    
- **C) It lists information about drivers running on a computer.**
    
- **D) It detects signed and unsigned device drivers on a computer.**
    

### Explanation

The System File Checker (sfc) utility repopulates the dllcache folder when the contents are corrupt. 
The Windows File Protection (wfp) service monitors changes to protected system files. The Driver Query tool lists information about drivers running on your computer. The File Signature Verification tool detects signed and unsigned device drivers on your computer.

# Q50
You are managing IT infrastructure changes. You need a centralized tool to store information about the relationships between components and their dependencies, so you can easily analyze the impact of future changes. Which of the following systems or tools should you use?

- **A) Standard operating procedure**
    
- **B) Configuration management database**
    
- **C) Asset management life cycle tools**
    
- **D) Inventory management software**
    

### Explanation

You should use a configuration management database (CMDB). A CMDB is a centralized repository that stores information about your IT assets, including details on relationships between and dependencies among the components. Software, hardware, systems (such as clusters or RAID configurations), personnel, and facilities can all be linked in a CMDB. Doing so enables organizations to effectively manage IT infrastructure changes, analyze the potential impact of modifications, and maintain an accurate overview of their IT environment.

Asset management life cycle tools help organizations track and manage the life cycle of their IT assets from acquisition and deployment to maintenance and disposal. While these tools provide valuable insights into asset usage and financial implications, they do not specifically focus on the relationships and dependencies between components like a CMDB does.

Inventory management software is designed to track physical assets, including hardware and software inventory, ensuring that organizations know what resources they have on hand. While this is important for asset management, it lacks the detailed information about relationships and dependencies that a CMDB provides, which is crucial for understanding the impact of changes within an IT infrastructure.

Standard operating procedures are the lists and policies that detail the instructions needed for workers to carry out their day-to-day routines. While these procedures can vary from organization to organization, the goal of these procedures is to ultimately improve performance, reduce miscommunication, and ensure industry regulation compliance. Some examples of standard operating procedures may be a process flowchart or communication pathways, or a written list of steps for installing new software.

# Q51

Your team must develop and add a new module into an existing software product. Your manager, Wendy Chen, is reviewing the proposed change; specifically, she is cataloging the sensitive data that will be handled and/or generated by the new application module. Which part of the change control process is Wendy engaged in?

- **A) Risk analysis**
    
- **B) Peer review**
    
- **C) Defining the scope of the change**
    
- **D) Impact analysis**
    
- **E) Defining the purpose of the change**
    

### Explanation

Wendy is performing an impact analysis. Specifically, she is identifying all sensitive data that will be handled or generated by the proposed solution. Sensitive data may have compliance requirements that would add additional steps not included within the initial scope of the proposed change. It is important to weigh documented business processes against a proposed change to ensure that implementing the change doesn't lead to unexpected consequences to other parts of the organization.

An impact analysis is part of a risk analysis. Only by understanding how the proposed new module will affect each aspect of the existing system can Wendy accurately understand how risky it could be to introduce the new module into the application. This is separate from determining how risky it would be to NOT code the new module, which is also part of risk analysis. Risk analysis assigns a qualitative risk score to proposed changes, such as "low impact" or "critical."

A peer review is an essential step in change management, particularly for normal and standard changes. Before implementation, proposed changes are reviewed by colleagues or cross-functional team members to validate the scope, risk level, impact, and rollback plans. This collaborative scrutiny reduces the likelihood of unintended consequences and helps ensure that changes align with organizational policies and security standards. Nothing in the scenario indicates that Wendy is reviewing another team's coding project.

Wendy is not defining the purpose or scope of the change. The person who requested the new software module did both of those things, which should be documented in the change request form.

According to CompTIA, you should be familiar with all of the following aspects of change control:

- Change request forms
    
- Purpose of the change
    
- Scope of the change
    
- Change types (standard change, normal change, emergency change)
    
- Date and time of change
    
- Change freezes (maintenance windows)
    
- Affected systems/impact analysis
    
- Risk analysis and risk levels
    
- Change board approvals
    
- Implementation of changes
    
- Peer review
    
- End-user acceptance
# Q52
A technician is implementing best practices to ensure the timely deployment of critical security updates on macOS devices without waiting for full OS updates. Which feature should they utilize to achieve this?

- **A) Updates/patches**
    
- **B) Rapid Security Response**
    
- **C) Antivirus**
    
- **D) Backups**
    

### Explanation

They would utilize Rapid Security Response (RSR). RSR was introduced by Apple to deliver critical security fixes to iOS, iPadOS, and macOS devices between regular software updates. These updates address vulnerabilities in components, including Safari, WebKit, and other essential system libraries, allowing for quicker mitigation of security issues that may be actively exploited. RSRs are automatically applied to devices running the latest OS versions, ensuring users receive important security improvements promptly without the need for a full system update.

Backups refer to the process of creating copies of data to prevent data loss which is essential for data recovery but does not address the timely deployment of security updates.

Antivirus software helps detect and prevent malware infections but does not facilitate the rapid application of critical security patches provided by the operating system.

Updates/patches typically refer to regular software updates that include new features and security fixes. However, they may not be deployed as swiftly as RSRs which are specifically designed for urgent security issues.

# Q55
Your IT department is implementing a centralized system to manage user identities, control access permissions across departments, and streamline login processes for multiple cloud-based services. Which option best describes your implementation?

- **A) ACL**
    
- **B) MFA**
    
- **C) MDM**
    
- **D) IAM**
    

### Explanation

Identity and access management (IAM) is a comprehensive framework used to centrally manage user identities and access permissions across multiple systems and services. It allows administrators to define roles, automate user provisioning and deprovisioning, enforce access policies, and integrate single sign-on (SSO) and multi-factor authentication (MFA). IAM platforms are especially effective in enterprise and cloud environments where centralized control and scalability are critical.

Access control lists (ACLs) define which users or systems can access specific objects (e.g., files or directories) and what actions they can perform. ACLs are rule-based and applied at the resource level, not across the entire identity infrastructure.

Mobile device management (MDM) is a platform that controls the delivery of programs, data, and configuration settings for company-owned mobile devices or devices that connect to the corporate network, such as smartphones, laptops, and tablets. It allows an administrator to deploy and manage software applications across all business mobile devices, as well as to secure, monitor, and support the devices with health policies and rules. If the device is lost, MDM can remotely wipe it, lock it, or block it from accessing corporate assets. It may be used across the organization to manage both company-owned and employee-owned (BYOD) devices. MDM can lower support costs and minimize security concerns.

The principle of least privilege is a security best practice where users are granted the minimum access necessary to perform their job. Unlike IAM, which is a system or platform, the principle of least privilege is a policy enforced within IAM or other access control mechanisms to limit unnecessary permissions.

Multifactor authentication (MFA) is an authentication method that requires users to provide two or more verification factors to gain access. It is often integrated into IAM solutions, but does not handle identity management or access provisioning on its own. IAM policies may (and should) be configured to require MFA when granting users access to internal resources.

# Q62

You are installing an operating system on a drive that appears to have sector issues. Which formatting option should you use?

- **A) exFAT**
    
- **B) Quick Format**
    
- **C) Full Format**
    
- **D) NTFS**
    

### Explanation

When you are installing an operating system on a drive that appears to have sector issues, you should use full format. A full format will take much longer than a quick format because a full format checks for bad sectors. It is critically important that the boot drive be properly formatted with the correct partitions and format.

Quick format is not correct because it does not check for bad sectors.

exFAT and NTFS are not correct because they describe the filesystem to be used, not the formatting process itself.

For the A+ exam, you need to understand the following filesystem and formatting terms:

- **FAT32** – This filesystem was introduced with Windows 95 Service Release 2 and allows a maximum partition size of 2 terabytes (TB).
    
- **NTFS** – This filesystem was introduced with Windows NT. It provides support for file compression, file encryption, and file/folder security.
    
- **exFAT** – This filesystem is the successor to FAT32. It allowed for larger files, particularly media files, and compatibility with flash media.
    
- **NFS** – This filesystem is used primarily in Linux systems. It allows users to access remote files the same way they would access local files.
    
- **ext4** – A newer version of EXT3. It supports file sizes to 16 TB. The maximum filesystem size is 1 exabyte.
    
- **ReFS** – The Resilient File System (ReFS) is a new filesystem from Microsoft, developed primarily for servers. It will beef up some of the weaknesses with the NTFS filesystem, particularly in the areas of scalability, efficiency and data integrity. The NTFS filesystem has been around since the early 1990's.
    
- **XFS** – XFS is the default filesystem on many Red Hat-based systems, known for high performance and journaling capabilities. It supports online resizing using tools like xfs_growfs.
    
- The FAT32 filesystem was introduced with Windows 95 Service Release 2 and allows a maximum partition size of 2 terabytes (TB).
    
- **Encrypting Filesystem (EFS)** is a file encryption technology that allows you to encrypt files to ensure that other users cannot read the files. EFS protects the files from being read, but does not ensure that users can control who has access to their files.
    
- **The Apple Filesystem (APFS)** is a proprietary filesystem developed by Apple for iOS 10 devices and later that was optimized for solid state drives. It was designed to support stronger encryption, snapshots, and data integrity.

# Q64
You are researching biometrics for identification and verification of employees in an organization.

Which attributes or details of an employee can be used by biometric devices? (Choose all that apply.)

- **A) iris**
    
- **B) signature**
    
- **C) hand geometry**
    
- **D) fingerprints**
    
- **E) hair**
    
- **F) face**
    

### Explanation

You can use the following attributes of a person to recognize the person through the use of biometric devices:

- Fingerprints
    
- Palmprint
    
- Face or facial recognition
    
- Written signature
    
- Iris
    
- Retina
    
- Hand geometry
    
- Voice
    

Biometric devices identify an individual by their physical or behavioral attributes, such as thumb- or fingerprints, geometry of a hand, or the style and speed in which the person produces their signature. These attributes are stored in a database during the enrollment process. During identification and verification, the individual is identified based on the attributes stored in the database. For example, if a thumb print was stored while enrolling the user, the user would have to provide his or her thumb print during the identification process. If the new thumb print matched the thumb print stored against the user's name, access to the resource would be granted. You can also use voice recognition to identify a person using biometric devices.

A person's hair cannot be used with biometric devices to identify users because hair analysis requires specialized laboratory equipment and trained technicians. Commercially implemented biometric devices use fingerprints, facial features, voice, an iris or retina, or hand geometry to identify individuals. Windows Hello, one of the most common biometric authentication systems, uses facial recognition, a fingerprint, or a memorized PIN to authenticate a user to a linked hardware key.

Biometrics is often associated with false negatives and false positives. False negatives occur when someone who is supposed to have access to the system is denied access. While these occurrences can affect the satisfaction of personnel, they do not result in security breaches. False positives occur when someone who is NOT supposed to have access to the system is granted access. These occurrences result in security breaches.

# Q70
Which of the following network resources typically requires a domain-joined environment, as opposed to a workgroup, in order to centralize management and access control?

- **A) Shared resources**
    
- **B) Mapped drives**
    
- **C) File servers**
    
- **D) Printers**
    

### Explanation

A file server would require a domain-joined environment when management and access control need to be centralized. This is particularly true in enterprise environments that benefit significantly from being part of a domain. In a domain-joined setup, file servers can leverage centralized authentication and authorization through Active Directory, allowing administrators to manage user access permissions efficiently across the network. This centralized control ensures that only authorized users can access specific files and folders, enhancing security and simplifying management.

While a workgroup allows for sharing, it does not provide centralized management and access control. Shared resources, such as folders or devices, printers, and mapped drives, are typically found in workgroups, where share control is at the local machine level.

# Q76
Which of the following workstation operating systems uses a master database to store all user, system, and application settings?

- **A) Chrome OS**
    
- **B) Microsoft Windows**
    
- **C) Linux**
    
- **D) Apple macOS**
    

### Explanation

Microsoft Windows uses a master database to store all user, system, and application settings. This database, called the registry, is organized into five hierarchical sections called hives.

By drilling down into the hives, you can find individual system settings, such as the default printer for a particular user.
Apple macOS stores the application settings in .plist files. The .plist file provides the configuration settings and particular properties for an application.

Linux stores configuration settings in initialization files, collectively called INI files. Initialization files may have the .ini, .cnf, .config, or .txt extension. The common practice is to store the system-level configuration files in the /etc directory, while user-level configurations are stored in the user's home directory.

Chrome OS follows the same methodology as Linux.

In addition, vendor-specific limitations, such as end-of-life for an operating system and update limitations, need to be considered before choosing an OS.

# Q77
Which of the following logical security technologies provides a centralized system for storing, organizing, and managing user identities and access permissions across a network?

- **A) Access control lists**
    
- **B) Mobile device management**
    
- **C) Directory services**
    
- **D) Multi-factor authentication**
    

### Explanation

Directory services provide a centralized and hierarchical structure for storing, organizing, and managing user identities and access permissions. Systems such as Microsoft Entra ID, on-premises Microsoft Active Directory, and OpenLDAP allow administrators to enforce consistent security policies, control login authentication, and assign access rights across the organization. Directory services are fundamental to organizing and securing digital resources in enterprise environments.

Access control lists (ACLs) are used to define permissions to specific resources, such as subnets, files, devices, or directories. While ACLs determine who can access or modify an object, they do not provide centralized identity management or network-wide user organization.

Mobile device management (MDM) is a platform that controls the delivery of programs, data, and configuration settings for company-owned mobile devices or devices that connect to the corporate network, such as smartphones, laptops, and tablets. It allows an administrator to deploy and manage software applications across all business mobile devices, as well as to secure, monitor, and support the devices with health policies and rules. If the device is lost, MDM can remotely wipe it, lock it, or block it from accessing corporate assets. It may be used across the organization to manage both company-owned and employee-owned (BYOD) devices. Directory services can be integrated with MDM solutions, but MDM applies to mobile devices and not to all user accounts.

The principle of least privilege is a best practice that limits a user's access rights to only what is strictly necessary to perform their job. Although this concept is often enforced through directory services, it is not itself a system or tool—it is a guiding policy.

Multi-factor authentication (MFA) enhances login security by requiring multiple forms of identity verification, such as a password and a mobile code. While often integrated into directory services, MFA is focused on authentication rather than user identity management or access control policies.

# Q78
Which security considerations should you take into account when installing and configuring applications on Windows desktops? (Choose all that apply.)

- **A) User privileges**
    
- **B) Remote PC access**
    
- **C) Impact to device**
    
- **D) Turning Windows features on or off**
    

### Explanation

You should consider the impact to the device, user privileges, and whether Windows features will be enabled or disabled as a result of the installation.

You should consider the impact to the device, specifically the application's access to the device's files, settings, and user accounts. If, for example, the application accesses information in the cloud, you might be vulnerable to an attack. You should also consider whether the application is allowed to make changes to the underlying operating system settings, registry keys, or inbound connections.

You might also want to consider which user privileges are required to install and run the application. User Account Control (UAC) will limit the users that will be able to install applications on a Windows computer. An administrative-level account is required to do this.

You should consider whether the application will enable or disable Windows features. If you have to disable Windows Firewall to install an application, what vulnerabilities does this expose?

For the A+ exam, you will also need to consider the impact to business and the impact to operations before installing a new application. A new application's impact to business refers to its effect on the business's wellbeing, such as the financial costs of purchasing or licensing the app or any risks/vulnerabilities the new application could create. You must also consider which teams are going to be tasked with ensuring the application is running properly, and the hardware requirements needed to run this application on a network.

Impact to operations refers to how a new application will impact the teams that are using it daily. This may include an impact on productivity, such as a slowdown while teams are trained to use the new application; what teams/users are able to access the new application; and what information is being stored on these applications.

# Q79
You are the desktop technician for your company. Your company has a strict security policy in place. While troubleshooting the computer issue, you discover that a user has given her password to two co-workers in her department at the request of her supervisor. This is in direct violation of the company's security policy.
What should you do?
A) Inform your supervisor of the department's violation of the security policy.
B) Tell the user to change her password and to keep it a secret.
C) Explain the company security policy to the user.
D) Explain the company security policy to the supervisor.
### Explanation
You should inform your supervisor of the department's violation of the security policy. It is always best practice to inform your supervisor of any security issues and let your supervisor address the situation.
You should not explain the company security policy to the user or supervisor. You should never try to correct co-workers or supervisors in any manner. You should not tell the user to change her password and to keep it a secret. You should never try to correct co-workers or supervisors in any manner.
A password is considered to be personally identifiable information (PII). Other PII includes full user names, addresses, identification numbers (including social security numbers and driver's license number), date of birth, and financial information. It is important that technicians understand that PII must be kept secure. User awareness training should include educating the end users on the importance of handling PII properly. Users should report all unauthorized access of PII to the appropriate personnel.

# Q80

You are an IT technician. You notice several offensive files on a user's computer while performing routine maintenance. Your company does not have an Acceptable Use Policy. What should you do?
A) Inform the user that the files must be removed.
B) Contact your supervisor.
C) Remove the offensive files.
D) Contact the user's supervisor.
### Explanation
Because your company does not have an Acceptable Use Policy, you should contact your supervisor and inform them of the offensive material. They will decide the appropriate action to take.
If your company has an Acceptable Use Agreement or Acceptable Use Policy (AUP) that users must sign, you should follow its written procedures for dealing with this violation. If a user signed the AUP, then he or she is bound by that agreement and its terms.
When dealing with prohibited content, you should always consult your company's policies. If procedures are given, you should follow these procedures. If no specific procedures are given, you should consult with your supervisor.
The Acceptable Use Agreement should include details on what is considered unacceptable behavior or computer usage and give possible repercussions for violating the agreement. It also contains guidelines for reporting any violations.
You should not contact the user's supervisor. Ideally, your supervisor should contact the user's supervisor if your supervisor feels it is necessary.
You should never inform a user that certain files must be removed or remove the offensive files yourself. It is not your job to determine the action to take, and doing so could destroy crucial digital evidence.
When you become aware of prohibited content, you must first identify the content. Then you should report that you have found prohibited content through the appropriate channels. It is also vital that you preserve the device and its data in the state it was in when the content was discovered, especially if the prohibited content could result in criminal charges. To preserve the validity of evidence, you should keep a detailed chain of custody for all assets in review. This will ensure that the evidence is documented and tracked throughout the process. In addition, you should provide documentation to accompany any evidence that is seized. Documentation changes should be recorded as well.
No matter the type of incident, an incident report would typically include user names, affected devices, a description of the incident, actions taken to resolve the incident, personnel involved in handling the incident, times, and dates. Ideally, an incident report should also include a root cause analysis and recommendations for future steps to prevent similar incidents.
# Q82

According to your company's new security policy, the administrator must define the number of days that a password can be kept before the user can change it. Which password policy setting should the administrator use?

- **A) the Maximum password age setting**
    
- **B) the Enforce password history setting**
    
- **C) the Minimum password length setting**
    
- **D) the Minimum password age setting** (Correct Answer)
    

### Explanation

You can configure the Minimum password age setting on a Windows computer to define number of days that a password must be kept before the user can change it. The Minimum password age setting determines how many days a new password must be kept before the user can change it. The Minimum password age setting is designed to work with the Enforce password history setting to prevent users from changing back to their old passwords by quickly resetting their passwords the required number of times.

When implementing a new password policy, you should encourage the users to create their passwords by using a combination of numbers and letters so that the passwords are difficult to guess. You should also encourage users to memorize their passwords instead of writing them down somewhere. Passwords that are written down on a piece of paper or stored in an easily accessible file on their computers can pose a security threat to the users' computers.

You cannot use the Enforce password history setting to define number of days that a password must be kept before the user can change it. The Enforce password history setting determines the number of unique new passwords a user must use before an old password can be reused, not the number of days that a password must be kept before the user can change it.

You cannot use the Maximum password age setting to define number of days that a password must be kept before the user can change it. The Maximum password age setting determines number of days a password can be used before the user is required to change it, not the number of days that a password must be kept before the user can change it.

You cannot use the Minimum password length setting to define number of days that a password must be kept before the user can change it. The Minimum password length determines the minimum number of characters a password must have, not the number of days that a password must be kept before the user can change it.

When preparing for the A+ exam, you should understand security best practices to secure a workstation, including the following:

- **Password expiration** – Administrators should configure password expiration policies. Most organizations set a 60- or 90-day expiration, meaning that passwords must be reset within that time limit.
    
- **BIOS/UEFI passwords** – Configuring a BIOS or UEFI password ensures that the system settings stored in the BIOS or UEFI cannot be accessed or changed by unauthorized users.
    
- **Restricting user permissions** – Users should only be granted permissions that they need to complete their jobs. For users that need administrative-level permission, the users should be given two accounts: one normal account with more restrictive permissions that they use for day-to-day activities and one administrative account that they use when performing administrative duties. Also, as a rule, permissions should be assigned to groups, and user accounts should be added to group accounts. This makes permission administration much more manageable.
    
- **Changing default user names and passwords** – Always change the user names and passwords for any default user accounts that are created when an operating system or application is installed. Most IT professionals and hacker are aware of default account credentials. Renaming these accounts provides a level of protection. Always research any operating system or application that you install to learn of any default user accounts that are created at installation.
    
- **Disabling the Guest account** – All default accounts that are created should be disabled if they will not be used. This is particularly important for the Guest account. If possible, you should also rename the account. The Guest account is disabled by default in Windows 10 and above.
    
- **Screensaver required password** – Screensavers start after a period of idle time. For security reasons, a screensaver password policy is used to ensure that a user is required to enter his password when returning to his session. In addition, many companies have logoff policies that require users to log off from a computer when leaving for prolonged periods of time.
    
- **Timeout/screen lock** – It is a good practice to configure a computer to implement a screen lock after a certain amount of time without user interaction. This can be employed as part of the screensaver required password.
    
- **Disable Autorun/Autoplay** – Because you are never ensured that media, including USB flash drives, CDs, DVDs, and so on, are safe and uncontaminated, you should be careful when inserting new media into a CD-ROM, DVD, or USB drive. Windows 10 and 11, by default, have disabled AutoPlay, but it is always worth double-checking to verify that it has not been enabled.
    
- **Login time restrictions** – Login time restrictions are configured by administrators to limit the hours during which a user can log in to a system. This security feature, however, can cause problems if for any reason a user works outside his normal business hours.