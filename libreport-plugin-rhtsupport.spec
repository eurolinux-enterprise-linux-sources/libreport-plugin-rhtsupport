Name:		libreport-plugin-rhtsupport
Version:	2.0.9
Release:	34.sl6
Summary:	libreport's RHTSupport plugin

Group:		System Environment/Libraries
License:	GPLv2+

%description
Plugin to report bugs into RH support system.


%prep


%build


%install


%files



%changelog
* Fri Jun 22 2018 Scientific Linux Auto Patch Process <SCIENTIFIC-LINUX-DEVEL@LISTSERV.FNAL.GOV>
- Added Source: libreport.ini
-->  Config file for automated patch script
- Added Source: libreport-spec_norhtsupport.patch
-->  Don't open upstream support cases

* Tue Jan 23 2018 Martin Kutlak <mkutlak@redhat.com> - 2.0.9-34
- Correctly trim spaces before values with augeas
- Prevent creating of customer case without reproducing knowledge
- Rely on configurated email
- Change URL in config for bug-report server
- Fix segfaulting abrt-cli
- Related #1422030, #1328768, #1323625, #1463316, #1421754

* Wed Nov 02 2016 Matej Habrnal <mhabrnal@redhat.com> - 2.0.9-33
- Avoid infinite crash loops
- Related: #1324586

* Thu Feb 25 2016 Matej Habrnal <mhabrnal@redhat.com> - 2.0.9-32
- Rebuild because of failed rpmdiff
- Related: #1261398

* Wed Feb 24 2016 Matej Habrnal <mhabrnal@redhat.com> - 2.0.9-31
- Add pkg_vendor, reproducer and reproducible to description
- Attach all dump dir's element to a new case
- Change libreport-version to 2.0.9.1
- Resolves: #1261398

* Fri Jan 29 2016 Matej Habrnal <mhabrnal@redhat.com> - 2.0.9-30
- Attach URL of uploaded problem data to uReport
- Resolves: #1300777

* Fri Jan 22 2016 Matej Habrnal <mhabrnal@redhat.com> - 2.0.9-29
- Change reporting workflow to enhance the quality of opened customer cases
- Limit the description section for ABRT reported cases
- Resolves: #1258474, #1261398

* Mon Jan 11 2016 Matej Habrnal <mhabrnal@redhat.com> - 2.0.9-28
- Make function uid_in_group() public
- Bugzilla private bugs
- Resolves: #1279454, #803769

* Tue Dec 08 2015 Jakub Filak <jfilak@redhat.com> - 2.0.9-27
- Enable configuration of SSH keys in report-upload
- Resolves: #1261120

* Thu Nov 19 2015 Jakub Filak <jfilak@redhat.com> - 2.0.9-26
- Correct augeas configuration parser
- Resolves: #1262246

* Sun Nov 15 2015 Jakub Filak <jfilak@redhat.com> - 2.0.9-25
- save all files changed by the reporter in the reporting GUI
- Fixes CVE-2015-5302
- Resolves: #1282144

* Fri May 22 2015 Jakub Filak <jfilak@redhat.com> - 2.0.9-24
- switch ownership of new directories from "abrt:user" to "user:abrt"
- fix a bug allowing libreport to read files outside dump directories
- Related: #1212095

* Fri May 15 2015 Jakub Filak <jfilak@redhat.com> - 2.0.9-23
- resolve symbolic and hard link vulnerabilities
- defend against directory traversal attack
- Resolves: #1212095

* Tue Feb 24 2015 Jakub Filak <jfilak@redhat.com> - 2.0.9-22
- Upstream uReport with Strata integration
- Resolves: #1152222

* Thu Jun 19 2014 Jakub Filak <jfilak@redhat.com> - 2.0.9-21
- Rebuild due to translation updates
- Resolves: #989530, #997871, #1090466, #1093375

* Thu Jun 19 2014 Jakub Filak <jfilak@redhat.com> - 2.0.9-20
- Bugzilla: pass Bugzilla_token in all XML RPC calls
- mailx: improve notification e-mail headers
- mailx: include hostane in notification e-mail
- Resolves: #989530, #997871, #1090466, #1093375

* Tue Aug 13 2013 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.9-19
- updated transaltion (ko) rhbz#993626
- fixed bugzilla reporter to work with the new xmlrpc api rhbz#991088
- Resolves: #991088, #993626

