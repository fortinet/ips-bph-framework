#include <GUIConstantsEx.au3>
#include <GuiHeader.au3>

Example()

Func Example()
	Local $hGUI, $hHeader

	; Create GUI
	$hGUI = GUICreate("Header", 400, 300)
	$hHeader = _GUICtrlHeader_Create($hGUI)
	_GUICtrlHeader_SetUnicodeFormat($hHeader, True)
	GUISetState(@SW_SHOW)

	; Add columns
	_GUICtrlHeader_AddItem($hHeader, "Column 1", 100)
	_GUICtrlHeader_AddItem($hHeader, "Column 2", 100)
	_GUICtrlHeader_AddItem($hHeader, "Column 3", 100)
	_GUICtrlHeader_AddItem($hHeader, "Column 4", 100)

	; Set up filters
	_GUICtrlHeader_EditFilter($hHeader, 0)
	Send("Filter 1")
	Sleep(1000)
	Send("{ENTER}")
	_GUICtrlHeader_EditFilter($hHeader, 1)
	Send("Filter 2")
	Sleep(1000)
	Send("{ENTER}")

	; Clear first filter
	_GUICtrlHeader_ClearFilter($hHeader, 0)

	; Loop until the user exits.
	Do
	Until GUIGetMsg() = $GUI_EVENT_CLOSE
EndFunc   ;==>Example
