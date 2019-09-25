#include <GUIConstantsEx.au3>
#include <GuiImageList.au3>
#include <GuiListView.au3>
#include <MsgBoxConstants.au3>

Example()

Func Example()
	Local $aInfo, $hImage, $idListview

	GUICreate("ListView Get Group Info", 400, 300)

	$idListview = GUICtrlCreateListView("", 2, 2, 394, 268)
	GUISetState(@SW_SHOW)

	; Load images
	$hImage = _GUIImageList_Create()
	_GUIImageList_Add($hImage, _GUICtrlListView_CreateSolidBitMap(GUICtrlGetHandle($idListview), 0xFF0000, 16, 16))
	_GUIImageList_Add($hImage, _GUICtrlListView_CreateSolidBitMap(GUICtrlGetHandle($idListview), 0x00FF00, 16, 16))
	_GUIImageList_Add($hImage, _GUICtrlListView_CreateSolidBitMap(GUICtrlGetHandle($idListview), 0x0000FF, 16, 16))
	_GUICtrlListView_SetImageList($idListview, $hImage, 1)

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

	; Build groups
	_GUICtrlListView_EnableGroupView($idListview)
	_GUICtrlListView_InsertGroup($idListview, -1, 1, "Group 1", 1)
	_GUICtrlListView_InsertGroup($idListview, -1, 2, "Group 2")
	_GUICtrlListView_SetItemGroupID($idListview, 0, 1)
	_GUICtrlListView_SetItemGroupID($idListview, 1, 2)
	_GUICtrlListView_SetItemGroupID($idListview, 2, 2)

	If @OSVersion = "WIN_XP" Then
		MsgBox($MB_SYSTEMMODAL, "Information", "The function does not work in WinXP")
	Else
		; Change group information
		For $x = 0 To _GUICtrlListView_GetGroupCount($idListview) - 1
			$aInfo = _GUICtrlListView_GetGroupInfoByIndex($idListview, $x)
			MsgBox($MB_SYSTEMMODAL, "Information", "Index " & $x + 1 & @CRLF & "Text: " & $aInfo[0] & @CRLF & "Group ID: " & $aInfo[2])
		Next
	EndIf
	_GUICtrlListView_SetGroupInfo($idListview, 1, "New Group 1 (Minimum OS: Vista)")

	; Loop until the user exits.
	Do
	Until GUIGetMsg() = $GUI_EVENT_CLOSE

	GUIDelete()
EndFunc   ;==>Example
