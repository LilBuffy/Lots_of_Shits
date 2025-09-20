' GC RAIDER V1.0.1 or idk

confirmation1 = MsgBox("This program is intended to spam text and can cause major issues when not properly used. Are you sure you want to continue?",4+32, "Comednog Spammer v1.0.1")

If confirmation1 = vbYes Then

    confirmation2 = MsgBox("Press 'OK' to start spamming, glhf!",1+64, "Comednog Spammer v1.0.1")
    
    If confirmation2 = vbOK Then
        Set WshShell = WScript.CreateObject("WScript.Shell")

        nig = 1
        stopNa = 10 ' Number of times to spam

        WshShell.SendKeys "%{TAB}"
        WScript.Sleep 500

        Do While nig <= stopNa
            WshShell.SendKeys "@zil"
            WScript.Sleep 150

            WshShell.SendKeys "{ENTER}"
            WScript.Sleep 150

	    WshShell.SendKeys "{ENTER}"
            WScript.Sleep 150

            nig = nig + 1
        Loop

        WScript.Quit(0)
    ElseIf confirmation2 = vbCancel Then
        WScript.Quit(0)
    Else
	WScript.Quit(0)
    End If
ElseIf confirmation1 = vbNo Then
    WScript.Quit(0)
Else
    WScript.Quit(0)
End If
