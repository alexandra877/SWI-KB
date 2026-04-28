Chrome OS - Installation and setup of Cisco AnyConnect
This guide is for Chrome OS and might not be accurate for other operating systems.
Additional info and guides for other systems -> Cisco AnyConnect generic info and Links to OS-specific User Guides
IMPORTANT UPDATE:
If your ChromeOS device is more recent and updated to latest ChromeOS version, then the Webstore variant of the Anyconnect VPN Client app will not
work anymore and report errors or, when run, stay locked up in "initiallizing . . ." state.
So, for updated ChromeOS variants, please proceed as described here:
if you (still) have the Webstore VPN client installed(The one from the Google Chrome Webstore) - some clean-up steps are needed:
go to ChromeOS settings and remove all related VPN profiles under the network section, as well as related certificates, if any.
go to Google Chrome Webstore and remove/uninstall the Anyconnect VPN Client App.
alternatively, you can go to Chrome Browser settings -> Manage extensions. From here, find and remove the Anyconnect VPN Client
extension
Follow these steps to set up the Google Play Store VPN Client variant:
The new Google Play Store VPN Client is now named "Cisco Secure Client" and is at the moment at version 5.x.x
The VPN Client can only be installed from Google Play Store(similar appstore to what is available on Android devices)
If you do not have the Google Play Store on your Chromebook, see this link on how to enable it in the settings: https://www.google.com
/chromebook/howto/enable-google-play-store/
Open Google Play Store app and search for "Cisco Secure Client", from Cisco Systems Inc., and install it.
Open the app and accept the license agreement by clicking on OK.
Next, click on Connections
this will open a pop-up where the currently set up VPN connections are listed, if any, so you can select the one you want to
connect to, or edit their settings.
Click the "+" sign to add a new connection
The description can be anything you consider as a useful name for the connection, like, for example, "Visma VPN"
The server address field must contain the address of the VPN gateway - "access.visma.com"
"Advanced Preferences" do not have to be adjusted.
Click on "Done" to create the VPN connection.
Connecting to VPN:
Make sure that the correct VPN connection is selected under "Connections". If not, then click on "Connections" and select it
from the list.
Now click on "AnyConnect VPN" .
Select the VPN profile from the dropdown - make sure you select a "PersonalDevice" profile for the login to work - access to
VPN resources is not affected by this selection.
Enter your credentials (user.name and password) and hit "connect"
When prompted, enter the 2FA code.
Confirm the connection request with "OK". If you do not agree to this, you will not be able to use the VPN service.
If you are now successfully connected, you will see this by the coloured slider - "Anyconnect VPN - connected".
Step-by-step guide - for older ChromeOS devices, running the Webstore VPN Client App.
To get Cisco AnyConnect to work on Chromebook there are some requirements, one of them are the Visma Wireless Certificate which is the same that’s
used for VismaL3 wireless network.
Download the apps Cisco AnyConnect and Certificate Enrolment for Chrome OS here.
Obtaining the required Visma Certificate
Important:
For some user/device combo, the certificate enrollment might not work properly. If this is the case for you and the below steps fail, just continue to next
step - setup of profile in Cisco Anyconnect.

When you open Chrome on your Chromebook you should have a small blue shield in the upper right corner where your extensions are visible.
PS! You will have to be at the office and connected to VismaL3 / Wired network to be able to get the certificate!
Click it and you’ll be sent to a site asking for your AD username and password.
Enter your regular Visma username + password and click "OK". (example username: john.doe - no domain name before user or "@visma.com" at the end.)
It will work for some seconds before it will give you a Success message if everything is correct.
By typing chrome://certificate-manager in the address-field you can check if it’s installed. It should look like this

Set up of profile in Cisco AnyConnect
The Cisco AnyConnect app is pushed to your Chromebook by policy.
You can still go to webstore and search for Cisco Anyconnect app and install it manually.
You can then locate the app by typing AnyConnect in the search field and open the AnyConnect app.
When you open the app, click Add New Connect as you can see below and type the information from the next picture.
Name: Visma VPN
Server Address: access.visma.com
Click on Select Certificate and click OK. (this step is only needed when the above steps for Certificate Enrollment worked for you )

When this is done, click Save Changes.
The setup of AnyConnect is done and you click close the application.
To connect, click on your profile picture in the lower right corner and select VPN (Disconnected).
Select Visma VPN (user)

Select PersonalDevice or PersonalDevice-NoSplit in the dropdown list for group.
When prompted to type your username and password, type your AD username and password.
Caution! - NoSplit option will route ALL traffic via VPN, including normal internet traffic.
The use of Youtube or other similar streaming services should be avoided while connected in this way to the VPN, in order to not put constrains on the
available VPN bandwidth at Oslo DC.
Enter your regular Visma username + password and click "OK". (example username: john.doe - no domain name before user or "@visma.com" at the end.)

IMPORTANT! If login fails at this point and you are sure the used credentials are OK, most probably your user does not have any 2fa token assigned
(SMS or Google Auth.)
Login does not work without a 2fa token. Please ask for support on setting this up via Visma Servicedesk.
When asked to enter your otp value, this is the 2FA token code. Click submit to continue.
If you do not have 2FA token set up for your user, the the prompt will ask you for an SMS code sent to you AD registered phone number.
(For setting up a 2FA token for your user, please contact it-servicedesk@visma.com)
When the connection is active, you can see it as Connected in the lower right corner menu.
That’s it! You’re now up and running on the new Cisco AnyConnect VPN for Chrome OS!
For issues, contact us by mail or via Support Portal.
Mail: it-servicedesk@visma.com
Visma ITC Local Support

Related articles
Linux Ubuntu LTS - Installation and setup of Cisco AnyConnect
Mac OS X - Installation and setup of Cisco AnyConnect
MS Windows OS - Installation and setup of Cisco AnyConnect
Chrome OS - Installation and setup of Cisco AnyConnect
Secure Private Access (SPA)