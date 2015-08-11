Title: The horror of Juniper VPN
Date: 2015-08-11 16:35
Author: Peter
Category: Espionage
Tags: Espionage, Linux
Slug: horror-of-juniper-vpn
Summary: We waste tax payers money on an outrageously bad piece of VPN software that also opens backdoors for government and industrial espionage.

I am generally happy with the services provided by the IT department in my institute, except when it comes to "Internet" access and especially to the VPN. They locked down the ports, so I am not allowed to sync the time online or use end-to-end encrypted VoIP. They did this to protect the IP produced in the institute and keep cyberspies away. Yet, I would be free to use an infamous American proprietary VoIP spyware, those ports are open. It is a twisted mindset. The VPN situation is even worse.

To use the VPN, I have to make my system more vulnerable and install several backdoors for the NSA. The institute pays Juniper Networks for their VPN solution. They provide mystery 32-bit binary Java blobs and I have to give root access to these blobs. This is sickening at multiple levels.

This is 2015 and Juniper gives you 32-bit, and only 32-bit software. They sank lower than Adobe, which is remarkable in itself. Spanish tax payers pour money into an NSA-backed US company that is only able to produce 32-bit software. We can be glad they made the jump from 16 bits. They only had twenty-nine years for that. I have to install 32-bit libraries only to run a 32-bit Java and Firefox to use the VPN. 

While some are lucky and a 32-bit Java is sufficient, I also must have the browser running, as the host is configured [not to accept](https://wiki.archlinux.org/index.php/Juniper_VPN#ncapp.error_Failed_to_connect.2Fauthenticate_with_IVE) command line access. On an Ubuntu system, and only on an Ubuntu system, it is theoretically possible to run the 32-bit Java from a 64-bit browser, but forget it from a non-Ubuntu distribution. Information on this should be available [here](https://kb.juniper.net/InfoCenter/index?page=content&id=KB25230), but you will get this error message:

    Either a login is required or the article was not found.
    You must be logged in to access Knowledge Center Subscriptions.

Again, we paid for the licenses. Clearly this knowledge is so precious we need to pay extra. So there is no other option, but to install a large number of 32-bit dependencies from untrusted user repositories and further compromise the security of my system.

The browser first runs the first mystery binary blob called Host Checker. This supposed to check the antivirus software. On a Linux system. This is just pure madness: both the idiots at Juniper and our IT department are guilty in sustaining the deception. This is the first binary blob that requires the root password, so I guess this is the one that sends over the contents of my crypttab to the NSA. The best part of it is that the config directory it creates in `$HOME` must be on a partition that allows flipping the uid bit. That took me two hours to figure. For security reasons, it was disabled on my home partition. So I have to disable one more security feature to connect "securely" to the institution's network from a "verified" "secure" computer. This is not a joke.

On a good day, Host Checker runs successfully, and I get to the next step, which is launching Network Connect. This 32-bit marvel of software engineering usually cannot launch on the first try. I have to log out and log in a few times before the GUI shows up and it successfully connects. My guess is that this binary blob broadcasts all data continuously to every espionage agency in all Five Eyes countries. I am not happy when I connect over 3G, my data plan is only two gigabytes a month.

Once I drilled all these security holes in my Linux box, Network Connect will automatically disconnect every three hours, crashing my entire network stack. A more appropriate name would be Network Disconnect, or perhaps Network Semiconnect. According to IT, the reason to this timed disconnection is that they have a limited number of licenses. 

Why do I need the VPN in the first place? My sole reason is to ssh to the login node of the cluster. I tried to convince IT to allow logging in without the VPN -- my setup is passwordless anyway, the computers involved exchange massive encrypted keys to connect. They could disable login with passwords, they could ensure other security measures, but no. We have to continue with this absurd solution: Catalonia is barely recovering from recession, yet we pay to the NSA people for a technologically outdated spyware to give a false sense of secure connection, while making the client computer less secure and destroying our privacy, moreover, we have to restart this junk every three hours. What can I say? Molt bé, molt bé.
