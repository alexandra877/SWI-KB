Mac OS X - Installation and setup of Cisco AnyConnect
This guide is for Mac OS and might not be accurate for other operating systems.
Additional info and guides for other systems -> Cisco AnyConnect generic info and Links to OS-specific User Guides
Anyconnect VPN Client software is now renamed to Cisco Secure Client VPN.
Cisco Secure Client VPN might not work as intended if other 3rd party VPN clients are used/connected at the same time.
We do not recommend nor support such use scenarios.
To get Cisco Secure Client VPN to work on Mac OS, there are some requirements:
you need to have all the OS updates installed up-to-date
you need to have the Firewall enabled in OS Security Settings
you need up-to-date AntiVirus and AntiMalware (see on Cisco.com site for supported versions to choose from)
if you already have Cisco AnyConnect installed, we recommend to remove/uninstall it prior to starting this HowTo
at some points during install, you may need to provide one-time agreement on OS security side. (you will be notified about this by the OS)
we recommend having all the above requirements, installed or set up prior to installing AnyConnect.
It is recommended to have your Mac OS machine enrolled in Intune, so it becomes a managed machine related to OS upgrades, Wifi certificates, AntiVirus
(SentinelOne Visma license), etc.
Without enrollment to Intune, you will have to manage OS upgrades and find suitable/working AntiVirus software by yourself.
You are also free to stop using Intune and un-enroll at any time.
For Intune enrollment, please contact our Service Desk team.
Step-by-step guide
>>Cisco Secure Client VPN install for Intune managed MacOS PCs:
If your MacOS is managed via Intune, then you can install the Cisco Secure Client VPN software and its components via the Company Portal app.
Open the Company Portal app, and install "Cisco Secure Client VPN".
Note that the version of the client depicted below may be different/older than what you currently have available because of software upgrades and rollouts.
>>Cisco Secure Client VPN install non-managed MacOS PCs :

Cisco Secure Client VPN download:
Go to https://sites.google.com/visma.com/vpnclient.
You may be first prompted for authentication if you are not already connected to the Visma Mail account in the browser.
Log in with your Visma Google credentials (Visma e-mail address and corresponding password/ Google Auth token)
Please note that download might not work properly unless you use incognito/private browser tab/window.
Once logged in, download page should look like below:
Choose the operating system that you use - in this case is should be "Apple Mac OS X", then click "Download", like below.

ISE Posture plugin is already included in the VPN Client install pack. Make sure you have it selected during software install.
ISECompliance is the definitions module for the ISE Posture plugin. You can download and install that separately, after the VPN Client setup is completed.
Cisco Secure Client VPN Software installation:
After download is done, according to steps described above, go to right-down corner of you Mac OS Desktop and check Downloads section status.
Then click on the downloaded Cisco Secure Client DMG file, like shown below:
===>>
Shortly, the DMG file will be mounted on your desktop and its content will be shown in a new window.

Now double-click on "Cisco Secure Client.pkg" and the install wizard will start.
Click "Continue"(agree to license terms when prompted), until you reach the "Installation Type" section.
Now, deselect all options except "VPN" and "ISE Posture".

Click "Continue" again. Then click "Install".
Operating system is now asking for installation approval and you are prompted to enter your MacOS user password for confirmation.
Enter your Mac OS credentials and then click "Install Software".
The selected package is now installed.
Wait a few minutes for the installation to finish. then click "Close".
You will be asked if you want to keep the VPN Client Installer or move it to Trash. Whatever option you select, does not affect the already installed
software.
In the end, go to the "AnyConnect" or "Cisco Secure Client" Image mount on your desktop, right-click and choose "Eject" option.

During a or at the end of the install process, you will get prompted to enable access for VPN Client and related Network extensions.
Make sure to allow access when/if prompted by Mac OS Security settings and toggle those setting to ON.
This concludes the basic VPN client software installation.
Now you can also install the separate ISECompliance module if, for some reason it fails to be automatically downloaded by the VPN Client after initial VPN
login.
Follow the steps in next sections in order to have it set up and configured for VPN access to Visma resources.
Client Setup and VPN connection:
Go to LaunchPad, or via Finder to Applications, find and start the Cisco Secure Client VPN software.
Please allow system access for the Cisco Secure Client VPN software via Mac OS security settings, if you get prompted for that.
This may happen when running the software for the first time, depending on the security settings of your operating system.
Make sure access.visma.com is in address field.
Click Connect. You will be prompted for credentials.

Make sure you select "PersonalDevice" or "PersonalDevice-NoSplit" for the Group option or you will not be able to connect.
(If you own a MacOS device issued by Visma and enrolled via/to Intune, then you can select one of the CorporateDevice profiles as well.)
Personal/Corporate profiles just define how the compliance related system scan is done, not the access level which is defined by the VPN group.
IMPORTANT!
We recommend to use normal "PersonalDevice" group option so that only Visma office and DC related traffic flows through VPN.
"*-NoSplit" Group options will route ALL traffic via the VPN tunnel, including internet related traffic.
Please be aware of this and use them only when needed to access internet destinations that require you to be behind a trusted/known IP address.
To save bandwidth it is strongly recommended that Youtube or other similar streaming services should not be used while connected with the "*-NoSplit" opt
ions.
Enter your regular Visma username + password and click "OK". (example username: john.doe - no domain name before user or "@visma.com" at the end.)
IMPORTANT! If login fails at this point and you are sure the used credentials are OK, most probably your user does not have any 2fa token assigned
(SMS or Google Auth.)
Login does not work without a 2fa token. Please ask for support on setting this up via Visma Servicedesk.
When prompted, input OTP 2FA token or SMS code. (SMS is sent to the phone number that is registered for your Visma AD user. For enabling OTP 2FA
token, please contact Visma ServiceDesk)
Please allow system access for the Anyconnect software modules via Mac OS security settings, if you get prompted for that.
This may happen when running the software for the first time, depending on the security settings of your operating system.

System scan will start.
If it does not, then please uninstall any Cisco Anyconnect related software from your computer and re-start from beginning. You might have had the
AnyConnect client installed from before.
Remember, you will still need to have an active Firewall, up-to-date Anti-Virus and Anti-Malware tool, up-to-date OS updates (you can find list of supported
vendors/versions on Cisco.com site).
You have 15 minutes to resolve any issues, then VPN will auto-disconnect, like below.
If the time is not enough for you, you can re-connect anytime back and you will continue from where you left.
After the scan is successful , you will get to "compliant" status and access to Visma resources is granted via VPN.

Related articles
Linux Ubuntu LTS - Installation and setup of Cisco AnyConnect
Mac OS X - Installation and setup of Cisco AnyConnect
MS Windows OS - Installation and setup of Cisco AnyConnect
Chrome OS - Installation and setup of Cisco AnyConnect
Secure Private Access (SPA)