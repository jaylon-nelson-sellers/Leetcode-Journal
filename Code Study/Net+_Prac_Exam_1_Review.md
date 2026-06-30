# Q1
## Question
You are examining the packets captured on your network. You notice some communication between your Cisco router and someone from outside your network. The packets indicate that the communication is occurring over TCP port 23. Which protocol is being used?  

## Answer
Telnet

## Explanation
Telnet is the protocol that communicates over TCP port 23. Telnet is a protocol that allows users to access remote computers and devices. Cisco routers can be configured to allow remote administration though this protocol.  

File Transfer Protocol (FTP) communicates over TCP ports 20 and 21 to transfer files. Secure Shell (SSH) communicates over TCP port 22 to allow secure data transfer. Trivial File Transfer Protocol (TFTP) communicates over UDP port 69 to transfer files.  

Telnet and FTP both work at the Application layer of the OSI model. SSH and TFTP both work at the Presentation layer of the OSI model.  

For the Network+ exam, you need to know the following protocols and their default ports:

FTP – 20, 21
SSH, SFTP – 22
TELNET – 23
SMTP – 25
DNS – 53
DHCP – 67, 68
TFTP – 69
HTTP – 80
NTP – 123
SNMP – 161/162
LDAP – 389
HTTPS – 443
SMB – 445
Syslog – 514
SMTP TLS – 587
LDAPS – 636
Structured Query Language (SQL) Server – 1433
RDP – 3389
SIP – 5060/5061

# Q2
## Question
Your company’s enterprise includes multiple subnets, each of which uses a different addressing class. Match the first two octets of the IPv4 addresses on the left with the IPv4 address type that describes it. Each address will only match to a single address type, and each address type will only match a single address.

### IPv4 Address Octets

- 162.58.x.x
- 219.214.x.x
- 172.16.x.x
- 225.47.x.x
- 169.254.x.x
- 12.174.x.x
- 127.0.x.x

## Answers and Explanation

The IPv4 address types should be matched with the given IPv4 addresses as follows:

- Class A – 12.174.x.x
- Class B – 162.58.x.x
- Class C – 219.214.x.x
- APIPA – 169.254.x.x
- Private – 172.16.x.x
- Loopback– 127.0.x.x
- Multicast – 225.47.x.x

# Q3
## Question
Prior to deploying a new wireless access point at a retail store that is located in a strip mall, you decide to perform a site survey. Which statements describe the purpose of doing this?

## Answer
to find the frequency and power settings to be used on access points and to calculate the number of access points required for the coverage area
## Explanation
Site surveys are done to assess the coverage area of each access point and the number of access points required for a specified coverage area.

A site survey should be done prior to installing a WLAN. Site surveying is required to determine the frequency and power settings of each access point to avoid channel overlapping and interference. A site survey is the only technique that helps the customer install complete WLAN coverage for mobile roaming clients. After a proper site survey, a site survey engineer can identify the position of access points within the facility. The quality of the output of the site survey depends on the experience and knowledge of the site survey engineer.

Site survey tools can collect data to show the relative strength of signals in the areas being serviced by the access points. This output can be color-coded and overlaid on top of the floor plan and is often referred to as a heat map of the wireless signals. A floor plan is used to detail the structures, devices, and other network elements positioning on any given floor. These plans can be useful for troubleshooting, identifying weaknesses, and designing policies and procedures.

None of the other options is valid.

Keep in mind that wireless access point (WAP) placement is very important. WAP placement varies based on the environment in which the WAP is placed. WAPs should be centrally placed to ensure that the maximum number of devices can use it. Also, you should consider the other devices in the area, such as cordless telephones, that can cause interference. Placement is particularly important if more than one WAP is implemented in the same area. It may be necessary to configure WAPs that are in close proximity to use different channels.

With the increased use of wireless, both coverage- and capacity-based planning should be completed to provide acceptable goodput. Goodput refers to the number of useful information bits that the network can deliver (not including overhead for the protocols being used).

# Q4
## Question
If a routing table contained multiple routes for the same destination, which were inserted by the following methods, which route will the router use to reach the destination network?

## Answer
The route configured as a static route.

