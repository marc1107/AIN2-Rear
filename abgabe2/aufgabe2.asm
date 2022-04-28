# boolean/int r (int x) { }

addi $s0, $zero, 6		# Der Wert 6 ist unser x (Übergabeparameter)

move $a0, $s0			# Übergabeparameter setzen

jal ISODD			# Prozedur aufrufen (Rücksprungadresse wird hier in $ra = PC + 4 gespeichert)

move $s1, $v0			# Rückgabeparameter in $s1 speichern

jal ISEVEN			# andere Prozedur aufrufen

move $s2, $v0			# Rückgabeparameter in $s2 speichern

j exit				# Zu exit, springen, ansonsten Endlosschleife in ISODD

ISODD:	# !!! Speichern der Werte von z.B. $s0 auf den Stack wird nur benötigt, !!!
	# !!! wenn in diesem Fall mit $s0 in der Prozedur gearbeitet wird.	!!!
	#addi $sp, $sp, -4 	# Stackpointer um ein Wort verringern
	#sw $s0, 0($sp) 	# $s0 auf den Stack schreiben

	# Rückgabewert berechnen
	andi $v0, $a0, 1	# Prüfen, ob binär ganz hinten eine 1 (für ungerade) steht
	#move $v0, $s0		# den berechneten Wert in Rückgabewert $v0 speichern
	
	#lw $s0, 0($sp)		# $s0 vom Stack wiederherstellen
	#addi $sp, $sp, 4	# Stackpointer um ein Wort erhöhen
	
	jr $ra			# Springt zurück zur gespeicherten Rücksprungadresse
	
ISEVEN:	andi $v0, $a0, 1	# Prüfen, ob binär ganz hinten eine 1 (für ungerade) steht
	slti $v0, $v0, 1	# 0 in 1 umwandeln oder 1 in 0 umwandeln
	jr $ra			# Zur Rücksprungadresse springen
	
exit: