#include <GUIConstantsEx.au3>
#include <GuiListView.au3>
#include <MsgBoxConstants.au3>

Example()

Func Example()
	Local $idListview

	GUICreate("ListView Get Item Checked State", 400, 300)
	$idListview = GUICtrlCreateListView("", 2, 2, 394, 268)
	_GUICtrlListView_SetExtendedListViewStyle($idListview, BitOR($LVS_EX_FULLROWSELECT, $LVS_EX_CHECKBOXES))
	GUISetState(@SW_SHOW)

	; Add columns
	_GUICtrlListView_AddColumn($idListview, "Column 1", 100)
	_GUICtrlListView_AddColumn($idListview, "Column 2", 100)
	_GUICtrlListView_AddColumn($idListview, "Column 3", 100)

	; Add items
	_GUICtrlListView_AddItem($idListview, "Row 1: Col 1", 0)
	_GUICtrlListView_AddSubItem($idListview, 0, "Row 1: Col 2", 1)
	_GUICtrlListView_AddSubItem($idListview, 0, "Row 1: Col 3", 2)
	_GUICtrlListView_AddItem($idListview, "Row 2: Col 1", 1)
	_GUICtrlListView_AddSubItem($idListview, 1, "Row 2: Col 2", 1)
	_GUICtrlListView_AddItem($idListview, "Row 3: Col 1", 2)

	; Check item 2
	_GUICtrlListView_SetItemChecked($idListview, 1)
	MsgBox($MB_SYSTEMMODAL, "Information", "Item 2 Checked: " & _GUICtrlListView_GetItemChecked($idListview, 1))

	; Loop until the user exits.
	Do
	Until GUIGetMsg() = $GUI_EVENT_CLOSE
	GUIDelete()
EndFunc   ;==>Example
