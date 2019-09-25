#include <GUIConstantsEx.au3>
#include <GuiToolTip.au3>
#include <MsgBoxConstants.au3>
#include <WinAPIConv.au3>

Example()

Func Example()
	Local $hGUI = GUICreate(StringTrimRight(@ScriptName, StringLen(".exe")), 350, 200)

	Local $idButton = GUICtrlCreateButton("This is a button", 30, 32, 130, 28)
	Local $hButton = GUICtrlGetHandle($idButton)
	; create a tooltip control using default settings
	Local $hToolTip = _GUIToolTip_Create(0)
	; add a tool to the tooltip control
	_GUIToolTip_AddTool($hToolTip, 0, "This is a ToolTip", $hButton)
	GUISetState(@SW_SHOW)
	_GUIToolTip_TrackActivate($hToolTip, True, 0, $hButton)

	Local $iBubbleHeight = _WinAPI_HiWord(_GUIToolTip_GetBubbleSize($hToolTip, 0, $hButton))
	Local $iBubbleWidth = _WinAPI_LoWord(_GUIToolTip_GetBubbleSize($hToolTip, 0, $hButton))
	; Display the height of the tooltip bubble in pixels
	MsgBox($MB_SYSTEMMODAL, "Info", "Bubble Height = " & @TAB & $iBubbleHeight & " Pixels" & @CRLF & _
			"Bubble Width = " & @TAB & $iBubbleWidth & " Pixels")
	While 1
		If GUIGetMsg() = $GUI_EVENT_CLOSE Then ExitLoop
	WEnd
	; Destroy the tooltip control
	_GUIToolTip_Destroy($hToolTip)
	GUIDelete($hGUI)
EndFunc   ;==>Example
