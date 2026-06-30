# Q1
Rooting occurs when a user tampers with an Android device to remove the restrictions that were put in place by the manufacturer or operator to prevent a user or malicious actor from installing unauthorized software. Rooting is a privilege escalation exploit that is often done through a series of kernel patches. It is seen as violation of many end-user licensing agreements, and creates multiple vulnerabilities within the device. The term for a similar process on Apple devices is jailbreaking.

An Android Package Source (APK) file contains all the necessary files need to run an Android program. Corrupt APK files can be installed inadvertently from untrusted third-party applications that can allow attackers to gain access to the device and modify code undetected. While corrupted APK sources can create security risks, they do not inherently enable a user to gain root access to a device.

Developer mode is a hidden feature within Android devices that enable users to gain access to developer tools and options. Developer mode gives a user the option to run USB debugging, view/control/end running services, submit bug reports, and create password-protected backups on a desktop, among other such features. While a general user should not have access to developer mode on a company-provided device, it would not give root access as seen in this scenario.

Bootleg and malicious applications should never be installed on a company-provided device, and should also be discouraged on personal devices. These applications create large security risks as they can contain malware that can enable a malicious actor to gain access and exploit a device or steal information. However, in this situation, a user would have had to jailbreak their device first to circumvent company application restrictions to install these applications.

For the A+ exam, you will also need to be aware of application spoofing. Application spoofing takes place when a malicious actor creates an application that is designed to impersonate a source that appears to be safe and secure. These applications are loaded with malware that will infect the device, enabling the attacker to gain access, steal information, and engage in other hostile actions. Whenever downloading an application, it is critical to verify that it is coming from a valid and trusted source to prevent any breaches.

# Q2
Biometric authentication and full device encryption would provide you with the highest level of security for Android mobile devices.

Biometric authentication matches a user’s uniquely identifiable physical attribute to a previously stored value. Biometrics is among the most secure physical security measures. Examples include fingerprints, iris or retinal scans, voice prints, and keyboard cadence.

Full device encryption requires that the user provide a PIN, password, or a swipe pattern in order to activate the decryption key on the device. If the user does not provide the correct information, the data remains encrypted and inaccessible.

Patching/OS updates are always a critical concern, but it doesn’t address security for Android mobile devices. The Android OS is typically patched or updated by the phone manufacturer or Google, and the timing of update availability may be outside the control of the organization. Ensuring that patches and updates are applied and current should be a basic component of system security.

There are firewalls for Android, but they would only protect traffic entering or exiting the device. You would want to block unauthorized access to the device itself as the primary security measure.

There are VPN products for Android, but they would only protect traffic to and from the device. They provide no physical protection if the device is stolen.

# Q3

According to RFC 3227 – Guidelines for Evidence Collection and Archiving, you should back up data in the following order, from MOST volatile (registers and cache) to LEAST volatile (backup media):

1. Registers, CPU cache, running processes
    
2. Routing table information, ARP cache, process tables, kernel statistics, RAM memory or virtual memory, page file contents
    
3. File system information (including temporary file systems)
    
4. Disk storage and files saved to memory
    
5. Remote logging and monitoring data (including active connections and session info)
    
6. Physical configurations and network topology
    
7. Archival media (backup media, CDs, DVDs)
    

The order of volatility is made up of the following items, from most to least volatile:

1. **Memory contents (registers, cache):** CPU registers and CPU cache are the most volatile data in a system. Registers store the current instructions and memory addresses the CPU is actively processing, while the cache holds recently used data for quick access. This data changes nanosecond by nanosecond and disappears immediately when the power is lost. Due to their fleeting nature, they are nearly impossible to capture without specialized forensic equipment.
    
2. **Routing tables, ARP cache, process tables, kernel statistics, pagefiles, and memory (both physical and virtual):** These components reside in memory and provide a real-time system and network state. Routing tables determine where network traffic is sent, the Address Resolution Protocol (ARP) cache maps IP addresses to MAC addresses, and kernel data tracks OS-level functions and processes. These elements are highly volatile and can be flushed or altered with normal system activity or a reboot.
    
3. **File system information and temporary files:** Temporary files—such as page/swap files—are created to support running applications. Though stored on disk, they can be overwritten quickly by the OS or deleted by system cleanup utilities. These files may contain information about recent activities or open documents and should be preserved early in the forensic process.
    
4. **Disk storage -** Disk-based storage (HDD, SSD): Hard drives and solid-state drives store long-term data such as documents, installed applications, system logs, and the operating system. Disk data is less volatile and remains intact after shutdown. However, it can still be deleted or overwritten, so imaging the drive (bit-by-bit copy) ensures the preservation of its contents at the time of the incident.
    
5. **Remote logging and monitoring data:** These would include information from connections to remote servers, such as logs and other monitoring data.
    
