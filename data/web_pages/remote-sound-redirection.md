# Remote sound redirection

RMM > Connecting to workloads for remote desktop or remote assistance > Remote sound redirection
Remote sound redirection

Connect Client supports audio streaming via the NEAR connection protocol. For more information about NEAR, see Remote connection protocols.

Redirecting sound from a remote Windows workload

For Windows workloads, the remote sound should be transmitted automatically. Ensure that there are sound output devices (speakers or headphones) connected to the remote workload.

Redirecting sound from a remote macOS workload

To enable sound redirection from a macOS workload, ensure that:

The workload has the Protection agent installed.

The workload has a sound capture driver installed.

The workload uses the NEAR protocol for remote connections.

For macOS 10.15 Catalina, the Microphone permission must be granted to the Connect Agent. For more information about granting the Microphone permission to the Connect Agent, see Granting the required system permissions to the Connect Agent.

The agent works with the following sound capture drivers: Soundflower or Blackhole.

The installation process on the newest versions is described on the Blackhole wiki page: https://github.com/ExistentialAudio/BlackHole/wiki/Installation.

Connect Client currently supports only the 2-channel version of Blackhole.

Alternatively, if Homebrew is installed on the workload, you can install Blackhole by running the following command:

brew install --cask blackhole-2ch

While the sound of a remote macOS workload is redirected, the user who is logged in to the remote workload will not hear the sound.

Redirecting sound from a remote Linux workload

The remote sound redirection should work automatically with most Linux distributions. If the remote sound redirection is not working by default, install PulseAudio driver by running the following command:

sudo apt-get install pulseaudio

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.