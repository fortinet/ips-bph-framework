#include <GUIConstantsEx.au3>
#include <GuiTab.au3>

Example()

Func Example()
	Local $idTab

	; Create GUI
	GUICreate("Tab Control Set Item Size", 400, 300)
	$idTab = GUICtrlCreateTab(2, 2, 396, 296, BitOR($TCS_BUTTONS, $TCS_FIXEDWIDTH))
	_GUICtrlTab_SetItemSize($idTab, 70, 40)
	GUISetState(@SW_SHOW)

	; Add tabs
	_GUICtrlTab_InsertItem($idTab, 0, "Tab 1")
	_GUICtrlTab_InsertItem($idTab, 1, "Tab 2")
	_GUICtrlTab_InsertItem($idTab, 2, "Tab 3")

	; Loop until the user exits.
	Do
	Until GUIGetMsg() = $GUI_EVENT_CLOSE
	GUIDelete()
EndFunc   ;==>Example