* Wed Aug 07 2013 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.9-18
- rebuild because of failed rpmdiff
- Related: #993626

* Tue Aug 06 2013 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.9-17
- updated translation rhbz#993626
- fixed bugs doscovered by coverity rhbz#905051
- Resolves: #993626, #905051

* Fri Jun 07 2013 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.9-16
- ABRT won't install debuginfos from rhn repository rhbz#759443
- Brewtap reports LibMissingRELRO rhbz#812283
- libreport attached sosreport into bugzilla with bad mimetype rhbz#885509
- reporter-rhtsupport on RHEL6.4 unable to open cases in RHT customer center rhbz#896090
- Change default set of reporters shown by CLI/GUI rhbz#948286
- [RFE] add the console notification to RHEL6 rhbz#961231
- Resolves: #885509, #812283, #961231, #961231, #961231, #948286, #759443, #896090, #875260

* Fri Jan 18 2013 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.9-15
- rebuilding beacause of failed rpmdiff - no changes
- Related: #895443

* Fri Jan 18 2013 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.9-14
- in same cases we have to follow symlinks
- Related: #895443

* Wed Jan 16 2013 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.9-13
- don't follow symlinks
- Resolves: #895443

* Mon Jan 07 2013 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.9-12
- fixed relro flags
- removed confusing warning message
- added versioned requirements to silence rpmdiff
- Resolved: #847291, #812283, #857425

* Thu Oct 18 2012 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.9-11
- removed reporter-bugzilla from config file re-added by mistake
- Related: #815339

* Thu Oct 18 2012 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.9-10
- updated translation rhbz#864025
- fixed brewtap warnings rhbz#812283
- silence few rpmdiff warnings rhbz#857425
- Resolves: #864025, #812283, #857425

* Fri Sep 14 2012 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.9-9
- don't show the user credentials in logs rhbz#856960
- Resolves: #856960

* Wed Aug 29 2012 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.9-8
- use the default template for bz reports rhbz#747410
- fix adding users to CC in bugzilla rhbz#841338
- Resolves: #747410, #841338

* Thu Aug 23 2012 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.9-7
- don't warn about daemon connection when deleting a problem rhbz#799909
- ignore non problem dirs when cleaning old problems rhbz#847291
- Resolves: #799909, #847291

* Thu Aug 09 2012 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.9-6
- opt kernel out of showing smolt information in abrt bug reports. rhbz#795548
- ABRT mailx plugin on by default causes crashes being always labelled as reported rhbz#803618
- pkg-config --cflags libreport includs -fPIC rhbz#803736
- Coverity revealed memory leaks and possibly other issues rhbz#809416
- GLib warnings by report-gtk when crash dir does not exist rhbz#813283
- `report' tool requires current working directory to be a crash dir rhbz#817051
- Searching for duplicate anaconda bugs while reporting exception against partner-bugzilla during install fails rhbz#820985
- Undefined non-weak symbols rhbz#826745
- ABRT has wrong URL in dialog
Resolves: #809416,#813283,#817051,#826745,#820985,#795548,#803618,#803736

* Wed May 23 2012 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.9-5
- rebuild due to rpmdiff
- Resolves: #823411

* Tue May 22 2012 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.9-4
- fixed compatibility with bugzilla 4.2
- Resolves: #823411

* Fri Mar 16 2012 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.9-3
- added notify-only option to mailx rhbz#803618
- Resolves: #803618

* Tue Mar 06 2012 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.9-2
- minor fix in debuginfo downloader
- updated translations
- Related: #759377

* Wed Feb 15 2012 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.9-1
- new upstream release
- fixed typos in man
- fixed handling of anaconda-tb file
- generate valid xml file
- Resolves: #759377, #758366, #746727

* Wed Oct 26 2011 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.5-20
- fixed i18n initialization
- Resolves: #749148

* Wed Oct 26 2011 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.5-19
- rebuild, some translations were not propagated to xml files
- Resolves: #731037

* Tue Oct 25 2011 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.5-18
- updated translations
- Resolves: #731037

* Tue Oct 25 2011 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.5-17
- minor spec file fix
- Resolves: #743198

* Tue Oct 25 2011 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.5-16
- minor fix to the search kbase
- Resolves: #743198

* Tue Oct 25 2011 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.5-15
- fix the kbase searching rhbz#743198
- updated translation Related: #731037
- Resolves: #743198 #731037

* Tue Oct 25 2011 Jiri Moskovcak <jmoskovc@redhat.com>
- fix the spec file changelog
- Resolves: #742474

* Fri Oct 21 2011 Nikola Pajkovsky <npajkovs@redhat.com>
- abrt-cli uses wrong return codes
- Resolves: #742474

* Wed Oct 19 2011 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.5-14
- reaply the man pages patch
- Resolves: #728190

* Wed Oct 19 2011 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.5-13
- bumped release
- Resolves: #731037

* Wed Oct 19 2011 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.5-12
- updated translation rhbz#731037
- search kbase before creating the ticket rhbz#743198
- Resolves: #731037 #743198

* Tue Oct 18 2011 Nikola Pajkovsky <npajkovs@redhat.com>
- man pages contain suspicious version string
  Resolves: #728190

* Thu Oct 13 2011 Jiri Moskovcak <jmoskovc@redhat.com> - 2.0.5-11
- disabled bugzilla rhbz#739936
- own /etc/libreport/plugins/ rhbz#744782
- removed unused patches to make rpmdiff happy
- updated translation
- Resolves: #739936 #744782

* Wed Sep 21 2011 Jiri Moskovcak <jmoskovc@redhat.com> - 2.0.5-10
- make wizard page titles translatable
- updated transaltion
- Resolves: #734789 #731037

* Wed Aug 31 2011 Jiri Moskovcak <jmoskovc@redhat.com> - 2.0.5-9
- fixed make check rhbz#729686
- fixed attaching anaconda-tb* rhbz#731389
- Resolves: #729686 #731389

* Fri Aug 26 2011 Nikola Pajkovsky <npajkovs@redhat.com> - 2.0.5-8
- Missing man pages of report and report.conf
  Resolves: #729957
- Update translations
  Resolves: #731037

* Thu Aug 25 2011 Denys Vlasenko <dvlasenk@redhat.com> - 2.0.5-7
- Fix report-cli crash if config files are missing.
  Resolves: #730942
- Pull in libreport-plugin-reportuploader on update
  (fixes a problem with "yum update" on RHEL system with old report package.
  Resolves: #732683

* Tue Aug 23 2011 Karel Klíč <kklic@redhat.com> - 2.0.5-6
- Added two patches (libreport-code-was-moved-to-abrt.git,
  libreport-fix-d-delete-option) from upstream making report-cli
  -d/--delete to remove DUMP_DIR after reporting. First patch also
  removes --list and --info and --full options, which were already
  moved to abrt-cli.
  Resolves: #726097
- Added fallback text editor for editing multiline fields in Anaconda
  Resolves: #728479

* Fri Aug 05 2011 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.5-5
- added the report cmdline tool rhbz#725660
- fixed man pages version rhbz#728190
- fixed text wrapping rhbz#728132
- improved dump_dir detection rhbz#728166
- fixed reporting from Anaconda newt ui rhbz#729566
- added defualt config file for rhtsupport rhbz#729566
- make reporters use default conf when -c is not used rhbz#729986
- Resolves: #725660 #728190 #728132 #728166 #729566 #729986

* Tue Aug 02 2011 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.5-4
- further improvement in Anaconda compatibility rhbz#727243
- warn silently when keyring is not available rhbz#725858
- Resolves: #727243 #725858

* Thu Jul 28 2011 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.5-3
- improved compatibility with bugzilla
- enabled bugzilla for libreport reports (analyzer=libreport)
- Resolves: #725857

* Mon Jul 25 2011 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.5-2
- removed mailx from possible reporter list (still enabled as post-create event)
- added python bindings to libreport client lib
- honor reporters minimal rating
- fixed (null) in bz summary
- Related: #714045

* Mon Jul 18 2011 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.5-1
- move reporter plugins from abrt to libreport
- fixed provides/obsolete to properly obsolete report package
- wizard: make more fields editable
- Related: #697494

* Tue Jul 12 2011 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.4-4
- added the python bindings -> obsoleting report

* Mon Jul 11 2011 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.4-3
- bump release

* Mon Jun 27 2011 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.4-2
- removed Provides/Obsoletes: report-gtk
- Resolves: #715373

* Mon Jun 20 2011 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.4-1
- new upstream release
- cleaned some header files

* Thu Jun 16 2011 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.3-1
- added report-cli
- updated translation

* Wed Jun 01 2011 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.2-1
- initial packaging

