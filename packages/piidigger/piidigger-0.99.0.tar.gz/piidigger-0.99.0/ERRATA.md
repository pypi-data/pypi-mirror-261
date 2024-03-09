# PIIDigger Errata
## Known Issues and Limitations
A few items worth noting about PIIDigger:

### Antivirus Alerts
Building a binary/executable file in Python seems to trigger something in anti-virus software such as Microsoft Defender.  If your A/V triggers on PIIDigger, consider one of the following solutions:
* Create an exception for the folder where you dowloaded the PIIDigger executable binaries.
* Install Python from [Python Official Source](https://www.python.org/downloads/) and then use the "Python Available" installation method.  NOTE: For Windows users: There is also a Python download available in the Microsoft Store, but PIIDigger was not tested against this version.  #YMMV
    * PIIDigger has been tested on Python versions 3.9 through 3.12.  While there's no reason to think it'll break on other versions, I recommend that new Python installations use versions which are still in "bugfix" status for long-term support provided by the Python community.

### Handling CTRL-C Events
Handling CTRL-C (KeyboardInterrupt events) -- Everytime I *think* that CTRL-C events are handled correctly everywhere, another one pops up.  Handliing CTRL-C in multi-threaded/process applications can be problematic.
* You could still get the odd stack trace -- if this happens, please open an issue (see below) and provide the full text that appeared on your screen.
* If, on the other hand, it appears to be hung up (see Troubleshooting below), a second CTRL-C may speed things up, but if all else fails, you can stop the processes manually using your operating system's methods:
    * Windows PowerShell: `Get-Process python | Stop-Process`
    * Windows Task Manager: Manually `End Task` on each Python process in the list
    * Linux/MacOS: `kill $(pidof python)`

### Cloud Storage Services (Windows Only)
For Windows-based OneDrive and Dropbox users, PIIDigger should ignore offline files that are not yet on the local drive.  This should avoid the lengthy scans and full drives that can occur when downloading lots of content from cloud storage providers.  There is a configuration setting to override this default behavior if you wish to.
* This is not yet implemented for MacOS and Linux users.  So you might need user interaction to avoid those downloads.
* This is based on File System Attributes (hence, not yet implemented for MacOS and Linux users).  If OneDrive or Dropbox change how they use these permissions, it could break.  That seems unlikely, but then again....
* Google Drive users -- Google Drive uses a completely different mechanism for managing which files are available offline, including a local cache stored in the users's `%APPDATA%` folder.  It is necessary to exclude the G\\: drive (see `[excludeDirs]` configuration option), but this is not enabled by default as G:\\ could have other purposes or you could have changed the letter used by your GDrive.  Any local files in the cache should be picked up by PIIDigger and scanned normally.

*MacOS and Linux uses of PIIDigger are not currently Cloud Storage Provider-aware.*

### MacOS Applicaton Permissions 
* On MacOS 14 (Sonoma), there is a new OS feature that prompts the user whenever an unknown application attempts to access various user data folders.  You'll need to permit PIIDigger to access these folders by responding to these prompts.

### Excel Formatting
* Some Excel files have "pretty formatting" applied to all cells.  This can cause `openpyxl` (XLSX files) and `xlrd` (xlrd) to misread the sheet's dimensions.  PIIDigger includes two safety valves:
    * Stop reading a row after encountering 500 empty cells.  
    * Stop reading a sheet after reading 250 blank rows.  
    * If the "interesting data" is outside those limits, PIIDigger will miss it.

## Troubleshooting
The primary tool for troubleshooting is the `logs/piidigger.log` file.  It is helpful to display this log in a second console/terminal window:
* Windows PowerShell: `Get-Content logs/piidigger.log -Wait`
* Linux/MacOS: `tail -f logs/piidigger.log`

The default configuration uses `"INFO"`-level logging, but for particularly sticky problems, it may be necessary to capture a `"DEBUG"` log.  Just know -- those files are HUGE easily 100s of MB.  See below for instructions on how to enable `"DEBUG"` mode, but don't leave PIIDigger running in this mode.

Common scenarios:
| Symptom                                                                   | Troubleshooting   |
| ---                                                                       | ---               |
| The program appears to hang with no updates being made to the status bar. | Monitor the log file and if you see messages about terminating processes, it has hung up.  Kill the processes as mentioned above. |
| The computer is really slow when working with other programs.             | PIIDigger will attempt to use all available CPU cycles in order to complete as quickly as possible.  Review the [PERFORMANCE](PERFORMANCE.md) page for tips on tuning PIIDigger performance. |
| Why are my results so low?  I used `<TOOLX>` and I had thousands more hits than with PIIDigger | PIIDigger reports on *UNIQUE* hits per file, so if the same item shows up dozens of times in the same file, PIIDigger will only count it once.  When tested against a data set that included approximately 500k fake credit card numbers and counting each instance of PIIDigger-identified data, PIIDigger was within 3% of `<TOOLX>` results.  I think that's a reasonable margin. |

## Reporting New Issues
To report a new issue, first create a PIIDigger debug log as follows:
* Create a PIIDigger configuration file with `piidigger -c piidigger.toml`.
* Edit the configuration file with your favorite text editor (Notepad on Windows is fine).
    * At the end, replace `logLevel = "INFO"` with `logLevel = "DEBUG"` (capitalization is important).
* Rerun PIIDigger -- it will pick up the new configuration file as long as you named it `piidigger.toml`.
    The log file will be `logs/piidigger.log`.
* Open an issue in GitHub on the PIIDigger [issues](https://github.com/flyguy62n/PIIDigger/issues) page.
* Be sure to attach a ZIP of the log file.  *It's quite large so be sure ZIP it first!*
* You can now delete the configuration file, after which the default configuration will automatically be used.
* You can also delete the log file.