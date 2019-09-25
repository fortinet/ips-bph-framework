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
	Local $pIA = _GDIPlus_ImageAttributesCreate() ;create an ImageAttribute object

	;create the color matrix used to adjust the colors of the image
	Local $tColorMatrix = _GDIPlus_ColorMatrixCreateTranslate(-1, -1, 0) ;use translation color matrix to create a blue scaled image

	_GDIPlus_ImageAttributesSetColorMatrix($pIA, 0, True, $tColorMatrix) ;adjust the ImageAttribute color-key color matrix

	Local $hHBmp = _ScreenCapture_Capture("", 0, 0, $iWidth, $iHeight) ;create a GDI bitmap by capturing an area on desktop
	Local $hBitmap = _GDIPlus_BitmapCreateFromHBITMAP($hHBmp) ;convert GDI to GDI+ bitmap
	_WinAPI_DeleteObject($hHBmp) ;release GDI bitmap resource because not needed anymore
	_GDIPlus_GraphicsDrawImageRectRect($hGraphics, $hBitmap, 0, 0, $iWidth, $iHeight, 0, 0, $iWidth, $iHeight, $pIA) ;draw the bitmap while applying the color adjustment

	Do
	Until GUIGetMsg() = $GUI_EVENT_CLOSE

	;cleanup GDI+ resources
	_GDIPlus_ImageAttributesDispose($pIA)
	_GDIPlus_GraphicsDispose($hGraphics)
	_GDIPlus_BitmapDispose($hBitmap)
	_GDIPlus_Shutdown()
	GUIDelete($hGUI)
EndFunc   ;==>Example
