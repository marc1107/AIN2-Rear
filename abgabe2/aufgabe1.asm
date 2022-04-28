	.data
n: 	.word 6
A: 	.word 1, 2, 3, 4, 5, 6

	.text
	lw $s1, n
	la $s2, A
	
	#move $t0, $zero
	#move $v0, $zero
loop:	slt $t1, $t0, $s1
	# solange $t0 kleiner als $s1 ist, ansonsten springe zu exit
	beq $t1, $zero, exit
		# Stelle A[i] in $t2 speichern
		lw $t2, 0($s2)
		# $t2 auf $v0 addieren
		add $v0, $v0, $t2
		# Speicheradresse des nächste Worts in A setzen (1 Wort = 4)
		addi $s2, $s2, 4 
		# Zählvariable (in Java i) um 1 erhöhen
		addi $t0, $t0, 1
		j loop

exit: