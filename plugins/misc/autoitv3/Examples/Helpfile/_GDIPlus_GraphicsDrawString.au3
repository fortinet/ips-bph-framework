#include <GDIPlus.au3>
#include <GUIConstantsEx.au3>

Example()

Func Example()
	Local $hGUI, $hGraphic

	; Create GUI
	$hGUI = GUICreate("GDI+", 400, 300)
	GUISetState(@SW_SHOW)

	; Draw a string
	_GDIPlus_Startup()
	$hGraphic = _GDIPlus_GraphicsCreateFromHWND($hGUI)
	_GDIPlus_GraphicsDrawString($hGraphic, "Hello world", 140, 110)

	; Loop until the user exits.
	Do
	Until GUIGetMsg() = $GUI_EVENT_CLOSE

	; Clean up resources
	_GDIPlus_GraphicsDispose($hGraphic)
	_GDIPlus_Shutdown()
EndFunc   ;==>Example
