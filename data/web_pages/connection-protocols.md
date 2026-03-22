# Remote connection protocols

RMM > Connecting to workloads for remote desktop or remote assistance > Remote connection protocols
Remote connection protocols

The remote desktop functionality uses the following protocols for remote connections.

NEAR

NEAR is a highly secure protocol developed by Acronis that has the following characteristics.

H.264

NEAR implements three quality modes: Smooth, Balanced and Sharp. In Smooth mode, NEAR uses hardware H.264 encoding on macOS and Windows to encode the desktop picture, and falling back to software encoder if hardware encoder is not available. The picture size is currently limited to Full HD resolution (1920x1080).

Adaptive codec

In Balanced and Sharp quality modes, NEAR uses Adaptive codec, which provides full picture quality in 32 bit, compared to the 'video' mode used by H.264.

In Balanced mode, the picture quality is automatically adjusted according to your current network conditions and retains the current framerate.

In Sharp mode, the picture is full quality, but it might be with a reduced framerate, if your network, processor, or video card are overloaded.

Adaptive codec is using OpenCL on Windows and macOS when it is available in their graphics drivers.

Sound transfer

NEAR is capable of capturing the remote computer sound and transfer that to host. For more information about enabling remote sound redirection on Windows, macOS, and Linux, see Remote sound redirection.

Different login options

You can use the following methods to log in to the remote workload.

Access code: the user who is logged in to the remote workload runs Quick Assist and tells you the access code. With this method, you always connect to the session of the currently logged in user.

Workload credentials: log in to the remote workload using administrator credentials that are registered in the workload.

Ask for permission to observe or control: the user who is logged in to the remote workload will be asked to allow or deny the connection.

Security

Your data is always two-way encrypted with AES encryption in NEAR.

RDP

Remote Desktop Protocol (RDP) is a proprietary protocol developed by Microsoft that enables connecting to the remote Windows computer over a network connection.

Apple Screen Sharing

Apple Screen Sharing is a VNC client by Apple included as part of macOS version 10.5 and later.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.