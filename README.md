# fs_arch_unofficial
Fresswitch PBX for Arch Linux (unofficial) package
This is the unofficial [Freeswich PBX](https://developer.signalwire.com/freeswitch/FreeSWITCH-Explained/) Arch Linux Repository based on [Freeswitch Arch Linux AUR](https://aur.archlinux.org/packages/freeswitch) published from the user "Korynkai", thank you.

these builds are licensed under the MPL 2.0 License as the sourcecode from the creators of this software.

If you just want to install this version of Freeswitch, no repository is needed to be setup. You just download the 2 files: "freeswitch-xxxx-x86_64.pkg.tar.zst" and "spandsp-git-x.x.x.x-1-x86_64.pkg.tar.zst" and execute (for example):
    
    pacman -U spandsp-git-3.0.0.r563.g7977601-1-x86_64.pkg.tar.zst freeswitch-1.10.12-1-x86_64.pkg.tar.zst 
    
which will install freeswitch with all dependencies on your server.

If you want to make use of this repository you will have to perform all operations as root user or sudo / run0.

1st init the pacman "master key"

    pacman-key --init

and then import my GPG public key in pacman:

    pacman-key --recv-key A39D375C947A2F33

In case the "ubuntu keyserver" is not reachable, you might fetch the key via DNSSEC (your ISP resolver has to be dnssec enabled), otherwise change your ISP dns resolver to "1.1.1.1" (cloudflare public dns resolver) or "8.8.8.8" (google public dns resolver) and execute

    gpg --homedir /etc/pacman.d/gnupg --auto-key-locate clear,nodefault,dane --locate-keys th80@s4us.info

Then you need to trust this imported key, otherwise pacman will reject this repo

    pacman-key --lsign-key A39D375C947A2F33

After successfully importing and signing (trusting) the key we need need to add the repository.

There are 2 ways to accomplish that, which is:

A) reposync on "sourceforge" (recommended as sf has lots of mirror servers). A special downloader had been written from my side that generates a local repository and syncs the data with the remote servers

or

B) the github way, where you can directly sync (very slow as GH is not a filesharing service itself)

## RepoSetup via GitHub (not recommended).

github in 1st sight is not a file sever, more a professional "git" repository service, but I have managed it to access the raw data. You simply add these 2 lines in "/etc/pacman.conf":

    [fs-repo]
    Server = https://github.com/thigazi/fs_arch_unofficial/raw/refs/heads/main/x64/

and run "pacman -Syu" which synchronized the DB with the final command "pacman -S freeswitch" that triggers the installation of the freeswitch PBX System package


## RepoSetup via sourceforge (recommended).

sourceforge is (perhaps one of the oldest) mirroring server network in the world to distribute software. On the other side, we cannot access data (in raw) mode directly, which makes it for us difficult to setup straight away the repo.

To make this happen, I have created an applicaiton that will create the repo, and sync all the data. and therfor 5 simple steps are needed, no libraries or whatever is needed

Install [python3](https://archlinux.org/packages/core/x86_64/python/), if not already on your system

    pacman -S python
    
download the "FSDLUpdater.py" script and place it in a location you might be is suitable, like "/usr/local/bin" and make it executable with "chmod 644 FSDLUpdater"

__(1/5)__ create a directory where the repo-folder will be created, for example: /opt/custom-apps

    sudo mkdir /opt/custom-apps
    
__(2/5)__ change the ownershop to your daily account:

    sudo chown -R $(whoami):$(whoami) /opt/custom_apps
    
__(3/5)__  execute the script (as user), this python script will do the rest to setup the repo and download through the sf network the data:

    /usr/local/bin/FSDLUpdater.py /opt/custom_apps

__(4/5)__ add custom pacman section /opt/custom_apps/fs-repo/pacman repo.txt as /etc/pacman.conf simply (as root user)

    echo -e "\n$(cat /opt/custom_apps/fs-repo/pacman_repo.txt)" >> /etc/pacman.conf
    
__(5/5)__ and finally sync  and install with:

    pacman -Syu && pacman -S freeswitch

(additionaly) add in our user cronjob an entry

    0 0 5 * * /run/media/tamer/work/devPro/fs-arch-unoffocial-code/FSDLUpdater.py /opt/custom_apps >/dev/null 2>&1

which will execute every month the 5th of a month to syncronize and update that repo as soon I release a new version




## "modules" included in this freeswitch installation

These modules are available in this FS build, for further modules that should be implemented please open an issue, i'll do my best to rebuild and make it in the repo available:

    applications/mod_cidlookup
    applications/mod_directory
    applications/mod_easyroute
    applications/mod_av
    applications/mod_blacklist
    applications/mod_commands
    applications/mod_conference
    applications/mod_db
    applications/mod_dptools
    applications/mod_enum
    applications/mod_esl
    applications/mod_esf
    applications/mod_expr
    applications/mod_fifo
    applications/mod_fsv
    applications/mod_hash
    applications/mod_spandsp
    applications/mod_spy
    applications/mod_test
    applications/mod_valet_parking
    applications/mod_voicemail
    codecs/mod_amr
    codecs/mod_b64
    codecs/mod_g723_1
    codecs/mod_g729
    codecs/mod_h26x
    codecs/mod_opus
    codecs/mod_clearmode
    codecs/mod_g729
    codecs/mod_dahdi_codec
    codecs/mod_isac
    codecs/mod_mp4v
    codecs/mod_theora
    dialplans/mod_dialplan_xml
    dialplans/mod_dialplan_directory
    endpoints/mod_loopback
    endpoints/mod_rtc
    endpoints/mod_sofia
    event_handlers/mod_cdr_csv
    event_handlers/mod_event_socket
    event_handlers/mod_cdr_pg_csv
    event_handlers/mod_fail2ban
    event_handlers/mod_format_cdr
    event_handlers/mod_json_cdr
    event_handlers/mod_odbc_cdr
    formats/mod_local_stream
    formats/mod_native_file
    formats/mod_png
    formats/mod_sndfile
    formats/mod_tone_stream
    languages/mod_lua
    languages/mod_python3
    loggers/mod_console
    loggers/mod_logfile
    loggers/mod_syslog
    say/mod_say_de
    say/mod_say_en
    xml_int/mod_xml_cd
    timers/mod_posix_timer
    timers/mod_timerfd