## Explanation
A static route will be preferred because it has the lowest administrative distance. Administrative distance is a feature that is used to select the best path when two or more routes to the same destination exist. These multiple routes are the result of different protocols being available to be used. Routing protocols are dynamic routing methods. With the default configuration, a router will prefer static routes to dynamic routes. The default administrative distances for the offered options are:

- RIP – 120
- OSPF – 110
- BGP – 20
- Static – 1    

When Routing Information Protocol (RIP), Open Shortest Path First (OSPF), Border Gateway Protocol (BGP), and static routing is enabled on a router, the router will prefer the static route.

Static routing does not consume the network bandwidth that dynamic routing does because static routing does not require routing broadcasts over the network. However, in large networks, dynamic routing is a better choice because static routing requires manual updates to all routing tables. In dynamic routing, convergence occurs when all devices have learned of a routing table change and have updated their routing table.

If a router receives a packet for a destination not on the router's routing table, it usually forwards the packet to the next available router until the packet is "forwarded out." However, if the router is configured with a gateway of last resort, it will automatically forward a packet for an unknown destination to the gateway of last resort.

For the Network+ exam, you need to understand static vs dynamic vs default routes. Static routes are manually configured by an administrator. Dynamic routes are discovered by the devices through the messages that they send out. Default routes are the routes on a computer that define the packet forwarding rule to use when no specific route can be determined for a given destination address.


# Q5
## Question
You are configuring a new small office home office (SOHO) at a small insurance office. After documenting the network requirements, you decide to use Network Address Translation (NAT) so that only one public address will be needed. You want to use the IANA-designated private IP address range that provides host IP addresses with a maximum of 16 bits. What is a valid host IP address in this range? 
## Answer
192.168.0.1
## Explanation
 Of the IP addresses listed, 192.168.0.1 is a valid host address within the range of IANA-designated private IP addresses that provide a maximum of 16 bits per host address. The IP address 11.0.1.0 is a public, or external, IP address. The Internet Engineering Task Force (IETF) is a working group that creates standards for the Internet. The IETF is divided into a number of smaller committees, including the Internet Assigned Numbers Association (IANA), which decides how the IP address space is used. The IANA has reserved three address spaces for private or internal IP addressing. Internal IP addresses are never assigned by the IANA for use on the public Internet. The private IP address ranges are as follows: 10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16. Note that the number after the slash (/) character is referred to as the network address prefix, which indicates the number of bits in the network address. Private IP addresses in the range 192.168.0.0/16 can be used as a Class B address space with a 16-bit network address and a 16-bit host address, or they can be subnetted into Class C addresses. Valid host IP addresses in this address space range from 192.168.0.1 through 192.168.255.254. The first 16 bits in the address correspond to the network address and the last 16 bits in the address correspond to the host address. The internal IP address range 10.0.0.0/8 provides IP addresses with an 8-bit network address and a 24-bit host address. The first 8 bits of a 10.0.0.0/8 internal IP address correspond to the network address, and the last 24 bits correspond to the host address. Valid host IP addresses in this address space range from 10.0.0.1 through 10.255.255.254. The address 10.251.250.100 is a valid host IP address in this range. The 172.16.0.0/12 private IP address range provides a 12-bit network address and a 20-bit host address. IP addresses in the range of 172.16.0.1 through 172.31.255.254 are valid host IP addresses for this address space; the first 12 bits correspond to the network address, and the last 20 bits correspond to the host address. The IP address 172.30.250.10 is a valid host IP address in the range 172.16.0.0/12.
# Q6
## Question
A user is complaining that she cannot log on to the network server. What specific steps should you take to locate the problem?
## Answer

A) Ping the server. C) Have a user on a remote segment try to log on to the server. D) Have a user on the local segment try to log on to the server.

## Explanation


A logical first place to start troubleshooting would be to determine if the condition is network-wide or workstation specific. Have other similar users both on local segments and remote segments attempt to perform the same actions. You should also verify that connectivity with the server can be established. You can do this by pinging the server.

Rebooting the network server or the user's workstation are not good first steps in attempting to resolve the problem.

The troubleshooting steps in order are:

