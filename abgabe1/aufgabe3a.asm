	sub $s2, $s0, $s1
	slt $t0, $s2, $zero
	bne $t0, $zero, Else
	j Exit
Else: 	sub $s2, $zero, $s2
Exit: