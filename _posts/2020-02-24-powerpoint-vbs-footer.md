# Powerpoint VBA 

## Footer einfügen 

	Option Explicit

	Sub SetFooterTextForSlides()
	   On Error Resume Next
	   Dim ftext1 As String
	   Dim ftext2 As String
	   Dim ftext3 As String
   
	   Dim ftext As String
	   Dim s As Slide
    
	   Dim PPathAndName As String
	   Dim PName As String

	  PPathAndName = ActivePresentation.Path & "\" & _
	  ActivePresentation.Name
	  PName = ActivePresentation.Name
	  Debug.Print (PPathAndName)

    
    
	   ftext1 = "Prof. "
	   ftext2 = "Prof. "

	   ftext3 = "Geschäftsprozessmodellierung"
      
		For Each s In ActivePresentation.Slides
			'Footer soll erst sichtbar werden
			' s.HeadersFooters.Footer.Visible = msoTrue

        
        
        
			If s.HeadersFooters.Footer.Visible = msoTrue Then
				Debug.Print (s.HeadersFooters.Footer.Text)
				Debug.Print (s.HeadersFooters.DateAndTime.Text)
				' finde "."
				Dim tmp As String
				tmp = StrReverse(PName)
            
				Dim ppos As Integer
				ppos = InStr(1, tmp, ".")
            
				ftext = ftext2 & " - " & Left(PName, Len(PName) - ppos)
            
            
				' s.HeadersFooters.Footer.Text = ActivePresentation.Name
				s.HeadersFooters.Footer.Text = ftext
            
            
				Dim fDatumText As String
				fDatumText = ""
            
				s.HeadersFooters.DateAndTime = fDatumText
            
			End If
       
		Next s

	End Sub
	Sub InsertPath()
	Dim PathAndName As String

	PathAndName = ActivePresentation.Path & "\" & _
	ActivePresentation.Name
	Debug.Print (PathAndName)

	End Sub


	Sub Auto_open()
	Debug.Print ("!")


	End Sub