6. **Physical configuration and network topology:** Active network sessions and open ports are volatile because they reflect what the system is doing in real time. Information such as source and destination IPs, protocols used, and session durations are crucial during an investigation—but once the connection closes or the system shuts down, this data is typically lost unless captured using tools such as packet analyzers or live forensics utilities.
    
7. **Archival media (backup media, CDs, DVDs):** These are the least volatile forms of data. Stored offsite or in cloud repositories, archives and backups contain historical snapshots of files, system images, or entire configurations. While stable and unchanging, they offer a retrospective view of system states and are typically used in later phases of analysis or recovery.

# Q4
You should return the empty toner cartridge to the manufacturer for recycling. Laser printers use toner cartridges that can usually be refurbished and refilled by the manufacturer. The toner in a particular brand or model of cartridge has a specific formulation, and using a cartridge with the wrong toner may ruin your printer.

Toner cartridges, circuit boards, batteries, and other computer components typically include recommendations from the manufacturers regarding any special requirements they may have for recycling or disposal.

# Q5
The md command should be used to create new folders and subfolders.

The rd (or rmdir) command removes the specified directory, provided the directory is empty.

The dir command should be used to display the contents of a directory or folder.

The cd command should be used to navigate to a different directory folder in the command prompt.

Whenever using these commands to navigate through your device’s various drives, you can specify which drives you would like to examine by specifying the drive name, such as C:\ or X:, after entering the command. This can enable users to navigate drives far faster and more efficiently that searching each drive manually.

The sfc command verifies the version of system files running on the computer. Corrupted files will be replaced with correct versions. When using this command, you need to be aware of the following parameters:

- /SCANNOW – Scans protected files immediately.
    
- /SCANONCE – Scans all protected files once.
    
- /SCANBOOT – Scans all protected files every time the computer reboots.
    
- /VERIFYONLY – Scans the protected files, but does not make repairs or changes.
    
- /SCANFILE – Scans only the specified file.

# Q6
The System Configuration utility no longer allows you to adjust which applications can be loaded at the boot time. Previous versions of Windows let you navigate to the Startup tab to adjust what applications could be loaded by checking or clearing the checkbox for the various applications listed. However, this feature has been shifted to Task Manager.

You should remove all unneeded applications from the Startup tab to reduce the startup time.

The General tab is the default tab that shows how the system will start by default. It also provides the ability to adjust startup for troubleshooting:

The Services tab shows all services and their statuses. You can enable or disable services from this tab. The Services tab is shown in the following exhibit:

The Boot tab displays a pane that allows the boot.ini file to be manipulated. The Boot Options check box area allows the computer to boot up in a user selected mode such as Safe mode or Safe mode with command prompt only. The Boot tab is shown in the following exhibit:

The Tools tab, which is not an option in this question, provides access to some Windows diagnostic tools. It is shown in the following exhibit:

# Q7
Automated System Recovery and Automatic repare are not options listed in the Advanced Startup Options menu.

The following options are available in the Advanced Startup menus:

- System Restore – Use a restore point recorded on your PC to restore Windows
    
- System Image Recovery – Recover Windows using a specific image file
    
- Startup Repair – Fix problems that keep Windows from loading
    
- Startup Settings – Use the Command Prompt for advanced troubleshooting
    
- Command Prompt – Change Windows startup behavior

# Q8
Boot options are not displayed when you run the systeminfo command on a Windows 10 computer. Boot options are displayed on the Boot tab of the System Configuration utility.

When you run the systeminfo command on a Windows 10 computer, you will see OS specifications, machine hardware specifications, :

```
Host Name:                  KPREMLT0146
OS Name:                    Microsoft Windows 10 Enterprise
OS Version:                 10.0.19042 N/A Build 19042
OS Manufacturer:            Microsoft Corporation
OS Configuration:           Member Workstation
OS Build Type:              Multiprocessor Free
Registered Owner:           Windows User
Registered Organization:
Product ID:                 00329-10100-00000-AA521
Original Install Date:      8/14/2021, 3:26:09 PM
System Boot Time:           12/30/2021, 11:14:17 AM
System Manufacturer:        Hewlett-Packard
System Model:               HP EliteBook 840 G1
System Type:                x64-based PC
Processor(s):               1 Processor(s) Installed.
                            [01]: Intel64 Family 6 Model 69 Stepping 1 GenuineIntel ~2501 Mhz
BIOS Version:               Hewlett-Packard L71 Ver. 01.20, 7/28/2014
Windows Directory:          C:\WINDOWS
System Directory:           C:\Windows\system32
Boot Device:                \Device\HarddiskVolume1
System Locale:              en-us;English (United States)
Input Locale:               en-us;English (United States)
Time Zone:                  (UTC-06:00) Central Time (US & Canada)
Total Physical Memory:      8,089 MB
Available Physical Memory:  1,509 MB
Virtual Memory: Max Size:   19,069 MB
Virtual Memory: Available:  4,282 MB
Virtual Memory: In Use:     14,787 MB
Page File Location(s):      C:\pagefile.sys
Domain:                     alpha.kaplaninc.com
Logon Server:               \\PWINADC409
Hotfix(s):                  8 Hotfix(s) Installed.
                            [01]: KB4578968
                            [02]: KB4562830
                            [03]: KB4570334
```

