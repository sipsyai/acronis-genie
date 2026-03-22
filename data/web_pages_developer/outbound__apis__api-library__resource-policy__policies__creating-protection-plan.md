---
title: "Creating a protection plan"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/resource-policy/policies/creating-protection-plan.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:25:26.359967"
---

# Creating a protection plan

Creating a protection plan

To create a protection plan

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'https://eu2.acronis.cloud/api'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}



Import the uuid4 function from the uuid python module:
>>> from uuid import uuid4



Define a variable named protection_plan_id, and then assign the UUID generated with the uuid4() function and converted to string to this variable:
>>> protection_plan_id = str(uuid4())
'5b15f6e1-88ec-4dce-b523-0e8394c0bc19'



Define a variable named plan_data, and then assign an object with the subject key with an object containing the policy key with an array containing a total protection policy to this variable:
>>> plan_data = {
...     'subject': {
...         'policy': [
...             {
...                 'id': protection_plan_id,
...                 'type': 'policy.protection.total',
...                 'origin': 'upstream',
...                 'enabled': True,
...                 'name': 'My Protection Plan'
...             }
...         ]
...     }
... }



Define the variable named policies and assign it with the list of protection policy objects.
As an example, a machine backup policy with default settings will be included:

Full code
1policies = [
2    {
3        "id": str(uuid4()),
4        # Machine backup policy type is 'policy.backup.machine'
5        'type': 'policy.backup.machine',
6        'parent_ids': [
7            protection_plan_id
8        ],
9        'origin': 'upstream',
10        'enabled': True,
11        'settings_schema': '2.0',
12        'settings': {
13            # Archive compression level. Available values: ``normal``, ``high``, ``max``. When value is not specified - no compression is applied.
14            'compression': 'normal',
15            # Format of the Acronis backup archive. Available values: ``11``, ``12``, ``auto``.
16            'format': 'auto',
17            # If true, snapshots of multiple volumes will be taken simultaneously. Equals to false if value is not specified.
18            'multi_volume_snapshotting_enabled': True,
19            # If true, the file security settings will be preserved. Equals to false if value is not specified.
20            'preserve_file_security_settings': True,
21            # Configuration of retries on recoverable errors during the backup operations like reconnection to destination. No attempts to fix recoverable errors will be made if retry configuration is not set.
22            'reattempts': {
23                # If true, enables retry on recoverable errors.
24                'enabled': True,
25                # An interval between retry attempts.
26                'interval': {
27                    # A type of the interval. Available values are: ``seconds``, ``minutes``, ``hours``, ``days``.
28                    'type': 'seconds',
29                    # The amount of value specified in ``interval.type``.
30                    'count': 30
31                },
32                # Max number of retry attempts. Operation will be considered as failed when max number of retry attempts is reached.
33                'max_attempts': 30
34            },
35            # If true, a user interaction will be avoided when possible. Equals to false if value is not specified.
36            'silent_mode_enabled': True,
37            # Determines the size to split backups on. Splitting is not performed if value is not specified.
38            'splitting': {
39                # The size of split backup file in bytes.
40                'size': 9223372036854775807
41            },
42            # Configuration of retries on errors during the creation of the virtual machine snapshot. No attempts to fix recoverable errors will be made if retry configuration is not set.
43            'vm_snapshot_reattempts': {
44                # If true, enables retry on errors.
45                'enabled': True,
46                # Configuration of the interval between retry attempts.
47                'interval': {
48                    # A type of the interval. Available values are: ``seconds``, ``minutes``, ``hours``, ``days``.
49                    'type': 'minutes',
50                    # The amount of value specified in ``interval.type``.
51                    'count': 5
52                },
53                # Max number of retry attempts. Operation will be considered as failed when max number of retry attempts is reached.
54                'max_attempts': 3
55            },
56            # Settings for the Volume Shadow Copy Service (VSS) provider. If not set, no VSS provider is used.
57            'vss': {
58                # If true, the VSS will be enabled.
59                'enabled': True,
60                # A type of VSS provider to use in backup. Only ``native`` and ``target_system_defined`` options are available.
61                'provider': 'target_system_defined'
62            },
63            # The archive properties.
64            'archive': {
65                # The name of the generated archive. The name may use the following variables: ``[Machine Name]``, ``[Plan ID]``, ``[Plan Name]``, ``[Unique ID]``, ``[Virtualization Server Type]``.
66                'name': '[Machine Name]-[Plan ID]-[Unique ID]A'
67            },
68            # Time windows for performance limitations of backup and storage maintenance operations.
69            "performance_window": {
70                "enabled": True,
71                # A tuple of 3 presets
72                "presets": [
73                    {
74                        # CPU priority - 'idle', 'low', 'normal', 'high', 'realtime'
75                        "cpu_priority": "normal",
76                        "disk_limit": {
77                            # Value in specified units
78                            "value": 50,
79                            # Units. 'percent' - percentage, 'speed' - speed in kilobytes
80                            "type": "percent"
81                        },
82                        # ID of preset. 'high' - green, 'low' - blue, 'cancel' - gray.
83                        "id": "high",
84                        "network_limit": {
85                            # Value in specified units
86                            "value": 50,
87                            # Units. 'percent' - percentage, 'speed' - speed in kilobytes per second
88                            "type": "percent"
89                        },
90                        # List of timetable objects
91                        "timetable": [
92                            {
93                                # Time from which the preset applies
94                                "time_from": {
95                                    "hour": 0,
96                                    "minute": 0
97                                },
98                                # Time until the preset applies
99                                "time_to": {
100                                    "hour": 23,
101                                    "minute": 59,
102                                    "second": 59
103                                },
104                                # Days of week in three-letter format
105                                "days_of_week": [
106                                    "sun",
107                                    "mon",
108                                    "tue",
109                                    "wed",
110                                    "thu",
111                                    "fri",
112                                    "sat"
113                                ]
114                            }
115                        ]
116                    },
117                    {
118                        "cpu_priority": "high",
119                        "disk_limit": {
120                            "value": 25,
121                            "type": "percent"
122                        },
123                        "id": "low", # Blue preset
124                        "network_limit": {
125                            "value": 25,
126                            "type": "percent"
127                        },
128                        "timetable": [
129                            {
130                                "time_from": {
131                                    "hour": 8,
132                                    "minute": 0
133                                },
134                                "time_to": {
135                                    "hour": 8,
136                                    "minute": 59,
137                                    "second": 59
138                                },
139                                "days_of_week": [
140                                    "sun",
141                                    "fri"
142                                ]
143                            }
144                        ]
145                    },
146                    {
147                        "id": "cancel", # Gray (inactive) preset
148                        "network_limit": {
149                            "value": 100,
150                            "type": "percent"
151                        },
152                        "disk_limit": {
153                            "value": 100,
154                            "type": "percent"
155                        },
156                        "timetable": [
157                            {
158                                "time_from": {
159                                    "hour": 8,
160                                    "minute": 0
161                                },
162                                "time_to": {
163                                    "hour": 15,
164                                    "minute": 59,
165                                    "second": 59
166                                },
167                                "days_of_week": [
168                                    "mon"
169                                ]
170                            }
171                        ]
172                    }
173                ],
174            },
175            # Configuration of backup retention rules.
176            'retention': {
177                # A list of retention rules.
178                'rules': [
179                    {
180                        # A list of backup sets where rules are effective.
181                        'backup_set': [
182                            'daily'
183                        ],
184                        # Configuration of the duration to keep backups in archive created by the policy.
185                        'max_age': {
186                            # A type of the duration. Available values are: ``seconds``, ``minutes``, ``hours``, ``days``.
187                            'type': 'days',
188                            # The amount of value specified in ``max_age.type``.
189                            'count': 7
190                        }
191                    },
192                    {
193                        'backup_set': [
194                            'weekly'
195                        ],
196                        'max_age': {
197                            'type': 'weeks',
198                            'count': 4
199                        }
200                    },
201                    {
202                        'backup_set': [
203                            'monthly'
204                        ],
205                        'max_age': {
206                            'type': 'months',
207                            'count': 6
208                        }
209                    }
210                ],
211                # If true, retention rules will be applied after backup is finished.
212                'after_backup': True
213            },
214            # Storage location of the archives.
215            'vault': {
216                # Type of storage location. Available values: ``local_folder``, ``network_share``, ``ftp``, ``sftp``, ``cd``, ``tape``, ``storage_node``, ``asz``, ``removable``, ``cloud``, ``nfs_share``, ``esx``, ``astorage2``, ``script``.
217                'type': 'cloud',
218                # If true, the vault will be accessed using the policy credentials.
219                'use_policy_credentials': True
220            },
221            # Configuration of policy-related alerts.
222            'alerts': {
223                # If true, the alerts will be enabled.
224                'enabled': False,
225                # Number of days that will trigger the alert about the passed number of days without a backup.
226                'max_days_without_backup': 5
227            },
228            # Configuration of the backup schedule.
229            'scheduling': {
230                # A list of schedules with backup sets that compose the whole scheme.
231                'backup_sets': [
232                    {
233                        'type': 'auto',
234                        'schedule': {
235                            'alarms': {
236                                'time': {
237                                    'weekdays': [
238                                        'mon',
239                                        'tue',
240                                        'wed',
241                                        'thu',
242                                        'fri'
243                                    ],
244                                    'repeat_at': [
245                                        {
246                                            'hour': 21,
247                                            'minute': 0
248                                        }
249                                    ]
250                                }
251                            },
252                            'conditions': {},
253                            'prevent_sleep': True,
254                            'type': 'weekly'
255                        }
256                    }
257                ],
258                # If true, the backup schedule will be enabled.
259                'enabled': True,
260                # Max number of backup processes allowed to run in parallel. Unlimited if not set.
261                'max_parallel_backups': 2,
262                'rand_max_delay': {  # Configuration of the random delay between the execution of parallel tasks.
263                    # A type of the duration. Available values are: ``seconds``, ``minutes``, ``hours``, ``days``.
264                    'type': 'minutes',
265                    # The amount of value specified in ``rand_max_delay.type``.
266                    'count': 30
267                },
268                # A backup scheme. Available values: ``simple``, ``always_full``, ``always_incremental``, ``weekly_incremental``, ``weekly_full_daily_incremental``, ``custom``, ``cdp``.
269                'scheme': 'always_incremental',
270                "task_failure": {
271                    "enabled": True,
272                    "interval": {
273                        "type": "hours", # Time units - hours, minutes, seconds
274                        "count": 1 # Number of time units
275                    },
276                    "max_attempts": 12 # Number of attempts between task restarts
277                },
278                # A day of week to start weekly backups in 3-letter abbreviation format.
279                'weekly_backup_day': 'mon'
280            },
281            # A configuration of Changed Block Tracking (CBT). Available values: ``use_if_enabled``, ``enable_and_use``, ``do_not_use``.
282            'cbt': 'enable_and_use',
283            # If true, determines whether a file has changed by the file size and timestamp. Otherwise, the entire file contents are compared to those stored in the backup.
284            'fast_backup_enabled': True,
285            # If true, a quiesced snapshot of the virtual machine will be taken.
286            'quiesce_snapshotting_enabled': True
287        }
288    },
289    # Put other policy objects here.
290]



