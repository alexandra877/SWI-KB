Visma Group is using Microsoft EntraID as the main Identity Provider (IDP) for all group-wide applications. This guide is for setting up Multi-Factor authentication for your Visma Group EntraID account (most commonly known as [firstname].[lastname]@visma.com) .
## Introduction to MFA
In our ongoing commitment to protect our data and maintain the highest level of security, setting up Multi-Factor Authentication (MFA) is mandatory. MFA adds an essential layer of security that significantly decreases the risk of unauthorized access, even if your password is compromised.
Enabling Multi-Factor Authentication (MFA) is a critical step in securing your account. MFA enhances security by requiring two or more verification factors to gain access to an account, network, or system, making it significantly harder for attackers to breach.
MFA combines two or more of the following authentication methods:
Something You Know: Usually your password.
Something You Have: A phone or another device that can receive verification codes.
Something You Are: Biometrics like fingerprints or facial recognition.
## Requirements
To use your Visma EntraID account, you will need the following:
A mobile phone (Android or Apple).
An activated Visma account.
In case you’re using your Visma account for the first time, then follow the steps below (<5 minutes).
Go to myaccount.microsoft.com
Click on Can’t access your account?
On the next window, enter your Visma email address [firstname].[lastname]@visma.com and the text mentioned, and click Next.
The option Send a text to my mobile phone number should be selected by default; if not, select it.
You will need to fill in the exact phone number you have in VOM.
If your phone number is set as Private in VOM, please contact the IT Service Desk, and they will be able to assist with this step.
IMPORTANT: if you fill in the phone number and click on Text for 3 attempts, you will lock the possibility to reset your password for 24 hours. If you do that, please contact IT Service Desk and they will have to reset the password manually.
After you fill in your number, click on Text and you will receive an SMS.
Enter the SMS token and click Next.
Fill in the new password and click on Finish




## Getting Started
### 1. Get the Authenticator App on your phone
Download the Microsoft Authenticator App on your phone by scanning the QR code or clicking the links below.

(Link to App in Google Play Store)		(Link to App in Apple App Store)
➡️ The Visma IAM Team recommends using the Microsoft Authenticator App for the following reasons:
It supports Push notifications. So you do not need to search and enter 6-digit code.
It supports Passwordless authentication, which greatly simplifies login
Shows you authentication context - Application that requested authentication and location information. This reduces the risk of MFA fatigue attacks.
If you want to use other Authenticator apps (like Google or Authy), then you can set up a different method during the first login or afterwards.

### 2. Login with Visma Group Entra ID on your computer
Upon signing in to an application with Visma Entra ID using your username and password for the first time, you’ll be prompted for a second form of identification, which ensures that only you can access your account.
Open https://aka.ms/mfasetup in your browser
Enter your @visma.com email address and click Next.
For example: [firstname].[lastname]@visma.com
In case your Visma username differs from your email address, then enter [username]@visma.com

Enter your password, and click Sign in.

You will be prompted with “More information is required”; click Next.


You will be prompted with “Start by getting the app”; click Next.



When registering for the first time, Entra ID will push you to use the Microsoft Authenticator on your phone. If you want to use other Authenticators (like Google or Authy), you must click on the text at the bottom left side of the window - I want to set up a different method. This will generate a QR code that will be accepted by other authenticators but it can also be accepted by Microsoft Authenticator.

You will be prompted with “Set up your account”, and click Next.





You will be prompted with “Scan the QR Code”.
Open the Microsoft Authenticator App on your phone📱.
Click on the + at the top right of the screen.
Select Work Account.
Select Scan QR code
Scan the QR code on your 💻 computer screen.

When OK, your “@visma.com” account will be listed in the Authenticator.
Click Next on your 💻 computer.

You will be prompted with “Let’s try it out”, a (random) 2 digit number is presented.


Wait for the push notification on your 📱phone prompting “Are you trying to sign in?”
Enter the 2-digit number on your 📱phone and click YES.

✅ Once you completed the above steps you will have the MFA set for your account.
👉 Hint: See screenshots below for a full walkthrough of the steps.


### 3. Recommendation: Add additional MFA methods in Entra ID
🆘 Tip: Add your phone number as a backup, just in case you switch phones or cannot use the Authenticator App.
You can manage your MFA methods by visiting one of these short links: https://aka.ms/mfasetup or in the new security info registration experience at https://aka.ms/setupsecurityinfo
In Security Info section, click on +Add sign-in method

2. Along with the Microsoft Authenticator method, you can add an additional one from the list below.
Authenticator App, Alternate phone, Email, Security Key, Office phone

Tip: More info for adding a Security Key, can be found here: Configuring Microsoft authentication with Yubikey

## Using your Visma EntraID account
When you successfully complete the above steps, you have access to many Visma Group resources. Below are some examples to get started with.
visma.enterprise.slack.com
jira.visma.com
confluence.visma.com
space.visma.com
mytools.visma.com
hubble.visma.com
index.visma.com
vom.visma.com
learn.visma.com
visma.peakon.com
app.dialog.nl
vismagpt.visma.com
⚠️ Please note that each system has its own Login Experience. For some systems, you’ll need to enter your Visma email address first; for others, you may need to select options like “Sign in with Visma EntraID,” “Sign in with Microsoft,” “Company Login,” or “Sign in with single sign-on.”
🚀 For the best user experience, we recommend setting up a browser profile in Microsoft Edge for your Visma account and enabling synchronization. This will save all your browser settings to your Visma account and automatically sync them across other Edge browsers on your phone, tablet, or other/new computers. Using a browser profile allows you to keep your work and personal browsing separate.