# E1Q43
Before implementing the change, you should develop a backout or rollback plan that would allow you to recover should something go awry. When you see that the implementation is not going as planned, the backout plan will allow you return the systems to an operational state. Rollback plans should be thoroughly documented to ensure that when it is necessary to roll back, you are reverting to the proper point. You may also need to implement rollback after you successfully implement a change, then discover that the change doesn't meet requirements or fails end user acceptance.

When implementing any approved change, you should document the date and time when the change was implemented. This enables IT teams to identify when changes were last made to a device or application if a change has begun causing problems so they can roll back the change to the appropriate backup timestamp.

The backup plan is implemented separately from the rollback plan. The backup plan outlines the steps to take to ensure that all data, configurations, and settings are saved to a viable restore point before any changes are made. The process includes identifying all assets that would be affected by the change and ensuring they are saved to the latest possible state before you begin work. By contrast, the rollback plan is a procedure for reversing changes after you make them. This could include taking file shares offline or moving network cables, not just restoring data.

The purpose of the change should be in the change request. Items to include in the purpose of the change statement could include why the change is needed, who is requesting it, which issue it addresses, what would be the implications if the change were not made, and what the intended result will be.

End-user acceptance is often critical to the successful implementation of the change. Open communication of how the change will impact their work life, the necessity of the change, and training will all go a long way towards end-user acceptance.

Documented business processes include items such as technical support procedures, customer service, and ordering procedures. In general, these deal with company policies and procedures. The change request should thoroughly address the effect on documented business processes.

# E1Q48
Operating systems are installed with default user and guest accounts. These accounts are well known to most attackers, who can use them to hack into a system. It is recommended that you rename the administrator account to prevent an attacker from using password-guessing techniques to gain entry into the system. In addition, you should disable and rename the guest accounts to prevent users without an account from accessing the system using these anonymous accounts. If you need to use the guest accounts, you should ensure that they have passwords.

Creating a secure administrator account is always a good idea. However, this action will not harden the OS if the administrative account uses the OS default name.

When you install an operating system, you should set a password for the default administrator account. This password should be changed at irregular intervals to enhance security, but it is not necessary to change the password immediately after installing the operating system. This action would do little to enhance security unless you think the password was compromised during the installation process.

You should not delete all default user and group accounts. You do not want to delete the default administrator account until you have created a new one with the same rights. Otherwise, you could lose the ability to manage the system.

When preparing for the A+ exam, you should understand security best practices to secure a workstation, including the following:

- **Password expiration** – Administrators should configure password expiration policies. Most organizations set a 60- or 90-day expiration, meaning that passwords must be reset within that time limit.
    
- **BIOS/UEFI passwords** – Configuring a BIOS or UEFI password ensures that the system settings stored in the BIOS or UEFI cannot be accessed or changed by unauthorized users.
    
- **Restricting user permissions** – Users should only be granted permissions that they need to complete their jobs. For users that need administrative-level permission, the users should be given two accounts: one normal account with more restrictive permissions that they use for day-to-day activities and one administrative account that they use when performing administrative duties. Also, as a rule, permissions should be assigned to groups, and user accounts should be added to group accounts. This makes permission administration much more manageable.
    
- **Changing default user names and passwords** – Always change the user names and passwords for any default user accounts that are created when an operating system or application is installed. Most IT professionals and hacker are aware of default account credentials. Renaming these accounts provides a level of protection. Always research any operating system or application that you install to learn of any default user accounts that are created at installation.
    
- **Disabling the Guest account** – All default accounts that are created should be disabled if they will not be used. This is particularly important for the Guest account. If possible, you should also rename the guest account. The Guest account is disabled by default in Windows 10 and above.
    
- **Timeout/screen lock** – It is a good practice to configure a computer to implement a screen lock after a certain amount of time without user interaction. This can be employed as part of the screensaver required password.
    
- **Disable Autorun/Autoplay** – Because you are never ensured that media, including USB flash drives, CDs, DVDs, and so on, are safe and uncontaminated, you should be careful when inserting new media into a CD-ROM, DVD, or USB drive. Windows 10 and 11, by default, have disabled AutoPlay, but it is always worth double-checking to verify that it has not been enabled.
    
