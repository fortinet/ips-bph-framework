#include <EventLog.au3>
#include <FontConstants.au3>
#include <GUIConstantsEx.au3>
#include <WinAPIHObj.au3>
#include <WinAPIProc.au3>

Global $g_idMemo

Example()

Func Example()
	Local $hEventLog, $hEvent, $iResult

	; Create GUI
	GUICreate("EventLog", 600, 300)
	$g_idMemo = GUICtrlCreateEdit("", 2, 2, 596, 294, 0)
	GUICtrlSetFont($g_idMemo, 9, $FW_NORMAL, $GUI_FONTNORMAL, "Courier New")
	GUISetState(@SW_SHOW)

	; Set up event
	$hEventLog = _EventLog__Open("", "Security")
	$hEvent = _WinAPI_CreateEvent(0, False, False, "")
	_EventLog__Notify($hEventLog, $hEvent)

	; Wait for new event to occur
	MemoWrite("Waiting for new event")
	$iResult = _WinAPI_WaitForSingleObject($hEvent)
	_WinAPI_CloseHandle($hEvent)
	_EventLog__Close($hEventLog)

	; Write results
	If $iResult = -1 Then
		MemoWrite("Wait failed")
	Else
		MemoWrite("New event occurred")
	EndIf

	; Loop until the user exits.
	Do
	Until GUIGetMsg() = $GUI_EVENT_CLOSE
EndFunc   ;==>Example

; Write a line to the memo control
Func MemoWrite($sMessage)
	GUICtrlSetData($g_idMemo, $sMessage & @CRLF, 1)
EndFunc   ;==>MemoWrite
