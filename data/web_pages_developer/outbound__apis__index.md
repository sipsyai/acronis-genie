---
title: "Acronis platform APIs"
source: "https://developer.acronis.com/doc/outbound/apis/index.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:27:50.262603"
---

# Acronis platform APIs

Acronis platform APIs

Acronis provides a library of public APIs. This chapter provides details of the operations you can perform with Acronis APIs, and step-by-step guides for how to code many of them.


API library






API
Documentation



Account Management API

Guide
Reference document



Agent Management API

Guide
Reference document



Alert Management API
Reference document

Integration Management API
Guide

Resource and Policy Management API

Guide
Reference document



Task Management API

Guide
Reference document



Acronis PSA API

Guide
Reference document



Event Manager API

Guide
Reference document



Disaster Recovery API

Guide
Reference document



Endpoint Detection and Response (EDR)

Guide
Reference document



Vaults Management API
Reference document

Other Acronis service APIs

File Sync & Share API reference document







API change log

The API change log provides details of changes to the public endpoints of the Acronis APIs. It is updated monthly.
To download the API change log, click here.


.grecaptcha-badge {
display: none !important;
}

.newsletter-subscription {
color: rgba(36, 49, 67, 0.9);
background: rgba(38, 104, 197, 0.05);
padding: 32px 24px;
}

.newsletter-subscription input[type=submit],
.newsletter-subscription button {
color: white;
background-color: #94c13d;
padding: 12px 16px;
width: 200px;
border-radius: 4px;
border: none;
font-family: 'Open Sans', sans-serif;
font-style: normal;
font-weight: 400;
font-size: 16px;
line-height: 24px;
text-decoration: none;
outline: none;
box-sizing: border-box;
user-select: none;
}

.newsletter-subscription input[type=email] {
width: 100%;
box-sizing: border-box;
border-radius: 4px;
border: 1px solid #c2cfe5;
color: rgba(36, 49, 67, 0.9);
font-family: 'Open Sans', sans-serif;
font-size: 16px;
padding: 8px 16px 8px;
height: 48px;
display: block;
outline: none;
}

.sub-state {
max-width: 648px;
}

.sub-state.hidden {
display: none;
}

.sub-inputs {
margin: 16px 0;
}

.sub-inputs fieldset {
border: none;
margin: 0;
padding: 0;
display: flex;
flex-wrap: nowrap;
}

.sub-inputs input[type=email] {
margin-right: 16px;
}

.sub-recaptcha-license {
margin-top: 16px;
font-size: 90%;
opacity: 0.9;
}

.sub-error-title {
font-weight: 600;
font-size: 18px;
margin-bottom: 16px;
}

.sub-error-code {
font-family: monospace;
}

.sub-try-again {
margin-top: 20px;
}

.sub-state-success {
font-size: 16px;
}






Please provide your email address if you want to receive notifications about the API changes.














I agree to the use of my personal data as described in the
Acronis Terms of Service
and
Privacy Policy.
I can unsubscribe from emails at any time using the unsubscribe link inside of emails.







This site is protected by reCAPTCHA and the Google
Privacy Policy
and
Terms of Service
apply





Thank you for your email!



An error has occurred




Try again






(async function() {
const form = document.querySelector('.sub-state-form form');

const setStep = (step) => {
[...document.querySelectorAll('.sub-state')].forEach((x) => x.classList.add('hidden'));
document.querySelector(`.sub-state-${step}`).classList.remove('hidden');
};

const setError = (body) => {
let code = 'network_error';
let message = '';

if (body?.code) {
code = body.code;
}

if (body?.ex?.reason) {
message = body?.ex?.reason;
} else if (body.errors?.length) {
message = body.errors[0].val;
}

document.querySelector('.sub-error-code').innerHTML = code;
document.querySelector('.sub-error-message').innerHTML = message;
};

form.addEventListener('submit', async (e) => {
e.preventDefault();

const recaptchaChallenge = await window.grecaptcha.enterprise.execute(recaptchaWidgetId);

const formData = new FormData(form);
const payload = Object.fromEntries(formData.entries());
payload.form_id = 'developer_doc_subscription';
payload.terms = payload.terms === 'on';
payload.country = geoCountry;

const fetchResource = 'https://websiteapi.acronis.com/svc/v1/marketing/forms/leads';
const fetchOptions = {
method: 'POST',
headers: {
'Content-Type': 'application/json',
'X-GRecaptcha-Response': recaptchaChallenge,
},
body: JSON.stringify(payload),
};

try {
form.querySelector('fieldset').disabled = true;
const res = await fetch(fetchResource, fetchOptions);
const body = await res.json();

if (body.success) {
setStep('success');
} else {
setError(body);
setStep('error');
}
} catch (e) {
console.error(e);
setError();
setStep('error');
} finally {
form.querySelector('fieldset').disabled = false;
window.grecaptcha.enterprise.reset();
}
});

document.querySelector('.sub-try-again').addEventListener('click', () => {
setStep('form');
});

// keep setTimeout, we want to fetch the geoapi in parallel with recaptha init
let geoCountry = null;
window.setTimeout(async () => {
try {
const resp = await fetch('https://websiteapi.acronis.com/geo/location/v1/ip/geolocation');
const geo = await resp.json();
geoCountry = geo.data.country.code;
} catch {

}
}, 0);

while (!window.grecaptcha?.enterprise?.render) {
await new Promise((resolve) => setTimeout(resolve, 0));
}

const recaptchaWidgetPlaceholder = document.querySelector('.g-recaptcha');
const recaptchaOptions = {
sitekey: '6LcMQSEjAAAAAPWFRMLg7n6NERJhIndKRAbBcoKo',
size: 'invisible',
};

const recaptchaWidgetId = window.grecaptcha.enterprise.render(
recaptchaWidgetPlaceholder,
recaptchaOptions,
);
})();

In this section

Getting started
Authentication
Requests and responses
Inspecting API response codes
HTTP status response codes
Pagination
API library