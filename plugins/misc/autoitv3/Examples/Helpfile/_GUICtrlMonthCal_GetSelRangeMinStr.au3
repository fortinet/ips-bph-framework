#include <GUIConstantsEx.au3>
#include <GuiMonthCal.au3>
#include <WindowsConstants.au3>

Global $g_idMemo

Example()

Func Example()
	Local $idMonthCal

	; Create GUI
	GUICreate("Month Calendar Get Sel Range Min String", 400, 300)
	$idMonthCal = GUICtrlCreateMonthCal("", 4, 4, -1, -1, BitOR($WS_BORDER, $MCS_MULTISELECT), 0x00000000)

	; Create memo control
	$g_idMemo = GUICtrlCreateEdit("", 4, 168, 392, 128, 0)
	GUICtrlSetFont($g_idMemo, 9, 400, 0, "Courier New")
	GUISetState(@SW_SHOW)

	; Get/Set selection
	_GUICtrlMonthCal_SetSelRange($idMonthCal, @YEAR, @MON, 1, @YEAR, @MON, 7)
	MemoWrite("Start date: " & _GUICtrlMonthCal_GetSelRangeMinStr($idMonthCal))
	MemoWrite("End date .: " & _GUICtrlMonthCal_GetSelRangeMaxStr($idMonthCal))

	; Loop until the user exits.
	Do
	Until GUIGetMsg() = $GUI_EVENT_CLOSE
	GUIDelete()
EndFunc   ;==>Example

; Write message to memo
Func MemoWrite($sMessage)
	GUICtrlSetData($g_idMemo, $sMessage & @CRLF, 1)
EndFunc   ;==>MemoWrite
