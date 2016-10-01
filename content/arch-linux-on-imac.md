Title: Running Arch Linux from an SD Card on an iMac
Date: 2014-03-06 01:53
Author: Peter
Category: Surveillance
Tags: Surveillance
Slug: arch-linux-on-imac
Summary: Why would you use the spyware operating system installed on an iMac when you can run Arch Linux from an SD card?

The office I was recently assigned to had an iMac with an almost nice
27-inch screen -- it would be nice if it was not glossy. I thought I
would put the machine to use to avoid lugging my laptop to work every
day. Naturally I never considered using the proprietary operating system
it was contaminated with, but I also did not want to install anything on
its hard drive. So my quest began to boot Arch Linux from an SD card.
After many false starts, I succeeded.

The hardware is not too bad: i5-2500S CPU clocked at 2.70GHz, a Radeon
GPU, and a measly 4 GByte of RAM. The way vendors discourage using Linux
these days is by making installing a boot loader insanely complicated.
This was in fact the only difficulty, albeit a major one. The solution
has two steps:

  1. Boot an install disk from the SD card.
  2. Boot the operating system from the SD card.

Only the first step requires using the proprietary operating system, and
only for a few minutes. Cover the built-in camera with a duct tape and boot. Install 
rEFInd from [here](http://www.rodsbooks.com/refind/). Then [run the
script install.sh](http://www.rodsbooks.com/refind/installing.html).
That is it, turn off the machine.

From your trusty Linux distribution, prepare the SD card. For the rest
of this write-up, I assume that the SD card shows up as ``/dev/mmcblk0`` in
both machines, the Linux in which you are preparing the partitions, and
the install system that you will boot up on the iMac. The partition
configuration should be the following:

  - Partition table: GPT.
  - Partition 1: 100 MByte FAT32.
  - Partition 2: Ext2 of a size of your choice.
  - Partition 3: 600 MByte FAT32.

The label of partition 3 must match the ISO file; in my case, it was
ARCH_201402. The other partitions can have arbitrary labels. Also
ensure that partition 1 is bootable. Download the latest [Arch ISO](https://www.archlinux.org/download/ "Download Arch Linux"); I used
2014-02. Mount the ISO and the third partition on the SD card, and copy
all files:

    :::bash
    mount -o loop archlinux-2014.02.01-dual.iso /mnt/dvd
    mount -t auto /dev/mmcblk0p3 /mnt/mmc
    cp -a /mnt/dvd/* /mnt/mmc

Unmount the SD card and plug it in the iMac. The obnoxious designers put
the card slot right next to the DVD drive on the side of the screen, so
it is easy to accidentally plug the SD card in the DVD drive. It takes
half an hour to fish it out. To prevent such accidents, I recommend
stuffing some brochures in the opening of the drive. Visit Singapore
fliers are particularly apt to solve the problem.

If you found the correct slot despite the schemes of the designers,
turning on the machine should display rEFInd, with an option to boot the
installer. If the installer does not start properly, check if the
partition has the correct label.

From here, follow the standard Arch [installation procedure](https://wiki.archlinux.org/index.php/Installation_guide).
Mount ``/dev/mmcblk0p2`` as ``/mnt``, and ``/dev/mmcblk0p1`` as ``mnt/boot``. I used
gummiboot as the UEFI bootloader for the operating system. If it fails
to install, you probably forgot to set the boot flag on ``/dev/mmcblk0p1``.

Before exiting the chroot environment, invoke a sync. Once you restart,
the SD card should boot straightaway, without ever showing the rEFInd
boot menu.

Once you exit the chroot environment and reboot, the third partition is
no longer necessary. Use your laptop to delete this partition, and
enlarge the second partition.

I tried the libre flavour of Arch, Parabola GNU Linux, running on the
machine, but the kernel froze after booting up. Apparently, your freedom
will always be limited if you use a product made by these people.

I invested a few dollars in a mouse, because the ridiculous wireless
trackpad refused to work. I also got a decent, wired keyboard instead of
the menace that came with the machine. Now if only I could scrape off
the glossy layer of the screen, the computer would be usable.

