# OTP Reliability: what changes

## Why
Interviews (10 users) and the funnel show 34% of Android users leave at OTP; 70% of them saw the SMS arrive after 60 seconds.

## What changes
- Retry OTP send with backoff, and show a countdown.
- Read the SMS automatically (SMS Retriever API) on Android.
- Fall back to a second SMS route when delivery receipts lag.

## Out of scope
- Email or voice OTP.
