; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "Remote Object Backup"
#define MyAppVersion "0.1pa"
#define MyAppPublisher "Ajayi Oluwaseun Emmanuel"
#define MyAppURL "http://www.oluwaseun.com/"
#define MyAppExeName "main.exe"

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{C4CEBDD3-7C1C-4458-801B-78F7DFB790F3}}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={pf}\Oluwaseun\Remote Object Backup
DisableDirPage=yes
DefaultGroupName= Oluwaseun
DisableProgramGroupPage=yes
OutputDir=C:\python_projects\remote-object-backup
OutputBaseFilename=RemoteObjectBackup-{#MyAppVersion}
Compression=lzma
SolidCompression=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Registry]            
Root: HKCR; Subkey: "*\shell\RemoteObjectBackup"; ValueType: string; ValueName: ""; ValueData: "Backup this file!"; Flags: uninsdeletekey
Root: HKCR; Subkey: "*\shell\RemoteObjectBackup\command"; ValueType: string; ValueName: ""; ValueData: """{app}\main.exe"" ""%1"""
Root: HKCR; Subkey: "Directory\shell\RemoteObjectBackup"; ValueType: string; ValueName: ""; ValueData: "Backup this folder!"; Flags: uninsdeletekey
Root: HKCR; Subkey: "Directory\shell\RemoteObjectBackup\command"; ValueType: string; ValueName: ""; ValueData: """{app}\main.exe"" ""%1""";


[Files]
Source: "C:\python_projects\remote-object-backup\src\build\exe.win32-3.5\main.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\python_projects\remote-object-backup\src\build\exe.win32-3.5\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files                 

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{group}\{cm:ProgramOnTheWeb,{#MyAppName}}"; Filename: "{#MyAppURL}"

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall runascurrentuser skipifsilent

