addi $s0, $zero, 6		# Der Wert 6 ist unser x (Übergabeparameter)

move $a0, $s0			# Übergabeparameter setzen

jal ISODD			# Prozedur aufrufen (Rücksprungadresse wird hier in $ra = PC + 4 gespeichert)

move $s1, $v0			# Rückgabeparameter in $s1 speichern

jal ISEVEN			# andere Prozedur aufrufen

move $s2, $v0			# Rückgabeparameter in $s2 speichern

j exit				# Zu exit, springen, ansonsten Endlosschleife in ISODD

ISODD:	# Rückgabewert berechnen
	andi $v0, $a0, 1	# Prüfen, ob binär ganz hinten eine 1 (für ungerade) steht
	#move $v0, $s0		# den berechneten Wert in Rückgabewert $v0 speichern
	
	jr $ra			# Springt zurück zur gespeicherten Rücksprungadresse
	
ISEVEN:	addi $sp, $sp, -4
	sw $ra, 0($sp)		# Rücksprungadresse sichern
	
	jal ISODD		# ISODD aufrufen
	
	lw $ra, 0($sp)		# Rücksprungadresse laden
	addi $sp, $sp, 4

	slti $v0, $v0, 1	# 0 in 1 umwandeln oder 1 in 0 umwandeln
	
	jr $ra			# Zur Rücksprungadresse springen
	
exit:
