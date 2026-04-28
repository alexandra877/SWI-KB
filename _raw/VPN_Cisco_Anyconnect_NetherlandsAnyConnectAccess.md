# Netherlands AnyConnect user documentation and Access Instructions

This article provides a step-by-step guide on how to use the Netherlands Anyconnect solution to access customer "legacy networks". This solution was designed to meet the common requirement of all NL Visma onboarded companies.

#### The following instruction set example is going to cover just the Windows operating system, since the login info + profiles to choose from at connecting time are the same for all other supported Anyconnect client operating systems.
## Step-by-step guide
Access instructions:
1 . Start Netherlands AnyConnect Client. Make sure  is in the address field.

2 . Click Connect. You will be prompted for credentials.

3 . Enter your regular Visma username + password and click "OK". (example username: john.doe - no domain name before user or "@" at the end.)
IMPORTANT!  *If login fails at this point and you are sure the used credentials are OK, most probably your user does not have any 2fa token assigned (SMS or Google Auth.)
Login does not work without a 2fa token. Please ask for support on setting this up via *Visma Servicedesk.

4 . When prompted, input OTP 2FA token or SMS code. (SMS is sent to the phone number that is registered for your Visma AD user. For enabling OTP 2FA token, please contact Visma ServiceDesk)

5 . The system scan will start.
If it does not, then please uninstall any Cisco Anyconnect related software from your computer and re-start from beginning. You might have had the AnyConnect client installed from before.

6 . After the scan is successful , you will get to "compliant" status and access to Visma resources is granted via VPN.

Important note*: When you connect for the first time to the NL Anyconnect solution,  wait until you get the "Network access allowed" message and then verify that you get a client IP for the Anyconnect virtual NIC card from the correct IP pool
For this, you have to compare the IP from ipconfig command output (for windows) with the Anyconnect Company IP Pools list and ensure a match.
If there is no match, you have to speak with the VPN group owner of your company (usually the IT manager) to put you in the correct group using .
Your company's Anyconnect VPN group name should be listed . If it isn't, then your company is not yet onboarded for Anyconnect access and you can request that by opening a ticket via Servicedesk.
**Anyconnect profiles explained:**
NL-Legacy-Split - allows dedicated/per company access to their legacy networks and resources, while internet destinations are reachable outside the tunnel
NL-Legacy-NoSplit - ALL traffic, meaning the dedicated/per company legacy networks+internet access is done via the tunnel
CorporateDevice-Split - this profile is for users that work on a Visma (Intune) device and which are employees of a company that migrated all legacy networks, services and resources into NL Datacentre area.  It allowes access to Datacentre hosted resources, while Internet destinations are reached outside the tunnel.
CorporateDevice-NoSplit - this profile is for users that work on a Visma (Intune) device and which are employees of a company that migrated all legacy networks, services and resources into NL Datacentre area.  It allowes both Datacentre hosted resources and Internet destinations to be reached via the tunnel.
PersonalDevice-Split - this profile is for users that work on a personal device and which are employees of a company that migrated all legacy networks, services and resources into NL Datacentre area.  It allowes access to Datacentre hosted resources, while Internet destinations are reached outside the tunnel.
PersonalDevice-NoSplit - this profile is for users that work on a personal device and which are employees of a company that migrated all legacy networks, services and resources into NL Datacentre area.  It allowes both Datacentre hosted resources and Internet destinations to be reached via the tunnel.
Note*  For reaching solutions that require whitelisting, you may need to whitelist following public IP on remote end side:  185.218.39.38.
## Related articles
Page:
Netherlands AnyConnect user documentation and Access Instructions
Page:
Norway AnyConnect Access Instructions
Page:
How-To Guide - Uninstalling Cisco AnyConnect VPN on MacOS: A How-To Guide