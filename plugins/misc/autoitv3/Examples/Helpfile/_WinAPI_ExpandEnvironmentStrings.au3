#include <MsgBoxConstants.au3>
#include <WinAPISys.au3>

MsgBox($MB_SYSTEMMODAL, "Environment string", "%windir% = " & _WinAPI_ExpandEnvironmentStrings("%windir%"))