- **Login time restrictions** – Login time restrictions are configured by administrators to limit the hours during which a user can log in to a system. This security feature, however, can cause problems if for any reason a user works outside his normal business hours.

# E1Q54
Directory services provide a centralized and hierarchical structure for storing, organizing, and managing user identities and access permissions. Systems such as Microsoft Entra ID, on-premises Microsoft Active Directory, and OpenLDAP allow administrators to enforce consistent security policies, control login authentication, and assign access rights across the organization. Directory services are fundamental to organizing and securing digital resources in enterprise environments.

Access control lists (ACLs) are used to define permissions to specific resources, such as subnets, files, devices, or directories. While ACLs determine who can access or modify an object, they do not provide centralized identity management or network-wide user organization.

Mobile device management (MDM) is a platform that controls the delivery of programs, data, and configuration settings for company-owned mobile devices or devices that connect to the corporate network, such as smartphones, laptops, and tablets. It allows an administrator to deploy and manage software applications across all business mobile devices, as well as to secure, monitor, and support the devices with health policies and rules. If the device is lost, MDM can remotely wipe it, lock it, or block it from accessing corporate assets. It may be used across the organization to manage both company-owned and employee-owned (BYOD) devices. Directory services can be integrated with MDM solutions, but MDM applies to mobile devices and not to all user accounts.

The principle of least privilege is a best practice that limits a user's access rights to only what is strictly necessary to perform their job. Although this concept is often enforced through directory services, it is not itself a system or tool—it is a guiding policy.

Multi-factor authentication (MFA) enhances login security by requiring multiple forms of identity verification, such as a password and a mobile code. While often integrated into directory services, MFA is focused on authentication rather than user identity management or access control policies.

# E1Q55
Scripts are not a good choice for offboarding users. While some aspects of offboarding a user could be automated, such as removing the user account's access to system files or network shares, offboarding also includes removing an employee's access to key fobs, door keys, security badges, computers, mobile devices, and other non-digital assets.

Scripting is intended to automate any repetitive task or workflow to make an IT technician's job more efficient. You should be familiar with all of the following use cases for scripting in the workplace:

- **Basic automation of administrative tasks**
    
- **Restarting machines**
    
- **Remapping network drives**
    
- **Installing applications**
    
- **Automating backups**
    
- **Gathering of information/data**
    
- **Initiating updates**
    

Automated backups are primarily used to protect important files by creating scheduled data copies without user intervention. Automated backups are a core scripting use case to ensure important data is preserved on a scheduled basis without human intervention. With scripting, backups can be configured to run regularly in the background, reducing the risk of data loss due to user error, hardware failure, or malware. This approach also supports off-peak execution and minimal disruption to end users.

Creating user accounts is a good use case for scripting. With a PowerShell cmdlet or a Bash script, an administrator can quickly automate a process that would otherwise involve clicking through a number of GUI buttons in an IAM console for each new account.

Restarting machines is a useful process for system management. Scripts can be used to reboot systems at scheduled times, often after updates or maintenance.

Remapping network drives is valuable for the user experience. This use case automates reconnecting users to shared network resources, such as departmental file servers.

Initiating updates is a use case that improves patching and security. System or software updates can be scheduled with scripting, ensuring devices remain current and secure.

Scripting is ideal for finding patterns in data and dumping the results into a file for review. It can be used to scrape Web sites for content, such as automated threat feeds, news articles, or a list of relevant keywords, and to search files and databases for text string matches.

One important security measure to remember is to never hard-code passwords in plaintext scripts. If a script must call a privileged account and enter a password to perform an action, the credentials should be stored in a separate file or called from a secure area, such as Windows Credential Manager. Otherwise, if the script file is accessed by an attacker, it can allow a malicious actor access into your systems.

# E1Q55
steps to remove SOHO Malware
The correct order of steps, with their explanations, is as follows:

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

# E1Q59
The following steps can be used as preventive measures against static electricity:

- **Wear anti-static bands while servicing computer components.**
    
- **Keep parts inside the manufacturer’s packaging until installation.**
    

Wearing anti-static bands or wrist straps and standing on antistatic mats while servicing computer components will keep static electricity from discharging to electrical components when a technician is servicing a computer. The anti-static bands or wrist straps need to be grounded. Even a small amount of static electricity can damage internal computer components, such as motherboard, random access memory, and hard disk. Small areas of discoloration on circuit boards usually indicate electrical damage.