1. Identify the problem. a. Gather information. b. Question users. c. Identify symptoms. d. Determine if anything has changed. e. Duplicate the problem, if possible. f. Approach multiple problems individually.
    
2. Establish a theory of probable cause. a. Question the obvious. b. Consider multiple approaches. i. Top-to-bottom/bottom-to-top OSI model ii. Divide and conquer
    
3. Test the theory to determine cause. a. If the theory is confirmed, determine next steps to resolve the problem. b. If the theory is not confirmed, re-establish new theory or escalate.
    
4. Establish a plan of action to resolve the problem and identify potential effects,
    
5. Implement the solution or escalate as necessary,
    
6. Verify full system functionality and, if applicable, implement preventive measures.
    
7. Document findings, actions, outcomes, and lessons learned.

# Q7

## Question
To segregate employee traffic and guest traffic on your wireless network, you have decided to implement a plan whereby guest traffic is quarantined in a separate part of the network. All employees have company-issued devices. What can you implement to ensure that only employees have access to the non-quarantined areas of the wireless network?
## Answer
MAC filtering
## Explanation

Media Access Control (MAC) filtering allows the administrator to restrict device access to the network based on the MAC address associated with the Network Interface Card (NIC) on that device. The administrator can set up a permission list (filter) on the router where only devices with specific MAC addresses are allowed on the network. A MAC address is uniquely associated with a NIC, and is analogous to a Vehicle Identification Number (VIN) on an automobile. In essence, the MAC address is the serial number of the NIC.

Shared authentication and open authentication were the two insecure methods of authentication utilized under Wired Equivalent Privacy (WEP). Neither of these allows you to limit access to certain areas of the network.

Authentication for wireless can be configured to OSA or open system authentication (no authentication), shared key authentication (SKA), pre-shared key (PSK), or 802.1x/EAP. An open wireless network does not require any form of authentication. Wireless OSA does not use an encryption key. Under SKA, all of the clients used the same key, making the key very vulnerable to being cracked.

Temporal Key Integrity Protocol-Rivest Cipher 4 (TKIP-RC4) is an encryption method that was designed to provide security enhancements to wireless networks using WEP. WEP was an extremely weak encryption standard. TKIP added a key distribution method whereby each transmission had its own encryption key, an authentication method to verify message integrity, and an encryption method called RC4 (Rivest Cipher 4). WEP is based on RC4, but was poorly designed and used a too-short IV of only 24 bits instead of the standard 64 bits used by RC4.

Wi-Fi Protected Access (WPA) was an interim security improvement over WEP. WPA was later replaced by Wi-Fi Protected Access version 2 (WPA2). The most current version is WPA3, offering enhanced protection against various cyber threats. It provides stronger encryption through the use of the Simultaneous Authentication of Equals (SAE) protocol, which protects against offline dictionary attacks and brute-force attacks. Additionally, WPA3 introduces individualized data encryption, ensuring that each wireless connection is encrypted separately. This feature significantly enhances security by preventing attackers from intercepting and decrypting wireless traffic.

# Q8
## Question
Which options is a RADIUS implementation that was created to deal with Voice over IP (VoIP) and wireless services?
## Answer
 Diameter
## Explanation
Diameter was created to deal with Voice over IP (VoIP) and wireless services. It was created to address new technologies that RADIUS was not designed to handle. Although Diameter was designed to be backward compatible with RADIUS, some RADIUS servers have trouble working with Diameter servers. A RADIUS server provides authentication, authorization, and accounting (AAA). The server may also be referred to as a AAA server.

Terminal Access Controller Access Control System (TACACS) is the CISCO implementation of RADIUS. TACACS is the first generation and combines the authentication and auditing process. XTACACS is the second generation and separates the authentication, authorization, and auditing processes. TACACS+ is the third generation and provide all the features of XTACACS along with extended two-factor user authentication. TACACS+ adheres to AAA via a centralized database and can service multiple routers and switches. TACACS+ also allows challenge/response and password encryption.

# Q9
## Question

Which of the following terms refers to the point at which a product or technology is no longer maintained by the vendor?
## Answer

EOS
## Explanation

