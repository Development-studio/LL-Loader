#include <Misc.au3>
#include <TrayConstants.au3>
#include <WinAPISys.au3>
#include <WinAPIProc.au3>
#include <WinAPI.au3>
#include <GuiComboBox.au3>

$n = (@ScriptDir & "\download.exe")
TrayTip("test", "script started", 10, 2)

Sleep("3000")

Run($n)
Sleep("1000")
Send("1")
Send("{ENTER}")
ProcessWaitClose("download.exe")

Run($n)
Sleep("1000")
Send("2")
Send("{ENTER}")
ProcessWaitClose("download.exe")

Sleep("1000")
Run("cmd.exe")
Sleep("1000")
Send("cscript unzip.vbs bedrock_server.zip")
Send("{ENTER}")
Sleep("1000")
Send("cscript unzip.vbs LiteLoader.zip")
Send("{ENTER}")
Sleep("1000")
Send("exit")

ProcessWaitClose("cmd.exe")
Sleep("1000")
Run("SymDB2.exe")

ProcessWaitClose("SymDB2.exe")
Run("bedrock_server.exe")
Send("hello world!")
Sleep("1000")
WinClose("bedrock_server.exe")


