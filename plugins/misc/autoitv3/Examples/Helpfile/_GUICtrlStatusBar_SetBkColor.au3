#include <ColorConstants.au3>
#include <GUIConstantsEx.au3>
#include <GuiStatusBar.au3>
#include <WinAPITheme.au3>

Example()

Func Example()
	Local $hGUI, $hStatus
	Local $aParts[3] = [75, 150, -1]
	; Create GUI
	$hGUI = GUICreate("StatusBar Set BkColor", 400, 300)
	$hStatus = _GUICtrlStatusBar_Create($hGUI)
	GUISetState(@SW_SHOW)

	; to allow the setting of Bk Color at least under Windows 10
	_WinAPI_SetWindowTheme($hStatus, "", "")

	; Set parts
	_GUICtrlStatusBar_SetParts($hStatus, $aParts)
	_GUICtrlStatusBar_SetText($hStatus, "Part 1")
	_GUICtrlStatusBar_SetText($hStatus, "Part 2", 1)
	_GUICtrlStatusBar_SetText($hStatus, "Part 3", 2)

	; Set background color
	_GUICtrlStatusBar_SetBkColor($hStatus, $CLR_MONEYGREEN)

	; Loop until the user exits.
	Do
	Until GUIGetMsg() = $GUI_EVENT_CLOSE
	GUIDelete()
EndFunc   ;==>Example