End of Support (EOS) refers to the point at which a product or technology is no longer supported or maintained by the vendor. After reaching EOS, the vendor stops providing updates, patches, or technical support for the product, leaving it vulnerable to security risks and compatibility issues.

End of Life (EOL) refers to the point at which a product or technology is no longer produced or sold by the vendor. After reaching EOL, the vendor may stop providing updates, patches, or technical support for the product.

Software management involves the processes and procedures for managing software applications within an organization. It includes tasks such as installation, configuration, updating, and monitoring of software to ensure optimal performance and security.

Decommissioning refers to the process of retiring or removing hardware, software, or other assets from a network or system. It involves safely shutting down and removing equipment, data migration, and ensuring compliance with legal and regulatory requirements. Owners, not vendors, decommission assets owned by the organization.

# Q10

## Question

Your company has decided to implement unified communication. You have been asked to implement a VoIP network. You need to connect the VoIP network to your company's PBX. What should you implement?

## Answer

F) UC gateway

## Explanation

You should implement a unified communication (UC) gateway to connect the VoIP network to your company's PBX.

Unified communications include VoIP, video, real-time services, quality of service (QoS), and UC devices. VoIP allows you to transmit voice communications over an IP network. Real-time services include instant messaging, presence information, voice, mobility features, conferencing services, desktop sharing, data sharing, call control, and speech recognition. Real-time services support both multicast and unicast communications. In unicast, one packet is transmitted to only one destination at a time. On the other hand, multicast sends packets to multiple destinations which is represented by a group address.

QoS allows you to give priority to communications based on different factors, including IP address, protocol, and so on. It includes Differentiated Services Code Point (DCSP) and Class of Service (COS). DCSP is a field in an IP packet that enables different levels of service to be assigned to network traffic. COS manages traffic in a network by grouping similar types of traffic together and treating each type as a class with its own level of service priority.

UC devices include UC servers, UC devices, and UC gateways. UC servers are responsible for managing the UC communications. UC devices help transport and monitor UC. UC gateways connect VoIP networks to other types of networks, such as PBX networks.

For VoIP implementations, you also need to understand VoIP private branch exchange (PBX) and VoIP gateway. A VoIP PBX is a device where voice traffic is encapsulated inside data packets for transmission across a data network. A VoIP PBX operates between a VoIP network and a traditional telephone network. A VoIP gateway is a device that converts telephony traffic into IP for transmission over a data network.

# Q11
## Question

Which of the following IP addresses are valid Class B host addresses if a default Class B mask is in use? (Choose all that apply.)

## Answer

A) 133.6.5.4 D) 190.6.5.4

## Explanation

The IP addresses 133.6.5.4 and 190.6.5.4 are both valid Class B addresses when a default mask is in use. The Class B default mask is 255.255.0.0 and the range of valid addresses is 128.0.0.0 – 191.255.255.255.

The IP address 10.6.8.35 is a Class A address. The Class A default mask is 255.0.0.0 and the range of valid addresses is 1.0.0.0 – 127.255.255.255, with the exception of the range 127.0.0.1 – 127.255.255.255, which is reserved and cannot be assigned.

The IP address 192.168.5.9 is a Class C address. The Class C default mask is 255.255.255.0 and the range of valid addresses is 192.0.0.0 – 223.255.255.255.

The IP address 127.0.0.1 is a Class A address, but it comes from a reserved portion that cannot be assigned. The range 127.0.0.1 – 127.255.255.255 is used for diagnostics, and although any address in the range will work as a diagnostic address, 127.0.0.1 is known as the loopback address. If you can ping this address, or any address in the 127.0.0.1 – 127.255.255.255 range, then the NIC is working and TCP/IP is installed.

# Q12
## Question

Click and drag the RSTP port state on the left to its matching equivalent STP role, on the right. RSTP port states may be used more once, and it may not be necessary to use all RSTP port states.

_(Note: The question text contains a minor typo, substituting "STP role" and "RSTP port state" headers relative to the instructions, but requires mapping the 802.1D STP states to their 802.1w RSTP equivalent states)._

## Answer

- **Blocking** -> Discarding
    
- **Listening** -> Discarding
    
