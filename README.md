# fs_arch_unofficial
Fresswitch PBX for Arch Linux (unofficial) package
This is the unofficial freeswich build based on [Freeswitch Artch Linux AUR Repository](https://aur.archlinux.org/packages/freeswitch) from Korynkai, thx.

These builds are therfor also under the MPL 2.0 License published, as the sourcecode from the creator.

to make use of this repository you will have 1st to to import my GPG public key in pacman which is done as (root):

    pacman-key --recv-key A39D375C947A2F33

or in case the "ubuntu keyserver" is not reachable (under what reason soever), you might fetch the key via DNSSEC (which required that your ISP resolver has dnssec enabled), otherwise change your ISP dns resolver to "1.1.1.1"

    gpg --homedir /etc/pacman.d/gnupg --auto-key-locate nodefault,dane --locate-keys th80@s4us.info

Then you need to trust this imported key, otherwise pacman will reject the repo:

    pacman-key --lsign-key A39D375C947A2F33

After successfully importing and signing (trusting) the key we need to add the repository in  /etc/pacman.conf with the following 2 lines:

    [fs-repo]
    Server = https://github.com/thigazi/fs_arch_unofficial/raw/refs/heads/main/x64/

and run "pacman -Syu"

These modules are available in this FS build, for further modules that should be implemented please open an issue:

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
