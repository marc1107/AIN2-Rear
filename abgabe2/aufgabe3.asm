	.data
n: 	.word 6
A: 	.word 3, 4, 6, 8, 11, 13
B: 	.word 0, 0, 0, 0, 0, 0

	.text
	lw $s1, n	# n is $s1 speichern
	la $s2, A	# Adresse von Array A in $s2 speichern
	la $s3, B	# Adresse von Array B in $s3 speichern
	
	jal evenElem	# Prozedur gerade ausführen
	
	move $s4, $v0	# Rückgabeparameter $v0 in $s4 schreiben
	
	j exit		# Programm beenden
		
evenElem:	slt $t1, $t0, $s1	# solange $t0 kleiner als $s1 ist,
		beq $t1, $zero, jumpra	# ansonsten springe zurück zu Rücksprungadresse (geht das ohne die Methode jumpra?)
	
			lw $t2, 0($s2)		# Stelle A[i] in $t2 speichern
			addi $s2, $s2, 4 	# Speicheradresse des nächste Worts in A setzen (1 Wort = 4)
			addi $t0, $t0, 1	# Zählvariable $t0 um 1 erhöhen
			
			# Vorige Rücksprungadresse auf Stack ablegen
			# Geht das irgendwie auch in der isEven Prozedur? Durch jal wird $ra ja schon beim Aufruf überschrieben?
			addi $sp, $sp, -4 	# Stackpointer um ein Wort verringern
			sw $ra, 0($sp) 		# $ra auf den Stack schreiben
			
			# isEven aufrufen
			move $a0, $t2 		# Übergabeparameter setzen
			jal isEven		# Prozeduraufruf
			move $t3, $v1		# Rückgabeparameter in $t3 schreiben
			
			# Rücksprungadresse wieder von Stack holen
			lw $ra, 0($sp)		# $s0 vom Stack wiederherstellen
			addi $sp, $sp, 4	# Stackpointer um ein Wort erhöhen
			
			beq $t3, $zero, evenElem	# Wenn nicht gerade, also $t3=0, nächsten Durchlauf starten
			
				addi $v0, $v0, 1	# Anzahl gerade um 1 erhöhen
				sw $t2, 0($s3)		# Wert in dementsprechende Stelle von Array B speichern
				addi $s3, $s3, 4	# Speicheradresse auf die nächste Adresse von B setzen
				j evenElem		# Nächsten Schleifendurchlauf starten
	

# schreibt 1 in $v1, wenn Übergabeparameter gerade, ansonsten 0			
isEven:	andi $v1, $a0, 1	# Prüfen, ob binär ganz hinten eine 1 (für ungerade) steht
	slti $v1, $v1, 1	# 0 in 1 umwandeln oder 1 in 0 umwandeln
	jr $ra			# Zur Rücksprungadresse springen
		
	

jumpra:	jr $ra

exit:
