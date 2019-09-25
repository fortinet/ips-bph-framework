#include <GuiButton.au3>
#include <GUIConstantsEx.au3>
#include <WindowsConstants.au3>

Global $g_idMemo

Example()

Func Example()
	Local $idRdo, $idRdo2, $idChk

	GUICreate("Buttons", 400, 400)
	$g_idMemo = GUICtrlCreateEdit("", 119, 10, 276, 374, $WS_VSCROLL)
	GUICtrlSetFont($g_idMemo, 9, 400, 0, "Courier New")

	$idRdo = GUICtrlCreateRadio("Radio1", 10, 10, 90, 50)
	_GUICtrlButton_SetFocus($idRdo)

	$idRdo2 = GUICtrlCreateRadio("Radio2", 10, 60, 90, 50)
	_GUICtrlButton_SetCheck($idRdo2)

	$idChk = GUICtrlCreateCheckbox("Check1", 10, 120, 90, 50, BitOR($BS_AUTO3STATE, $BS_NOTIFY))
	_GUICtrlButton_SetCheck($idChk, $BST_INDETERMINATE)

	GUISetState(@SW_SHOW)

	MemoWrite(StringFormat("$idRdo focus status.: %s", _GUICtrlButton_GetFocus($idRdo)))
	MemoWrite(StringFormat("$idRdo2 focus status: %s", _GUICtrlButton_GetFocus($idRdo2)))
	MemoWrite(StringFormat("$idChk focus status.: %s", _GUICtrlButton_GetFocus($idChk)))

	While 1
		Switch GUIGetMsg()
			Case $GUI_EVENT_CLOSE
				ExitLoop
		EndSwitch
	WEnd

	Exit
EndFunc   ;==>Example

; Write a line to the memo control
Func MemoWrite($sMessage)
	GUICtrlSetData($g_idMemo, $sMessage & @CRLF, 1)
EndFunc   ;==>MemoWrite