For more policy settings, see Protection policy settings.

Merge the list of protection policy objects into the policy key of the plan_data object:
>>> plan_data['subject']['policy'] += policies



Convert the plan_data object to a JSON text:
>>> plan_data = json.dumps(plan_data, indent=4)



Send a POST request with the JSON text to the /policy_management/v4/policies endpoint:
>>> response = requests.post(
...     f'{base_url}/policy_management/v4/policies',
...     headers={'Content-Type': 'application/json', **auth},
...     data=plan_data,
... )



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the protection plan has been created.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.

Also, the response body contains an object with the result key, containing an array of policy IDs formatted as a JSON text. When converted to an object, it will look like this:
>>> pprint.pprint(response.json())
{'result': ['5b15f6e1-88ec-4dce-b523-0e8394c0bc19@policy.protection.total',
'256f2ee5-c9fd-4aad-8607-97a977deeaae@policy.backup.machine',
'260a95af-366f-4331-ad88-6f188f034870@policy.security.vulnerability_assessment',
'fce55bf0-efb2-4220-b9bf-6fdebc5af660@policy.security.backups_scanning',
'a1d5efa0-f9d7-4493-9bc9-c159879c7724@policy.security.windows_defender',
'23f0fc3c-1b52-4da5-a765-fd856255b023@policy.security.patch_management',
'9502bbc1-b37c-4617-8a8e-c174a945e98d@policy.security.microsoft_security_essentials',
'f354c80f-5b7a-4466-97f1-df670cccb673@policy.security.antimalware_protection',
'4f3c7359-2a83-40cf-9733-172253d85484@policy.security.data_protection_map',
'3c496736-8fdf-48b7-bd4d-66c770448e83@policy.security.active_protection',
'6c120d91-7ce3-463e-abae-b6c43ab27c87@policy.security.url_filtering']}