You can also pull up detailed system information, including a high-level view that includes most of the output from the systeminfo command, by opening the System Information console from the Run command prompt (msinfo32.exe) or from the shortcut in Administrative Tools:

The System Information console is a much more robust tool than the systeminfo command, and includes a searchable interface to find the details of nearly every hardware resource, component, or software element on the machine.

You would run the msconfig command to open the System Configuration utility. The Boot tab is shown in the exhibit:

# Q9
You should use Mask.

**systemd** allows you to _mask_ a service. **systemd** units work on various levels of "off". There are three levels of "off" when considering **systemd** services. The first level of "off" is when using start or stop for a service as this will initiate or terminate a service immediately. The second level of "off" is when you use enable or disable for a service. This affects services _after_ the next system boot. The third level of "off" involves masking. **systemd** can start a service that was previously disabled in order to satisfy a dependency needed for another service to function. Similarly, **systemd** will not stop a service that may be needed for others to function. Masking involves _forcing_ **systemd** to stop a service that it otherwise would not. To do unit masking, **systemd** uses configuration files in **/etc/systemd** and creates a link file to **/dev/null**. The following code illustrates masking:

Bash

```
#systemctl mask https.service
Created symlink from /etc/systemd/system/https.service to /dev/null.
```

To unmask the service, run the unmask command as shown:

Bash

```
#systemctl unmask https.service
```

Daemon-reload is incorrect because it only reloads a service and does not check dependencies. The `systemctl daemon-reload` command is used when you need **systemd** to reload configuration files used for a certain unit that may be updated or changed. The following code illustrates this:

Bash

```
#systemctl daemon-reload
#systemctl start myservice.service
```

Hostnamectl is incorrect because it does not check dependencies for services. `Hostnamectl` is used to change the host name of the Linux system and to query the same. `Hostnamectl` distinguishes between three hostnames:

- pretty, which includes special characters like “Josh’s Server”
    
- static like “josh-server” or
    
- transient hostname, which is received via a network configuration. This static hostname is stored in **/etc/hostname**.
    

You can set a static hostname using the following code:

Bash

```
#hostnamectl set-hostname joshmachine --static
```

Reload-or-restart is incorrect because it reloads or restarts a specific service but doesn’t check dependencies. Systemctl command allows you to control the **systemd** daemon. You can start and stop the system service using systemctl. You can also restart or reload it if required. Additionally, you can check the status of the **systemd** service and enable or disable specific services on your system.

To start or stop services using `systemctl`, use the following code:

Bash

```
#systemctl start myservice.service
#systemctl stop myservice.service
```

To enable or disable services using systemctl, use the following code:

Bash

```
#systemctl enable myservice.service
#systemctl disable myservice.service
```

Similarly, you use the following code to restart or reload a service:

Bash

```
#systemctl reload myservice.service
#systemctl restart myservice.service
```

The reload-or-restart option will attempt to first reload the specified service. If the service cannot be reloaded, it will be restarted. This is indicated in the following code:

Bash

```
#systemctl reload-or-restart myservice.service
```

You can also check the status of a service to verify if it is enabled or disabled using `is-active`, as indicated in the following code:

Bash

```
#systemctl is-active myservice.service
#systemctl is-enabled myservice.service
```

**systemd** is a suite of fundamental programs that help run the Linux system. This includes the **systemd** service and system manager, running with Process ID (PID) 1 that starts the Linux system. The **systemd** daemon manages the system by starting and stopping daemons, maintaining mount and automounts, system snapshots and tracking processes. **systemd** replaced SysVinit as the default init program for most Linux distributions by offering a faster boot time by allowing parallel start of services while also providing alternatives for cron jobs.

# Q10 (Q40 on Exam)
If you need to determine if a Trojan horse is loading at system startup, you should use Settings. Then select Apps and Startup. Check each application shown in the list to ensure that it is a valid application you need. As shown in the following exhibit, you can prevent an application from loading at startup simply by turning off the application:

The Task Manager can also be used to Disable startup applications.

Keep in mind, however, that this does not remove the Trojan horse from the computer. It just keeps it from loading at startup.

Anti-malware software does not remove Trojan horses from startup, which is what was requested in the scenario. The anti-malware software may be able to remove the Trojan horse from the system itself, but you should make sure that the anti-malware software is updated to ensure that it is capable of detecting the newest threats that have emerged.

System Restore restores a computer to a previously saved state. It does not remove Trojan horses from computer startup, especially if the Trojan were included in the restore image.

The Windows Recovery Environment is a recovery environment that can repair common causes of unbootable operating systems. It does not remove Trojan horses from computer startup.