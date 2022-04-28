	add $s0, $zero, $zero
	addi $s1, $zero, 1
	addi $s3, $zero, 10
loop: 	beq $s3, $zero, continue
	slt $t0, $s3, $zero
	bne $t0, $zero, continue
	add $s2, $s0, $s1
	add $s0, $zero, $s1
	add $s1, $zero, $s2
	addi $s3, $s3, -1
	j loop
continue: