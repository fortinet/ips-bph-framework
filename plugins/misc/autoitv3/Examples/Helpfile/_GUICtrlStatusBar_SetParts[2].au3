; == Exampe 2 With array of Widths

#include <GUIConstantsEx.au3>
#include <GuiStatusBar.au3>
#include <WindowsConstants.au3>

Global $g_idMemo

Example()

Func Example()
	Local $hGUI, $hStatus
	Local $aPartWidth[3] = [75, 75, -1]

	; Create GUI
	$hGUI = GUICreate("StatusBar Set Parts", 400, 300)
	$hStatus = _GUICtrlStatusBar_Create($hGUI)

	; Create memo control
	$g_idMemo = GUICtrlCreateEdit("", 2, 2, 396, 274, $WS_VSCROLL)
	GUICtrlSetFont($g_idMemo, 9, 400, 0, "Courier New")
	GUISetState(@SW_SHOW)

	; Set parts
	_GUICtrlStatusBar_SetParts($hStatus, -1, $aPartWidth)

	;Set Text/ Get Width
	Local $iParts = _GUICtrlStatusBar_GetCount($hStatus)
	For $iI = 1 To $iParts
		_GUICtrlStatusBar_SetText($hStatus, "Text " & $iI, $iI - 1)
		MemoWrite("Part " & $iI & " width .: " & _GUICtrlStatusBar_GetWidth($hStatus, $iI - 1))
	Next

	; Loop until the user exits.
	Do
	Until GUIGetMsg() = $GUI_EVENT_CLOSE
	GUIDelete()
EndFunc   ;==>Example

; Write message to memo
Func MemoWrite($sMessage = "")
	GUICtrlSetData($g_idMemo, $sMessage & @CRLF, 1)
EndFunc   ;==>MemoWrite