- **Disabled** -> Discarding
    
- **Forwarding** -> Forwarding
    
- **Learning** -> Learning
    

## Explanation

Rapid Spanning Tree Protocol (RSTP) was developed to reduce the high convergence times required in Spanning Tree Protocol (STP), and introduces the alternate port and backup port. RSTP is an Institute of Electrical and Electronics Engineers (IEEE) standard, 802.1w, and is interoperable with 802.1d (STP). There are fewer transitional states used in RSTP than in STP. In RSTP, there are only Forwarding, Learning, and Discarding. The three states are defined as follows:

- **Forwarding** – the state of all root ports and designated ports. The port is passing traffic.
    
- **Learning** – the state of a port that was formerly discarding but due to a change in the topology (link down) it has transitioned to learn its new state. The port could return to discarding or move to forwarding depending on the new topology needs.
    
- **Discarding** – the state of all non-root and non-designated ports. The port is not passing traffic to prevent potential switching loops.
    

RSTP can reconfigure the spanning tree in less than a second, compared to the 50 seconds that STP may take. This is achieved through having fewer transition states, the use of alternate and backup ports, and faster transitions.

# Q13
## Question

Users are reporting Internet connectivity issues. After researching, you discover that the routing protocols in use on your network are experiencing routing loops. You must prevent this from happening. What should you do?

## Answer

Implement split horizon.

## Explanation

You should implement split horizon to prevent routing loops. Split-horizon route advertisement prevents routing loops in distance-vector routing protocols by prohibiting a router from advertising a route back onto the interface from which it was learned. None of the other options would solve the routing loop issue.

For the Network+ exam, you must understand the following common WAN issues:

- **Loss of internet connectivity** – Before you contact your Internet service provider (ISP), you need to troubleshoot the problem to determine if the problem is with internal devices or cabling. Once you have tested all internal equipment, you should contact your ISP if you are still having problems.
    
- **Interference** – If you discover WAN interference, you need to determine what is causing the interference. Once that is determined, you should take measures to prevent the interference.
    
- **Satellite issues** – The main issues with satellite connections is latency. If satellite does not offer the bandwidth needed, you need to research other possible WAN connections that you can implement.
# Q14
## Question

You have been called to troubleshoot a workstation problem in the oldest building on your company's corporate campus. The network workstations in that building are unreliable. When the room lights are on, connectivity is lost, but when the room lights are off, the network is functional. Upon arrival, you quickly survey the work environment. You observe the following conditions:

- Lighting consists mainly of fluorescent lights.
- Temperature is 65 degrees Fahrenheit (18 degrees Celsius).
- Humidity is 75%.
- Employees own space heaters, but they are not using them.
- Electrical outlets appear outdated.

What is most likely causing the loss of connectivity?

## Answer

Fluorescent lighting in the room

## Explanation

Because the loss of connectivity is only occurring when the fluorescent lights are turned on, it points to electromagnetic interference (EMI) being emitted by fluorescent lighting. EMI is essentially electrical noise that is picked up on the network cable. EMI from fluorescent lights can corrupt data; therefore, you should consider your choice of network cable carefully if you must place the cable near fluorescent lights. Ideally, network equipment should be maintained at a room temperature of 70 degrees Fahrenheit (21 degrees Celsius). However, even lower-than-ideal temperatures would not affect equipment.

Defective network hubs would not cause fluctuating connectivity problems. Rather, connectivity would be permanently lost until the problem hub is replaced. A bad switch module would also cause loss of connection. Switches can include Gigabit interface converter (GBIC) and small form-factor pluggable (SFP) modules. If one of these modules goes bad, you can either replace it if possible. Otherwise, the switch will have to be replaced. To determine if the module has failed, you need to use an LC loopback tester.

Voltage fluctuation in the outlets would not affect network connectivity. Instead, computers rebooting, computer power supply failures, or temporary loss of power could result from voltage fluctuation. EMI affects cable placement. Cable placement issues may vary depending on the type of media (twisted pair, coaxial, or fiber) used. You should avoid running cables near objects that may cause problems with the cabling. You should arrange cables to minimize interference. Ideally, Ethernet cables should not be placed close to high voltage cables, generators, motors, or radio transmitters. Often using shielded cabling will prevent this problem. You could also move the interfering device or the cable.

