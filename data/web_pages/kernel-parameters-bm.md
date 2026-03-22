# Kernel parameters

Managing the backup and recovery of workloads and files > Creating bootable media to recover operating systems > Bootable Media Builder > Kernel parameters
Kernel parameters

You can specify one or more parameters of the Linux kernel that will be automatically applied when the bootable media starts. These parameters are typically used when you experience problems while working with the bootable media. Normally, you can leave this field empty.

You can also specify any of these parameters by pressing F11 while you are in the boot menu.

Parameters

When specifying multiple parameters, separate them with spaces.

acpi=off

Disables Advanced Configuration and Power Interface (ACPI). You may want to use this parameter when experiencing problems with a particular hardware configuration.

noapic

Disables Advanced Programmable Interrupt Controller (APIC). You may want to use this parameter when experiencing problems with a particular hardware configuration.

vga=ask

Prompts for the video mode to be used by the bootable media's graphical user interface. Without the vga parameter, the video mode is detected automatically.

vga= mode_number

Specifies the video mode to be used by the bootable media's graphical user interface. The mode number is given by mode_number in the hexadecimal format—for example: vga=0x318

The screen resolution and the number of colors corresponding to a mode number may be different on different machines. We recommend that you use the vga=ask parameter first to choose a value for mode_number.

quiet

Disables displaying of startup messages when the Linux kernel is loading, and starts the management console after the kernel is loaded.

This parameter is implicitly specified when creating the bootable media, but you can remove this parameter while you are in the boot menu.

If this parameter is removed, all startup messages will be displayed, followed by a command prompt. To start the management console from the command prompt, run the command: /bin/product

nousb

Disables loading of the USB (Universal Serial Bus) subsystem.

nousb2

Disables USB 2.0 support. USB 1.1 devices still work with this parameter. This parameter allows you to use some USB drives in the USB 1.1 mode if they do not work in the USB 2.0 mode.

nodma

Disables direct memory access (DMA) for all IDE hard disk drives. Prevents the kernel from freezing on some hardware.

nofw

Disables the FireWire (IEEE1394) interface support.

nopcmcia

Disables the detection of PCMCIA hardware.

nomouse

Disables the mouse support.

module_name =off

Disables the module whose name is given by module_name. For example, to disable the use of the SATA module, specify: sata_sis=off

pci=bios

Forces the use of PCI BIOS instead of accessing the hardware device directly. You may want to use this parameter if the machine has a non-standard PCI host bridge.

pci=nobios

Disables the use of PCI BIOS; only direct hardware access methods will be allowed. You may want to use this parameter when the bootable media fails to start, which may be caused by the BIOS.

pci=biosirq

Uses PCI BIOS calls to get the interrupt routing table. You may want to use this parameter if the kernel is unable to allocate interrupt requests (IRQs) or discover secondary PCI buses on the motherboard.

These calls might not work properly on some machines. But this may be the only way to get the interrupt routing table.

LAYOUTS=en-US, de-DE, fr-FR, ...

Specifies the keyboard layouts that can be used in the bootable media's graphical user interface.

Without this parameter, only two layouts can be used: English (USA) and the layout that corresponds to the language selected in the media's boot menu.

You can specify any of the following layouts:

Belgian: be-BE

Czech: cz-CZ

English: en-GB

English (USA): en-US

French: fr-FR

French (Swiss): fr-CH

German: de-DE

German (Swiss): de-CH

Italian: it-IT

Polish: pl-PL

Portuguese: pt-PT

Portuguese (Brazilian): pt-BR

Russian: ru-RU

Serbian (Cyrillic): sr-CR

Serbian (Latin): sr-LT

Spanish: es-ES

When working under a bootable media, use CTRL + SHIFT to cycle through the available layouts.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.