Manufacturers ship computer components sealed inside antistatic bags or nested in antistatic foam. You should keep them in this protective packaging until you are ready to install them. Unpacking a component and placing it on your unprotected work surface, like a metal table, could convey enough static discharge to damage the part.

Ensuring the humidity level does not exceed 40% will not prevent static electricity because static electricity is typically generated in dry conditions when the humidity is low. Central heating and cooling can both reduce indoor humidity to levels that generate static. Higher humidity levels (typically in excess of 60%) can cause corrosion, but not static electricity.

Shoes are known to be conductors of static electricity, and wearing leather soles will help transfer static electricity instead of preventing it. By contrast, rubber-soled shoes can provide some resistance if the soles are made up of conductive rubber that scatters static electricity.

Carpets are known to be conductors of static electricity, and special care should be taken if you want a carpet in the server room. You should ensure that either the carpets themselves are anti-static, or the carpets are sprayed with anti-static agent.

# E1Q60
A user wants to change his local password on a Windows 10 computer using the least amount of administrative effort. What are the user’s best options? (Choose two.)
### Explanation

The user can click start and search Sign-In Options. Afterwards, they should select Password and then choose Change. The user may also press Ctrl+Alt+Del and select change a password.

While you could click Start, Control Panel, User Accounts, and Change Your Windows Password, this requires more administrative effort.

You should not click Start, Control Panel, User Accounts, and the user's account name, and select Change My Password. This process worked in Windows XP if you were using an administrative account. The Ctrl+Alt+Del key combination could also be used in Windows XP.

# E1Q62
### Explanation
An IT consultant is setting up new laptops for a small business. The systems need to join a domain, use BitLocker encryption, and be managed through Group Policy. There is no need for the features in ReFS. Which Windows 11 edition best meets the business requirements?

### Explanation

Windows 11 Pro is the best edition for this situation. It is best for small and medium-sized businesses that need enhanced security and device management features without the added complexity of an enterprise-level deployment. It supports joining domains, Group Policy, BitLocker drive encryption, remote desktop, and other business tools not available in the Home edition. Windows 11 Pro is compatible with NTFS but not ReFS. These features allow IT administrators to manage multiple systems efficiently and enforce security policies across the organization.

Windows 11 Home does not have essential business features such as joining domains, Group Policy editor, and BitLocker. This makes this version unsuitable for managed environments or professional use where centralized control is required.

Windows 11 Enterprise includes all the features from Pro and adds advanced security, device management, and deployment tools. It is intended for large organizations with volume licensing, not small businesses. Windows 11 Enterprise licenses are per-user, not per-device. It offers:

- Credential Guard
    
- Always-On VPN and Direct Access
    
- File-based data encryption
    
- Advanced BitLocker configuration options
    
- Universal Print cloud-based print servers
    

Windows 11 Pro for Workstations is designed for high-end hardware and intensive computing environments such as data analysis and CAD. It supports the Resilient File System (ReFS) and persistent memory, but offers no benefit for a casual user.

# E1Q63
Your company has adopted a new security policy that states that all computers must be locked if a user leaves his desk for any reason. What is the quickest way to lock a Windows computer?

### Explanation

The quickest way to lock a Windows computer is to press the Windows Logo + L keys. This feature works in Windows 10 and higher.

You can also lock a Windows computer by pressing Ctrl+Alt+Del and selecting Lock, but it requires more keystrokes.

Another method of locking a Windows computer is to click Start, click your profile symbol, and select Lock.

If you right-click the taskbar and select Lock the taskbar, you are locking the taskbar, not the computer. Locking the taskbar ensures that the auto-hide feature is disabled.

When preparing for the A+ exam, you should understand security best practices to secure a workstation, including the following:

- **Password expiration** – Administrators should configure password expiration policies. Most organizations set a 60- or 90-day expiration, meaning that passwords must be reset within that time limit.
    
- **BIOS/UEFI passwords** – Configuring a BIOS or UEFI password ensures that the system settings stored in the BIOS or UEFI cannot be accessed or changed by unauthorized users.
    
