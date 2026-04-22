# 2.1.2. Visma EntraID Account & Multi-Factor Authentication (MFA)

Visma Group uses Microsoft EntraID as the identity provider (IdP) for all group-wide applications. MFA is mandatory for all Visma EntraID accounts (`firstname.lastname@visma.com`).

---

## What is MFA?

MFA requires two or more verification factors to access an account:

| Factor type | Example |
|---|---|
| Something you know | Password |
| Something you have | Phone with authenticator app or SMS |
| Something you are | Fingerprint or face recognition |

---

## Requirements

- A mobile phone (Android or iOS)
- An activated Visma account

---

## First-time Account Activation

If this is your first time using a Visma account, reset your password first:

1. Go to https://myaccount.microsoft.com
2. Click **Can't access your account?**
3. Enter your Visma email address (`firstname.lastname@visma.com`) and the CAPTCHA, then click **Next**.
4. Select **Send a text to my mobile phone number**.
5. Enter the phone number registered in VOM. If it is marked Private in VOM, contact IT Service Desk.
6. Click **Text** — you will receive an SMS code. **Warning:** after 3 failed attempts, password reset is locked for 24 hours.
7. Enter the SMS code and click **Next**.
8. Set your new password and click **Finish**.

---

## Step 1 — Install the Microsoft Authenticator App

Download Microsoft Authenticator from the App Store (iOS) or Play Store (Android).

The Visma IAM Team recommends Microsoft Authenticator because it supports:
- Push notifications (no need to type a 6-digit code)
- Passwordless authentication
- Authentication context (shows the app and location requesting access, reducing MFA fatigue risk)

Other authenticators (Google Authenticator, Authy) are also supported if preferred.

---

## Step 2 — Register MFA on Your Account

1. Open https://aka.ms/mfasetup in your browser.
2. Enter your Visma email (`firstname.lastname@visma.com`) and click **Next**.
3. Enter your password and click **Sign in**.
4. When prompted with "More information is required", click **Next**.
5. Click **Next** on the "Start by getting the app" screen.
6. On your phone, open Microsoft Authenticator, tap **+** in the top-right, and select **Work Account** → **Scan QR code**.
7. Scan the QR code shown on your computer screen.
8. Click **Next** on your computer.
9. When prompted with "Let's try it out", a 2-digit number appears — enter it on your phone when the push notification arrives.
10. MFA is now set up.

**To use a different authenticator** (Google, Authy): click "I want to set up a different method" at the bottom-left of the setup screen. This generates a QR code accepted by any TOTP authenticator.

---

## Step 3 — Add a Backup MFA Method

Add a phone number as backup in case you switch phones or lose access to the authenticator.

1. Go to https://aka.ms/mfasetup or https://aka.ms/setupsecurityinfo
2. In the **Security Info** section, click **+ Add sign-in method**.
3. Choose from: Authenticator App, Alternate phone, Email, Security Key, Office phone.

---

## Accessing Visma Resources

Once MFA is configured, you have access to:

| Service | URL |
|---|---|
| Slack | visma.enterprise.slack.com |
| Jira | jira.visma.com |
| Confluence | confluence.visma.com |
| Space | space.visma.com |
| MyTools | mytools.visma.com |
| Hubble | hubble.visma.com |
| Index | index.visma.com |
| VOM | vom.visma.com |
| Learning | learn.visma.com |
| VismaGPT | vismagpt.visma.com |

Each system has its own login experience. You may need to select "Sign in with Visma EntraID", "Sign in with Microsoft", "Company Login", or "Sign in with single sign-on" depending on the platform.

**Recommendation:** Set up a dedicated browser profile in Microsoft Edge for your Visma account with sync enabled. This keeps work and personal browsing separate and syncs settings across devices.

---

## Related guides

- [Setting up Microsoft Authenticator App on mobile](authenticator-app-setup.md)
- [Updating Gmail 2FA phone and authenticator](gmail-2fa-update.md)

---

*Source: `_raw/Visma EntraID User Account & Multi-Factor Authentication (MFA).md`*
