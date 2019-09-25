#include <GUIConstantsEx.au3>
#include <GuiTreeView.au3>
#include <MsgBoxConstants.au3>
#include <WindowsConstants.au3>

Example()

Func Example()
	Local $aidItem[11], $idTmp_item, $idTreeView
	Local $iStyle = BitOR($TVS_EDITLABELS, $TVS_HASBUTTONS, $TVS_HASLINES, $TVS_LINESATROOT, $TVS_DISABLEDRAGDROP, $TVS_SHOWSELALWAYS, $TVS_CHECKBOXES)

	GUICreate("TreeView Get Children", 400, 300)

	$idTreeView = GUICtrlCreateTreeView(2, 2, 396, 268, $iStyle, $WS_EX_CLIENTEDGE)
	GUISetState(@SW_SHOW)

	_GUICtrlTreeView_BeginUpdate($idTreeView)
	For $x = 0 To 3
		$aidItem[$x] = GUICtrlCreateTreeViewItem(StringFormat("[%02d] New Item", $x), $idTreeView)
		For $y = 0 To 2
			$idTmp_item = GUICtrlCreateTreeViewItem(StringFormat("[%02d] New Item", $y), $aidItem[$x])
		Next
	Next
	$aidItem[4] = GUICtrlCreateTreeViewItem(StringFormat("Looking for me?", $x), $idTmp_item)
	For $x = 5 To 9
		$aidItem[$x] = GUICtrlCreateTreeViewItem(StringFormat("[%02d] New Item", $x), $idTreeView)
		For $y = 0 To 2
			GUICtrlCreateTreeViewItem(StringFormat("[%02d] New Item", $y), $aidItem[$x])
		Next
	Next
	$aidItem[10] = GUICtrlCreateTreeViewItem(StringFormat("[%02d] New Item", 10), $idTreeView)
	_GUICtrlTreeView_EndUpdate($idTreeView)

	MsgBox($MB_SYSTEMMODAL, "Information", "Item 0 has Children? " & _GUICtrlTreeView_GetChildren($idTreeView, $aidItem[0]))
	MsgBox($MB_SYSTEMMODAL, "Information", "Item 10 has Children? " & _GUICtrlTreeView_GetChildren($idTreeView, $aidItem[10]))
	_GUICtrlTreeView_SetChildren($idTreeView, $aidItem[10])
	MsgBox($MB_SYSTEMMODAL, "Information", "Item 10 has Children? " & _GUICtrlTreeView_GetChildren($idTreeView, $aidItem[10]))

	; Loop until the user exits.
	Do
	Until GUIGetMsg() = $GUI_EVENT_CLOSE
	GUIDelete()
EndFunc   ;==>Example
