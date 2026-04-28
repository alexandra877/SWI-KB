Linux Ubuntu LTS - Installation and setup of Cisco AnyConnect
This guide is for Linux Ubuntu LTS ( v22.04 and/or v24.04 ) and does not apply other operating
systems/versions.
Additional info and guides for other systems -> Cisco AnyConnect generic info and Links to OS-specific User Guides
Anyconnect VPN Client software is now renamed to Cisco Secure Client VPN.
Cisco Secure Client VPN might not work as intended if other 3rd party VPN clients are used/connected at the same time.
We do not recommend nor support such use scenarios.
All requests need to go via Servicedesk.
Service Desk can be contacted at https://jira.visma.com/servicedesk/customer/portal/8.
You are still required to go through and read below HowTo article in order to be informed what is needed and under what conditions you can connect from
a Linux machine.
Step-by-step guide
Steps you need to do in order:
1. Read through the listed prerequirements section and make sure you have a supported Ubuntu OS version and the proper AD groups are already
added to your user. (Leave the SSM Agent part as the last step).
2. Follow the steps below to download and install the VPN Client. After completing this, you will be able to connect to VPN but you will get
disconnected every 10 minutes or so - SSM Agent and compliance is needed to fix that.
3. Last step needed is to have SSM Agent set up on your PC so that system scan and compliance status are reported, keeping you VPN connection
up. Do not try and install SSM Agent yourself from other sources as it may lead to problems.
Contact ServiceDesk and ask them to assist you in SSM Agent installation and enrollment via AWS. They will provide you with the needed
downloads and command lines and activation codes so that everything is installed properly, including other dependencies.
Please note that we do not recommend having two or more Linux machines enrolled per VPN username as their alternate compliance reports will
lead to confusion and VPN disconnects.
To get Cisco Secure Client VPN to work on Ubuntu LTS, there are following prerequirements:
At username/AD level:
your INTERNAL user needs to be a member of your company's VPN group.
a list of onboarded companies and their VPN group name can be found linked here.
if your company is not in the list linked above, then please contact your IT manager to initiate onboarding via service
management.
access to VPN group can be requested via MimPortal (only accessible from internal Visma networks). HowTo instructions can be found li
nked here.
additionally, your INTERNAL user needs to be a member of VIT-S-VPN-LinuxEnabled AD group. This can be requested via ServiceDesk.
Direct Manager approval is needed.
your INTERNAL user needs to have an OTP SMS/GoogleAuth token assigned, different from the token you use to sign in to Google with
Visma account.
SMS or GAuth(time based) token can be enabled via https://selfservice2fa.visma.com/ . Login with your INTERNAL username
/password.
if you need help, please contact ServceDesk.
At OS level you need:
run Ubuntu Linux LTS 22.04 or 24.04. You will not be able to log in to VPN if using other Linux distributions.
you must run X-Window (you can only use the VPN Client via GUI)

optional, if you already have Cisco AnyConnect VPN Client or Cisco Secure Client VPN installed, it is recommended to remove/uninstall
it prior to starting this HowTo
all the OS updates installed up-to-date
the Firewall enabled (UFW needs to run as a service and also be in "enabled" state)
up-to-date AntiVirus and AntiMalware:
for personal computers please install and use ClamAV(install instructions are provided below - scroll down to reach that section)
for Visma issued PCs running Ubuntu Linux, you should use SentinelOne. Please see and follow dedicated SentinelOne install
instructions.
you need to have the SSM Agent installed. Please contact Servicedesk and work together to set this up on your machine.(HowTo is
included in the linked article)
SSM Agent - short description of what it does/why it is needed.
It is a service running on your system and checking for compliance (Firewall, Antivirus, OS updates).
Compliance status is reported securely (at request or periodically) to SSM server located in AWS Europe.
AWS server is polled periodically by VPN system and found non-compliant users are automatically disconnected from
VPN.
Cisco Secure Client VPN download:
Go to https://sites.google.com/visma.com/vpnclient.
You may be first prompted for authentication if you are not already connected to the Visma Mail account in the browser.
It is recommended to user private/incognito window while doing the below download steps.
Log in with your Visma Google credentials (Visma e-mail address and corresponding password/ Google Auth token)
Once logged in, download page should look like below:

