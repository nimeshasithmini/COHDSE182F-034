Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> plaintext=input("Enter message:")
Enter message: im nimesha.
>>> alphabet="abcdefghijklmnopqrstuvwxyz"
>>> key=1
>>> cipher=''
>>> for c in plaintext:
	if c in alphabet:
		cipher+=alphabet[(alphabet.index(c)+key)%(len(alphabet))]
		print('your encrypted message is:'+cipher)

		
your encrypted message is:j
your encrypted message is:jn
your encrypted message is:jno
your encrypted message is:jnoj
your encrypted message is:jnojn
your encrypted message is:jnojnf
your encrypted message is:jnojnft
your encrypted message is:jnojnfti
your encrypted message is:jnojnftib
>>> 