Cross-talk is a specialized type of EMI caused by parallel runs of twisted-pair cables. The only solution to this problem is to change the path of the cables. Near-end crosstalk (NEXT) measures the ability of the cable to resist crosstalk. Most commercial cabling will give you the minimum NEXT values that are guaranteed. Far-end crosstalk (FEXT) measures interference between two pairs of a cable measured at the other end of the cable with respect to the interfering transmitter.

# Q15
## Question

You utilize different components, protocols, and technologies on your company's network. You need to determine the layer of the OSI model where each functions. Match the components on the left with the layer from the OSI model on the right within which they operate.

## Answer

- **Physical layer** – Network cable
    
- **Data Link layer** – FDDI
    
- **Network layer** – IPSec
    
- **Transport layer** – TCP
    
- **Session layer** – RPC
    
- **Presentation layer** – MIME
    
- **Application layer** – DHCP
    

## Explanation

The components match the OSI layers as follows:

- **Physical Layer (Layer 1):** Deals with the physical transmission of data, such as **Network cables**.
    
- **Data Link Layer (Layer 2):** Responsible for node-to-node data transfer and physical addressing, such as **FDDI** (Fiber Distributed Data Interface).
    
- **Network Layer (Layer 3):** Handles packet forwarding and routing, where **IPSec** operates to secure IP packets.
    
- **Transport Layer (Layer 4):** Manages end-to-end communication and error recovery, such as the **TCP** (Transmission Control Protocol) protocol.
    
- **Session Layer (Layer 5):** Manages sessions between applications, such as **RPC** (Remote Procedure Call).
    
- **Presentation Layer (Layer 6):** Handles data formatting, encryption, and translation, such as **MIME** (Multipurpose Internet Mail Extensions).
    
- **Application Layer (Layer 7):** Provides network services directly to applications, such as **DHCP** (Dynamic Host Configuration Protocol).

# Q16
## Question

Which suppression methods are recommended for a fire in a facility that involves paper, laminates, and wooden furniture? (Choose two.)
## Answer
- A) Water
- B) Soda acid
## Explanation

Water or soda acid should be used to suppress a fire that has wood products, laminates, and paper as its elements. These materials represent Class A fires. The suppression method should be based on the type of fire in the facility; for example, soda acid removes the fuel, while water reduces the temperature.

It is important to select the appropriate fire suppression system:

- **Class A fires:** Involve common combustibles (wood, paper, etc.). Water and soda acid are appropriate.
    
- **Class B fires:** Involve flammable liquids (petroleum, coolants). Never use water on these fires.
    
- **Class C fires:** Involve electrical equipment and wires. Agents like Halon (now largely banned due to ozone depletion) or carbon dioxide are typically used.
    
- **Class D fires:** Involve combustible metals (magnesium, sodium, potassium). Dry powder is the required suppression method.
    

Note that some systems, such as those using carbon dioxide to eliminate oxygen, can be harmful to humans and are typically reserved for unattended facilities.

# Q17
## Question

You have recently been hired as a network administrator. After starting your new job, you discover that the network devices are not being monitored on a regular basis. You need to deploy a technology or protocol that will provide this service. Which protocol or technology should you deploy?

## Answer

A) SNMP

## Explanation

You should deploy **SNMP (Simple Network Management Protocol)** to monitor network devices. SNMP typically uses port 161 for communication. Information about a managed device's resources and activity is defined by a series of objects contained within a **Management Information Base (MIB)**.

SNMP management software uses several message types to interact with managed devices:

- **Get:** Requests and retrieves specific information from a managed device.
    
- **Set:** Modifies a variable or triggers an action on a managed device.
    
- **Trap:** An unsolicited message sent automatically from a managed device to an SNMP manager to notify it of a significant event or alert.
    

Other protocols mentioned serve different functions:

- **SMTP (Simple Mail Transfer Protocol):** Used for sending email.
    
- **DNS (Domain Name System):** Used to resolve hostnames to IP addresses.
    
