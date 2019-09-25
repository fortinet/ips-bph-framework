; == Example 2 for suppression of the timer

#include <GUIConstantsEx.au3>
#include <Timers.au3>

Local $hForm1 = GUICreate("Form1", 615, 437, 192, 124)

; to be use when the timeOut fire
; so that action can be taken to stop the timer
Global $g_idDummy = GUICtrlCreateDummy()

GUISetState(@SW_SHOW)

Local $iTimerID = _Timer_SetTimer($hForm1, 1000, "_TimedActivated") ; create timer

While 1
	Switch GUIGetMsg()
		Case $GUI_EVENT_CLOSE
			Exit

		Case $g_idDummy
			Local $iResult = _Timer_KillTimer($hForm1, $iTimerID)
			MsgBox(262144, 'Time Out Fired', '_Timer_KillTimer() result = ' & $iResult)
	EndSwitch
WEnd

Func _TimedActivated($hWnd, $iMsg, $iIDTimer, $iTime)
	#forceref $hWnd, $iMsg, $iIDTimer, $iTime
	; to handle the event outside the callback
	GUICtrlSendToDummy($g_idDummy)
EndFunc   ;==>_TimedActivated
