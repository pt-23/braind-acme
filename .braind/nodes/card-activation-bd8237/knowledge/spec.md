# Card Activation: how it works

## What it does
A new card is activated in the app: the cardholder confirms the last four digits, receives a one-time passcode (OTP) by SMS, and enters it within 5 minutes.

## How it behaves
- OTPs are 6 digits, valid 5 minutes, at most 3 resends per hour.
- SMS goes through Twilio; delivery receipts are logged.
- After 3 wrong codes the card locks for 30 minutes.

## Limits and known issues
- Android 14 devices with aggressive battery savers delay SMS (see the defect in this Feature's register).
