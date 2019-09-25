#include <GUIConstantsEx.au3>
#include <StructureConstants.au3>
#include <WinAPIDlg.au3>
#include <WindowsConstants.au3>

Global $g_idMemo

_Example_Defaults()
_Example_ExplorerStyleMultiSelect()
_Example_OldStyle()
_Example_ExplorerStyleSingleSelect()
_Example_ExplorerStyle_NoPlaceBar()

Func _Example_Defaults()
	Local $hGui, $id_Dialog, $aFile, $sError

	; Create GUI
	$hGui = GUICreate("GetOpenFileName use defaults", 400, 296)
	$g_idMemo = GUICtrlCreateEdit("", 2, 32, 396, 226, $WS_HSCROLL)
	GUICtrlSetFont($g_idMemo, 9, 400, 0, "Courier New")
	$id_Dialog = GUICtrlCreateButton("Open Dialog", 155, 270, 90, 20)
	GUISetState(@SW_SHOW)

	While 1
		Switch GUIGetMsg()
			Case $id_Dialog
				$aFile = _WinAPI_GetOpenFileName() ; use defaults
				If @error Then
					$sError = _WinAPI_CommDlgExtendedError()
					MemoWrite("CommDlgExtendedError (" & @error & "): " & $sError)
				Else
					For $x = 1 To $aFile[0]
						MemoWrite($aFile[$x])
					Next
				EndIf
			Case $GUI_EVENT_CLOSE
				ExitLoop
		EndSwitch
	WEnd
	GUIDelete($hGui)
EndFunc   ;==>_Example_Defaults

Func _Example_ExplorerStyleMultiSelect()
	Local $hGui, $id_Dialog, $aFile, $sError

	; Create GUI
	$hGui = GUICreate("GetOpenFileName use Explorer Style (Multi Select)", 400, 296)
	$g_idMemo = GUICtrlCreateEdit("", 2, 32, 396, 226, $WS_HSCROLL)
	GUICtrlSetFont($g_idMemo, 9, 400, 0, "Courier New")
	$id_Dialog = GUICtrlCreateButton("Open Dialog", 155, 270, 90, 20)
	GUISetState(@SW_SHOW)

	While 1
		Switch GUIGetMsg()
			Case $id_Dialog
				$aFile = _WinAPI_GetOpenFileName("My Open File Dialog", _
						"Text File (*.txt;*.au3)", ".", @ScriptName, "", 1, _
						BitOR($OFN_ALLOWMULTISELECT, $OFN_EXPLORER), 0, $hGui)
				If @error Then
					$sError = _WinAPI_CommDlgExtendedError()
					MemoWrite("CommDlgExtendedError (" & @error & "): " & $sError)
				Else
					For $x = 1 To $aFile[0]
						MemoWrite($aFile[$x])
					Next
				EndIf
			Case $GUI_EVENT_CLOSE
				ExitLoop
		EndSwitch
	WEnd
	GUIDelete($hGui)
EndFunc   ;==>_Example_ExplorerStyleMultiSelect

Func _Example_OldStyle()
	Local $hGui, $id_Dialog, $aFile, $sError

	; Create GUI
	$hGui = GUICreate("GetOpenFileName use Old Style (Multi Select)", 400, 296)
	$g_idMemo = GUICtrlCreateEdit("", 2, 32, 396, 226, $WS_HSCROLL)
	GUICtrlSetFont($g_idMemo, 9, 400, 0, "Courier New")
	$id_Dialog = GUICtrlCreateButton("Open Dialog", 155, 270, 90, 20)
	GUISetState(@SW_SHOW)

	While 1
		Switch GUIGetMsg()
			Case $id_Dialog
				$aFile = _WinAPI_GetOpenFileName("My Open File Dialog", _
						"Text File (*.txt)|AutoIt File (*.au3)", ".", @ScriptName, _
						"", 2, $OFN_ALLOWMULTISELECT, 0, $hGui)
				If @error Then
					$sError = _WinAPI_CommDlgExtendedError()
					MemoWrite("CommDlgExtendedError (" & @error & "): " & $sError)
				Else
					For $x = 1 To $aFile[0]
						MemoWrite($aFile[$x])
					Next
				EndIf
			Case $GUI_EVENT_CLOSE
				ExitLoop
		EndSwitch
	WEnd
	GUIDelete($hGui)
EndFunc   ;==>_Example_OldStyle

Func _Example_ExplorerStyleSingleSelect()
	Local $hGui, $id_Dialog, $aFile, $sError

	; Create GUI
	$hGui = GUICreate("GetOpenFileName use Explorer Style (Single Select)", 400, 296)
	$g_idMemo = GUICtrlCreateEdit("", 2, 32, 396, 226, $WS_HSCROLL)
	GUICtrlSetFont($g_idMemo, 9, 400, 0, "Courier New")
	$id_Dialog = GUICtrlCreateButton("Open Dialog", 155, 270, 90, 20)
	GUISetState(@SW_SHOW)

	While 1
		Switch GUIGetMsg()
			Case $id_Dialog
				$aFile = _WinAPI_GetOpenFileName("My Open File Dialog", _
						"Text File (*.txt)|AutoIt File (*.au3)", ".", @ScriptName, _
						"", 2, 0, 0, $hGui)
				If @error Then
					$sError = _WinAPI_CommDlgExtendedError()
					MemoWrite("CommDlgExtendedError (" & @error & "): " & $sError)
				Else
					For $x = 1 To $aFile[0]
						MemoWrite($aFile[$x])
					Next
				EndIf
			Case $GUI_EVENT_CLOSE
				ExitLoop
		EndSwitch
	WEnd
	GUIDelete($hGui)
EndFunc   ;==>_Example_ExplorerStyleSingleSelect

Func _Example_ExplorerStyle_NoPlaceBar()
	Local $hGui, $id_Dialog, $aFile, $sError

	; Create GUI
	$hGui = GUICreate("GetOpenFileName use Explorer Style (Single Select)", 400, 296)
	$g_idMemo = GUICtrlCreateEdit("", 2, 32, 396, 226, $WS_HSCROLL)
	GUICtrlSetFont($g_idMemo, 9, 400, 0, "Courier New")
	$id_Dialog = GUICtrlCreateButton("Open Dialog", 155, 270, 90, 20)
	GUISetState(@SW_SHOW)

	While 1
		Switch GUIGetMsg()
			Case $id_Dialog
				$aFile = _WinAPI_GetOpenFileName("My Open File Dialog", _
						"Text File (*.txt)|AutoIt File (*.au3)", ".", @ScriptName, _
						"", 2, $OFN_EXPLORER, $OFN_EX_NOPLACESBAR, $hGui)
				If @error Then
					$sError = _WinAPI_CommDlgExtendedError()
					MemoWrite("CommDlgExtendedError (" & @error & "): " & $sError)
				Else
					For $x = 1 To $aFile[0]
						MemoWrite($aFile[$x])
					Next
				EndIf
			Case $GUI_EVENT_CLOSE
				ExitLoop
		EndSwitch
	WEnd
	GUIDelete($hGui)
EndFunc   ;==>_Example_ExplorerStyle_NoPlaceBar

; Write a line to the memo control
Func MemoWrite($sMessage)
	GUICtrlSetData($g_idMemo, $sMessage & @CRLF, 1)
EndFunc   ;==>MemoWrite
