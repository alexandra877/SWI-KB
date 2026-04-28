MS Windows OS - Installation and setup of Cisco AnyConnect
This guide is for Microsoft Windows OS, including Windows on ARM64, and might not be
accurate for other operating systems.
Additional info and guides for other systems -> Cisco AnyConnect generic info and Links to OS-specific User Guides
Anyconnect VPN Client software is now renamed to Cisco Secure Client VPN.
Cisco Secure Client VPN might not work as intended if other 3rd party VPN clients are used/connected at the same time.
We do not recommend nor support such use scenarios.
To get Cisco Secure Client VPN to work on Microsoft Windows OS, there are some requirements:
We recommend that you upgrade your Windows 10 install to build 22H2 or later and Windows 11 to build 23H2 or later.
you need to have all the OS updates installed up-to-date
you need to have the Firewall enabled in OS Security Settings.
3rd party vendors for OS Firewall (usually shipped with "Internet Security" software suites) do usually not play well with Anyconnect VPN.
We recommend having that 3rd party FW component disabled and use default OS Windows Defender Firewall.
you need up-to-date AntiVirus and AntiMalware.(see on Cisco.com site for supported versions to choose from)
if you are using a 3rd party vendor for Antivirus/AntiMalware, make sure that the default Windows Defender Antivirus is disabled in
Windows security options/settings
if you already have Cisco AnyConnect installed, we recommend to remove/uninstall it prior to starting this HowTo
at some points during install, you may need to provide one-time agreement on OS security side. (you will be notified about this by the OS)
we recommend having all the above requirements, installed or set up prior to installing Cisco Secure Client.
>>Cisco Secure Client VPN install for Windows or Windows on ARM PCs, managed by Visma
via Intune or SCCM:
Please note:
When AD-user is added to the VPN group (manually or via approved request in MimPortal), the needed software package is automatically pushed to
managed windows-PCs via Intune/SCCM tool.
The package contains Cisco Secure Client VPN, ISEPosture plugin and DART tool.
Below HowTo can still be done manually in case the above automation does not work for you, or for troubleshooting.
Open the Software Center app or, in case of Intune managed devices - the Company Portal app, and install "Cisco Secure Client VPN".
Note that the version of the client depicted below may be different/older than what you currently have available because of software upgrades and rollouts.

>>Cisco Secure Client VPN install Non-domain/non-managed computers :
Note: Install procedure for Windows 32/64 or Windows on ARM64 is the same, but there are different install packages for the two variants.
Make sure you download and install the packages that are suitable for your own Windows OS variant.
Go to https://sites.google.com/visma.com/vpnclient.
You may be first prompted for authentication if you are not already connected to the Visma Mail account in the browser.
Log in with your Visma Google credentials (Visma e-mail address and corresponding password/ Google Auth token)
Please note that download might not work properly unless you use incognito/private browser tab/window.
Once logged in, download page should look like below:

Choose the operating system that you use - in this case is should be "Microsoft Windows 32/64bit" or "Microsoft Windows on ARM", then click "Download",
like below.
Use similar steps as described above in order to download matching ISE Posture plugin and ISECompliance (needed later).

>> Client Setup and VPN connection for Windows OS:
Install downloaded packages (VPN Client and then ISE Posture plugin then ISECompliance).
Once install finishes, start Cisco Secure Client.
Make sure access.visma.com is in address field.
Click Connect. You will be prompted for credentials.
For unmanaged device (that is not registered on Visma AD) make sure you select "PersonalDevice" or "PersonalDevice-NoSplit" for the Group option or
you will not be able to connect.
For AD registered Windows machines, select "CorporateDevice" or "CorporateDevice-NoSplit" Group option.
IMPORTANT!
We recommend to use normal "PersonalDevice" or "CorporateDevice" group options so that only Visma office and DC related traffic flows through VPN.
"*-NoSplit" Group options will route ALL traffic via the VPN tunnel, including internet related traffic.
Please be aware of this and use them only when needed to access internet destinations that require you to be behind a trusted/known IP address.
To save bandwidth it is strongly recommended that Youtube or other similar streaming services should not be used while connected with the "*-NoSplit" opt
ions.

Enter your regular Visma username + password and click "OK". (example username: john.doe - no domain name before user or "@visma.com" at the end.)
IMPORTANT! If login fails at this point and you are sure the used credentials are OK, most probably your user does not have any 2fa token assigned
(SMS or Google Auth.)
Login does not work without a 2fa token. You can enrol a token yourself via the Selfservice Portal or ask for support on setting this up via Visma
ServiceDesk in One Support Portal.
When prompted, input OTP 2FA token or SMS code. (SMS is sent to the phone number that is registered for your Visma AD user. For enabling OTP 2FA
token, go to the Selfservice Portal or please contact Visma ServiceDesk)
System scan will start.
If it does not, then please uninstall any Cisco Anyconnect or Cisco Secure Client related software from your computer and re-start from beginning. You
might have had the AnyConnect client installed from before.

You will still need to have an active Firewall, up-to-date Anti-Virus and Anti-Malware tool, up-to-date OS updates (usually provided by Windows or pre-
installed on AD registered PCs).
You have 15 minutes to resolve any issues, then VPN will auto-disconnect, like below.
If the time is not enough for you, you can re-connect anytime back and you will continue from where you left.
After the scan is successful , you will get to "compliant" status and access to Visma resources is granted via VPN.

Related articles
Linux Ubuntu LTS - Installation and setup of Cisco AnyConnect
Mac OS X - Installation and setup of Cisco AnyConnect
MS Windows OS - Installation and setup of Cisco AnyConnect
Chrome OS - Installation and setup of Cisco AnyConnect
Secure Private Access (SPA)