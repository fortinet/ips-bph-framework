#include <MsgBoxConstants.au3>
#include <Security.au3>
#include <SecurityConstants.au3>
#include <WinAPIError.au3>
#include <WinAPIHObj.au3>

Local $hToken = _Security__OpenThreadTokenEx($TOKEN_ADJUST_PRIVILEGES)
If $hToken Then
	; $hToken is this thread's token with $TOKEN_ADJUST_PRIVILEGES access
	MsgBox($MB_SYSTEMMODAL, "OpenThreadTokenEx", "$hToken is " & $hToken)

	_WinAPI_CloseHandle($hToken)
Else
	ConsoleWrite("! _Security__OpenThreadTokenEx failed with error description: " & _WinAPI_GetLastErrorMessage())
EndIf
