#include <GDIPlus.au3>
#include <GUIConstantsEx.au3>
#include <ScreenCapture.au3>
#include <WinAPIHObj.au3>

Example()

Func Example()
	_GDIPlus_Startup() ;initialize GDI+
	Local Const $iWidth = 600, $iHeight = 600

	Local $hGUI = GUICreate("GDI+ Example (" & @ScriptName & ")", $iWidth, $iHeight) ;create a test GUI
	GUISetState(@SW_SHOW)

	Local $hGraphics = _GDIPlus_GraphicsCreateFromHWND($hGUI) ;create a graphics object from a window handle
	Local $hIA = _GDIPlus_ImageAttributesCreate() ;create an ImageAttribute object

	Local $tColorMatrix = _GDIPlus_ColorMatrixCreateTranslate(0.75, 0.75, 0.75) ;create the brightness color matrix (RGB)

	_GDIPlus_ImageAttributesSetColorMatrix($hIA, 0, True, $tColorMatrix) ;adjust the image brightness to be 75% brighter

	Local $hHBmp = _ScreenCapture_Capture("", 0, 0, $iWidth, $iHeight) ;create a GDI bitmap by capturing an area on desktop
	Local $hBitmap = _GDIPlus_BitmapCreateFromHBITMAP($hHBmp) ;convert GDI to GDI+ bitmap
	_WinAPI_DeleteObject($hHBmp) ;release GDI bitmap resource because not needed anymore

	_GDIPlus_GraphicsDrawImageRectRect($hGraphics, $hBitmap, 0, 0, $iWidth, $iHeight, 0, 0, $iWidth, $iHeight, $hIA) ;draw the bitmap while applying the color adjustment

	Do
	Until GUIGetMsg() = $GUI_EVENT_CLOSE

	;cleanup GDI+ resources
	_GDIPlus_ImageAttributesDispose($hIA)
	_GDIPlus_GraphicsDispose($hGraphics)
	_GDIPlus_BitmapDispose($hBitmap)
	_GDIPlus_Shutdown()
	GUIDelete($hGUI)
EndFunc   ;==>Example