- **Restricting user permissions** – Users should only be granted permissions that they need to complete their jobs. For users that need administrative-level permission, the users should be given two accounts: one normal account with more restrictive permissions that they use for day-to-day activities and one administrative account that they use when performing administrative duties. Also, as a rule, permissions should be assigned to groups, and user accounts should be added to group accounts. This makes permission administration much more manageable.
    
- **Changing default user names and passwords** – Always change the user names and passwords for any default user accounts that are created when an operating system or application is installed. Most IT professionals and hacker are aware of default account credentials. Renaming these accounts provides a level of protection. Always research any operating system or application that you install to learn of any default user accounts that are created at installation.
    
- **Disabling the Guest account** – All default accounts that are created should be disabled if they will not be used. This is particularly important for the Guest account. If possible, you should also rename the guest account. The Guest account is disabled by default in Windows 10 and above.
    
- **Screensaver required password** – Screensavers start after a period of idle time. For security reasons, a screensaver password policy is used to ensure that a user is required to enter his password when returning to his session. In addition, many companies have logoff policies that require users to log off from a computer when leaving for prolonged periods of time.
    
- **Timeout/screen lock** – It is a good practice to configure a computer to implement a screen lock after a certain amount of time without user interaction. This can be employed as part of the screensaver required password.
    
- **Disable Autorun/Autoplay** – Because you are never ensured that media, including USB flash drives, CDs, DVDs, and so on, are safe and uncontaminated, you should be careful when inserting new media into a CD-ROM, DVD, or USB drive. Windows 10 and 11, by default, have disabled AutoPlay, but it is always worth double-checking to verify that it has not been enabled.
    
- **Login time restrictions** – Login time restrictions are configured by administrators to limit the hours during which a user can log in to a system. This security feature, however, can cause problems if for any reason a user works outside his normal business hours.

# E1Q68
Which of the following is an example of phishing?
### Explanation

An example of phishing is an email request pretending to be from a financial institution asking you to log in and change your password using the provided link. Phishing attacks always appear to be from a legitimate source.

An example of a Trojan is a Visual Basic script attached to an email that infects your system. A virus could also infect you in this way.

Spam is unsolicited email.

An example of spyware is a program that sends out your personal information to an advertiser usually without your permission.

# E1Q69
A technician has been tasked with deploying a set of consistent security settings across dozens of company-issued tablets, including Wi-Fi credentials, VPN access, and restrictions on app installations. Which of the following mobile security methods would best allow the technician to apply and manage these settings efficiently?

### Explanation

Configuration profiles are used to centrally define and deploy settings across multiple mobile devices. These profiles can include network settings, VPN credentials, password requirements, restrictions on app usage, and more. They are commonly managed through a mobile device management (MDM) system and are especially useful in environments where uniform policy enforcement is critical.

Device encryption protects data stored on the device by making it unreadable without proper authentication. While it secures the device's contents, it does not assist in configuring or managing system settings.

Screen locks help prevent unauthorized access to the device when it is idle but are configured locally on the device and do not manage broader settings.

Patch management ensures that the device's operating system and apps are up to date with the latest security fixes. It is an important part of mobile security but does not address the deployment of custom configuration settings.

# E1Q72
In a security awareness class, the instructor discusses malicious software that relies on other applications to execute and infect the system. Which type of malware is being discussed?
## Explanation
A virus is malicious software (malware) that relies on other application programs to execute and infect a system. The main criterion for classifying a piece of executable code as a virus is that it spreads itself by means of host applications. The hosts could be any application on the system.
The standard security best practices for mitigating risks from malicious programs, such as viruses, worms, and Trojans, include implementation of antivirus software, use of a host-based intrusion detection system, and the imposition of limits on the sharing and execution of programs.
A worm does not require the support of application programs to be executed. It is a self-contained program capable of executing and replicating on its own. Typically, a worm is spread by emails, transmission control protocols (TCPs), networks, and disk drives.
A logic bomb malware is similar to a time bomb that is executed at a specific time on a specific date. A logic bomb implies a dormant program that is triggered following a specific action by the user or after a certain interval of time. The primary difference between logic bombs, viruses, and worms is that a logic bomb is triggered when specific conditions are met.
A Trojan horse is malware that is disguised as a useful utility, but actually embeds malicious codes within it. Trojan Horses use covert channels to perform malicious activities. When the disguised utility is run, the Trojan horse provides a useful utility at the front end and performs malicious activities in the background, such as deleting system files and planting a backdoor into a system.