Choose the operating system that you use - in this case is should be "Linux Ubuntu LTS", then click "Download", like below.
If download does not work for you, please use a private/incognito browser window and log in using Visma google account.
Please note that the VPN Client version number may differ from what is depicted below.

Cisco Secure Client VPN Software installation:
After download is done according to steps described above, go to your Downloads folder (or to the location where you saved them).
Files downloaded should be present there like pictured below:
Please note that the VPN Client version number may differ from what is depicted in these example images.
Then right-click on the downloaded AnyConnect TAR.GZ file and choose "Extract here", like shown below:
Shortly, the TAR.GZ file will be extracted and you can access the content as below:

Open Terminal window and go to Downloads/ and then to the extracted sub-directories similar to what is pictured below:
Please note that the VPN Client version number may differ from what is depicted in these example images.
Now, as you can see, you have here needed scripts for install/uninstall the VPN Client.
Execute "sudo ./vpn_install.sh" then enter your local system SUDO password when/if prompted.

Then accept license terms by typing "y" when prompted.
VPN Client is now installed.
The Cisco Secure Client App Icon can now be found on the taskbar or in the Apps menu.

If you want, you can now safely delete the extracted VPN Client folder in Downloads, and the related TAR.GZ file.
It is though recommended to keep the TAR.GZ file if you need to install or uninstall the VPN Client in future.
This concludes the Cisco Secure Client VPN software installation.
See further below for instructions on how to connect to VPN.
ClamAV install instructions:
Important! - If your PC, that runs Ubuntu Linux, was issued by Visma, please install SentinelOne as a solution for AntiVirus/AntiMalware. Please see and
follow dedicated SentinelOne install instructions.
Personal PCs should run ClamAV as an AntiVirus/AntiMalware solution.
Please see and execute the steps below in order to setup ClamAV on your Ubuntu Linux machine:
1. Open Terminal
2. Run "sudo apt update" to update package lists.
3. Execute "sudo apt install clamav clamav-daemon -y" to install ClamAV and its daemon. (both are
needed for system compliance)
4. Run "sudo freshclam" to download the latest signature database.
5. Make sure the process runs by executing "sudo systemctl restart clamav-daemon"
6. You can now exit/close the Terminal window.

Client Setup and VPN connection:
Start the Cisco Secure Client VPN by clicking on the Icon in the taskbar or from the Apps menu.
Once started, enter "access.visma.com" in the Connect To text box, then click on "Connect" button below.
Please ignore and click on "Close" if you get a prompt with "Certificate Validation Failure".
By default, the CorporateDevice Group is selected, which looks for installed AD certificate. This does not apply to Linux.

Next, select "PersonalDevice" or "PersonalDevice-NoSplit" for the Group dropdown option, to be able to connect.
Note that VPN access level for PersonalDevice or CorporateDevice is the same.
IMPORTANT!
It is recommend to use normal "PersonalDevice" group option so that only Visma office and DC related traffic flows through VPN.
"*-NoSplit" Group options will route ALL traffic via the VPN tunnel, including internet related traffic.
Please be aware of this and use them only when needed to access internet destinations that require you to be behind a trusted/known IP address.
To save bandwidth it is strongly recommended that Youtube or other similar streaming services should not be used while connected with the "*-NoSplit" opt
ions.
Enter your regular Visma username + password and click "OK".
Username format should be just "user.name" (example username: john.doe ) - do NOT use "internal\" domain name before username or "@visma.com" at
the end.)

IMPORTANT! If login fails at this point and you are sure the used credentials are OK, most probably your user does not have any 2fa OTP token assigned
(SMS or Google Auth.)
Login does not work without a 2fa OTP token. Please ask for support on setting this up via Visma Servicedesk.
When prompted, input OTP 2FA token or SMS code. (SMS is sent to the phone number that is registered for your Visma AD user. For enabling OTP 2FA
token, please contact Visma ServiceDesk)
Click on Continue.
You are now connected to VPN. Click on Application in taskbar to show status.

Related articles
Linux Ubuntu LTS - Installation and setup of Cisco AnyConnect
Mac OS X - Installation and setup of Cisco AnyConnect
MS Windows OS - Installation and setup of Cisco AnyConnect
Chrome OS - Installation and setup of Cisco AnyConnect
Secure Private Access (SPA)