- **DHCP (Dynamic Host Configuration Protocol):** Used to dynamically assign IP addresses to devices on a network.

# Q18
## Question

File Transfer Protocol (FTP) and Simple Mail Transfer Protocol (SMTP) work at which layer in the Open Systems Interconnection (OSI) model?

## Answer

D) the Application layer

## Explanation

FTP and SMTP work at the application layer in the OSI model. The application layer is responsible for interacting directly with the application. It provides application services, such as e-mail and FTP.

The following protocols work on the Application layer:

- FTP: Used to transfer data between hosts through the Internet or a network.
    
- SMTP: A Transmission Control Protocol (TCP)/ Internet Protocol (IP) protocol used to send and receive e-mail messages.
    
- TELNET: Used to allow remote logins and command execution.
    

The Session layer is incorrect because this layer creates, manages, and terminates sessions between communicating nodes. Session Control Protocol (SCP) works at the Session layer.

The Presentation layer is incorrect because this layer enables coding and conversion functions for application layer data. The Presentation layer includes graphic image formats, such as Graphics Interchange Format (GIF), Joint Photographic Experts Group (JPEG), and Tagged Image File Format (TIFF).

The Network layer is incorrect because this layer defines the network address or the Internet Protocol (IP) address, which are then used by the routers to make forwarding decisions.

Encapsulation is the process of packing of data and functions into a single component. De-encapsulation is the exact opposition of encapsulation, as information is removed from a package during this process. The steps of encapsulation are:

1. The Application, Presentation, and Session layers convert the message to data and send it to the Transport layer.
    
2. The Transport layer converts the data to segments and sends it down to the Network layer.
    
3. The Network layer converts the segments to packets and sends them to the Data Link layer.
    
4. The Data Link layer converts the packets to frames and sends them to the Physical layer.
    
5. The Physical layer converts the frames to 1's and 0's (electrical signals) and sends them across the network.
    

At each layer, header information is added. At the receiving end, the process is reversed, with headers being stripped off at each layer. This reverse process is known as de-encapsulation.

# Q19
## Question

What is the purpose of a pointer (PTR) DNS record?

## Answer

F) It maps an IP address to a hostname.

## Explanation

A pointer (PTR) record maps an IP address to a hostname.

A host or address (A) record maps a hostname to an IPv4 address. An AAAA record maps a hostname to an IPv6 address. A mail exchange (MX) record maps a domain name to an e-mail server. A canonical name (CNAME) record contains an alias for an existing A record. A start of authority (SOA) record contains information regarding a particular DNS zone's start of authority.

A Domain Name System (DNS) server is the authority for a DNS zone, which contains DNS records. DNS servers allow users to request access to devices using either the devices' hostname or IP address. A DNS server stores fully qualified domain name (FQDN) to IP address mappings. This server allows clients to use the easier-to-remember FQDNs to access remote devices.

Dynamic DNS is an implementation of DNS that allows real-time updates to DNS records. With Dynamic DNS (DDNS), devices can automatically update their DNS records or allow a DHCP server to implement the updates on behalf of the DNS client.

# Q20
## Question

Which of the following would you perform periodically to ensure that the normal traffic patterns and volume have not changed?

## Answer

A) Reviewing baselines

## Explanation

It is important for a company to have a policy for reviewing baselines periodically, because network traffic may change over an extended period. Reviewing baselines is an important tool in identifying abnormal behavior. You would first need to establish a baseline. To establish a baseline, you would monitor network traffic (or some other metric) for a predetermined amount of time. This establishes what the “normal” amount of traffic is for that period of time. By comparing network traffic against the baseline, you can identify spikes that might indicate abnormal behavior.

Traffic analysis, also referred to as packet analysis, is performed with network monitoring tools. Two such tools are Wireshark and Solar Winds. Traffic analysis begins with capturing and logging traffic(packets). Once captured, the traffic can be analyzed, look for patterns and abnormalities indicating abnormal activity.

Notifications are system-generated communications indicating an event has triggered an alert. The notification may come in the form of an email, a text message, a signal to a pager, or a pre-recorded message to a cell phone.

Alerts are indicators that an event has reached a certain threshold.