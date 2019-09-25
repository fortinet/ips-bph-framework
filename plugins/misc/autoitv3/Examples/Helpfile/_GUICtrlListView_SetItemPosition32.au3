#include <GUIConstantsEx.au3>
#include <GuiListView.au3>
#include <MsgBoxConstants.au3>

Example()

Func Example()
	Local $idListview

	GUICreate("ListView Set Item Position32", 400, 300)
	$idListview = GUICtrlCreateListView("", 2, 2, 394, 268)
	GUISetState(@SW_SHOW)

	; Add columns
	_GUICtrlListView_AddColumn($idListview, "Items", 100)

	; Add items
	_GUICtrlListView_BeginUpdate($idListview)
	For $iI = 1 To 10
		_GUICtrlListView_AddItem($idListview, "Item " & $iI)
	Next
	_GUICtrlListView_EndUpdate($idListview)

	; Set icon view
	_GUICtrlListView_SetView($idListview, 3)
	MsgBox($MB_SYSTEMMODAL, "Information", "Moving item 2")
	_GUICtrlListView_SetItemPosition32($idListview, 1, 100, 100)

	; Loop until the user exits.
	Do
	Until GUIGetMsg() = $GUI_EVENT_CLOSE
	GUIDelete()
EndFunc   ;==>Example
