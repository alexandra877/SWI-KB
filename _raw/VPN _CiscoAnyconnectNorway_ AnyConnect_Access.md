# Norway AnyConnect user documentation and Access Instructions
#### The following instruction set example is going to cover just the Windows operating system, since the login info + profiles to choose from at connecting time are the same for all other supported Anyconnect client operating systems.
## Step-by-step guide
1. Start Norway AnyConnect Client and make sure  is in the address field.

2. Click Connect. You will be prompted for credentials.

For unmanaged device (that is not registered on Visma AD) make sure you select "PersonalDevice" or "PersonalDevice-NoSplit" for the Group option or you will not be able to connect. For AD registered Windows machines, select "CorporateDevice" or "CorporateDevice-NoSplit" Group option.

IMPORTANT! 
We recommend using normal "PersonalDevice" or "CorporateDevice" group options so that only Visma office and DC-related traffic flows through VPN. "*-NoSplit" Group options will route ALL traffic via the VPN tunnel, including internet related traffic.
Please be aware of this and use them only when needed to access internet destinations that require you to be behind a trusted/known IP address. To save bandwidth it is strongly recommended that Youtube or other similar streaming services should not be used while connected with the "*-NoSplit" options.

3. Enter your regular Visma username + password and click "OK". (example username: john.doe - no domain name before user or "@" at the end.)

IMPORTANT!  *If login fails at this point and you are sure the used credentials are OK, most probably your user does not have any 2fa token assigned (SMS or Google Auth.) Login does not work without a 2fa token. Please ask for support on setting this up via *Visma Servicedesk.

4. When prompted, input OTP 2FA token or SMS code. (SMS is sent to the phone number that is registered for your Visma AD user. For enabling OTP 2FA token, please contact Visma ServiceDesk)

5. The system scan will start.
If it does not, then please uninstall any Cisco Anyconnect related software from your computer and re-start from beginning. You might have had the AnyConnect client installed from before.

You will still need to have an active Firewall, up-to-date Anti-Virus and Anti-Malware tool, up-to-date OS updates (usually provided by windows or pre-installed on AD registered PCs).
You have 15 minutes to resolve any issues, then VPN will auto-disconnect. If the time is not enough for you, you can re-connect anytime back and you will continue from where you left.

6. After the scan is successful, you will get to "compliant" status and access to Visma resources is granted via VPN.

## Related Links
Cisco AnyConnect client software installation guides can be found .