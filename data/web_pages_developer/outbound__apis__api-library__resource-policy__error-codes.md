---
title: "API error codes"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/resource-policy/error-codes.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:25:13.709346"
---

# API error codes

API error codes

You can inspect response codes via curl by adding the --include option.
For more information, see Inspecting API response codes.

The following table lists the description of error codes returned by the Resource and Policy Management API in the error.code key:








Code
Domain
Description



AccessDenied
Access
Access was denied.

UnauthorizedRequest
Access
Authorization failed.

AuthenticationTimeout
Access
Access token is already expired or invalid.

NotFound
General
Specified resource not found.

BadRequest
General
Request is malformed.

DataConflict
General
The request violates some data invariant and cannot be performed.

InternalServerError
General
Server encountered an unexpected condition that prevented it from fulfilling the request.

DependencyValidationError
General
Dependency validation error between subject policy and target policy.

MethodNotAllowed
General
Unsupported resource access method.

ValidationError
General
Validation failed.

UnsupportedTypeError
General
Object type is unsupported.

MultipleApplicationsWithPolicyTypes
PolicyManagement
Policy application failed due to conflict with other policy applications within the same context.

UnsupportedPolicyType
PolicyManagement
An unsupported policy type.

SchemaValidationError
PolicyManagement
Schema validation error.

NoApplicationsError
PolicyManagement





FailedEnabledInvariantError
PolicyManagement





ResourceNotFound
ResourceManagement
Could not find the resource with the ID.

NotLicensedError
Licensing
Global or context-dependent features not licensed for the policy for some reason.