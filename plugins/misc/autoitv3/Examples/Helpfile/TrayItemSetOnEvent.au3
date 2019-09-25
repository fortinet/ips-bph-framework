#NoTrayIcon
#include <MsgBoxConstants.au3>
#include <StringConstants.au3>
#include <TrayConstants.au3>

Opt("TrayMenuMode", 3) ; The default tray menu items will not be shown and items are not checked when selected. These are options 1 and 2 for TrayMenuMode.
Opt("TrayOnEventMode", 1) ; Enable TrayOnEventMode.

Example()

Func Example()
	TrayCreateItem("About")
	TrayItemSetOnEvent(-1, "About")

	TrayCreateItem("") ; Create a separator line.

	TrayCreateItem("Exit")
	TrayItemSetOnEvent(-1, "ExitScript")

	TraySetOnEvent($TRAY_EVENT_PRIMARYDOUBLE, "About") ; Display the About MsgBox when the tray icon is double clicked on with the primary mouse button.

	TraySetState($TRAY_ICONSTATE_SHOW) ; Show the tray menu.

	While 1
		Sleep(100) ; An idle loop.
	WEnd
EndFunc   ;==>Example

Func About()
	; Display a message box about the AutoIt version and installation path of the AutoIt executable.
	MsgBox($MB_SYSTEMMODAL, "", "AutoIt tray menu example." & @CRLF & @CRLF & _
			"Version: " & @AutoItVersion & @CRLF & _
			"Install Path: " & StringLeft(@AutoItExe, StringInStr(@AutoItExe, "\", $STR_NOCASESENSEBASIC, -1) - 1)) ; Find the folder of a full path.
EndFunc   ;==>About

Func ExitScript()
	Exit
EndFunc   ;==>ExitScript
