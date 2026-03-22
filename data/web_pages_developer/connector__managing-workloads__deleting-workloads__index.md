---
title: "Deleting a workload"
source: "https://developer.acronis.com/doc/connector/managing-workloads/deleting-workloads/index.html"
source_domain: "developer"
scraped_at: "2026-03-22T01:54:09.090938"
---

# Deleting a workload

Deleting a workload
You can delete workloads from Acronis Cyber Protect Cloud by sending a DELETE request to the /api/workload_management/v5/workloads endpoint.

Request structure







Parameter
Type
Description



workload_id
string

Filter by one or more workload IDs. Maximum 100 items.
To filter by one workload ID, specify a workload ID: 2f4b84d8-6aad-487b-b0b1-40845bf72737.
To filter by multiple workload IDs, specify workloads in the following format: or(2f4b84d8-6aad-487b-b0b1-40845bf72737,c70134c4-a244-4b22-99ad-e081301f7530).







Response structure
If the workloads were deleted successfully, the response returns status 204, without payload.

In this section

Step-by-step procedure