# E1Q78
When scheduling a maintenance window for customer-facing systems, which of the following is the LEAST important consideration?

**Explanation**

The priority of the project(s) that rely on the systems undergoing maintenance is the least important consideration. System maintenance can be corrective, preventative, or perfective, meaning it can be undertaken to fix a problem, to prevent a problem from occurring, or to improve the system's performance or stability. If maintenance is intended to add a feature or improve the user experience, then it could be scheduled around the needs of a high-priority project that relies on those system resources. However, maintenance to fix an issue should be scheduled to occur as soon as possible, regardless of the needs of the various projects.

A maintenance window refers to the predefined period during which changes are allowed to occur, which is typically during off-hours. Maintenance windows are likely to be held for normal and standard changes. Standard changes are pre-approved, low-risk updates that follow established procedures and require minimal oversight, such as driver updates. Normal changes are those that go through the full change management process, but are not performed to fix an urgent condition.

All of the other options are important considerations when scheduling maintenance for customer-facing IT systems. Customers can be internal or external users. Customer notifications are critical if and when customer access will be affected. They should get advance warning so they can plan for the temporary lack of access.

Rollback plans are designed to recover operations if something goes wrong with the upgrade or maintenance tasks. A rollback plan allows the system to quickly be returned to its prior working state.

Validation checks are assessments made after the maintenance is complete to ensure that the system has been properly serviced and is functioning well, and the changes did not adversely affect other systems.

# E1Q79
While performing your IT technician duties, you plan to use the USMT tool. Why should you use this tool?


**Explanation**

The User State Migration Tool (USMT) is used to migrate user settings from one operating system to another in Windows 10.

The Windows Upgrade Advisor is a tool used to determine if your computer is able to run a new operating system version.

The Microsoft Assessment and Planning Toolkit is a tool used to plan desktop and server migrations.

A hardware compatibility list (HCL) is a list of hardware that is compatible with a particular operating system version. Each version of Windows has its own HCL.

# E1Q90
You plan to replace some components within a computer. As a recommended practice, what should be the first step towards disassembling a computer?
**Explanation**

As a recommended practice, you should disconnect the power cord from the power supply unit socket in the system case before disassembling a computer. Even in the shutdown state, the power supply unit will be powered on if the power cord is connected to the live socket on the wall. You should also ensure that you follow proper ESD precautions.

If a separate monitor is connected and powered on, ensure that you have also disconnected the monitor. Any other devices that have their own power source should also be disconnected as a precaution. In addition, it is a good idea to disconnect any wired telephone lines, as they can carry electrical current.

You should not remove the processor from the motherboard while disassembling your computer. The motherboard is typically powered on when the power supply is connected to power cords that send power signals. Removing the processor is not a standard step in disassembling a computer unless the processor or motherboard is to be replaced.

You should not disconnect the power supply unit from the motherboard. If the power supply unit is connected to a power cord that is sending power signals, you should remove the power cord first. With the power supply unit powered on, you can damage the motherboard and attached devices by attempting to remove the power supply unit in the live state.

You should not remove the memory modules from the motherboard. Removing memory modules without disconnecting the power cord from the power supply unit can damage the memory modules.

According to CompTIA, there several safety tips that computer technicians should keep in mind:

- Disconnect the power before repairing PC. This includes disconnecting all parts from the electrical outlet.
    
- Remove jewelry and ties. You should remove anything that may become caught on the computer parts.
    
- Use proper lifting techniques. Always lift with your legs, not your back.
    
- Be aware of personal weight limitations as well as weight limits for inanimate objects. You should be aware of your own personal weight limitations to ensure that you do not try to lift an object that is too heavy for you. Also, any surface on which you place the computer may also have weight limits.
    
- Be aware of electrical fire safety. Know the location of fire extinguishers. Understand the proper techniques for fighting small fires. Familiarize yourself with evacuation procedures.
    
- Understand cable management techniques. Always keep safety in mind when routing cable.
    
- Wear safety goggles and air filter masks when needed.
    
- Understand and follow all local, state, and federal government regulations. This includes Occupational Safety and Health Administration (OSHA) and Environmental Protection Agency (EPA) guidelines.