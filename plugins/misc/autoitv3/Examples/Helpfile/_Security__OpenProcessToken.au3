#include <MsgBoxConstants.au3>
#include <Security.au3>
#include <SecurityConstants.au3>
#include <WinAPIHObj.au3>

Local $hToken = _Security__OpenProcessToken(_WinAPI_GetCurrentProcess(), $TOKEN_QUERY)
If $hToken Then
	; $hToken is this process' token with $TOKEN_QUERY access

	;... Do whatever with this token now and here...
	MsgBox($MB_SYSTEMMODAL, "OpenProcessToken", "$hToken = " & $hToken)

	; Close handle when done
	_WinAPI_CloseHandle($hToken)
EndIf
