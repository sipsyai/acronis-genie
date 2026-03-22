---
title: "Verifying callback requests"
source: "https://developer.acronis.com/doc/callback-handler/request-verification.html"
source_domain: "developer"
scraped_at: "2026-03-22T01:53:01.233665"
---

# Verifying callback requests

Verifying callback requests
The callback handler should verify the origin of a request in order to accept or reject the request. Requests from the Acronis API Callback Gateway include the Authorization
header, which contains a JWT (JSON Web Token).
signed by Acronis.

To verify callback requests
The callback handler must ensure that the JWT is valid and originated from Acronis.


Fetch JWKs (JSON Web Keys)
Send a GET request to the https://acronis.cloud/api/idp/v1/keys endpoint to get the list of public JWKs.
Example response:



{
"keys": [
{
"use": "sig",
"kty": "RSA",
"kid": "f9294926-b89b-460b-9c50-8f2e74e6d3db",
"alg": "RS256",
"n": "xDm80_tNLSuJxBETvhfyTm5miZqn08fJwPRo0UghBRfYotTAhPma3Uj2hvCO2jOB1777D3-OMmhlJ7oxXOFZcYRElw6FOYTZzfix_jtd6ButcUkfWBQuUUE51w-WGxVhbNagF5no2W4b9zQCLs3Omg1VdA-q1KJe6lIsKdE0ZXEQyfDh2rDFd1mbVj2DkyRrjWoLlpWIZbH--NMO2od047om14oTsaF2Xv6rlm4GMwTs6EKAGtXAKMxX1nu0U3lpgF_8n9fJf98N3nETjIUS5v85-Qxy1kzranzWqZHxt-fxin3GXukifuYF4m5QTb1By5sSiQVL8keZGb1rt-_XpQ",
"e": "AQAB"
},
"..."
]
}




Note
You can cache the JWKs to reduce the number of requests and update them according to the Acronis keys rotation policy. The JWKs are updated every 24 hours.




Verify the received JWT
When the callback handler receives a request:




Fetch the value of the Authorization header, and extract the JWT.
The format is Bearer <jwt> (where <jwt> is the JWT).



Decode the JWT header using the library of your choice, and fetch the value of the kid field.
Example:


{
"alg": "RS256",
"iri": "ac294f6ec37c7857ba95371bc43d95cd",
"kid": "c2618afb-9881-472e-a4e4-683f5f057b62"
}




Find the corresponding key among stored JWKs by matching the value of the kid field.
Decode and verify the JWT signature.

Important
If the JWT signature is invalid - deny the request.



Decode the JWT payload.
Example:


{
"aud": "acronis.cloud",
"exp": 1710855607,
"jti": "0e8c4f42-b3f6-4585-8137-880c95f49eff",
"iat": 1710852007,
"iss": "https://acronis.cloud",
"sub": "0d780ce3-adcc-5bce-9904-3be60cbd1b9d",
"scope": [
{
"role": "cti.a.p.acgw.endpoint.v1.0~vendor.app.endpoint.v1.0"
}
],
"ver": 2,
"sub_type": "platform-acgw"
}




Verify in the iss field that the JWT issuer is https://acronis.cloud.

Important
If the issuer does not match - deny the request.


Verify that the JWT is not expired. This is based on the exp field.

Important
If the token is expired - deny the request.


Verify that the scope list has a role that matches the context.endpoint_id provided in the request body.

Important
If the endpoint ID does not match - deny the request.