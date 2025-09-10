# fs_arch_unofficial
Fresswitch PBX for Arch Linux (unofficial) package
This is the unofficial [Freeswich PBX](https://developer.signalwire.com/freeswitch/FreeSWITCH-Explained/) Arch Linux Repository based on [Freeswitch Arch Linux AUR](https://aur.archlinux.org/packages/freeswitch) published from the user "Korynkai", thank you.

these builds are licensed under the MPL 2.0 License as the sourcecode from the creators of this software.

To make use of this repository you will have to perform all operations as root user or sudo / run0.

1st init the pacman "master key"

    pacman-key --init

and then import my GPG public key in pacman:

    pacman-key --recv-key A39D375C947A2F33

In case the "ubuntu keyserver" is not reachable, you might fetch the key via DNSSEC (your ISP resolver has to be dnssec enabled), otherwise change your ISP dns resolver to "1.1.1.1" or "8.8.8.8" and execute

    gpg --homedir /etc/pacman.d/gnupg --auto-key-locate clear,nodefault,dane --locate-keys th80@s4us.info

Then you need to trust this imported key, otherwise pacman will reject the repo

    pacman-key --lsign-key A39D375C947A2F33

After successfully importing and signing (trusting) the key we need to add the repository in  /etc/pacman.conf with the following 2 lines

    [fs-repo]
    Server = https://github.com/thigazi/fs_arch_unofficial/raw/refs/heads/main/x64/

and run "pacman -Syu" which synchronized the DB with the final command "pacman -S freeswitch" that triggers the installation of the freeswitch PBX System package

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
