---
layout: post
title: Powerpoint Autoupdate Überschriften
categories: 
tags:
  - VBA
  - automation
  - Powerpoint
  - Skript
lastupdate: 2024-08-30
date: 2024-08-30
---
Erstelle von Header 1 Zeilen aus Zwischenüberschriften 

# Powerpoint Autoupdate Überschriften 

PPT - VBA 

``` vb
Sub LeseUndFuegeTextEin()
    Dim pptSlide As Slide
    Dim pptShape As Shape
    Dim textToInsert As String
    Dim targetHeight As Double
    Dim targetLeft As Double
    Dim insertHeight As Double
    Dim insertWidth As Double
    Dim insertTop As Double
    Dim insertLeft As Double
    Dim shapeFound As Boolean
    Dim lnr As Integer
    lnr = -1
    
    ' Zielwerte für das Shape, aus dem der Text gelesen wird
    targetHeight = 85.03937
    targetLeft = 244.8972
    
    ' Zielwerte für das Shape, in das der Text eingefügt werden soll
    insertHeight = 14.54063
    insertWidth = 893.9164
    insertTop = 4.971102
    insertLeft = 11.3152
    
    ' Text aus dem Shape auf der aktuellen Folie lesen
    For Each pptSlide In ActivePresentation.Slides
        shapeFound = False
        
        ' Durchlaufen aller Shapes auf der Folie
        For Each pptShape In pptSlide.Shapes
            ' Überprüfen, ob das Shape die gewünschten Positionen hat
            If Abs(pptShape.Height - targetHeight) < 0.01 And Abs(pptShape.Left - targetLeft) < 0.01 Then
                ' Überprüfen, ob das Shape einen Textframe enthält und Text hat
                If pptShape.HasTextFrame Then
                    If pptShape.TextFrame.HasText Then
                        textToInsert = pptShape.TextFrame.TextRange.Text
                        shapeFound = True
                        lnr = lnr + 1
                        textToInsert = lnr & " - " & textToInsert
                        Debug.Print (textToInsert)
                        Exit For ' Stoppt die Schleife, wenn das Shape gefunden wurde
                    End If
                End If
            End If
        Next pptShape
        
        ' Wenn das Shape auf der aktuellen Folie gefunden wurde, Text auf den nächsten Folien einfügen
        If shapeFound Then
            Dim nextSlide As Slide
            For Each nextSlide In ActivePresentation.Slides
                If nextSlide.SlideIndex > pptSlide.SlideIndex Then
                    ' Durchlaufen aller Shapes auf der nächsten Folie
                    For Each pptShape In nextSlide.Shapes
                        ' Überprüfen, ob das Shape die gewünschten Positionen und Maße hat
                        If Abs(pptShape.Height - insertHeight) < 0.01 And Abs(pptShape.Width - insertWidth) < 0.01 _
                            And Abs(pptShape.Top - insertTop) < 0.01 And Abs(pptShape.Left - insertLeft) < 0.01 Then
                            ' Text in das Shape einfügen
                            If pptShape.HasTextFrame Then
                                pptShape.TextFrame.TextRange.Text = textToInsert
                            End If
                        End If
                        
                                ' Überprüfen, ob das Shape die gewünschten Positionen hat
                        If Abs(pptShape.Height - targetHeight) < 0.01 And Abs(pptShape.Left - targetLeft) < 0.01 Then
                            ' Überprüfen, ob das Shape einen Textframe enthält und Text hat
                            If pptShape.HasTextFrame Then
                                If pptShape.TextFrame.HasText Then
                        textToInsert = pptShape.TextFrame.TextRange.Text
                        shapeFound = True
                        lnr = lnr + 1
                        textToInsert = lnr & " - " & textToInsert
                        Debug.Print (textToInsert)
                        Exit For ' Stoppt die Schleife, wenn das Shape gefunden wurde
                                End If
                            End If
                        End If
                        
                    Next pptShape
                End If
            Next nextSlide
            
            Exit For ' Stoppt die Schleife, nachdem der Text eingefügt wurde
        End If
    Next pptSlide
    
    ' Nachricht an den Benutzer
    MsgBox "Text wurde auf den nächsten Folien eingefügt."
End Sub


```